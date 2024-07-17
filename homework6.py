my_dict = {'Tailo': 2002, 'Ilgiz': 2002, 'Olivia': 2005, 'Isla': 2004}
print(my_dict)
print(my_dict.get('Tailo'))
print(my_dict.get('Akbulat'))
my_dict.update({'Akbulat': 2000 ,'Stephan': 2006})
print(my_dict)
print(my_dict.pop('Olivia'))

my_set = {1, 2,'dog', 3.4, 3.45, 1, 1, 1.2, 'dog'}
print(my_set)
my_set.add(6)
my_set.add(7)
print(my_set)
my_set.remove(3.45)
print(my_set)
