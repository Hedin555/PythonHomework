def my_func(**kwags):
    return kwags


total = my_func(
    name=input('Name: '),
    surname=input('Surname: '),
    date=input('Birthday: '),
    city=input('City: '),
    mail=input('Mail: '),
    phone=input('Phone: ')
         )

print(total)
