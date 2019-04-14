# Writeup 7 - Binaries I

Name: Teimuraz Trapaidze
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Teimuraz Trapaidze

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
int main() {
    static int a = 0;
    static int b = 0;

    a = 485163226;
    b = 4277009102;
    
    a = (b ^ a) ^ (a ^ (b ^ a));
    printf("%d", a); 

    b = a ^ (b ^ a);
    printf("%d", b);

    return 0;
}
```

### Part 2 (10 Pts)

This assembly program declares two static variables and then performs some math operations and stores the values into the variables. The first things stored are two hex values; then, some exclusive or operations are conducted and then stored back into the variables. Every time the value of the variables change, the new value is printed. After the last print, the program quits. 

