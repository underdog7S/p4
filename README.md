# p4

# Python File Handling Assignment

This repository contains two Python scripts for basic file handling tasks using Python.

---

## Task 1: Read a File and Handle Errors

**Functionality:**
- Attempts to open and read the contents of a file named `sample.txt`.
- If the file exists, it prints each line with a line number.
- If the file does not exist, it displays an error message.

**Code Overview:**

```python
file_1  = "sample.txt"

try:
    with open(file_1, "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")



Task 2: Write, Append, and Read from a File
Functionality:

Prompts the user to input text and writes it to a file named output.txt.

Prompts for additional input and appends it to the same file.

Finally, reads and displays the full content of the file.

Author
Shadab Sheikh

License
This project is for educational use only.
