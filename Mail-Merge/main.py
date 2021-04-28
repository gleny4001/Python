# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open starting letter
with open(
        "/Users/USER/Desktop/일병 양희재 (코딩공부)/projects/mail_merger/Mail Merge Project Start/Input/Letters/starting_letter.txt",
        mode="r") as file:
    # Read lines
    line = file.readlines()

    # open invited names to get the names
    with open(
            "/Users/USER/Desktop/일병 양희재 (코딩공부)/projects/mail_merger/Mail Merge Project Start/Input/Names/invited_names.txt",
            mode="r") as name:
        # Read names
        names = name.readlines()
        for i in names:
            line[0] = f"Dear {i}"

            # Open ReadyToSend and write new letter and saves it
            with open(
                    "/Users/USER/Desktop/일병 양희재 (코딩공부)/projects/mail_merger/Mail Merge Project Start/Output/ReadyToSend/" + i.strip() + ".txt",
                    mode="w") as letter:
                for item in line:
                    letter.write("%s\n" % item.strip())

