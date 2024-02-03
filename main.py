f=open('students.csv').read()
f=f.split('\n')
a=[]
for i in f:
    a.append(i.split(','))
a=a[1:]
for el in a:
    if 'Хадаров Владимир' in el[1]:
        print('Ты получил: '+ el[4]+ ', за проект-'+el[2])
summ=0
cnt=0
for el  in a:
    if el[4]!='None':
        summ+=int(el[4])
        cnt+=1
avg=round(summ/cnt,3)
for el in a:
    if el[4]=='None':
        el[4]=str(avg)

f=open("student_new.csv","w")
for el in a:
    f.write(','.join(el)+'\n')

#2
for i in range(1,len(a)):
    x=a[i]
    j=i
    while j>0 and float(a[j - 1][4]) > float(x[4]):
        a[j] = a[j - 1]
        j-=1
    a[j]=x

b=[]
for el in a:
    if '10' in el[3] and el[4]=='5':
        b.append(el)

def getShortName(b):
    name = b.split()
    first = name[0]
    second = name[1]
    return second[0]+'. '+first

for i in range(3):

    shortName=getShortName(b[i][1])
    print(str(i+1)+' место: '+shortName)

3
while True:
    s=input('Введите id проекта или СТОП для выхода\n')
    if s=='СТОП':
        break
    flag=0
    for el in a:
        if el[2]==s:
            print('Проект № '+el[2]+ ' делал: '+getShortName(el[1])+' он(а) получил(а) оценку - '+el[4])
            flag=1
    if flag==0:
        print('Ничего не найдено')

# 4
import random
def f():
    A='QWERTYUIOPASDFGHJKLZXCVBNM'
    aa='qwertyuiopasdfghjklzxcvbnm'
    n='1234567890'
    A1 = random.randint(0,len(A)-1)
    A2 = random.randint(0, len(A)-1)
    A3 = random.randint(0, len(A)-1)
    a1 = random.randint(0, len(aa)-1)
    a2 = random.randint(0, len(aa)-1)
    a3 = random.randint(0, len(aa)-1)
    n1 = random.randint(0, len(n)-1)
    n2 = random.randint(0, len(n)-1)
    return A[A1]+A[A2]+A[A3]+aa[a1]+aa[a2]+aa[a3]+n[n1]+n[n2]
for el in a:
    fullname=el[1]
    parts=fullname.split()
    secondname=parts[1]
    lastname=parts[2]
    login=parts[0]+"_"+secondname[0]+lastname[0]
    password=f()
    el.append(login)
    el.append(password)


f=open("students_password.csv","w")
for el in a:
    f.write(','.join(el)+'\n')

#5
def hash(s):
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + ord(c) * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


f=open("students_with_hash.csv","w")
for el in a:
    f.write(str(hash(el[1]))+','+','.join(el[1:])+'\n')