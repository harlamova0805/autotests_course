import pymorphy3
morph = pymorphy3.MorphAnalyzer()
p = morph.parse('инженеры-тестировщики')[0]
print(p)


job_title = 'инженеры-тестировщики'
#  Творительный падеж - ablt
#job_title_1.inflect({'ablt'})




name = 'Надежда Харламова'
job = 7  # Стаж
#  job_title = 'инженером-тестировщиком'  # Должность
"""
print('Меня зовут -', name)
print('Я работаю -', job_title.)
print('Мой стаж работы -', job, 'лет')
https://pymorphy2.readthedocs.io/en/stable/user/guide.html
"""


print(f'Меня зовут {name}.\nЯ работаю {job_title}.\nМой стаж работы - {job} лет.')



"""
Нормальное решение
"""
name = 'Надежда Харламова'  # Можно разделить фамилию и имя в 2 переменные, но в задании они были в 1 строку,
# поэтому так оставила
job = 7  # Стаж
job_title = 'инженером-тестировщиком'  # Должность

# Вывод на разных строках, несколько print
print('Меня зовут -', name)
print('Я работаю -', job_title)
print('Мой стаж работы -', job, 'лет')
print('\n')  # Чтобы отделить 2 варианта решения на выводе

# Вывод на разных строках через один print
print(f'Меня зовут {name}.\nЯ работаю {job_title}.\nМой стаж работы - {job} лет.')