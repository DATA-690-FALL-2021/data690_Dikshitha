def addition(x,y):
  return x+y

def substraction(x,y):
  return x-y

def add(x,y):
  if x.isnumeric() and y.isnumeric():
    return int(x)+int(y)
  else:
    raise ValueError('The inputs must be numberic')
  
