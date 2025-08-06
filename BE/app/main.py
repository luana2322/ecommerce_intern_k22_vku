from fastapi import FastAPI
from app.config.database import Base, engine
from app.model import *  # Import all models
from app.data.seed_data import seed_data
from app.controller import (
    admin_controller, role_controller, admin_role_controller, bank_controller,
    country_controller, customer_controller, cart_controller, product_controller,
    cart_item_controller, category_controller, city_controller, color_controller,
    contact_controller, customer_bank_controller, customer_role_controller,
    orders_controller, order_detail_controller, product_category_controller,
    product_image_controller, product_review_controler, wishlist_controller
)

app = FastAPI()
# Include all routers
# app.include_router(admin_controller.router)


Base.metadata.create_all(bind=engine)
app.include_router(role_controller.router)
app.include_router(admin_role_controller.router)
app.include_router(bank_controller.router)
app.include_router(country_controller.router)
app.include_router(customer_controller.router)
app.include_router(cart_controller.router)
app.include_router(product_controller.router)
app.include_router(cart_item_controller.router)
app.include_router(category_controller.router)
app.include_router(city_controller.router)
app.include_router(contact_controller.router)
app.include_router(customer_bank_controller.router)
app.include_router(customer_role_controller.router)
app.include_router(orders_controller.router)
app.include_router(order_detail_controller.router)
app.include_router(product_category_controller.router)
app.include_router(product_image_controller.router)
app.include_router(product_review_controler.router)
app.include_router(wishlist_controller.router)
app.include_router(admin_controller.router)

seed_data()