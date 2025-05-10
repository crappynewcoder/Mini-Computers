def calculator():
    print("\n--- Calculator ---")
    print("Type 'exit' to return to the main menu.")
    while True:
        try:
            expression = input("Enter a mathematical expression: ")
            if expression.lower() == 'exit':
                break
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def text_writer():
    print("\n--- Text Writer ---")
    print("Type 'exit' to return to the main menu.")
    print("Type 'save' to save your text to a file.")
    text = []
    while True:
        line = input("Enter text: ")
        if line.lower() == 'exit':
            break
        elif line.lower() == 'save':
            filename = input("Enter filename to save (e.g., notes.txt): ")
            try:
                with open(filename, 'w') as file:
                    file.write("\n".join(text))
                print(f"Text saved to {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            text.append(line)

def terminal():
    print("\n--- Terminal ---")
    print("Type 'exit' to return to the main menu.")
    while True:
        command = input("Enter a command: ")
        if command.lower() == 'exit':
            break
        try:
            output = os.popen(command).read()
            print(output)
        except Exception as e:
            print(f"Error: {e}")

def main_menu():
    while True:
        print("\n--- Mini Computer ---")
        print("1. Calculator")
        print("2. Text Writer")
        print("3. Terminal")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            calculator()
        elif choice == '2':
            text_writer()
        elif choice == '3':
            terminal()
        elif choice == '4':
            print("Exiting Mini Computer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    import os  # Importing here to avoid unnecessary imports if terminal isn't used
    main_menu()
