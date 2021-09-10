password = "wsxtfd"
f = open("text.txt", "w")

text = input("Please guess the correct password:")
while text != password:
    f.write(text + "\n")
    text = input("Incorrect, please add another one:")

print("Correct!")
f.close()
