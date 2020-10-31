
def recursive_palindrome(word, left=0, right=-1):        

        print(word[left], word[right])

        if word[left] == word[right]:
            
            if left >= (len(word)-1) // 2:
                return True

            else:
                return recursive_palindrome(word, left+1, right-1)

        else:
            return False

def ispalindrome(word):    
    if len(word) < 2: 
        return True    
    if word[0] != word[-1]: 
        return False    
    return ispalindrome(word[1:-1])

def is_palindrome(word):

    left = 0
    right = -1

    # or do while left < right abs value
    for item in range((len(word)-1) // 2):

        if word[left] == word[right]:
            left = left + 1
            right = right - 1
        else: 
            return False 
    
    return True 

if __name__ == "__main__":
    
    # print(is_palindrome('howdy'))
    # print(is_palindrome('racecar'))
    print(recursive_palindrome('howdy'))
    print(recursive_palindrome('racecar'))

