def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args  
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args 
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0] 
    return f"{name}: {contacts[name]}" 


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        cmd, args = parse_input(user_input)

        if cmd in ("exit", "close"):
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
