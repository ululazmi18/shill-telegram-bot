import os
import glob
import json
import asyncio
import random
from pyrogram import Client, errors

# Membaca konfigurasi dari file config.json, buat jika tidak ada
def baca_config():
    config_file = "config.json"
    if not os.path.exists(config_file):
        default_config = {
            "api_id": 123456,
            "api_hash": "your_api_hash_here",
            "JumlahPost": 2
        }
        with open(config_file, "w", encoding="utf-8") as file:
            json.dump(default_config, file, indent=4)
        print("[ℹ️] File config.json dibuat dengan pengaturan default. Silakan isi dengan API ID dan API Hash yang benar.")
    
    with open(config_file, "r", encoding="utf-8") as file:
        return json.load(file)

# Mengambil satu file secara acak dari folder tertentu dengan ekstensi yang diberikan
def ambil_file_acak(folder, ekstensi):
    files = glob.glob(os.path.join(folder, f"*.{ekstensi}"))
    return random.choice(files) if files else None

# Mengambil semua file session (.session) yang tersedia dalam folder sessions
def ambil_session_files():
    return [f for f in os.listdir("sessions") if f.endswith(".session")]

# Mengambil daftar channel dari file yang dipilih secara acak di folder channel
def ambil_channel_list():
    files = glob.glob("channel/*")
    if files:
        file_terpilih = random.choice(files)
        with open(file_terpilih, "r", encoding="utf-8") as f:
            return [line.strip().replace("https://t.me/", "") for line in f if line.strip()]
    return []

# Fungsi utama untuk mengirim pesan dari akun Telegram tertentu
async def send_message(session_file, api_id, api_hash, jumlah_post):
    folder_sessions = "sessions"
    folder_text = "text"
    folder_media = "media"
    channels = ambil_channel_list()
    
    if not channels:
        print(f"[❌] Tidak ada channel yang ditemukan di folder 'channel'")
        return
    
    async with Client(name=session_file.replace(".session", ""), api_id=api_id, api_hash=api_hash, workdir=folder_sessions) as app:
        try:
            me = await app.get_me()
            print(f"[✅] Login sebagai {me.first_name} ({me.phone_number})")
            
            for i in range(jumlah_post):
                target_channel = random.choice(channels)  # Pilih channel secara acak
                text_file = ambil_file_acak(folder_text, "txt")  # Pilih teks secara acak
                media_file = ambil_file_acak(folder_media, "jpg") or ambil_file_acak(folder_media, "mp4")  # Pilih media secara acak
                
                message_text = ""
                if text_file:
                    with open(text_file, "r", encoding="utf-8") as f:
                        message_text = f.read().strip()  # Baca isi file teks
                
                if media_file:
                    try:
                        if media_file.endswith(".mp4"):
                            await app.send_video(target_channel, media_file, caption=message_text)  # Kirim video
                        else:
                            await app.send_photo(target_channel, media_file, caption=message_text)  # Kirim foto
                        print(f"[📢] Berhasil mengirim ke {target_channel} ({os.path.basename(media_file)})")
                    except errors.FloodWait as e:
                        print(f"[⏳] FloodWait: Menunggu {e.x + 10} detik...")
                        await asyncio.sleep(e.x + 10)  # Tunggu sebelum mencoba lagi
                else:
                    await app.send_message(target_channel, message_text)  # Kirim teks jika tidak ada media
                    print(f"[📢] Berhasil mengirim teks ke {target_channel}")
                
                await asyncio.sleep(random.randint(5, 10))  # Tambahkan jeda acak agar tidak terdeteksi spam
        except Exception as e:
            print(f"[❌] Error: {e}")

# Fungsi utama yang akan menjalankan semua tugas secara bersamaan
async def main():
    # Pastikan folder yang diperlukan tersedia
    os.makedirs("sessions", exist_ok=True)
    os.makedirs("text", exist_ok=True)
    os.makedirs("media", exist_ok=True)
    os.makedirs("channel", exist_ok=True)
    
    config = baca_config()
    api_id = config["api_id"]
    api_hash = config["api_hash"]
    jumlah_post = config.get("JumlahPost", 2)  # Default jumlah posting adalah 2 jika tidak ada di config.json
    
    session_files = ambil_session_files()
    if not session_files:
        print("[❌] Tidak ada file session di folder 'sessions'")
        return
    
    tasks = [send_message(session, api_id, api_hash, jumlah_post) for session in session_files]
    await asyncio.gather(*tasks)  # Jalankan semua akun secara bersamaan

if __name__ == "__main__":
    asyncio.run(main())
