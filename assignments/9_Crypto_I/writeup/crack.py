#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt") # open and read hashes.txt
    passwords = open("passwords.txt") # open and read passwords.txt
    characters = string.ascii_lowercase
    for c in characters:
        passwords.seek(0)
        for p in passwords:
            # crack hashes

            p = p.rstrip('\n')
            curr = c + p
            currHash = hashlib.sha256((c + p.rstrip('\n')).encode()).hexdigest()

            hashes.seek(0)
            for h in hashes:
                h = h.rstrip('\n')
                if currHash == h:
                    print(p + ":" + currHash)

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
