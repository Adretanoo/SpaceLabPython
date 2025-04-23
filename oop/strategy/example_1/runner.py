from payment_context import PaymentContext
from credit_card_payment import CreditCardPayment
from pay_pal_payment import PayPalPayment
from cash_payment import CashPayment

amount = 10

payment = PaymentContext(CreditCardPayment())
payment.execute_payment(amount)

payment.set_strategy(PayPalPayment())
payment.execute_payment(amount)

payment.set_strategy(CashPayment())
payment.execute_payment(amount)
