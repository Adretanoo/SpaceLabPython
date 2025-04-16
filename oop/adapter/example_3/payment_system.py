from pay_pal_payment import PayPal
from pay_pal_adapter import PayPalAdapter
from card_payment import CardPayment

card = CardPayment()
card.process_payment(333,32453451342314)




pay_pal_payment = PayPal()
adapter = PayPalAdapter(pay_pal_payment)

adapter.process_payment(100, 'Adriatanoo')


