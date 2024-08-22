# Create an empty dictionary to store information about a person
personal_info = {}

# Ask the user for input and store it in the dictionary
personal_info['name'] = input("Enter your name: ")
personal_info['age'] = int(input("Enter your age: "))
personal_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary to the console
print("\nPerson Information:")
print(personal_info)
