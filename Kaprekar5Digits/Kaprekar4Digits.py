def main():
    user_input = take_input()
    sorted_input_asc = routine_asc(user_input)
    print(sorted_input_asc)

def take_input():
    # Loop until the input is correct
    while True:
        # Take user input
        user_input = input("Please enter exactly 4 integers: ")

        if(len(user_input)==4):
            try:
                user_input = int(user_input)
            except:
                print("Please ensure your input is an integer")
            if(isinstance(user_input,int)):
                return user_input
        if(len(user_input)!=4):
            print("Please input exactly 4 integers")
def routine_asc(user_input):
    # Convert the integer to a string
    user_input = str(user_input)

    # Convert the string to a list of characters
    char_list = list(user_input)

    # Iterate over the list from the second character
    for i in range(1, len(char_list)):
        # Store the current character
        current_char = char_list[i]

        # Compare the current character with previous characters
        j = i - 1
        while j >= 0 and char_list[j] > current_char:
            # If the current character is smaller, move the previous character up
            char_list[j + 1] = char_list[j]
            j -= 1

        # Insert the current character in its correct position
        char_list[j + 1] = current_char

    # Convert the list of characters back to a string
    sorted_string = ''.join(char_list)

    return sorted_string


    return 0

if __name__ == "__main__":
    main()