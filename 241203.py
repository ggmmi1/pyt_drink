#while문 실습
i = 0
while i <5:
    i += 1
    print("안녕하세요", i)
print('끝')

#1부터10까지 홀수만 나타내기
num = 0
while num < 10:
    num = num +1
    if num % 2 == 0:
        continue #아래 print문 실행 x
    print(num)

#for문 실습
shop = ["반팔", "바지", "이어폰", "키보드"]
for i in shop:
    print(i)
 
#실습1. 1부터 사용자가 입력한 수까지 정수의 합 계산   
n = int(input("어디까지 계산할까요?"))
sum = 0
 
for i in range(1, n+1):
    sum += i
print(f'\n합계: {sum}')

#실습 번외 홀수의 합만 구하기 
n = int(input("어디까지 계산할까요?"))
for i in range(num):
    if i %2!=0:
        num+=i
print(num)

#실습 입력한 숫자만큼 카운트하고 "발사" 출력
n = int(input("몇 초?"))


for i in range(n,0,-1):
    print(i,end="") # end = "": 줄을 바꾸지 않고 스페이스만 출력하라는 의미
print("발사!")

#실습 구구단 만들기 - 사용자가 입력한 숫자의 구구단 출력
n =  int(input("몇 단을 출력할까요?"))
         
for i in range(1,10):
    result = n*i
    print(f"{n} * {i} = {result}")
    

#표현식 for 항목(요소) in 리스트
a=[1,2,3,4,5]
a1=[]
a2=[]
a3=[]
a4=[]

a3 = [i*3 for i in a]
print(a3)

a4 = [i*3 for i in a if i%2==0]
print(a4)
    
#이중 for문
for y in range(3):
    for x in range(2):
        print(f"y:{y}, x:{x}")
    print()  

for i in range(2,10):
    print(f'[{i} 단]')
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()
    
#자리배치도
print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1

for i in range(0, row):
    for j in range(1, column + 1):
        seat = i * column + j
        if seat > customer:
            break
        print(seat, end=" ")
    print()
    
#실습4 별 찍기 - 아래와 같이 출력되도록 코드를 작성 
#1번
n =  int(input("몇 줄?"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="") 
    print()
    
#2번
n =  int(input("몇 줄?"))
for i in range(1,n+1):
    print(" " * (n-i)+ "*"*i)

#3번
n =  int(input("몇 줄?"))
for i in range(1,n+1):
    print(" " * (n-i)+ "*" * (2 * i -1))
    
# 리스트 평균 구하기 
n = list(map(int,input("숫자 여러 개 입력: ").split()))
print(n)
a = max(n)
print("가장 큰 값: ", a)
b = min(n)
print("가장 작은 값: ", b)

n.remove(a)
n.remove(b)
ave = sum(n)/len(n)
print("나머지 값의 평균: ", ave)






