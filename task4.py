# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_list = 'фаб абв привет жестокий абв'
print(my_list)

res_list = [x for x in my_list.split('абв')]
print(''.join(res_list))