
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
print(loop1())

def loop1Rec(num,odd_sum):
    if num <= 20:
        if (num % 2) == 1:
            odd_sum += num
        num += 1
        return loop1Rec(num, odd_sum)
    else:
        return odd_sum
    
print(loop1Rec(0,0))

print("________________________")


def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
print(loop2())

def loop2Rec(num,even_sum):
    if num < 20:
        if (num % 2) == 0:
            even_sum += num
        num += 1
        return loop2Rec(num, even_sum)
    else:
        return even_sum
print(loop2Rec(0,0))