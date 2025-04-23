from payment_strategy import PaymentStrategy


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплачено {amount} грн готівкою.")
