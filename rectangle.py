def area_rectangle(length, breadth):
  a = length * breadth
  return a

def perimeter_rectangle(length, breadth):
  p = 2 * (length + breadth)
  return p

l = float(input('Enter length: ')) # '5' -> 5.0
b = float(input('Enter breadth: '))

a = area_rectangle(l, b)
p = perimeter_rectangle(l, b)

# built in functions
print(a)
print(p)