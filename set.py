# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter integers for the first set, separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set, separated by spaces: ").split()))

# Create a new set that contains only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Print the new set
print(f"The common elements in both sets are: {common_elements}")
