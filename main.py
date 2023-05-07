# Exercise07

# 1
import os


def create_file(file_name):
    file_name = file_name.replace('(', '').replace(')', '')
    # define a list of names
    names = ['Ada', 'Alan', 'Charlie', 'David', 'Emma', 'Meltem', 'Jakob', 'Hannah', 'Max', 'Julia']
    with open(os.path.join(os.path.dirname(__file__), file_name), 'w') as file:
        file.write(','.join(names))


# open and print the content
with open('names.txt', 'r') as file:
    contents = file.read()
print(contents)

# 2


def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as file:
        # read the contents of the input file
        contents = file.read()

        # split the contents into a list of words
        words = contents.split(',')

        with open(output_file, 'w') as output:
            # write each word to a new line in the output file
            for word in words:
                output.write(word.strip() + '\n')


# usage
transform_to_row('names.txt', 'names_row.txt')

with open('names_row.txt', 'r') as file:
    contents = file.read()
print(contents)


# 3


def add_greeting(input_file, output_file):
    with open(input_file, 'r') as file:
        contents = file.read()

        words = contents.splitlines()

        # add the greeting to each word
        greetings = ["Hello " + word for word in words]

        with open(output_file, 'w') as output:
            for greeting in greetings:
                output.write(greeting + '\n')


# usage
add_greeting('names_row.txt', 'greetings.txt')
with open('greetings.txt', 'r') as f:
    contents = f.read()
print(contents)


# 4


def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f:
        for line in lines:
            stripped = line.strip().replace('Hello ', '')
            f.write(stripped + '\n')


# usage
strip_greeting('greetings.txt', 'stripped.txt')
with open('stripped.txt', 'r') as f:
    contents = f.read()
print(contents)


# 5

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read and split the contents of the files
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Make sure that both files have the same length
    if len(lines1) != len(lines2):
        print("Files must have the same number of lines.")
        return

    # Combine the lines from the input files and write to the output file
    with open(output_file, 'w') as out_f:
        for line1, line2 in zip(lines1, lines2):
            combined_line = f"{line1.strip()} {line2.strip()}\n"
            out_f.write(combined_line)


