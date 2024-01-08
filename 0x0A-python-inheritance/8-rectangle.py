#!/usr/bin/python3
geometry_module = __import__('7-base_geometry')
BaseGeometry = getattr(geometry_module, 'BaseGeometry')


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        base_geometry_instance = BaseGeometry()
        if base_geometry_instance.integer_validator("width", width):
            width.self = width
        if base_geometry_instance.integer_validator("height", height):
            height.self = height
