input = 20
primes = []


def find_prime_list_under_number(number):
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)
    return primes


result = find_prime_list_under_number(input)
print(result)
