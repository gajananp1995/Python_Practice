def read_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read and print each line
            for line in file:
                print(line.strip())  # strip() removes extra spaces/newlines
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Calling the function with 'sample.txt'
read_file("sample.txt")
