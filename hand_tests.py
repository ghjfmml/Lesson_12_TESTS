from functions import salary, hello_who
# Тесты с омощью if
if salary != 20:
    print('Error')
if hello_who('Max') != 'Hello,Max':
    print('Failed')
else:
    print('Good')
if hello_who('Leo') != 'Hello,Leo':
    print('Failed')
else:
    print('Amazing')

if hello_who('Max') != 'Hello,Leo':
    print('Неповезло')
else:
    print('Молодец')
if hello_who('Leo') != 'Hello,Leo':
    print('Неповезло')
else:
    print('Удивительно')

'''print(hello_who('Max'))
print(salary(hours:2, salary_by_hours:10))
'''