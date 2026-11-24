
from aggregator import AggregatorFactory


def main():

    try:
        aggregator_name = input(
            "Enter aggregator (Stripe/Razorpay): "
        ).lower()

        aggregator = AggregatorFactory.get_aggregator_object(
            aggregator_name
        )

        method_type = input(
            "Enter method (Card/UPI): "
        ).lower()

        if method_type == "card":
            details = input("Enter card number: ")
            kwargs = {"card_number": details}

        elif method_type == "upi":
            details = input("Enter UPI ID: ")
            kwargs = {"upi_id": details}

        else:
            raise ValueError("Invalid payment method")

        amount = float(input("Enter amount: "))

        if amount <= 0:
            raise ValueError("Amount must be positive")

        result = aggregator.call_get_payment_object(
            method_type, amount, **kwargs
        )

        if result:
            print("\nPayment Successful!")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
