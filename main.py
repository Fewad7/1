f = open("space.txt", encoding = "UTF-8").read()
f = f.split("/n")
a = []

for el in f:
    a.append(el.split("#"))

f = open("space_new.txt", "w")
for s in a:
    if s[2] == "0 0":
        print(s[3])
        xd, yd = s[3].split()
        code, number = s[0].split("-")
        n = int(number[0])
        m = int(number[1])
        t = len(s[1])
        if n > 5:
            x = n + int(xd)
        else:
            x = -(n+int(xd))*4 + t
        if m > 3:
            y = m+t+int(yd)
        else:
            y = -(n + int(yd))*m

        s[2]= str(x)+ " " + str(y)
        if code[-1] == "V":
            f.write("<" + code + "> - <" + str(x) + ">, <" + str(y) + ">")


def getNumber(name):
    code, number = s[0].split("-")
    return numder


for i in range(1, len(a)):
    x = a[i]
    j = i
    while j>0 and float(getNumber(a[j-1][0])) > float(getNumber(x[0])):
        a[j] = a[j-1]
        j-=1
    a[j] = x

b= a[:10]
for el in b:
    print(el[0])


while True:
    s = input("Ввод")
    if s == "Stop":
        break
    f = 0
    for el in a:
        if el[0] == s:
            print("Корабль" + el[0] + "был отправлен с планеты:" + el[1] + "направление" + el[])