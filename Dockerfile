# استفاده از نسخه سبک پایتون
FROM python:3.10-slim

# تعیین پوشه کاری
WORKDIR /app

# کپی کردن لیست نیازمندی‌ها و نصب آن‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کدهای منبع و مدل ذخیره شده
COPY src/ ./src/
COPY models/ ./models/
COPY notebooks/ ./notebooks/

# دستور پیش‌فرض برای اجرای یک اسکریپت دمو (یا اجرای نوت‌بوک)
CMD ["python", "src/utils/helpers.py"]