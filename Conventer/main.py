
from Conventer.api_handler_conventer import handler
from Conventer.storage import storage


from_currency_choise = input("Enter a currency(from): ")
to_currency_choise = input("Enter a currency(to): ")
amount_choise = input("Enter amount: ")


date = handler(fromcurrency=from_currency_choise, tocurrency=to_currency_choise, amount=amount_choise)

storage(date=date, to_currency=to_currency_choise)



