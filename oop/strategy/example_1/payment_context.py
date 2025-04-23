class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)