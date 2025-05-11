# Define the file name
file_name = "output.txt"

# Step 1: Take user input and write to the file
user_input = input("Enter data to write to the file: ")
with open(file_name, "w") as file:  # 'w' mode overwrites the file if it exists
    file.write(user_input + "\n")

print("Data written successfully!")

# Step 2: Append additional data
additional_data = input("Enter additional data to append: ")
with open(file_name, "a") as file:  # 'a' mode appends new data without overwriting
    file.write(additional_data + "\n")

print("Data appended successfully!")

# Step 3: Read and display the final content of the file
print("\nFinal content of the file:")
with open(file_name, "r") as file:  # 'r' mode reads the file
    content = file.read()
    print(content)
