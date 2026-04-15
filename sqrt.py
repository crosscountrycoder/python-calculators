"""
Calculates the square root of an integer using Newton's method.
Examples:
python3 sqrt.py 2 30 - Prints sqrt(2) to 30 decimal digits of precision (after the decimal point)
python3 sqrt.py 3 1000000 write - Writes a file, sqrt3_1000000.txt, with 1 million digits of sqrt(3) after the decimal point.
Using the write option, each line contains 100 decimal digits.
"""
import sys
import helpers
from gmpy2 import mpfr, mpz, get_context
from time import perf_counter
from math import isqrt

def squareRoot(n: int, bits: int) -> mpfr:
    if n < 0:
        return None
    if n < 2:
        return mpfr(n)
    
    # Find integer square root (initial guess)
    int_sqrt = isqrt(n)
    if int_sqrt ** 2 == n: # if n is a perfect square
        return mpfr(int_sqrt)
    
    # If n is not a perfect square, find the square root to given precision
    n_mpz = mpz(n)
    p = mpz(int_sqrt) + 1
    q = mpz(1)
    e = (n.bit_length() - 1) // 2 # error bound: abs(p/q-sqrt(n)) / sqrt(n) < 2**-e
    while e < bits:
        p0 = p
        q0 = q
        p = p0 ** 2 + n_mpz * q0 ** 2
        q = 2 * p0 * q0
        e = 2 * e + 1
    return mpfr(p) / mpfr(q)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Syntax:")
        print("python3 sqrt.py <n> <d> (Prints sqrt(n) to d digits after the decimal point)")
        print("python3 sqrt.py <n> <d> write (Writes a text file containing d digits of sqrt(n) after the decimal point)")
        exit(1)

    start = perf_counter()

    n = int(sys.argv[1])
    num_digits = int(sys.argv[2])
    if n < 0:
        print("Square root of a negative number is not real")
    if num_digits < 0:
        print("Number of digits must be greater than or equal to 0")
        exit(1)

    bits = helpers.bits_needed(num_digits) + (n.bit_length() + 1) // 2
    ctx = get_context().copy()
    ctx.precision = bits
    with ctx:
        sqrt_n = squareRoot(n, bits)
        sqrt_string = format(sqrt_n, f".{num_digits}Zf")

    if len(sys.argv) >= 4 and sys.argv[3] == "write":
        file_name = f"sqrt{n}_{num_digits}.txt"
        with open(file_name, "w") as f:
            f.write(helpers.format_for_file(sqrt_string))
        print(f"Wrote {file_name}")
    else:
        print(sqrt_string)

    end = perf_counter()
    helpers.print_time(start, end) # evaluate runtime of algorithm