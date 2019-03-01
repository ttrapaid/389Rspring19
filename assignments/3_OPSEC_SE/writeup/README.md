# Writeup 3 - Operational Security and Social Engineering

Name: *Teimuraz Trapaidze*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Teimuraz Trapaidze*

## Assignment Writeup

### Part 1 (40 pts)

I'm going to use the following questions to establish a pretext: 
    Who are you pretending to be?
        I am pretending to be an employee associated with Elizabeth Moffet's bank. 
    Why are you calling/talking to your target? 
        I am calling because there was a security issue recognized with her account, 
        and her account has been "flagged as vulnerable". 
    Why do you need the information you are asking for?
        In order to restore her account to full access, she needs to answer her 
        "security questions" and confirm her pin number. 
        This is how I would get her to answer the 5 questions. As for the browser
        question, I'd probably just ask the other four first and then ask her what
        her browser of choice is because I am going to send her a web app that "we use
        that is dependent on your browser."

### Part 2 (60 pts)

The first thing I'd tell her about is how much information I got from simply using 
DNSdumpster, like DNS records as well as the latest git commit. Simply knowing this 
information can lead to a lot of damage when the wrong person knows about it. To 
prevent so much information from being released, she could put her servers behind 
another firewall. 

The second thing I'd tell her about is how easily I was able to brute force my way 
into her account. Obviously this is a huge issue, as I could simply destroy everything
she has inside her account. In order to prevent this, she should 100% create a more 
secret password, one that is not common enough to be found in a list of words that is
known to be common passwords.

The third thing I would tel her about is how I found which of her ports were open using 
nmap. This is how I was able to connect to her server and log into her account, which is
clearly a problem. Similar to the first issue, she could put her servers behind some
firewalls. 

*Replace this text with your repsonse to our prompt for part 1!*