def function1(x):
  return 1

def function2(x):
  return x

def function3(x):
  return x**2 - 3*x

def integral(function, a, b, dx):
    # function es un callBack
  result = 0
  x = a
  while (x + dx) <= b:
    result += function(x) * dx
    x += dx
  return result

print( integral(function1, 10, 15, 0.0001) )
print( integral(function2, 1, 2, 0.0001) )
print( integral(function3, 0, 3, 0.0001) )