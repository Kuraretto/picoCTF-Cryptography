#!/usr/bin/env python3
# decode.py — try all single-letter keys and show results
import string

ALPHABET = string.ascii_lowercase[:16]  # 'abcdefghijklmnop'

def b16_decode(enc):
    """Take pairs of chars from ALPHABET and convert back to bytes."""
    if len(enc) % 2 != 0:
        raise ValueError("length must be even")
    out_bytes = []
    for i in range(0, len(enc), 2):
        hi = ALPHABET.index(enc[i])
        lo = ALPHABET.index(enc[i+1])
        out_bytes.append((hi << 4) | lo)
    return bytes(out_bytes)

def unshift(enc_char, key_char):
    t1 = ALPHABET.index(enc_char)
    t2 = ALPHABET.index(key_char)
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

ciphertext = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

def is_printable(bs):
    try:
        s = bs.decode('utf-8')
    except Exception:
        return False
    return all(32 <= ord(c) <= 126 for c in s)

results = []
for key in ALPHABET:
    # undo the shift for the entire ciphertext
    unshifted = "".join(unshift(c, key) for c in ciphertext)
    try:
        decoded_bytes = b16_decode(unshifted)
    except Exception as e:
        results.append((key, None, f"decode error: {e}"))
        continue

    printable = is_printable(decoded_bytes)
    decoded_text = decoded_bytes.decode('utf-8', errors='replace')
    results.append((key, decoded_text, printable))

# print a compact summary
for key, text, printable in results:
    tag = "PRINTABLE" if printable else "non-print"
    print(f"key = {key} | {tag} | {text}")

# try to auto-detect likely flag (best-effort)
likely = [ (k,t) for (k,t,p) in results if p and (t.count('_')>0 or 'picoCTF' in t or len(t)>10) ]
if likely:
    print("\nLikely candidates:")
    for k,t in likely:
        print(f"key={k} -> {t}")
        # if it's the inner secret, optionally wrap:
        print("Wrapped flag:", "picoCTF{" + t + "}")
else:
    print("\nNo obvious printable candidate found. Check ciphertext or try printing all results above.")
