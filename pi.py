"""
Calculates pi using the Chudnovsky algorithm with binary splitting.
Examples:
python pi.py 30 - Prints pi to 30 decimal digits of precision (after the decimal point)
python pi.py 10000 - Prints pi to 10000 decimal digits
python pi.py 1000000 write - Writes a file, pi_1000000.txt, with 1 million digits of pi after the decimal point.
Using the write option, each line contains 100 decimal digits.
"""
import sys
import helpers
from gmpy2 import mpfr, mpz, get_context, sqrt
from time import perf_counter

A = mpz(13591409)
B = mpz(545140134)
C = mpz(640320)
C3_OVER_24 = (C**3) // 24

def bs(a: int, b: int) -> tuple[mpz, mpz, mpz]:
    """Binary splitting to calculate pi using Chudnovsky algorithm.
    P, Q, T = bs(0, n) calculates the Chudnovsky series to n terms. The value of pi is then 426880 * sqrt(10005) * Q / T.
    P, Q, T are returned as gmpy2.mpz values."""
    if b - a == 1:
        if a == 0:
            P = Q = mpz(1)
        else:
            a_mpz = mpz(a)
            P = (6*a_mpz-5) * (2*a_mpz-1) * (6*a_mpz-1)
            Q = a_mpz ** 3 * C3_OVER_24
        T = (-1 if a % 2 else 1) * P * (A + B * a)
        return P, Q, T

    m = (a + b) // 2
    P1, Q1, T1 = bs(a, m)
    P2, Q2, T2 = bs(m, b)
    P = P1 * P2
    Q = Q1 * Q2
    T = T1 * Q2 + P1 * T2
    return P, Q, T

def pi_chudnovsky(bits: int) -> mpfr:
    """Calculates pi using the Chudnovsky algorithm with the given number of significant bits."""
    P, Q, T = bs(0, bits // 47 + 1)
    return mpfr(426880) * sqrt(mpfr(10005)) * mpfr(Q) / mpfr(T)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Syntax:")
        print("python3 pi.py <d> (Prints pi to d digits after the decimal point)")
        print("python3 pi.py <d> write (Writes a text file containing d digits of pi after the decimal point)")
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
        pi = pi_chudnovsky(bits)
        pi_string = format(pi, f".{num_digits}Zf")

    if len(sys.argv) >= 3 and sys.argv[2] == "write":
        file_name = f"pi_{num_digits}.txt"
        with open(file_name, "w") as f:
            f.write(helpers.format_for_file(pi_string))
        print(f"Wrote {file_name}")
    else:
        print(pi_string)

    end = perf_counter()
    helpers.print_time(start, end) # evaluate runtime of algorithm