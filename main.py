import hendler
    
def main():
    print("Welcome to the assistant bot!\
          \n Write 'help' to see how can i help you")
    book = hendler.load_data()
    while True:
        user_input = input("Enter a command: ")
        command, *args = hendler.parse_input(user_input)

        if command in ["close", "exit"]:
            hendler.save_data(book)
            print("Good bye!")
            break
        elif command == "help":
            print(hendler.available_commands())
        elif command == "add":
            print(hendler.add_contact(args, book))
        elif command == "change":
            print(hendler.change_number(args, book))
        elif command == "phone":
            print(hendler.phone_username(args, book))
        elif command == "all":
            print("Your contacts list:")
            print(hendler.show_all_conacts(book))
        elif command == "add-birthday":
            print(hendler.add_birthday(args, book))
        elif command == "show-birthday":
           print(hendler.show_birthday(args, book))
        elif command == "birthdays":
            print(hendler.birthdays(book))
        else:
            print("Invalid command.") 
    return book       
               
if __name__ == "__main__":
    main()


