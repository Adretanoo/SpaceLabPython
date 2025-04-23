from payment_strategy import PaymentStrategy


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} грн через PayPal.")
