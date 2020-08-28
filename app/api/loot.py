import sys
#import config
import requests
from flask import Flask, request, Response, jsonify
from flask_restful import Api, Resource, reqparse
from flasgger import Swagger, swag_from
import concurrent.futures
import xml.etree.ElementTree as ET
from typing import List, NamedTuple
from dto.loot import Loot

class LootService(Resource):
    

    def load() -> ET.ElementTree:
        return ET.parse('./dayzOffline.chernarusplus/db/types.xml')

    # @swag_from("../swagger/loot.yml")
    def get(self) -> List[Loot]:
        items = sorted(load().getroot().findall('type'), key=lambda x: x.attrib['name'])
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(Loot.from_xml, items))
            return results
