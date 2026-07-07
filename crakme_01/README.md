# Solusi Crackme 01: Analisis String Statis (Easy Level)

- **Sumber Tantangan:** crackmes.one
- **Kakas yang Digunakan:** Ghidra Decompiler
- **Target Operasi:** Melacak *password* otentik yang tersembunyi di dalam biner.

### Langkah Analisis:
1. Berkas biner diimpor ke dalam Ghidra untuk dianalisis struktur fungsinya.
2. Penelusuran pada jendela *Defined Strings* menunjukkan adanya teks konstan berupa perintah "Enter Password: ".
3. Saya melacak referensi silang (*cross-reference*) dari string tersebut untuk menemukan fungsi validasi utamanya.
4. Hasil dekompilasi pseudokode bahasa C menunjukkan penggunaan fungsi standar `strcmp` (String Compare). Program membandingkan data input pengguna secara langsung dengan kunci rahasia yang di-*hardcoded*.

### Solusi Bendera (Flag):
Kunci rahasia yang ditemukan di dalam memori `.rodata` adalah: `SuperSecretPassword123`. Ketika string ini dimasukkan, program sukses memberikan respons "Access Granted".
