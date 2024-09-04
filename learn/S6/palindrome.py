# python docstrings become an attribute of a function

def is_palindrome(text: str) -> bool:
    """Check if `str` is equivalent to its reverse representation"""
    text = text.casefold()
    return text == text[::-1] 


def setence_palindrome(string: str) -> bool:
    """Checks to see if given string is a palindrome. String is equivalent to its reverse 
    
    The function ignores whitespace, capitalisation and
    punctuation in the sentence, allowing only alphanumeric characters to
    be parsed.
    
    :param string: string to check
    :type string: `str`
    :return: `True` if string matches its reverse, or `False` otherwise
    :rtype: `bool`
    """

    a = list(string)
    for i in range(len(a) - 1, -1, -1):
        if a[i].isalnum() == False:
            del a[i]
    a = "".join(a)
    return is_palindrome(a)


print(
    setence_palindrome(
        "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"
    )
)
