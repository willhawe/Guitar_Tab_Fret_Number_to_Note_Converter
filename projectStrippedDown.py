from flask import Flask, request
app = Flask(__name__)


def Replace(filename):
    # Define a dictionary mapping the numbers on the strings to notes
    note_map = {
        0: ["E", "B", "G", "D", "A", "E"],  # open string
        1: ["F", "C", "G#", "D#", "A#", "F"],
        2: ["F#", "C#", "A", "E", "B", "F#"],
        3: ["G", "D", "A", "E", "B", "G"],
        4: ["G#", "D#", "A#", "F", "C", "G#"],
        5: ["A", "E", "B", "F#", "C#", "A"],
        6: ["A#", "F", "C", "G", "D", "A#"],
        7: ["B", "F#", "C#", "G#", "D#", "B"],
        8: ["C", "G", "D", "A", "E", "C"],
        9: ["C#", "G#", "D#", "A#", "F", "C#"],
        10: ["D", "A", "E", "B", "F#", "D"],
        11: ["D#", "A#", "F", "C", "G", "D#"],
    }

    # Read the tab file into a string
    with open(filename, "r") as f:
        tab_string = f.read()

    # Split the string into lines
    lines = tab_string.split("\n")

    # Iterate through the lines and replace the numbers with notes
    for i, line in enumerate(lines):
        # Split the line into individual characters
        chars = list(line)
        # Iterate through the characters
        for j, char in enumerate(chars):
            # if the charchter is a bend "b" replace it with a slide "/"
            if chars[j] in ("b", "H"):
                chars[j] = "/"
            # If the character is a number, replace it with the corresponding note
            if char.isdigit():
                # Get the string number based on the position of the character in the line
                string_dict = {"e": 1, "B": 2, "G": 3, "D": 4, "A": 5, "E": 6}
                string_num = string_dict[lines[i][0]]
                # Replace the character with the corresponding note
                note = note_map[int(char)][string_num]
                # Check if the note has a sharp or flat symbol
                if "#" in note or "b" in note:
                    # If the note has a sharp or flat symbol, remove one "-" from the line
                    chars[j - 1] = ""
                # Replace the character with the corresponding note
                chars[j] = note
        # Rejoin the characters into a modified line
        lines[i] = "".join(chars)

    # Rejoin the modified lines into a single string
    modified_tab_string = "\n".join(lines)

    # Write the modified string to a new file
    with open("modified_tab.txt", "w") as f:
        f.write(modified_tab_string)



@app.route("/modify-tab", methods=["POST"])
def modify_tab():
    tab_text = request.data.decode()
    with open("tab.txt", "w") as f:
        f.write(tab_text)
    Replace("tab.txt")
    with open("modified_tab.txt", "r") as f:
        modified_tab = f.read()
    return modified_tab

if __name__ == "__main__":
    app.run()

