import xml.etree.ElementTree as ET
from typing import List, NamedTuple

class Flags(NamedTuple):
    count_in_cargo: int = 0
    count_in_hoarder: int = 0
    count_in_map: int = 1
    count_in_player: int = 0
    crafted: int = 0
    deloot: int = 0

    @staticmethod
    def from_xml(data: ET.Element):
        return Flags(
            count_in_cargo=data.attrib['count_in_cargo'],
            count_in_hoarder=data.attrib['count_in_hoarder'],
            count_in_map=data.attrib['count_in_map'],
            count_in_player=data.attrib['count_in_player'],
            crafted=data.attrib['crafted'],
            deloot=data.attrib['deloot']
        )

class Loot(NamedTuple):
    name: str
    nominal: int
    lifetime: int
    restock: int
    min: int
    quantmin: int
    quantmax: int
    cost: int
    flags: Flags
    categories: tuple
    usages: tuple
    tiers: tuple

    @staticmethod
    def from_xml(data: ET.Element):
        return Loot(
            name=data.attrib['name'],
            nominal=data.find('nominal').text,
            lifetime=data.find('lifetime').text,
            restock=data.find('restock').text,
            min=data.find('min').text,
            quantmin=data.find('quantmin').text,
            quantmax=data.find('quantmax').text,
            cost=data.find('cost').text,
            flags=Flags.from_xml(data.find('flags')),
            categories=tuple(x.attrib['name'] for x in data.findall('category')),
            usages=tuple(x.attrib['name'] for x in data.findall('usage')),
            tiers=tuple(x.attrib['name'] for x in data.findall('value'))
        )