#Foo and Bar
#print foo for prime numbers and Bar for perfect squares
def is_prime(number):
    if number == 1 or number ==2:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for check in range(5, int(number/2)+1, 2):
        if number % check == 0:
            return False
    return True


def is_square(number):
    helper = 0
    if number >= 0:
        while helper*helper <number:
            helper += 1
        if helper*helper != number:
            return False
        else:
            return True

for number in range(100, 10000):
    if is_prime(number) and is_square(number):
        print "Holy Toledo, Batman, You Broke Math!"
    elif is_prime(number):
        # print number, " Foo"
        print "Foo"
    elif is_square(number):
        # print number, " Bar"
        print "Bar"
    else:
        print "Foobar"