with open('decrypt.txt') as f:
	ciphertext = f.read();
asciichars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b=1
for i in range(len(ciphertext)):
	if i == b*b*b:
		print(ciphertext[i])
		b += 1

