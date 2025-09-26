# recover_flag.py
# Usage: python recover_flag.py
# or: import recover(scrambled_string)

def recover_scrambled(s: str) -> str:
    """Recover a string where every 3-char block was scrambled.
    For each scrambled block `b0 b1 b2` the original was `b2 b0 b1`."""
    out_chars = []
    for i in range(0, len(s), 3):
        block = s[i:i+3]
        if len(block) < 3:
            # append any leftover (1 or 2 chars) unchanged
            out_chars.append(block)
        else:
            out_chars.append(block[2] + block[0] + block[1])
    return ''.join(out_chars)


if __name__ == "__main__":
    corrupted = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
    recovered = recover_scrambled(corrupted)
    print("Corrupted: ", corrupted)
    print("Recovered: ", recovered)
