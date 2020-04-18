name = input("What is your name? ")
weight = int(input("How many lbs are you? "))
height = int(input("Give me your height in inches: "))

# weight = 270
# height = 70
# print(type(weight))
# print(type(height))

def bmi_calculator(name, weight, height):
    bmi = round((weight * 703) / (height ** 2),2)
    print(name + ", your bmi is: " + str(bmi))
    if (bmi < 18.5): 
        print('You\'re a bit underweight')
    elif (bmi >= 18.5 and bmi <= 24.9):
        print('Congratulations you\'re normal')
    elif (bmi >= 25 and bmi <= 29.9):
        print('You\'re a bit overweight')
    else: 
        print('You\'re considered obese. Start getting more active.')

bmi_calculator(name, weight, height)
