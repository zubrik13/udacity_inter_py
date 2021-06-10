def product(*nums, start=1):
    running_product = start
    for number in nums:
        running_product *= number
    return running_product

if __name__ == "__main__":
    test = product(3, 4, 2, 5)
    print(test)

    # iterables
    primes = (2, 3, 5, 7, 11)
    test2 = product(*primes)
    print(test2)