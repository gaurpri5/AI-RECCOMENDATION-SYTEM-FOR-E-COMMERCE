"""Main Application Entry Point."""

import reflex as rx

# Application State Imports
from ai_recommendation_engine.state.state import State

# Import all pages
import ai_recommendation_engine.pages.home
import ai_recommendation_engine.pages.login
import ai_recommendation_engine.pages.signup
import ai_recommendation_engine.pages.product_detail
import ai_recommendation_engine.pages.cart
import ai_recommendation_engine.pages.checkout
import ai_recommendation_engine.pages.payment
import ai_recommendation_engine.pages.profile
import ai_recommendation_engine.pages.wishlist
import ai_recommendation_engine.pages.orders
import ai_recommendation_engine.pages.products


app = rx.App(
    _state=State,
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="red",
    )
)
