def get_city_from_user():
    user_city = input("Enter your city: ")
    return user_city

if __name__ == "__main__":
    while True:
        print("Welcome")
        print("Choose one option from the list \n 1. Auto \n 2. Type your city")

        user_input = input("Enter your answer: ")
        if user_input == "2":
            print(get_city_from_user())
            break
