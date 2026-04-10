from math import ceil, floor, log2

def bits_needed(digits: int) -> int:
    """Number of bits needed to return a given number of decimal digits.
    To minimize chance of error in last digit, 64 guard bits are added."""
    return ceil(digits * log2(10)) + 64

def format_for_file(s: str, line_length: int = 100) -> str:
    if "." not in s:
        return "\n".join(s[i:i+line_length] for i in range(0, len(s), line_length))
    else:
        parts = s.split(".")
        return parts[0] + ".\n" + format_for_file(parts[1])
    
def print_time(start: float, end: float) -> None:
    t = end - start
    h, m, s = floor(t/3600), floor(t/60) % 60, t % 60
    if h >= 1:
        print(f"Time taken: {h} hours, {m} minutes, {s:.3f} seconds")
    elif m >= 1:
        print(f"Time taken: {m} minutes, {s:.3f} seconds")
    else:
        print(f"Time taken: {s:.3f} seconds")