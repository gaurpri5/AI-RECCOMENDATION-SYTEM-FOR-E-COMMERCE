import reflex as rx


def payment():

    return rx.container(

        rx.heading("Payment"),

        rx.text("Scan QR to Pay"),

        padding="2em"
    )