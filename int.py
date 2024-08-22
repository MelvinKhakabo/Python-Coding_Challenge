# Accept user input to create a list of integers
integers = input("Enter integers separated by spaces: ").split()
integers = [int(num) for num in integers]  # Convert input strings to integers

# Compute the sum of all the integers in the list
total_sum = sum(integers)

# Print the sum
print(f"The sum of the integers is: {total_sum}")
