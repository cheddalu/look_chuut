from datetime import datetime
birth_year = int(input('What year were you born? '))
current_year = datetime.now().year
age = current_year - birth_year
print(f'Today you are {age} years old')