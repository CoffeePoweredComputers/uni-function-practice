def concat(val1, val2):
    '''
    Args:
        val1 -> Some arbitrary file 
        val2 -> Some arbitrary file

    Returns: If both values are strings it returns the concatenation of those
    strings. Otherwise, it returns the string literal "Invalid Operation".

    Note: This is a sample function provided to you alone with the test cases.
    please do no modify it in any way.
    '''
    if type(val1) == str and type(val2) == str:
        return val1 + val2
    else:
        return "Invalid Operation"

def contains_duplicate(set1):
    '''
    Args:
        set1 (set) -> A set of arbitrary values

    Returns: This function returns true if the set contains duplicates and
    False if it does not.
    '''
    pass


def remove_list_duplicates(list1):
    '''
    Args:
        list1 (list) -> A list of arbitrary values
    Returns: Takes the list and returns a new list without any of the duplicate
    values.
    '''
    pass

def odd_or_even(num1):
    '''
    Args:
        num1 (int) -> An arbitrary non negative integer

    Returns: This function returns the string literal "Odd" if num1 is "Odd"
    and even otherwise.
    '''
    pass

def is_positive(num1):
    '''
    Args:
        num1 (int) -> An arbitrary non zero integer

    Returns: This function returns the string literal "Odd" if num1 is "Odd"
    and even otherwise.
    '''
    pass

def safe_divide(num1, num2):
    '''
    Args:
        num1 (int or float) -> An arbitrary int or float
        num2 (int or float) -> An arbitrary int or float

    Returns: This function divides num1 by num2 if num2 is a non zero integer.
    If num2 is zero then it simply prints "Cannot divide" and returns None.
    '''
    pass


def get_initials(first_name, middle_name, last_name):
    '''
    Args:
        first_name (str), middle_name (str), last_name (str) 

    Returns: This function takes three string values as parameter and returns
    the persons initials. If any of the strings are empty strings (i.e., len of 0)
    those names are skipped in creating the initials. 

    Example:
    get_initials("David", "Hamilton", "Smith")  -> "DHS"
    get_initials("David", "", "Smith") -> "DS"
    '''
    pass


def convert_k_to_f(kelvin_temp):
    '''
    Args:
        kelvin_temp (float) -> An arbitrary float or int

    Returns: If parameter is non negative value it converts and returns the
    value in Fahrenheit. Otherwise it returns None. 
    '''
    pass
