#!/usr/bin/python3
from .base import *
from .rectangle import *


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super(Square, Square).width.fset(self, value)
        super(Square, Square).height.fset(self, value)

    def update(self, *args, **kwargs):
        if len(args) != 0:
            for (key, _), arg in zip(self.__dict__.items(), args):
                setattr(self, key, arg)
        elif len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        myself = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y
                  }
        return myself
