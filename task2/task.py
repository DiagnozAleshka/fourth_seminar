""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """

x = int(input("введите число: "))
if x == 1 or x == 2 or x == 3 or x == 5 or x == 7:
    print("вы ввели простое число")

list1=[]
i = 2
while i <= x:
    if x %i==0:
        list1.append(i)
        x //= i
        i = 2
    else:
      i +=1
print (list1)