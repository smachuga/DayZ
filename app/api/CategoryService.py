from dataclasses import dataclass
from api.BaseService import BaseService

@dataclass(init=True,frozen=True)
class CategoryService(BaseService):
    file_name='./dayzOffline.chernarusplus/cfglimitsdefinition.xml'
    container_name='categories'
    item_name='category'