
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.model.admin import Admin
from app.model.category import Category
from app.model.color import Color
from app.model.product import Product
import random
from datetime import datetime

def seed_data():
    db = SessionLocal()
    try:
        # Check if products already exist
        if db.query(Product).count() >= 50:
            print("Database already seeded with 50 or more products.")
            return

        # Clear existing products to ensure exactly 50
        db.query(Product).delete()
        db.commit()

        # Seed an admin (for created_by)
        admin = db.query(Admin).first()
        if not admin:
            admin = Admin(
                email="admin@example.com",
                first_name="Admin",
                last_name="User",
                password="secure123",  # In production, hash this password
                is_email_verified=True,
                registration_date=datetime.now(),
                created_at=datetime.now()
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)

        # Seed categories
        categories = [
            Category(category_name="Smartphones", description="Mobile phones and accessories", created_by=admin.admin_id, created_at=datetime.now()),
            Category(category_name="Laptops", description="Laptops and notebooks", created_by=admin.admin_id, created_at=datetime.now()),
            Category(category_name="Headphones", description="Audio devices", created_by=admin.admin_id, created_at=datetime.now()),
            Category(category_name="Clothing", description="Apparel and fashion", created_by=admin.admin_id, created_at=datetime.now()),
            Category(category_name="Home Appliances", description="Household electronics", created_by=admin.admin_id, created_at=datetime.now()),
        ]
        if db.query(Category).count() == 0:
            db.add_all(categories)
            db.commit()

        # Seed colors (no description)
        colors = [
            Color(color_name="Red", created_by=admin.admin_id, created_at=datetime.now()),
            Color(color_name="Blue", created_by=admin.admin_id, created_at=datetime.now()),
            Color(color_name="Black", created_by=admin.admin_id, created_at=datetime.now()),
            Color(color_name="White", created_by=admin.admin_id, created_at=datetime.now()),
            Color(color_name="Silver", created_by=admin.admin_id, created_at=datetime.now()),
        ]
        if db.query(Color).count() == 0:
            db.add_all(colors)
            db.commit()

        # Get category and color IDs
        category_ids = [cat.category_id for cat in db.query(Category).all()]
        color_ids = [col.color_id for col in db.query(Color).all()]

        # Generate realistic product names
        product_names = [
            f"{brand} {type_} {suffix}" for brand in ["Apple", "Samsung", "Sony", "Dell", "HP", "Bose", "Nike", "Adidas"]
            for type_ in ["Phone", "Laptop", "Headphones", "Smartwatch", "Tablet", "Jacket", "Shoes", "Speaker"]
            for suffix in ["Pro", "Plus", "Ultra", "X", "2023", "SE"]
        ]
        random.shuffle(product_names)
        product_names = product_names[:50]  # Ensure exactly 50 unique names

        # Seed 50 products
        products = [
            Product(
                product_name=product_names[i],
                product_sku="product"+str(i),
                description=f"High-quality {product_names[i]} for modern use",
                sale_price=round(random.uniform(50.0, 2000.0), 2),  # Use product_price instead of price
                stock=random.randint(5, 100),
                created_by=admin.admin_id,
                created_at=datetime.now()
            ) for i in range(50)
        ]
        db.add_all(products)
        db.commit()
        print("Successfully seeded exactly 50 products.")
    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()