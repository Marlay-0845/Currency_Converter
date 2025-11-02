from Conventer.api_handler_conventer import handler
from Conventer.storage import storage


while True:
    from_currency_choise = input("Enter a currency(from): ")
    to_currency_choise = input("Enter a currency(to): ")
    
    try:
        amount_choise = float(input("Enter amount: "))
        if amount_choise <= 0:
            print("The amount must be greater than zero!")
            continue
        break

    except ValueError:
        print("Enter a number!")

date = handler(fromcurrency=from_currency_choise, tocurrency=to_currency_choise, amount=amount_choise)


if date:
    storage(date=date, to_currency=to_currency_choise)
else:
    print("Data not received!")



