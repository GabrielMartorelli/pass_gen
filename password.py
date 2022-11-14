import random

print("Password Generator")

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=?/\<>,."

pnum = int(input("How many password you want to generate: "))
plen = int(input("What is the passwords size: "))

print("Generated Passwords!")
print()

for password in range(pnum):
    passwords = ""
    for i in range(plen):
        passwords += random.choice(alpha)
    print(passwords)
