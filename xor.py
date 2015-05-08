import time
from itertools import product

def xor_decryption(stream):
    """Input: A stream of encrypted text.
       Output: The sum of the decrypted ASCII values."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in [p for p in product(alphabet, repeat=3)]:
        text = ''
        for i in range(40):
            text += chr(stream[i] ^ ord(key[i % 3]))
        if sum([1 for word in text.split() if word == 'the']) > 0:
            for j in range(i + 1, len(stream)):
                text += chr(stream[j] ^ ord(key[j % 3]))
            return sum([ord(c) for c in text])

def main():

    stream = [int(i) for i in open("cipher.txt").read().split(',')]
    
    t0 = time.time()
    ans = xor_decryption(stream)
    t1 = time.time()
    elapsed = t1 - t0

    print("Found " + str(ans) + " in " + str(round(elapsed, 5)) + " seconds")

if __name__ == '__main__':
    main()
