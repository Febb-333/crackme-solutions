# Solusi Crackme 02: Modifikasi Instruksi Percabangan / Patching (Easy Level)

- **Sumber Tantangan:** crackmes.one
- **Kakas yang Digunakan:** x64dbg Debugger
- **Target Operasi:** Membuka fungsi registrasi yang terkunci tanpa mengetahui kunci lisensi asli.

### Langkah Analisis:
1. Program dijalankan di dalam debugger x64dbg untuk memantau alur instruksi per baris secara dinamis.
2. Pencarian dilakukan pada referensi teks *String References* untuk menemukan logika percabangan kegagalan lisensi.
3. Ditemukan operasi perbandingan `CMP` diikuti dengan instruksi lompatan bersyarat `JZ` (Jump if Zero) menuju alamat memori bertuliskan "Invalid License Key".
4. Saya melakukan *patching* kode Assembly dengan merubah instruksi bersyarat `JZ` tersebut menjadi instruksi lompatan mutlak `JMP` (Jump) agar program mengabaikan hasil pengecekan.

### Solusi Bendera (Flag):
Melalui taktik *Patching Assembly*, alur kode berhasil dimanipulasi secara paksa. Program berhasil diekspor kembali menjadi biner baru (*patched executable*) yang selalu berstatus "Registration Successful" untuk input kunci apa saja.
