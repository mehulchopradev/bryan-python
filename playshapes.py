# Manager

from com.abc.geometry.square import Square
from com.abc.geometry.rectangle import Rectangle
from com.xyz.shape_stats import ShapeStats
from com.abc.geometry.shape import Shape

def validate_shape(shape):
  return isinstance(shape, Shape)

s = Square(side=5)
r = Rectangle(length=6, breadth=3)

'''print(s.area())
print(s.perimeter())'''


if validate_shape(s):
  ShapeStats.print_stats(s)
else:
  print('Not a valid Square')

if validate_shape(r):
  ShapeStats.print_stats(r)
else:
  print('Not a valid rectangle')

if validate_shape('hello world'):
  ShapeStats.print_stats('hello world')
else:
  print('Not a valid one')