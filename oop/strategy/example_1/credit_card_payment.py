from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} грн кредитною карткою.")