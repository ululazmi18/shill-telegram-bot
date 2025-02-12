## **Instruksi Penggunaan**

### **1. Persiapan Awal**
Pastikan Anda memiliki file dan folder berikut:
```
📂 sessions/   → Menyimpan file sesi (.session)
📂 text/       → Menyimpan teks pesan (.txt)
📂 media/      → Menyimpan gambar (.jpg) & video (.mp4)
📂 channel/    → Menyimpan daftar channel (satu file berisi list channel)
📄 config.json → Menyimpan api_id, api_hash, dan jumlah pesan yang dikirim
```

### **2. Isi `config.json`**
Buat file `config.json` di direktori utama dengan isi seperti ini:
```json
{
  "api_id": 123456,
  "api_hash": "abc123def456",
  "JumlahPost": 3
}
```

### **3. Menambahkan File-File yang Dibutuhkan**
- **File `.session`** → Masukkan semua akun sesi Telegram ke dalam `sessions/`.
- **File `.txt` dalam `text/`** → Simpan pesan yang akan dipilih secara acak.
- **File `.jpg` atau `.mp4` dalam `media/`** → Simpan media untuk dikirim.
- **File daftar channel dalam `channel/`** → Contoh isi `channel_list.txt`:
  ```
  https://t.me/channel1
  https://t.me/channel2
  ```

### **4. Menjalankan Skrip**
Jalankan dengan:
```bash
python b.py
```
Skrip akan secara otomatis:
- Menggunakan semua akun `.session` yang tersedia.
- Memilih teks, media, dan channel secara acak.
- Mengirim pesan sesuai jumlah yang diatur di `config.json`.

---
