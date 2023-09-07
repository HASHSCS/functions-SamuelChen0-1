def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    #pass  # Implement your solution here
    s = number*number
    return s


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    #pass  # Implement your solution here
    reversed = s[::-1]
    return reversed



def is_prime(n):
    """
    This function takes a number as input and returns True if the number is prime, otherwise False.
    :param n: int
    :return: bool, True if the number is prime, otherwise False
    """
    #pass  # Implement your solution here
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True



def factorial(n):
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
    #pass  # Implement your solution here
    r=1
    for i in range(1,n+1):
        r=r*i
    return(r)


def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    #pass  # Implement your solution here
    if not lst:
       return None
    else:
        return max(lst)

    


def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    #pass  # Implement your solution here
    if n/2-n//2==0:
        return("Even")
    else:
        return("Odd")

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    #pass  # Implement your solution here
    reversed = s[::-1]
    if reversed=s:
        return("True")
    else:
        return("False")



def find_gcd(a, b):
    """
    This function takes two positive integers `a` and `b` and returns their greatest common divisor (GCD).
    
    :param a: int
    :param b: int
    :return: int, the greatest common divisor of `a` and `b`.
    """
    #pass  # Implement your solution here
    while b:
        a, b = b, a % b
    return a

    
