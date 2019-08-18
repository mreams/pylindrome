import re

class PalindromeChecker:

    def is_palindrome(self, input):
        # a one character string is technically a palinedrome but an empty string is not
        if (len(input) < 1):
            return False

        # strip special characters and whitespace
        clean = re.sub('[^A-Za-z0-9]+', '', input)

        # convert string to lowercase only 
        clean = clean.lower()

        # if there aren't any characters left after stripping whitespace and punctuation, this is not a palindrome
        if (len(clean) < 1):
            return False
        
        reversed = self.__reverse_string(clean)
        return clean == reversed

    def __reverse_string(self, input):
        # thanks stackoverflow: https://stackoverflow.com/questions/931092/reverse-a-string-in-python
        # this produces a reversed string by slicing the original one into characters starting at the end
        return input[::-1]