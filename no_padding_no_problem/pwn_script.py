#!/usr/bin/env python3
# script.py — fixed pwntools client for the challenge

from pwn import remote
import binascii

HOST = "mercury.picoctf.net"
PORT = 33780

r = remote(HOST, PORT)

# helper to read an integer after a prompt like "n:" or "e:" etc.
def read_int(prompt):
    r.recvuntil(prompt)           # wait for the prompt text
    line = r.recvline().strip()   # read the next line, strip newline
    return int(line)              # decode & convert to int

# read n, e, c from server
n = read_int(b"n:")      # pwntools accepts bytes or str here
print("n =", n)
e = read_int(b"e:")
print("e =", e)
c = read_int(b"ciphertext:")
print("c =", c)

# wait for the "to decrypt:" prompt (server wording may differ)
r.recvuntil(b"to decrypt:")

# compute (2^e * c) % n — must reduce mod n to stay in range
m = (pow(2, e, n) * c) % n
r.sendline(str(m))   # send as ascii line
print("[+] sent:", m)

# read the server's response containing p2 (or whatever it returns)
r.recvuntil(b"you go:")    # adjust the prompt string if needed
p2_line = r.recvline().strip()
p2 = int(p2_line)
print("[+] p2 =", p2)

# compute p2//2 (as in your original)
half = p2 // 2
print("[+] p2//2 =", half)

# hexify and unhexlify safely (handle odd-length hex)
hexstr = "{:x}".format(half)
if len(hexstr) % 2 == 1:
    hexstr = "0" + hexstr

plaintext = binascii.unhexlify(hexstr)
print("[+] recovered bytes:")
print(plaintext)

r.close()
