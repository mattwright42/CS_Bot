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


def existing_customer():
    print(
        "What kind of support do you need? \n [1] Television Support \n [2] Internet Support \n [3] Speak to a support representative")
    respone = input("Please enter the number corresponding to your choice: ")
    if response == "1":
        television_support()
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        existing_customer()
