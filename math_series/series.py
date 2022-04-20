def fibonacci(n): 
  if n == 1: 
    return 0
  elif n == 2: 
    return 1 
  else: 
    return fibonacci(n-2) + fibonacci(n-1)

def lucas(n): 
  if n == 1: 
    return 2 
  elif n == 2: 
    return 1 
  else: 
    return lucas(n-2) + lucas(n-1)

def sum_series(n, num1=0, num2=1): 
  if n == 1: 
    return num1
  elif n == 2: 
    return num2
  else: 
    return sum_series(n-2, num1, num2) + sum_series(n-1, num1, num2)