def main():
    greeting = input("input your greeting: ").lower()
    firstWord = analize_greeting(greeting)
    print(type(firstWord))
    give_reward(firstWord)


def analize_greeting(greet):
    first_word = greet.split(" ")[0]
    return (str(first_word))


def give_reward(w):
    # if "hello" in w:
    #     print("0$")
    # elif "h" in w:
    #     print("20$")
    # else:
    #     print("100$")
    match w:
        case "hello":
            print("0$")
        case "h":
            print("20$")
        case _:
            print("100$")


main()
