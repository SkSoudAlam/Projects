def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def start_game():
    try:
        while True:
            number = str(input("Enter a number to check if it is  even or odd(enter q for exiting): "))
            if number == "q":
                break
            number = int(number)
            even_odd(number)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    start_game()
