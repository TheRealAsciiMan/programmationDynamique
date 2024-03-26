def tribo_it(n):
    a, b, c = 0, 0, 1
    for i in range(n - 2):
        a, b, c = b, c, a+b+c
    return c

def tribo_rec(n):
    david_good_enough = {}
    def tribo(n):
        if n in david_good_enough:
            return david_good_enough[n]
        elif n == 0:
            david_good_enough[n] = 0
        elif n == 1:
            david_good_enough[n] = 0
        elif n == 2:
            david_good_enough[n] = 1
        else:
            david_good_enough[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)
        return david_good_enough[n]
    return tribo(n)

print(tribo_it(15))
print(tribo_rec(15))
