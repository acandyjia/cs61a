# 相互递归
# 迭代是递归的一种特例
def spilt(n):
    return n//10,n%10

def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last , last =spilt(n)
        return sum_digits(all_but_last) + last
    

def luhn_sum(n):
    """
    The Luhn Algorithm
    Used to verify credit card numbers
    From Wikipedia: http://en.wikipedia.org/wiki/Luhn algorithm
    1. From the rightmost digit, which is the check digit, moving left, 
    double the value ofevery second digit; 
    if product of this doubling operation is greater than 9 (e.g., 7 *2=14),
    then sum the digits of the products(e.g.,10:1+0=1,14:1+4= 5).
    2.Take the sum of all the digits.
    3.Check: The Luhn sum of a valid credit card number is a multiple of 10.
    """
    if n < 10:
        return n
    else:
        all_but_last,last = spilt(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last , last = spilt(n)
    luhn_digit = sum_digits(2 * last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
    

if __name__ == "__main__":
    print(luhn_sum(114514))

"""
迭代是递归的一种特例：
迭代中在循环里发生变化的值 作为 递归的参数

def sum_digits_iter(n):
    digit_sum =0
    while n>0:
        n,last = spilt(n)
        digit_sum += last
    return digit_sum

def sum_digits_rec(n,digit_sum):
    if n==0:
        return digit_sum
    else:
        n,last=spilt(n)
        return sum_digits_rec(n,digit_sum+last)

"""