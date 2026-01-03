#1330번
a, b= map(int, input().split())
if a>b:
    print(">")
elif a==b:
    print("==")
else:
    print("<")


#2753번
a= int(input())
if (a%4==0 and a%100!=0) or (a%400==0):
    print("1")
else:
    print("0")


#14681번
a= int(input())
b= int(input())
if a>0 and b>0:
    print("1")
elif a<0 and b>0:
    print("2")
elif a<0 and b<0:
    print("3")
else:
    print("4")


#2884번
h, m = map(int, input().split())
if m>=45:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else:
    print(23, m+15)


#2525번
h, m = map(int, input().split())
t = int(input())
h = (h + (m + t) // 60) % 24
m = (m + t) % 60
print(h, m)


#2480번
a, b, c = map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(max(a, b, c)*100)