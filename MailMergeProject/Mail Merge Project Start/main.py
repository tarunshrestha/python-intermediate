PLACEHOLDER = "[name]"

# Read the list of names
with open('./Input/Names/invited_names.txt') as names:
    name_list = names.readlines()

# Read the starting letter template
with open('./Input/Letters/starting_letter.txt') as demo:
    letter = demo.read()

# Iterate over each name and generate a letter
for name in name_list:
    stripped_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, stripped_name)
    with open(f'./Output/ReadyToSend/letter_for_{stripped_name}', mode='w') as completed:
        completed.write(new_letter)

