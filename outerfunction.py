x = 10
def outer_function():
  #  print(f"value of x in outer function {x}")
    x = 20 
    print(f"value of x in outer function after modificatioin {x}")
    def inner_function():
  #       print(f"value in inner function before modification is {x}")
        x = 30
        print(f"value in inner function{x}")
    inner_function()
    print(x)
    
print(f"value of x in global scope before function execution {x}")

outer_function()
print(f"value of x in global scope after function execution {x}")
