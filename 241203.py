
    
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






