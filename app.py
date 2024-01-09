# prompt user to add ingredients

total = []

while True:
    prompt = input("What ingredients do you have? (Press Enter to Exit) ")
    total.append(prompt)
    if prompt == "":
        for i in total:
            print(f"{i}, ", end = "")
        break

# store all ingredients
# return all possible recipes based on ingredients provided

