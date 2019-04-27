#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def crack(check, passwords):
    # open and read hashes.txt
    # open and read passwords.txt
    characters = string.ascii_lowercase
    for c in characters:
        for p in passwords:
            # crack hashes

            p = p.rstrip('\n')
            curr = c + p
            currHash = hashlib.sha256((c + p.rstrip('\n')).encode()).hexdigest()

            if currHash == check:
                return curr

def server_crack():
    hashes = open("hashes.txt") # open and read hashes.txt
    passwords = open("passwords.txt").readlines() # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337






    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    ctr = 3
    while (ctr > 0):
        data = s.recv(1024)
        print(data.decode('utf-8'))
        lst = data.decode('utf-8').splitlines()
        test = crack(lst[2], passwords)
        s.send((test + "\n").encode())

        time.sleep(1)
        ctr -= 1

    print(s.recv(1024).decode('utf-8'))



if __name__ == "__main__":
    server_crack()
