#Creating user input and beginning print
phrase = str(input("What phrase do you see? "))
print()
print("Reversing...")
print()
print("The phrase is ",end = "")
#creating the loop to print backwards(reversed)
for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")