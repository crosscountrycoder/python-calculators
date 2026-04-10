from gmpy2 import mpfr, mpz, get_context, is_finite, get_exp, get_emin_min, get_emax_max
from sys import argv

if __name__ == "__main__":
    ctx = get_context()
    ctx.precision = 2**31-1
    ctx.emin = -2**47+1
    ctx.emax = 2**47-1
    print("Precision:", ctx.precision)
    print("Min exp:", ctx.emin)
    print("Max exp:", ctx.emax)
    print("Min e_min:", get_emin_min())
    print("Max e_max:", get_emax_max())
    e = int(argv[1])
    n = mpz(2) ** e
    print("Bit length of n:", n.bit_length())
    print("Last 50 digits of n:", n % (10 ** 50))
    n_mpfr = mpfr(2) ** e
    print("n_mpfr precision:", n_mpfr.precision)
    print("n_mpfr exponent:", get_exp(n_mpfr))
    print("n_mpfr is finite:", is_finite(n_mpfr))