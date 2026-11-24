
from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Razorpay Card: " + self.card_number[-4:]

    def pay(self, amount):
        print("Razorpay Card Payment Successful:", amount)
        return True


class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Razorpay UPI: " + self.upi_id

    def pay(self, amount):
        print("Razorpay UPI Payment Successful:", amount)
        return True


class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return "Stripe Card: " + self.card_number[-4:]

    def pay(self, amount):
        print("Stripe Card Payment Successful:", amount)
        return True


class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return "Stripe UPI: " + self.upi_id

    def pay(self, amount):
        print("Stripe UPI Payment Successful:", amount)
        return True


class FactoryPaymentMethod(ABC):

    factory = {}

    @classmethod
    @abstractmethod
    def get_payment_object(cls, method_type, **kwargs):
        pass


class RazorpayFactory(FactoryPaymentMethod):

    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)


class StripeFactory(FactoryPaymentMethod):

    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)
