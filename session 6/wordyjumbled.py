from random import shuffle
word = 'text'
word = list(word)
shuffle(word)
for w in word:
    print(w, end=" ")
    
print(word)


