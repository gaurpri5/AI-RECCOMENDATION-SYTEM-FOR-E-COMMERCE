import reflex as rx


def checkout():

    return rx.container(

        rx.heading("Checkout"),

        rx.text("Review your order"),

        rx.button("Proceed to Payment"),

        padding="2em"
    )