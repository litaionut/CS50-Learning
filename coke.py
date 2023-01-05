# Initialize the amount due to 0
amount_due = 0

# Accept coins until the amount due is at least 50 cents
while amount_due < 50:
    print(f"Amount due: {abs(50 - amount_due)}")

    # Prompt the user to insert a coin
    coin = int(input("Please insert a coin: "))

    # Check if the coin is a valid denomination
    if coin in [1, 5, 10, 25]:
        # Add the coin to the amount due
        amount_due += coin
# Calculate the change owed to the user
change_owed = 50 - amount_due

# Output the change owed to the user
print(f"You are owed {abs(change_owed)} cents in change.")
