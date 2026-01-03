#2739번
a= int(input())
for i in range(1, 10):
   #range(start, end, step) -> start부터 end-1까지 step만큼 증가하며 반복,
   #range(end) -> 0부터 end-1까지 반복, step 생략 시 1
   print(f"{a} * {i} = {a*i}")
   #f-string -> 문자열 앞에 f를 붙여 변수나 표현식을 중괄호{} 안에 넣어 문자열로 삽입하는 방법


#10950번
n= int(input())
for i in range(0, n):
    a, b= map(int, input().split())
    print(a+b)


#8393번
n= int(input())
sum=0
for i in range(1, n+1):
    sum += i
print(sum)


#25304번
total= int(input())
n= int(input())
sum=0
for i in range(n):
    price, count= map(int, input().split())
    sum += price*count
if sum == total:
    print("Yes")
else:
    print("No")


# 25314번
n= int(input())
for i in range(n//4):
    print("long", end=" ")
print("int")
# end 매개변수 -> print 함수가 출력 후 끝나는 방식을 지정, 기본값은 줄바꿈(\n)
# n//4이 0일 경우 for문이 실행되지 않아 "int"만 출력됨
# 예시: n=8 -> "long long int"


#15552번
import sys
n= int(sys.stdin.readline())
for i in range(n):
    a, b= map(int, sys.stdin.readline().split())
    print(a+b)
# sys.stdin.readline() -> 표준 입력에서 한 줄을 읽어오는 함수, input()보다 빠름
# 많은 양의 입력을 처리할 때 유용함
# 예시: n=3, 입력: "1 2\n3 4\n5 6\n" -> 출력: "3\n7\n11\n"


#11021번_readline 사용_36ms_140B
import sys
t= int(sys.stdin.readline())
for i in range(t):
    a, b= map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')
#11021번_input 사용_40ms_103B
t= int(input())
for i in range(t):
    a, b= map(int, input().split())
    print(f'Case #{i+1}: {a+b}')


#11022번_readline 사용_36ms_152B
import sys
t= int(sys.stdin.readline())
for i in range(t):
    a, b= map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
#11022번_input 사용_36ms_115B
t= int(input())
for i in range(t):
    a, b= map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')


#2438번
n= int(input())
for i in range(1, n+1):
    print('*' * i)
# print 안에 문자열*n -> 문자열을 n번 반복하여 출력


#2439번
n= int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
# 공백(n-i) + 별(i) -> 오른쪽 정렬된 별 출력


#10952번_input 사용_36ms_94B
while True:
    a, b = map(int, input().split())
    if a==b==0:
        break
    print (a+b)
#10952번_sys.stdin.readline 사용_32ms_124B
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==b==0:
        break
    print (a+b)
#10952번_예외 처리 풀이
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a==b==0:
            break
        print (a+b)
    except EOFError:
        # EOFError -> 입력이 더 이상 없을 때 발생하는 예외, 주로 파일 끝에 도달했을 때 발생
        # 다만 성능과 가독성이 떨어져서 라이브러리 내부가 아닌 이상 잘 안씀.
        break
#10952번_for line in sys.stdin 사용_36ms_112B
import sys
for line in sys.stdin:
    # 표준 입력에서 한 줄씩 꺼내서 그 줄을 line에 넣어라.
    # sys.stdin -> 표준 입력 스트림을 나타내는 객체(입력 통로라고 보면 됨)이고,
    # 반복가능한(iterable) 객체이므로 for문으로 한 줄씩 읽을 수 있다.
    # while true와 readline()을 합친 것과 비슷한 효과이다.
    # 추가로, EOF 도달 시 내부적으로 멈추기 때문에 예외처리도 필요없다.
    a, b = map(int, line.split())
    if a==b==0:
        break
    print(a+b)
# for line in sys.stdin -> 표준 입력의 각 줄을 반복하여 처리
# line.split() -> 각 줄을 공백 기준으로 나누어 리스트로 반환


#10951번
import sys
for line in sys.stdin:
# for line in sys.stdin.readline():
# 로 적을 경우 한 줄 문자열을 문자 단위로 반복함.
# 따라서 "1 2\n"이 들어오면 '1', ' ', '2', '\n'로 반복하게 되어 오류 발생.
    a, b = map(int, line.split())
    print(a+b)
# 리눅스나 맥 환경에서는 Ctrl + D
# 윈도우 환경에서는 Ctrl + Z를 눌러 EOF(End Of File)를 입력할 수 있다.




# 전체 주석처리 시 단축키
# Ctrl + / (윈도우, 리눅스)
# Command + / (맥)