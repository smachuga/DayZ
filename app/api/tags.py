from api.controller import Controller
from typing import List

class TagsService():
    ctl = Controller(
        file_name='./dayzOffline.chernarusplus/cfglimitsdefinition.xml',
        container_name='tags',
        item_name='tag'
    )
    
    def get(self) -> List[str]:
        return ctl.search()

    def create(self, value: str) -> bool:
        return ctl.post(value)

    def delete(self, value: str) -> HTTPStatus:
        return ctl.delete(value)
