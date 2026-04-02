import reflex as rx
from ai_recommendation_engine.state.state import State


def products():

    return rx.container(

        rx.heading("Products"),

        rx.text("All Products From Dataset"),

        padding="2em"
    )
    