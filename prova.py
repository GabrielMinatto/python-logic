
word = input("Entre com a palavra")
anagram = input("anagrama")

def check_anagram(word, anagram):
    if word not in anagram: return False
    else:
        return True
    
print(check_anagram(word,anagram))