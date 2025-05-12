# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))  # Generates numbers from 1 to 10

# Step 2: Extract the first five elements using slicing
extracted_list = numbers[:5]  # Slices the first five elements

# Step 3: Reverse the extracted list
reversed_list = extracted_list[::-1]  # Slices the list in reverse order

# Step 4: Print both lists
print(f"Extracted list: {extracted_list}")
print(f"Reversed list: {reversed_list}")
