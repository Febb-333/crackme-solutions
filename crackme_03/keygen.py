import random

def generate_crackme_license():
    """
    Skrip Keygen Generator Otomatis untuk Solusi Crackme 03.
    Aturan Lisensi: Diawali karakter 'A' dan diikuti 4 digit angka acak.
    """
    prefix = "A"
    # Menghasilkan 4 digit angka acak secara matematis
    numeric_part = "".join([str(random.randint(0, 9)) for _ in range(4)])
    license_key = prefix + numeric_part
    
    print("="*45)
    print("      CRACKME 03 LICENSE KEY GENERATOR       ")
    print("="*45)
    print(f"[+] Berhasil memproduksi kunci lisensi valid: {license_key}")
    print("="*45)

if __name__ == "__main__":
    generate_crackme_license()
