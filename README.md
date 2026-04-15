# python-calculators
A series of calculators in Python for high-precision mathematical calculations, including calculations of constants such as e, pi,
and square roots such as sqrt(2) and sqrt(3).

These files make use of the [https://github.com/gmpy2/gmpy2/issues](GMPY2) library, a highly optimized library implemented in C for
multiple-precision arithmetic. GMPY2 improves on libraries such as the Python standard library's "Decimal" module.

## Setup instructions
1) Clone the repository: `git clone https://github.com/crosscountrycoder/python-calculators.git`
2) In your venv, run `pip install gmpy2` to install the required GMPY2 module.

## About the scripts ##

### pi.py ###
Calculates pi using the [https://en.wikipedia.org/wiki/Chudnovsky_algorithm](Chudnovsky algorithm), a rapidly converging series.
- `python3 pi.py <d>` prints pi to d digits after the decimal point.
- `python3 pi.py <d> write` writes a text file containing d decimal digits of pi, with 100 digits per line.

### e.py ###
Calculates e using the formula `e = Σ(n=0..inf, 1/n!)`, the Taylor series of the exponential function at x = 1.
- `python3 e.py <d>` prints e to d digits after the decimal point.
- `python3 e.py <d> write` writes a text file containing d decimal digits of e, with 100 digits per line.

### sqrt.py ###
Calculates the square root of a positive integer using 
[https://en.wikipedia.org/wiki/Square_root_algorithms#Heron's_method](Heron's method).
- `python3 sqrt.py <n> <d>` prints sqrt(n) to d digits after the decimal point.
- `python3 sqrt.py <n> <d> write` writes a text file containing d decimal digits of sqrt(n), with 100 digits per line.

## estimate_pi.py ##
Estimates pi by generating random numbers. For some positive integer n, generate n random ordered pairs `(x, y)` with each value 
uniformly distributed in the range \[0, 1\). As n approaches infinity, the share of values that are in the circle `x^2 + y^2 <= 1`
approaches pi/4.

## Coming soon ##
- Calculate the golden ratio `(1 + sqrt(5)) / 2`
- Calculate prime factorizations and quadratic residues, including for large integers