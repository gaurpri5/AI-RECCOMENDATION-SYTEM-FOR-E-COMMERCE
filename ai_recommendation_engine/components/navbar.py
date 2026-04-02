import reflex as rx


def navbar():
    return rx.hstack(

        rx.heading("AI Store", size="6", color="white"),

        rx.spacer(),

        rx.hstack(
            rx.link(rx.button("Home", bg="white", color="black"), href="/home"),
            rx.link(rx.button("Products", bg="white", color="black"), href="/products"),
            rx.link(rx.button("Cart", bg="white", color="black"), href="/cart"),
            rx.link(rx.button("Orders", bg="white", color="black"), href="/orders"),
            rx.link(rx.button("Profile", bg="white", color="black"), href="/profile"),
            rx.link(rx.button("Login", bg="white", color="black"), href="/login"),
        ),

        padding="1em",
        bg="black",
        width="100%",
    )