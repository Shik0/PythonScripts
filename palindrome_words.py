import string
letters = string.ascii_lowercase

def isPalindrome(s):

    def to_char(s):
        s = s.lower()
        return ''.join([x for x in s if x in letters])

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(to_char(s))

print(isPalindrome('Aziza'))