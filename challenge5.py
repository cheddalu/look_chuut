'''
Coding challenge part 5 
Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
'''

def divide_conquer(a,b):  
    try:
        return a/b
    except ZeroDivisionError:
        print("Oops you can't divide by zero")
        return 0
    
a = int(input('Enter in 1st int: '))
b = int(input('Enter in 2nd int: '))

result = divide_conquer(a, b)
print(result)

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("There is a divide by zero error")
#         return 0


# x = float(input('Enter a number'))
# y = float(input('Enter value by which you want to divide the number'))
# result = divide(x, y)
# print(result)