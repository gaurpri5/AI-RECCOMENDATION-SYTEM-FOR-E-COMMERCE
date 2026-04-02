import reflex as rx


def header():
    return rx.center(
        rx.vstack(
            rx.heading(
                "AI Powered Product Recommendations",
                size="8",
                text_align="center"
            ),

            rx.text(
                "Discover products tailored just for you",
                font_size="1.2em",
                color="gray"
            ),

            rx.button(
                "Explore Products",
                color_scheme="purple"
            ),

            spacing="5",
            align="center"
        ),

        padding="4em",
    )


def product_grid():
    return rx.grid(
        rx.box(
            rx.heading("Laptop"),
            rx.text("AI recommended laptop"),
            rx.button("Add to Cart")
        ),

        rx.box(
            rx.heading("Headphones"),
            rx.text("Noise cancelling"),
            rx.button("Add to Cart")
        ),

        rx.box(
            rx.heading("Smart Watch"),
            rx.text("Fitness tracking"),
            rx.button("Add to Cart")
        ),

        columns="3",
        spacing="6",
        padding="3em"
    )