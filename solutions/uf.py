
def read_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split()

def read_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split('\n')

#String manipulation
def remove_newlines(line): #Removes the character '\n' from strings.
    if line[len(line)-1] == '\n':
        return line[:-1]
    else:
        return line


