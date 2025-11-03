from Conventer.api_handler_conventer import handler
from Conventer.storage import storage
from Conventer.logger_config import setup_logger


while True:
    from_currency_choise = input("Enter a currency(from): ")
    to_currency_choise = input("Enter a currency(to): ")
    
    try:
        amount_choise = float(input("Enter amount: "))
        if amount_choise <= 0:
            setup_logger().error("The amount must be greater than zero!")
            continue
        break

    except ValueError:
        setup_logger().error("Invalid input for amount. Please enter a numeric value.")

date = handler(fromcurrency=from_currency_choise, tocurrency=to_currency_choise, amount=amount_choise)


if date:
    storage(date=date, to_currency=to_currency_choise)
else:
    setup_logger().error("Data not received!")



