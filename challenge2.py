'''Coding challenge part 2.
Create a list of your favorite food items, the list should have minimum 5 elements.
List out the 3rd element in the list.
Add additional item to the current list and display the list.
Insert an element named tacos at the 3rd index position of the list and print out the list elements.
'''

fav_foods = ['eggs', 'pizza', 'cupcake', 'burger', 'salmon']
print(fav_foods[2])
fav_foods.append('cake')
print(fav_foods)
# print(len(fav_foods))
fav_foods.insert(3,'tacos')
print(fav_foods)
# print(len(fav_foods))
