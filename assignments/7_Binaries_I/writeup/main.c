/*
 * Name: *PUT YOUR NAME HERE*
 * Section: *PUT YOUR SECTION NUMBER HERE*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *PUT YOUR NAME HERE*
 */

/* your code goes here */
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
