'''Coding challenge part 4
Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:

 BMI = (weight in Kg)/(Height in Meters)^2.

Write python code which can accept the weight and height of a person and calculate his BMI.

note: Make sure to use a function which accepts the height and weight values and returns the BMI value.
'''

w = int(input('what is weight? '))
h = int(input('what is height? '))

def bmi_calc(w,h):
    return (w / (h * h))

bmi = bmi_calc(w, h)
print(bmi)

#Solution
# def calculate_BMI(new_weight, new_height):
#     new_bmi = new_weight/(pow(new_height, 2))
#     return new_bmi

# weight = float(input('Enter weight in Kgs'))
# height = float(input('Enter height in meters'))
# bmi = calculate_BMI(weight, height)
# print(bmi)