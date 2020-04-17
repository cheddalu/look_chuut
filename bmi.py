# weight = int(input("How many lbs are ya? "))
# height = int(input("Give me your height in inches: "))

# bmi_weight = (weight * 703)
# bmi_height = (height ** 2)

# bmi = round((bmi_weight / bmi_height),2)

# print(f'Your BMI is {bmi}')

weight = 180.5

height = 70
# print(type(weight))
# print(type(height))

def bmi_calculator(weight, height):
    # print(weight)
    # print(height)
    # htsq = (height ** 2)
    # print(htsq)

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



# bmi = 18
# if bmi < 18.5: 
#     print('Underweight')
# else: 
#     if bmi > 30.0:
#         print('Obesly fat')
    # elif bmi in range(18.5,24.9):
    #     print('Normal')
    # elif bmi in range(25,29.9):
    #     print('Overweight')


# def bmifunction(x):
#     return 2*x

# a = bmifunction(3)

# print(a)
