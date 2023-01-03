def main():
    input_time = input("What is the time? ")
    hour = convert(input_time)
    meal(hour)
# convert time to hours


def convert(time):
    hours = time.replace(":", ".")
    hours = float(hours)
    return hours

# What meal should we get?


def meal(hour):
    if 7 <= hour <= 8:
        print("Breakfast")
    elif 12 <= hour <= 13:
        print("Launch")
    elif 18 <= hour <= 19:
        print("Dinner")
    else:
        print("No meal")


if __name__ == '__main__':
    main()
