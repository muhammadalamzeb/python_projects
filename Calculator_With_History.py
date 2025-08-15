#!/usr/bin/env python3
HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            
        if len(lines) == 0:
            print("No history yet!")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history file found!")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        file.close()
    print("History cleared!")

def save_to_history(equation: str, result: str):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation}={result}\n")

def calculate(input_user):
    try:
        parts = input_user.split()
        if len(parts) != 3:
            print("Invalid format! Use: number operator number")
            return
            
        num1 = float(parts[0])
        num2 = float(parts[2])
        operator = parts[1]
        
        result = 0
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error! Division by zero is not allowed.")
                return
        else:
            print("Invalid operator! Use +, -, *, or /")
            return
            
        if result == int(result):
            result = int(result)
        print("Result:", result)
        save_to_history(input_user, result)
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except IndexError:
        print("Invalid format! Use: number operator number")

def main():
    print("------------- CALCULATOR -----------------")
    while True:
        user_input = input("Calculation-> ( + - / * ) OR COMMAND (History, Clear, Quit): ")
        if user_input.capitalize() == "History":
            show_history()
        elif user_input.capitalize() == "Clear":
            clear_history()
        elif user_input.capitalize() == "Quit":
            break
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()
