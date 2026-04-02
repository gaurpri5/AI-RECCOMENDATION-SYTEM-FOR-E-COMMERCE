import reflex as rx
from ai_recommendation_engine.state.state import State


def signup():

    return rx.center(

        rx.vstack(

            rx.heading("Create Account"),

            rx.input(
                placeholder="Username"
            ),

            rx.input(
                placeholder="Email"
            ),

            rx.input(
                placeholder="Password",
                type="password"
            ),

            rx.button("Sign Up"),

            spacing="4",
            padding="2em",
            border="1px solid #eee",
            border_radius="10px"
        ),

        height="80vh"
    )