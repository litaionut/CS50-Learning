def main():
    input_formula = input("Enter x: ")
    print(separate_string(input_formula))


def separate_string(words):
    word = words.split(' ', 2)
    x = int(word[0])
    y = word[1]
    z = int(word[2])
    if y == "-":
        res = x - z
    elif y == "+":
        res = x + z
    elif y == "*":
        res = x * z
    elif y == "/":
        res = x / z
    elif y == "%":
        res = x % z
    return res


main()
