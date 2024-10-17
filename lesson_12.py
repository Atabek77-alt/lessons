# def multiplication_table(size):
#     nums = []
#     for i in range(1,size+1):
#         for j in range(1,size+1):
#             print(i * j, end="\t")
#             print()
            
#     return nums


# Dekoratory

# def my_decorator(func):
#     def wrapper():
#         print("Something is happined the function is called.")
#         func()
#         print("Something is happined the function is called.")
#     return wrapper


# @my_decorator
# def say_heello():
#   return
# say_heello()
     

# def my_decorator(func):
#     def wrapper(*args):
#         print("Something is happined the function is called.")
#         print(func(*args))

#         print("Kvadrat")
#     return wrapper


# @my_decorator
# def say_hello(num, num2):
#     return num+num2

# say_hello(5,5)


# neckolko decoratorov


# def my_decorator1(func):
#     def wrapper():
#         print("Something is happined the function is called.")
#         func()
        
#     return wrapper

# def my_decorator2(func):
#     def wrapper():
#         print("Something is happined the function is called.")
#         func()
       
#     return wrapper

# @my_decorator1
# @my_decorator2
# def say_hello():
#     print('hello')

# say_hello()


# decorator c args y cebya

# def repeat(num):
#     def decorator_repeat(func):
#         def wrapper(*args):
#             for i in range(num):

#                 func(*args)
#         return wrapper
#     return decorator_repeat

# @repeat(5)
# def say_hello(name):
#     print(f"Heello {name}")

# say_hello('Ali')



# 1.
# from random import randint

# def check_result(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)

#         if result > 10:
#             print("Result is greater than 10")
#         else:
#             print("Result is not greater than 10")
#             return result
#     return wrapper

# @check_result
# def random_number():

#     return randint(1 ,15)

# random_number()

# 3.

# from random import randint

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         number = func(*args,**kwargs)

#         if number % 2 != 0:
#             print("Result is not an odd number")
#         else:
#             print("Result is an odd number")
#             return number
#     return wrapper

# @my_decorator
# def random_number():
#     return randint(1,10)

# random_number()

# 2.
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#              func(*args, **kwargs)
#         except Exception as i:
#             print("An exception occurred!")
            
#             print(f"Exception: {i}")

#     return wrapper


# @my_decorator
# def number(a, b):
#     return a / b 

# number(10, 0)


