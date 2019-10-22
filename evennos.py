n = int(input('Enter n : '))

i = 0

# while loop

'''while i <= n:
  if not i % 2:
    print(i)
  i = i + 1'''


# for loop
'''
for v in <<sequence of elements>>:
  I1
  I2
  I3
'''

# 0 to n
# range(0, n + 1)

'''for v in range(n+1):
  if not v % 2:
    print(v)'''

for v in range(0, n + 1, 2):
  print(v)