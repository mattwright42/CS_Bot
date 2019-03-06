def cs_service_bot():
    print(
        "Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer? \n [1] New Customer \n [2] Existing Customer")
    response_one = input(
        "Please enter the number corresponding to your choice: ")
    if response_one == "1":
        new_customer()
    elif response_one == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()
