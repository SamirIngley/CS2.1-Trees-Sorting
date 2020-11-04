
def count_vowels(word, index=0, vowels_count=0):
    
    vowels = ['a', 'e', 'i', 'o', 'u']

    if index >= len(word)-1:
        return vowels_count
    # character is a vowel
    elif word[index] in vowels:
        vowels_count += 1
        index += 1
        return count_vowels(word, index, vowels_count)
    # character is not a vowel
    else:
        index += 1
        return count_vowels(word, index, vowels_count)

    
if __name__ == "__main__":

    # should return 4
    word1 = 'makeschool'
    # should return 0
    word2 = 'hgytrz'

    print(count_vowels(word1))
    print(count_vowels(word2))