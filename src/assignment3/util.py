def mutate_string():
    input_string = input("Enter a string: ")
    position = int(input("Enter the position to mutate: "))
    character = input("Enter the character to replace: ")

    result = input_string[:position] + character + input_string[position + 1:]
    return result


# Call the function
#mutate_string()
