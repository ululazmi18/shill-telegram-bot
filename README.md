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
  channel2
  ```

### **4. Menjalankan Skrip**
Jalankan dengan:
```bash
python main.py
```
Skrip akan secara otomatis:
- Menggunakan semua akun `.session` yang tersedia.
- Memilih teks, media, dan channel secara acak.
- Mengirim pesan sesuai jumlah yang diatur di `config.json`.

---

| **No** | **Fungsi/Fitur**                  | **Penjelasan** |
|-------|--------------------------------|-------------|
| **1** | **Menggunakan semua file `.session`** | Skrip akan membaca semua file sesi yang ada di folder `sessions/` dan menggunakannya untuk mengirim pesan. |
| **2** | **Mengambil `api_id` dan `api_hash` dari `config.json`** | Skrip tidak lagi meminta `api_id` dan `api_hash` dari `akun.txt`, melainkan langsung mengambil dari `config.json`. |
| **3** | **Mengambil jumlah pesan (`JumlahPost`) dari `config.json`** | Skrip akan mengirim pesan sebanyak angka yang ada di `JumlahPost`. Jika tidak ada, defaultnya adalah **2**. |
| **4** | **Memilih teks secara acak dari folder `text/`** | Setiap kali mengirim pesan, skrip akan memilih file `.txt` secara acak dari folder `text/` sebagai isi pesan. |
| **5** | **Memilih media secara acak dari folder `media/`** | Skrip akan memilih satu file secara acak dari folder `media/` yang bisa berupa `.jpg` atau `.mp4`. |
| **6** | **Menentukan jenis media secara otomatis** | Jika file media yang terpilih adalah `.jpg`, akan dikirim sebagai foto. Jika `.mp4`, akan dikirim sebagai video. |
| **7** | **Memilih daftar channel secara acak dari folder `channel/`** | Skrip akan memilih satu file secara acak dari folder `channel/`, kemudian mengambil daftar channel dari file tersebut. |
| **8** | **Menggunakan akun Telegram secara bersamaan** | Skrip akan menjalankan setiap akun `.session` dalam proses async, sehingga semua akun dapat mengirim pesan bersamaan. |
| **9** | **Mengatasi `FloodWait` secara otomatis** | Jika ada batasan dari Telegram (FloodWait), skrip akan otomatis menunggu selama waktu yang diminta + 10 detik sebelum melanjutkan. |
| **10** | **Melanjutkan ke pesan berikutnya jika ada kesalahan** | Jika pengiriman pesan gagal karena alasan lain (misalnya akun diblokir dari channel), skrip tidak akan berhenti, tetapi langsung lanjut ke pengiriman berikutnya. |
| **11** | **Tidak mengulang pesan yang gagal** | Jika sebuah pesan gagal dikirim, skrip tidak akan mencoba mengulangnya, tetapi tetap lanjut ke jumlah pengiriman yang tersisa. |
| **12** | **Menggunakan jeda acak antar pengiriman** | Skrip memberikan jeda acak antara **5-10 detik** antar pengiriman untuk menghindari deteksi spam oleh Telegram. |

---
