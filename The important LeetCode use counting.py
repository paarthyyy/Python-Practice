<<<<<<< HEAD
letters = "banana"
count = {} #counting the number of times each letter appears in the word

for letter in letters: #for each letter in the string "banana", check if it is already in the count dictionary. If it is, increment its count by 1. If it is not, add it to the dictionary with a count of 1. Finally, print the count dictionary to see how many times each letter appears in the word.
    if letter in count: #if the letter is already in the count dictionary, increment its count by 1
        count[letter] += 1
    else:               #if the letter is not in the count dictionary, add it with a count of 1
        count[letter] = 1

=======
letters = "banana"
count = {} #counting the number of times each letter appears in the word

for letter in letters: #for each letter in the string "banana", check if it is already in the count dictionary. If it is, increment its count by 1. If it is not, add it to the dictionary with a count of 1. Finally, print the count dictionary to see how many times each letter appears in the word.
    if letter in count: #if the letter is already in the count dictionary, increment its count by 1
        count[letter] += 1
    else:               #if the letter is not in the count dictionary, add it with a count of 1
        count[letter] = 1

>>>>>>> 0981ad8685c870ca7bf0ce4be72d496e180f8ead
print(count)