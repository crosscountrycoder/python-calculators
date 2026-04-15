"""
Calculates e using its Taylor series: e = Σ(n=0..inf, 1/n!) = 1/0! + 1/1! + 1/2! + 1/3! + ...
Examples:
python3 e.py 30 - Prints e to 30 decimal digits of precision (after the decimal point)
python3 e.py 10000 - Prints e to 10000 decimal digits
python3 e.py 1000000 write - Writes a file, e_1000000.txt, with 1 million digits of e after the decimal point.
Using the write option, each line contains 100 decimal digits.
"""
import sys
import helpers
from gmpy2 import mpfr, mpz, get_context
from time import perf_counter
from math import log

def terms_needed(bits: int) -> int:
    """Estimates the number of terms in the Taylor series needed to compute e to the given number of bits,
    using Stirling's approximation. This value is always a slight overestimate, because Stirling's approximation
    is a lower bound for n!."""
    if bits <= 1:
        return 2
    t = 1
    while t * (log(t) - 1) / log(2) < bits:
        t *= 2
    t0 = t // 2
    while t - t0 >= 2:
        a = (t0 + t) // 2
        if a * (log(a) - 1) / log(2) < bits:
            t0 = a
        else:
            t = a
    return t

def bs_e(a: int, b: int) -> tuple[mpz, mpz]:
    """Binary splitting to calculate e using Taylor series.
    Returns p, q such that p/q = Σ(x=a..b, (a-1)!/x!) for integers a >= 1 and b >= a.
    If p, q = bs_e(1, t), then e is the limit of 1 + p/q as t approaches infinity."""
    if a == b:
        return mpz(1), mpz(a)
    m = (a + b) // 2
    P1, Q1 = bs_e(a, m)
    P2, Q2 = bs_e(m + 1, b)
    return P1 * Q2 + P2, Q1 * Q2

def compute_e(bits: int) -> mpfr:
    """Computes e to the given number of significant bits, using the Taylor series."""
    t = terms_needed(bits)
    P, Q = bs_e(1, t) # p/q = 1/1! + 1/2! + ... + 1/t!
    return mpfr(1) + mpfr(P) / mpfr(Q)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Syntax:")
        print("python3 e.py <d> (Prints e to d digits after the decimal point)")
        print("python3 e.py <d> write (Writes a text file containing d digits of e after the decimal point)")
        exit(1)

    start = perf_counter()

    num_digits = int(sys.argv[1])
    if num_digits < 0:
        print("Number of digits must be greater than or equal to 0")
        exit(1)

    bits = helpers.bits_needed(num_digits)
    ctx = get_context().copy()
    ctx.precision = bits
    with ctx:
        e = compute_e(bits)
        e_string = format(e, f".{num_digits}Zf")

    if len(sys.argv) >= 3 and sys.argv[2] == "write":
        file_name = f"e_{num_digits}.txt"
        with open(file_name, "w") as f:
            f.write(helpers.format_for_file(e_string))
        print(f"Wrote {file_name}")
    else:
        print(e_string)

    end = perf_counter()
    helpers.print_time(start, end) # evaluate runtime of algorithm