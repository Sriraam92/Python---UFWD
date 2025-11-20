import random

print("\nLets play some Rock! Paper! Scissors!")
print("Type 'Exit' to Quit \n")

r = 1
w = 0
d = 0
l = 0
s = 0
o = ["Rock", "Paper", "Scissors"]

while s == 0:
    print("Round: ", r)
    c = input("Enter your choice: ")
    if c.lower() == "exit":
        s = 1
        break
    
    if c != "Rock" or c != "Paper" or c != "Scissors":
        print("Please enter a correct choice")
        continue

    else:
        m = random.choice(o)
        print(f"Computer choice: {m}")
        if c == m:
            d += 1
        elif (c == "Rock" and m == "Scissors") or (c == "Paper" and m == "Rock") or (c == "Scissors" and m == "Paper"):
            w += 1
        else:
            l += 1
    print(f"Current Score: W - {w}, L - {l} \n")
    r += 1

if w > l:
    print(f"\nYou won against the computer by margin of {w}-{l}")
elif w == l:
    print(f"\nYou drew with the computer {w}-{l}")
else:
    print(f"\nYou lost against the computer by margin of {w}-{l}")


    

    




