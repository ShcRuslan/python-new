num=int(input('Введите число: '))
num=str(num)
my_list=[]
for i in num:
    my_list.append(i)
for n in range(len(my_list)):
    if my_list[n]==my_list[-(n+1)]:
        count=0
    else:
        count=1
if count==0:
    print('True')
else:
    print('False')