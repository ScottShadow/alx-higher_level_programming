#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if not isinstance(id, type(None)):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        listdict = []
        for obj in list_objs:
            listdict.append(obj.to_dictionary())
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(cls.to_json_string(listdict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        newobj = cls(1, 1)

        newobj.update(**dictionary)

        return newobj

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        listdict = {}
        with open(filename, 'r+', encoding='utf-8') as f:
            listdict = f.read()
        newdict = json.loads(listdict)
        newlistobj = []
        for obj in newdict:
            newobj = cls.create(**obj)
            newlistobj.append(newobj)
        return newlistobj
