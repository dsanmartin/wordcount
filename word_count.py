happy = input("Enter a phrase to check word frequency: ")

words = happy.split() # split user input on spaces

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("The word frequency of your statement is: ")   
print(counts)
