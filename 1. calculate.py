a= input()        #문자열로 입력 받음.
b= input()
#print(type(a), type(b))
l = len(b)-1
while (l>=0):
    print(int(a)*int(b[l]))
    l -= 1
print(int(a)*int(b))