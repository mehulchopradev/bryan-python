# it can accept 0 to n arguments (parameters)
def myadd(*args):
  # print(args) # tuple object consisting of the parameters passed during the function call
  sum = 0
  for arg in args:
    sum += arg
  return sum

# positional arguments packing
print(myadd()) # 0
print(myadd(5)) # 5
print(myadd(5, 5, 2)) # 12
print(myadd(5, 6, 7, 8, 2, 3, 4, 5))


def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (5, 3) # can be a list too
print(perimeter(stats[0], stats[-1]))
print(perimeter(*stats)) # unpacking to positional parameters


def area(**rect_stats):
  # print(rect_stats) # is a dictionary consisting of the keyword arguments passed during the function call
  return rect_stats['length'] * rect_stats['breadth']

# print(area(5.3, 3.4))
print(area(length=5.3, breadth=3.4)) # keyword arguments packing
# print(area(l=5.3, b=3.4)) # this will not work

stats_map = {'breadth': 4, 'length': 6}
print(perimeter(stats_map['length'], stats_map['breadth']))
print(perimeter(**stats_map)) # dictionary data is unpacked to the respective positional parameters