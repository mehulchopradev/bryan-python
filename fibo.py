n = int(input('Enter n : '))

# n = 8 : 0 1 1 2 3 5 8 13
'''
1st 0 a
2nd 1 b a
3rd 1 c b a
4th 2   c b
5th 3     c
'''

a, b = 0, 1
print(a)
print(b)

# 3 to n
for v in range(3, n + 1):
  c = a + b
  print(c)
  a, b = b, c