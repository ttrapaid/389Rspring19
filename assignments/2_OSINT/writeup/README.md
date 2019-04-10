# Writeup 2 - OSINT

<<<<<<< HEAD
<<<<<<< HEAD
Name: *Teimuraz Trapaidze*
Section: *0201E*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Teimuraz Trapaidze*
=======
Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *PUT YOUR NAME HERE*
>>>>>>> upstream/master
=======
Name: *Teimuraz Trapaidze*
Section: *0201E*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Teimuraz Trapaidze*
>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305

## Assignment Writeup

### Part 1 (45 pts)

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305
1.
v0idcache's real name is Elizabeth Moffet.

2.
v0idcache works for an "Elite Banking" firm - http://1337bank.money/

3.
The information listed so far I found from v0idcache's twitter
account (@v0idcache), which I found by simply using usersearch.org.
I followed her twitter account to her website, where I found her email: v0idcache@protonmail.com.
The only follower on twitter account is the user Dev0id_cache (@CacheDev0id).

4.
Using DNSdumpster, I found:
1337bank.money - 142.93.136.81 - Canada
d22.verisigndns.com - 216.87.155.33 - AS36619 Verisign Global - United States
dns4.registrar-servers.com - 216.87.152.33 - AS36617 Verisign Global - United States
eforward.web-hosting.com - 162.255.118.62 - AS22612 Namecheap, Inc. - United States


5.
One flag I found was hidden in the HTML file of the home page of v0idcache's website,
in the one of the divisions in the section division in the body.
It's just a comment that says "<!-- Good find! CMSC389R-{h1dd3n_1n_plain_5ight} -->".
I also looked at robots.txt file, went to secret_directory, and found the
"Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}" flag.

6.
The open ports on the website are 22/tcp, 80/tcp, and 1337/tcp. Port 22 is for ssh - logins, file
transfers, and port forwarding. Port 80 is for HTTP. I found this by running the command
"nmap -v -A 1337bank.money".
Port 1337 is for a file sharing service.

7.
When running nmap, I found under "Service Info" the following OS description:
"OS: Linux; CPE: cpe:/o:linux:linux_kernel"

8.
I used DNSdumpster to look for more information about the website,
and I found under "TXT Records" the following flag:
"CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}".

When using nmap to try and learn more about the ports/OS of the website,
nmap found the git repository for the website, revealing the last commit
Message and another flag: "CMSC389R-{h1d3_s3cret_g1ts}"

Something else I found but did not know what to make use of was when I googled the username
V0idcache, one of the results was a link to a pastebin file - https://pastebin.com/WghDuAr7.
It appears to be a log of v0idcache and some user named "fl1nch," where they make mention of a file called "AB4300.txt".
<<<<<<< HEAD

### Part 2 (75 pts)

I edited stub.py to achieve what this part of the assignment was asking for.
I simply used a while loop to iterate through the rockyou.txt file and repeatedly open
and close a socket connection to 142.93.136.81 and try a different password each time,
knowing that the username was v0idcache. Then, once I found the password, I simply used
a python environment to send linux commands through a socket to the shell (s.send) and
read the result with s.recv (of course I had to log in with the user name and pass first).

I found the flag file within the "root@3ec51ffed684:/home#" directory, called flag.txt.
The file contained the following: "Good work! Here's a flag: CMSC389R-{brut3_f0rce_m4ster}"

Inside AB4300.txt (from earlier), I found CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}.


=======
*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*
>>>>>>> upstream/master
=======

### Part 2 (75 pts)

I edited stub.py to achieve what this part of the assignment was asking for.
I simply used a while loop to iterate through the rockyou.txt file and repeatedly open
and close a socket connection to 142.93.136.81 and try a different password each time,
knowing that the username was v0idcache. Then, once I found the password, I simply used
a python environment to send linux commands through a socket to the shell (s.send) and
read the result with s.recv (of course I had to log in with the user name and pass first).

I found the flag file within the "root@3ec51ffed684:/home#" directory, called flag.txt.
The file contained the following: "Good work! Here's a flag: CMSC389R-{brut3_f0rce_m4ster}"

Inside AB4300.txt (from earlier), I found CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}.


>>>>>>> 145c3c6bcd28ed7c68034266714738d438eed305
