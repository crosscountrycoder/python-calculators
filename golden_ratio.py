"""
Calculates the golden ratio (phi) = (1 + sqrt(5)) / 2.
Examples:
python3 golden_ratio.py 1000 - Prints e to 30 decimal digits of precision (after the decimal point)
python3 golden_ratio.py 1000000 write - Writes a file, phi_1000000.txt, with 1 million digits of phi after the decimal point.
Using the write option, each line contains 100 decimal digits.
"""
import sys
import helpers
from gmpy2 import mpfr, mpz, get_context
from time import perf_counter

def calc_golden_ratio(bits: int) -> mpfr:
    """Calculates the golden ratio by first calculating sqrt(5) using Newton's method (aka Heron's or Babylonian method), then 
    adding 1 and dividing by 2."""
    MPZ_5 = mpz(5) # constant
    p = mpz(3) # numerator
    q = mpz(1) # denominator
    e = 1 # relative error bound (<= 2^-e)
    while e < bits:
        p0 = p
        q0 = q
        p = p0 ** 2 + MPZ_5 * q0 ** 2
        q = 2 * p0 * q0
        e = 2 * e + 1
    return (mpfr(1) + mpfr(p) / mpfr(q)) / mpfr(2)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Syntax:")
        print("python3 golden_ratio.py <d> (Prints golden ratio to d digits after the decimal point)")
        print("python3 golden_ratio.py <d> write (Writes a text file containing d digits of golden ratio after the decimal point)")
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
        phi = calc_golden_ratio(bits)
        phi_string = format(phi, f".{num_digits}Zf")

    if len(sys.argv) >= 3 and sys.argv[2] == "write":
        file_name = f"phi_{num_digits}.txt"
        with open(file_name, "w") as f:
            f.write(helpers.format_for_file(phi_string))
        print(f"Wrote {file_name}")
    else:
        print(phi_string)

    end = perf_counter()
    helpers.print_time(start, end) # evaluate runtime of algorithm