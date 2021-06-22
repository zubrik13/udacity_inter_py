import os


# infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        print(num) # just hint
        num += 1


# fibonacci generator
def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def fibs_under(n):
    for fib in generate_fibs():  # Loops over 1, 1, 2, ...
        if fib > n:
            break
        print(fib)


# tribonacci generator
def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    while True:
        a, b, c = b, c, a + b + c
        yield a


def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    for fib in generate_tribonacci_numbers():
        if fib == num:
            return num in generate_tribonacci_numbers()
        if fib > num:
            return False


if __name__ == "__main__":
    g = infinite_sequence()
    next(g)
    next(g)

    print(is_tribonacci(4))
    print(is_tribonacci(5))
    print(is_tribonacci(13))

    # reading csv data
    file_name = "techcrunch.csv"
    print(os.path.exists("techcrunch.csv"))
    lines = (line for line in open(file_name))
    list_line = (s.rstrip().split(",") for s in lines)
    cols = next(list_line)
    company_dicts = (dict(zip(cols, data)) for data in list_line)
    funding = (
        int(company_dict["raisedAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )
    total_series_a = sum(funding)
    print(f"Total series A fundraising: ${total_series_a}")

