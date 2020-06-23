from connexion import NoContent
from dataclasses import dataclass
from http import HTTPStatus
from typing import List
import xml.dom.minidom as mini
import xml.etree.ElementTree as ET

@dataclass(init=True, frozen=True)
class Controller:
    file_name: str
    container_name: str
    item_name: str

    def __read(self) -> ET.Element:
        return ET.parse(self.file_name).getroot()

    def __write(self, data: ET.Element):
        xml = self.prettify(data)
        with open(self.file_name, 'w') as f:
            f.write(xml)

    @staticmethod
    def prettify(data):
        xml = mini.parseString(ET.tostring(data))
        return '\n'.join([line for line in xml.toprettyxml(indent=' ' * 2).split('\n') if line.strip()])

    def search(self) -> List[str]:
        items = self.__read().findall(f'{self.container_name}/{self.item_name}')
        sorted_items = sorted(items, key=lambda x: x.attrib['name'])
        return [item.attrib['name'] for item in sorted_items]

    def post(self, value: str) -> (NoContent, HTTPStatus):
        if value.lower() in map(lambda item: item.lower(), self.search()):
            return NoContent, HTTPStatus.CONFLICT, {'x-error': f'{self.item_name} already exists'}

        root = self.__read()
        container = root.find(self.container_name)
        element = container.makeelement(self.item_name, {'name': value})
        container.append(element)
        self.__write(root)
        return NoContent, HTTPStatus.CREATED

    def delete(self, value: str) -> (NoContent, HTTPStatus):
        # TODO: Remove all usages of category in other files
        if value not in self.search():
            return NoContent, HTTPStatus.NOT_FOUND, {'x-error': f'{self.item_name} does not exists'}

        root = self.__read()
        container = root.find(self.container_name)
        for x in container.findall(f'.//{self.item_name}[@name="{value}"]'):
            container.remove(x)
        self.__write(root)
        return NoContent, HTTPStatus.NO_CONTENT
