# Yazilim Kalitesi ve Test API Projesi

[Python](https://img.shields.io/badge/Python-3.11-blue)
[FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
[Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
[CI/CD](https://github.com/aliekici/software-quality-api--dev-are/actions/workflows/main.yml/badge.svg)

Bu proje, Yazilim Kalitesi dersi final odevi kapsaminda gelistirilmistir. Modern bir REST API mimarisi kullanilarak; otomatik test surecleri, veri dogrulama ve CI/CD prensipleri uygulanmistir.

---

## 1. CANLI ERISIM (Swagger UI)

Projeyi kurmadan dogrudan test etmek icin asagidaki linki kullanabilirsiniz:

URL: https://final-odev-ali.onrender.com/docs


## 2. KURULUM TALIMATLARI

Projeyi yerel bilgisayarinizda calistirmak icin asagidaki adimlari sirasiyla uygulayin.

### Adim 1: Projeyi Klonlayin
Terminali acin ve asagidaki komutlari girin:

git clone https://github.com/aliekici/software-quality-api--dev-are.git
cd software-quality-api--dev-are

### Adim 2: Sanal Ortam (Virtual Environment) Kurulumu
Kutuphanelerin cakismamasi icin sanal ortam olusturun:

Windows icin:
python -m venv venv
.\venv\Scripts\activate

MacOS / Linux icin:
python3 -m venv venv
source venv/bin/activate

### Adim 3: Gereksinimlerin Yuklenmesi
Gerekli kutuphaneleri yukleyin:

pip install -r requirements.txt

### Adim 4: Uygulamanin Baslatilmasi
Sunucuyu baslatin:

uvicorn main:app --reload

Kurulum tamamlandiginda tarayicinizdan su adrese gidin:
http://127.0.0.1:8000/docs

---

## 3. TESTLERIN CALISTIRILMASI

Birim testleri calistirmak icin proje ana dizininde su komutu kullanin:

pytest

Detayli test ciktisi icin:

pytest -v

---

## 4. API ENDPOINT LISTESI

Method: GET
URL: /
Aciklama: API durum kontrolu

Method: POST
URL: /items/
Aciklama: Yeni veri girisi ve dogrulama

Method: GET
URL: /items/{item_id}
Aciklama: ID ile veri sorgulama

---

## 5. ÖĞRENCİ BILGILERI

Ad Soyad: Ali Rıza Ekici
Öğrenci NO : 4011130253
Ders: Yazilim Kalitesi ve Test
