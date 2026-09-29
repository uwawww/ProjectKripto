# Vigenère Cipher – Classical Cryptography

## 1. Project Description
Aplikasi web pembelajaran kriptografi yang mengimplementasikan **Vigenère Cipher klasik** secara manual (tanpa library kriptografi). Semua proses berjalan lokal, tanpa database dan tanpa API eksternal.

## 2. Features
- Enkripsi dan dekripsi Vigenère
- Detail proses per huruf (tabel Position, Input, Key, nilai, Operation, Output)
- Tabel Vigenère (tabula recta) 26×26 yang dibuat dinamis dengan JavaScript
- Menjaga spasi, angka, tanda baca, dan huruf besar/kecil
- Validasi input, tombol Copy Result dan Clear
- UI dark, responsif, berbasis kartu
- Unit test untuk algoritma dan API

## 3. Vigenère Cipher
Cipher substitusi polialfabetik yang memakai keyword. Setiap huruf digeser sejauh nilai huruf key, dan key diulang sepanjang teks. Karakter non-huruf tidak dienkripsi dan tidak menggeser posisi key.

## 4. Formula
Mapping: `A=0, B=1, ..., Z=25`

```text
Enkripsi: C = (P + K) mod 26
Dekripsi: P = (C - K) mod 26
```

## 5. Project Structure
```text
vigenere-cipher/
├── app.py                 # Flask app & API route
├── cipher/
│   ├── __init__.py
│   └── vigenere.py        # Logika Vigenère (murni Python)
├── templates/index.html
├── static/css/style.css
├── static/js/script.js
├── tests/test_vigenere.py
├── requirements.txt
└── README.md
```

## 6. Installation
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 7. How to Run
```bash
python app.py
```
Buka http://127.0.0.1:5000

Menjalankan test:
```bash
python -m unittest -v tests.test_vigenere
```

## 8. Example Encryption
```text
Plaintext  : HELLO WORLD
Key        : KEY
Ciphertext : RIJVS UYVJN
```
Contoh huruf pertama: H = 7, K = 10, (7 + 10) mod 26 = 17 = R.

## 9. Example Decryption
```text
Ciphertext : RIJVS UYVJN
Key        : KEY
Plaintext  : HELLO WORLD
```
Contoh nilai negatif: B - Z = 1 - 25 = -24, lalu (-24 + 26) mod 26 = 2 = C.

## 10. Technologies Used
Python 3, Flask, HTML5, CSS3, JavaScript (vanilla).