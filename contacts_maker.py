filename = input('What is the file name? ')
contact = input('Please enter contacts in the format "Name, email", followed by a return. When finished enter "d" for "done": ')    
address_book = {}
while contact != 'd' and contact != 'done':
    person = contact.split(",")
    address_book[person[0].strip()] = person[1].strip()
    contact = input('Enter another contact as "name, email" (or type "d" to finish): ')
print(address_book)

with open(filename, "w") as contacts:
    content_str = ''
    for key, value in address_book.items():
        content_str += f'{key}: {value}\n'
    contacts.write(content_str.rstrip())
# with open(filename, "a") as contacts:
#     for key, value in address_book.items():
#         contacts.write(f'{key}: {value}\n')

open_file = input(f'would you like to review {filename}? (Y / N) ')
if open_file.lower() in ['y', 'yes']:
    with open(filename, 'r') as file:
        print(file.read())