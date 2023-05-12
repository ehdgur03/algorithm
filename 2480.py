num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 == num3 :
    print(10000 + num1 * 1000)
elif num1 == num2 and num1 != num3:
    print(1000 + num1 * 100)
elif num1 == num3 and num1 != num2:
    print(1000 + num1 * 100)
elif num2 == num3 and num1 != num2:
    print(1000 + num2 * 100)
else : 
    #여기서 가장 큰 눈이 나오게 하는 법을 모르겠어용 ㅠ ㅠ