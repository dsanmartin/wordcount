#happy = "I felt happy because I saw the others were happy and because I knew I should feel happy but I was not really happy"
happy = input("Enter a statement to word count: ")

words = happy.split() # split user input on spaces

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("The word frequency of your statement is: ")   
print(counts)
