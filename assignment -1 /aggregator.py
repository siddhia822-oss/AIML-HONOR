
from abc import ABC, abstractmethod
from payment import RazorpayFactory, StripeFactory


class Aggregator(ABC):

    def __init__(self, name, processing_fee):
        self.name = name
        self.processing_fee = processing_fee

    @abstractmethod
    def get_payment_factory(self):
        pass

    def call_get_payment_object(self, method_type, amount, **kwargs):

        factory = self.get_payment_factory()

        payment = factory.get_payment_object(
            method_type, **kwargs
        )

        print("\nPayment Details:", payment.get_details())

        fee = amount * self.processing_fee
        total_amount = amount + fee

        print(f"Original Amount: Rs.{amount:.2f}")
        print(f"Processing Fee: Rs.{fee:.2f}")
        print(f"Total Amount: Rs.{total_amount:.2f}")

        return payment.pay(total_amount)


class RazorpayAggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay", 0.02)

    def get_payment_factory(self):
        return RazorpayFactory


class StripeAggregator(Aggregator):

    def __init__(self):
        super().__init__("Stripe", 0.029)

    def get_payment_factory(self):
        return StripeFactory


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def register_aggregator(cls, name, aggregator_class):
        cls.factory[name.lower()] = aggregator_class

    @classmethod
    def get_aggregator_object(cls, aggregator_name):

        aggregator_name = aggregator_name.lower()

        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator!")

        aggregator_class = cls.factory[aggregator_name]

        return aggregator_class()
