answer = input(
    "What is the answer of Great Question of Life, the Universe and Everything? ").lower().strip()
# OPTION 1
# if answer == "42":
#     print("Yes")
# elif answer == "forty-two":
#     print ("Yes")
# elif answer == "forty two":
#     print("Yes")
# else:
#     print("No")

# OPTION 2
# match answer:
#     case "42" | "forty-two" | "forty two":
#         print ("Yes")
#     case _:
#         print ("No")

# OPTION 3
if answer in ("42", "forty two", "forty-two"):
    print("Yes")
else:
    print("No")
