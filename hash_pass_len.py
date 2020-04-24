usr_name = input('What is your username? ')
password = (input('Enter in a password: '))

hash_len = len(password)
hash_pass = '*' * hash_len
print(f'Hi {usr_name} your password {hash_pass} is {hash_len} letters long')