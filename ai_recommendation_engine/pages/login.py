import reflex as rx
from ai_recommendation_engine.state.state import State


def login():

    return rx.center(

        rx.vstack(

            rx.heading("Login to AI Store"),

            rx.input(
                placeholder="Enter Username",
                on_change=State.set_user
            ),

            rx.button(
                "Login",
                on_click=rx.redirect("/")
            ),

            spacing="4",
            padding="2em",
            border="1px solid #eee",
            border_radius="10px"
        ),

        height="80vh"
    )
    