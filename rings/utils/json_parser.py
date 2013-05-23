# coding=utf-8

import json


class JSONParserException(Exception):
    pass


class JSONParser(object):

    @staticmethod
    def to_json(collection):
        """
        Serialize a Python Collection to a JSON String

        collection: Python Collection
        Returns: String
        """
        try:
            json_str = json.dumps(collection)
            return json_str
        except Exception as e:
            raise JSONParserException(e)

    @staticmethod
    def to_collection(json_str):
        """
        Deserialize a JSON String into a Python Collection

        json_str: String
        Returns: Python Collection
        """
        try:
            collection = json.loads(json_str)
            return collection
        except Exception as e:
            raise JSONParserException(e)
