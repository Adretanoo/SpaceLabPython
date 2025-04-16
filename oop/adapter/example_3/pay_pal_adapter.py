from pay_pal_payment import PayPal

class PayPalAdapter:
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self, amount, account):
        self.paypal.process_paypal_payment(amount, account)