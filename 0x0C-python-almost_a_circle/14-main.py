#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    r2 = Square(10, 3, 4)
    dictionary2 = r2.to_dictionary()
    json_dictionary = Base.to_json_string([])
    print(json_dictionary)
    print(type(json_dictionary))
