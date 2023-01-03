def main():
    user_input = input("What is the answer? ").lower().strip()
    if check_answer(user_input):
        print("Yes")
    else:
        print("No")


def check_answer(phrase):
    match phrase:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


main()
