contacts = {}
def handle_hello():
    return "How can I help you?"


def handle_add(command):
    args = command.split()
    if len(args) == 3:
        _, name, phone = args
        contacts[name] = phone
        print(phone)
        return f"Contact {name} with phone {phone} added."
    else:
        return "Invalid format. Please provide name and phone separated by a space."

def handle_change(command):
    args = command.split()
    if len(args) == 3:
        _, name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Phone number for {name} updated to {phone}."
        else:
            raise KeyError(f"{name} not found in contacts.")
    elif len(args) == 2:
        _, name = args
        raise ValueError(f"Phone number not provided for {name}. Please provide both name and phone.")
    else:
        return "Invalid format. Please provide name and phone separated by a space."
    
def handle_phone(command):
    args = command.split()
    if len(args) == 2:
        _, name = args
        if name in contacts:
            return f"The phone number for {name} is {contacts[name]}."
        else:
            raise KeyError(f"{name} not found in contacts.")
    elif len(args) == 1:
        raise ValueError("Please provide a name for the 'phone' command.")
    else:
        return "Invalid format. Please provide only the name."

def handle_show_all():
    if contacts:
        result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return result
    else:
        return "No contacts found."

def main():
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input in ['good bye', 'close', 'exit']:
            print("Good bye!")
            break
        elif user_input == 'hello':
            print(handle_hello())
        elif user_input.startswith('add'):
            print(handle_add(user_input))
        elif user_input.startswith('change'):
            print(handle_change(user_input))
        elif user_input.startswith('phone'):
            print(handle_phone(user_input))
        elif user_input.startswith('show all'):
            print(handle_show_all())
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
