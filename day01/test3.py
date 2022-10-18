from itertools import count

from sympy import NumberSymbol


def seperate():
    a = int(input('수 입력'))
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')


def addResult(a, b):
    return a+b


def sum(num):
    sum = 0
    for i in range(1, num+1):
        print(i)
        sum += i
    return sum


nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]


def max_count(nums):
    counts = {}
    for i in nums:
        # max_count[i] = nums.count(i)
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


counts = max_count(nums)
print(counts)  # {1: 4, 2: 4, 3: 5}
print("counts 최대값 ", max(counts.values()))
##########################################
first = []  # List형
maxValue = max(counts.values())
for name, count in counts.items():
    print(name, ":", count)
    if(count == maxValue):
        first.append(count)
print('first:', first)
##########################################
print(counts.values())
# seperate()


print(addResult(3, 5))
ret = addResult(10, 20)
print(ret)
print("sum :", sum(10))  # 1부터 10까지의 합
