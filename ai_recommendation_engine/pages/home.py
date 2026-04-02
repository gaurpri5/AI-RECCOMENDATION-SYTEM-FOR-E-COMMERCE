import reflex as rx
from ai_recommendation_engine.components.navbar import navbar


def home():
    return rx.container(
        navbar(),
        rx.heading("Home Page", size="8"),
        rx.text("Welcome to AI Recommendation Store"),
        bg="black",
        color="white",
        min_height="100vh",
    )
    