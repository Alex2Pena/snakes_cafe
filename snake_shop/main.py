print ("hi, there, how are you?", 5)

# response = input("> ")

# print (f"You said\"{response}\"")

orders = {
    "Root Beer" : 1
}

print (orders["Root Beer"])

response = input("> ")
orders[response] = f"You ordered this {response}"
print (orders)