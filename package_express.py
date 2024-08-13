# Welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Prompt user for the package weight
weight = float(input("Please enter the package weight: "))

# Check if the package is too heavy
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
else:
    # Prompt user for package dimensions
    width = float(input("Please enter the package width: "))
    height = float(input("Please enter the package height: "))
    length = float(input("Please enter the package length: "))

    # Check if the package is too big
    if (width + height + length) > 50:
        print("Package too big to be shipped via Package Express.")
    else:
        # Calculate the shipping quote
        dimensions_product = width * height * length
        quote = (dimensions_product * weight) / 100

        # Display the shipping quote
        print(f"Your estimated total for shipping this package is: ${quote:.2f}")
        print("Thank you!")
