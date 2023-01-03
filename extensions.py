def main():
    user_input = input('Please enter the image name: ')
    var1 = extract_format(user_input)
    print(var1)
    return_adress(var1)


def extract_format(img):
    if "." in img:
        return img.split(".")[1]
    else:
        print("Invalid format")


def return_adress(adress):
    match adress:
        case "jpg" | "jpeg" | "png" | "gif":
            print(f"image/{adress}")
        case _:
            print(f"application/{adress}")


main()
