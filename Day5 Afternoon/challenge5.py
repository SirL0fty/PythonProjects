#5)ask the user to put in their name. tell the user how many letters there are in their name. added credit - tell them if any of the letters are the same

name = input("Please enter a name: ").lower()

# Get the length of the name
name_length = len(name)

# Print the length of the name
print("Your name is", name_length, "characters long.")

# Initialize an empty list to store repeating characters
repeats = []

# Loop through each character in the name
for i in name:
    # Check if the character repeats in the name
    if name.count(i) > 1:
        # If the character repeats, check if it is already in the repeats list
        if i not in repeats:
            # If not, add it to the repeats list
            repeats.append(i)

# Check if there are any repeating characters
if len(repeats) > 0:
    # If there are, print the repeating characters separated by commas
    print("The following letters repeat:", ', '.join(repeats))
else:
    # If there are no repeating characters, print a message
    print("No letters repeat.")
