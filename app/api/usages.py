from connexion import NoContent
from api.controller import Controller
from http import HTTPStatus
from typing import List

ctl = Controller(
    file_name='./dayzOffline.chernarusplus/cfglimitsdefinition.xml',
    container_name='usageflags',
    item_name='usage'
)

def search() -> List[str]:
    return ctl.search()

def post(value: str) -> (NoContent, HTTPStatus):
    return ctl.post(value)

def delete(value: str) -> (NoContent, HTTPStatus):
    return ctl.delete(value)
