num1 = int(input())
num2 = int(input())
n = list(str(num2))
n.reverse()
for i in n:
    print(num1 * int(i))
print(num1*num2)