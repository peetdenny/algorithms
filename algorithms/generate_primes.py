primes = [2]


def generate():
    curr = 3
    while True:
        if is_prime(curr):
            primes.append(curr)
            print 'new prime found', curr
        curr += 2


def is_prime(candidate):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

if __name__ == '__main__':
    generate()


