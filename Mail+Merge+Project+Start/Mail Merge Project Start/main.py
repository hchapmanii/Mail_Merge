# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
START_LETTER = "[name]"

add_list = []
# file_num = 1

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name_file = names.read().split()
    for n in name_file:
        add_list.append(n)
    print(add_list)

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_file = letter.read()

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for add in range(len(add_list)):
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/starting_letter{add_list[add]}.txt", "x") as letter:
        word_replace = letter_file.replace(START_LETTER, add_list[add])
        letter.write(word_replace)
        # file_num += 1
    # print(letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
