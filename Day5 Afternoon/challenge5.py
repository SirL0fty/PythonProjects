#5)ask the user to put in their name. tell the user how many letters there are in their name. added credit - tell them if any of the letters are the same

name = input("Enter your name: ")
print(f"The number of letters is {len(name)}")

repeats = set()

for i in name:
    if name.count(i) > 1:
        repeats.add(i)
print("Repeated letters")
for i in repeats:
    print(i)