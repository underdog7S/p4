#T1

# Task 1: Read a File and Handle Errors

file_1  = "sample.txt"

try:
    with open(file_1, "r") as file:
        print("Reading file content:")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


#T2


text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")


text1 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text1 + "\n")
print("Data successfully appended.")


print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
