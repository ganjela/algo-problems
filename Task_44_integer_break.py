"""
assuming n >= 2
If n <= 3 we get maximum by:
3 = 2 + 1 product = 2 x 1 rather than  1 x 1 x 1
2 = 1 + 1 product = 1 x 1

if n >= 4 for integer m
we get maximum product by breaking down m in such way
m = 3 + 3 + 3 + 3 + ... if m is divided by 3 without reminder
if reminder == 1
m = 4 + 3 + 3 + 3 ...
if reminder == 2
m = 2 + 3 + 3 + 3 ...

(don't use ones and instead use as many threes as possible.
for example, n = 10 instead of n = 3 + 3 + 3 + 1 use one 4 and two 3, n = 4 + 3 + 3)


"""
def get_maximum_product(n):
    if n <= 3:
        return n-1

    if n % 3 == 0:
        return pow(3, n//3)
    elif n % 3 == 1:
        return 4 * pow(3, (n-4)//3)
    else:
        return 2 * pow(3, (n-2)//3)