# Python 3.9 slim base image'ını kullanıyoruz
FROM python:3.9-slim

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# requirements.txt dosyasını container'a kopyalıyoruz
COPY requirements.txt /app/

# Gereksinimleri yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını container'a kopyalıyoruz
COPY . /app/

# Django server'ı başlatıyoruz
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

