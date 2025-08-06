from sqlalchemy import text
from app.config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Kết nối MySQL thành công!")
except Exception as e:
    print("❌ Lỗi kết nối đến MySQL:")
    print(e)
