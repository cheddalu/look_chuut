# weight = int(input("How many lbs are ya? "))
# height = int(input("Give me your height in inches: "))
weight = 180.5
height = 70

# print(type(weight))
# print(type(height))

def bmi_calculator(weight, height):
    bmi = round((weight * 703) / (height ** 2),2)
    print("bmi: " + str(bmi))
    if (bmi < 18.5): 
        print('You is underweight')
    elif (bmi >= 18.5 and bmi <= 24.9):
        print('You\'re normal')
    elif (bmi >= 25 and bmi <= 29.9):
        print('You\'re overweight')
    else: 
        print('You obese!!!')

bmi_calculator(weight, height)
