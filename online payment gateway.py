print("Online Payment Gateway")
print("Available methods: card/upi/netbanking/wallet")
while True: 
    payment_method=input("Choose payment method: ").lower()
    if payment_method=="card":
        card_type=input("Enter card type(credit/debit): ").lower()
        if card_type=="credit":
            card_number = input("Enter 16-digit credit card number: ")
            if len(card_number) == 16 and card_number.isdigit():
                print("Processing credit card payment...")
                print("Payment Successful!")
                break
            else:
                print("Invalid card number. Try again.")
        elif card_type=="debit":
            card_number=input("Enter 16-digit debit card number: ")
            if len(card_number) == 16 and card_number.isdigit():
                print("Processing debit card payment...")
                print("Payment Successful!")
                break
            else:
                print("Invalid card number.Try again.")
        else:
            print("Invalid card type.Please try again.")
    elif payment_method=="upi":
        upi_id = input("Enter UPI ID: ")
        if "@" in upi_id:
            print("Processing UPI payment...")
            print("Payment Successful!")
            break
        else:
            print("Invalid UPI ID. Try again.")
    elif payment_method=="netbanking":
        print("Available Banks: SBI/IOB/HDFC or OTHER")
        bank_name = input("Enter your bank name: ").upper()
        user_id = input("Enter NetBanking User ID: ")
        password = input("Enter NetBanking Password: ")

        if bank_name in ["SBI", "IOB", "HDFC"] and password == "sona":
            print(f"Connecting to {bank_name} NetBanking...")
            print("Payment Successful!\n")
            break
        else:
            print("Invalid NetBanking details. Try again.")
    elif payment_method=="wallet":
        wallet_number=input("Enter Wallet Mobile Number: ")
        password = input("Enter Password: ")
        if len(wallet_number)==10 and password == "sona" and wallet_number.isdigit():
            print("Processing Wallet payment...")
            print("Payment Successful!")
            break
        else:
            print("Invalid Wallet number. Try again.")
    else:
        print("Invalid payment method. Please choose again.")
