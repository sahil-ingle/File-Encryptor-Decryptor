# File Encryptor & Decryptor

A simple Python project to **encrypt any file into a black-and-white image** and later **decrypt it back to the original file**.
This project demonstrates file encoding using **hexadecimal and binary representations** stored visually in an image.

---

## 🔹 Project Overview

* **Encrypt**: Converts a file → hex → binary → black-and-white image (`crypted.png`).
* **Decrypt**: Reads the black-and-white image → binary → hex → reconstructs the original file (`output.png`).
* Ideal for learning **file encoding and basic image-based data storage**.

> ⚠️ **Note:** This is not cryptographically secure. Use only for educational purposes.

---

## 🔹 Project Structure

```
.
├── encrypt.py       # Script to encrypt a file into an image
├── decrypt.py       # Script to decrypt the image back to original
├── main.py          # For testing purposes (unreliable)
├── input2.png       # Example input file
├── crypted.png      # Output encrypted image
├── output.png       # Reconstructed decrypted file
├── hex_data.txt     # Temporary hex data
├── binary_data.txt  # Temporary binary data
└── hex_data_opt.txt # Optimized hex data used for reconstruction
```

---

## 🔹 Installation

1. Make sure you have **Python 3.x** installed.
2. Install the required library:

```bash
pip install Pillow
```

---

## 🔹 Usage

### Encrypt a file

```bash
python encrypt.py
```

* The input file is converted into `crypted.png`.

### Decrypt a file

```bash
python decrypt.py
```

* The encrypted image is converted back to the original file as `output.png`.

> ⚠️ Avoid using `main.py`; it is only for testing and may be unreliable.

---

## 🔹 Notes

* Ensure the encrypted image dimensions are large enough to store **all binary bits** of the file.
* Black pixels represent `1` and white pixels represent `0`.
* Temporary files (`hex_data.txt`, `binary_data.txt`, `hex_data_opt.txt`) are used internally and can be safely deleted.

---

## 🔹 Example Workflow

1. Place your file as `input2.png`.
2. Run `encrypt.py` → generates `crypted.png`.
3. Run `decrypt.py` → restores the file as `output.png`.

---

## 🔹 License

This project is open-source and free to use for **educational purposes**.
