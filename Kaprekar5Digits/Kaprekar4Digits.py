def main():
    while True:
        user_input = input("Please enter exactly 4 characters: ")
        if len(user_input) == 4:
            print("Valid input!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()