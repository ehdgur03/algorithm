n = int(input())        #0보다 크거나 같고, 99보다 작거나 같은 정수 입력            
num = n                 #입력받은 수를 변수로 저장
cycle = 0               #사이클 길이 초기화

while True:
    cycle += 1          #사이클 길이 1씩 증가시키기
    tens = num // 10    #10의 자리
    ones = num % 10     #1의 자리
    next_num = tens + ones #새로운 다음 수 
    if next_num == n:       #다음 수가 n이랑 같으면 중단
        break

print(cycle)