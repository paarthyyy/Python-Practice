name = "Paarth"
print(name[0]) # Print the first letter of the name

for letter in name: # Print each letter in the name
    print(letter)

print(len(name)) #find the length of the name

text = "hello world" # Initialize a string variable

print(text.upper()) 
print(text.lower()) 

if "world" in text: # Check if "world" is in the text
    print("Found!")
    word = "banana"

count = 0

for letter in word: #print the number of times the letter "a" appears in the word
    if letter == "a":
        count += 1

print(count)