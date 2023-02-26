# a
def prime(n):
    if n <= 2:
        return False
    i = 2
    while i != n:
        if n % i == 0:
            return False
            break
        else:
            i += 1
    return True
# b
def select_primes(x):
    prime_list = []
    for i in x:
        if prime(i) == True:
            prime_list.append(i)
    return prime_list

print(select_primes([3, 6, 11, 25, 19]))