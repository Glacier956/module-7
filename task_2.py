print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

summ_salary = 0

for month in range (1, 13):
  salary = int(input("Введите зарплату за " + str(month) + " месяц: "))
  summ_salary += salary
  average_salary = summ_salary / 12
print("Средняя заплата за год:", average_salary)
