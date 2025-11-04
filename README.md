# UTS: PENERAPAN SISTEM PAKAR PADA SMART BUDGETING ASSISTANT

# 📃 Identitas Kelompok

- **Nama Kelompok**    : Kelompok NPC
- **Anggota Kelompok** : 1. Betrand Daffarel (4523210029)
                         2. Eka Lidya Rahmadini (4523210039)
                         3. Revalina Adelia (4523210091)
- **Mata Kuliah**      : Intelligent System (A)
- **Dosen Pengampu**   : Ninuk Wiliani, S.Si., M.Kom., Phd
- **Tanggal**          : 29 Oktober 2025
- **Materi**           : Sistem Pakar

---
## 🎯 Tujuan Pembelajaran

Proyek ini dibuat:
1. Menerapkan konsep **Sistem Pakar (_Expert System_)** dalam konteks kehidupan nyata.
2. Memahami cara kerja **penalaran berbasis aturan (_rule-based reasoning_)** menggunakan **_Forward Chaining_** dan **_Backward Chaining_**.
3. Melatih kemampuan analisis dalam menyusun **basis pengetahuan (_knowledge base_) yang terdiri dari aturan dan fakta.
4. Mengembangkan aplikasi **interaktif berbasis Streamlit** yang dapat membantu pengguna mengelola keuangan secara cerdas.
5. Menunjukkan penerapan **Artificial Intelligence sederhana** di bidang finansial pribadi.

---
## 💰 Domain Sistem

Domain yang digunakan dalam proyek ini adalah **Smart Budgeting Assistant**, yaitu sistem pakar yang berfokus pada pengelolaan keuangan pribadi. Sistem ini membantu pengguna dalam mengambil keputusan finansial yang lebih cerdas berdasarkan kondisi aktual, seperti jumlah pendapatan, total pengeluaran, serta rencana alokasi dana untuk investasi, tabungan, dan dana darurat. Melalui pendekatan sistem pakar, _Smart Budgeting Assistant_ dapat memberikan saran dan rekomendasi otomatis, misalnya menambah alokasi tabungan jika persentasenya terlalu kecil, atau mengingatkan pengguna untuk mengurangi pengeluaran jika melebihi batas wajar. Dengan demikian, sistem ini tidak hanya berfungsi sebagai alat bantu hitung, tetapi juga sebagai **asisten keuangan cerdas** yang membantu pengguna mencapai stabilitas finansial secara terarah dan rasional. 

---
## 🤖 Jenis Agent

Sistem ini menggunakan **_Rule-Based Agent_**, yaitu agen yang bekerja dengan memanfaatkan kumpulan aturan (_rules_) dan fakta (_facts_) yang tersimpan dalam basis pengetahuan. Agen ini berperan sebagai "otak" sistem yang mampu melakukan proses penalaran untuk menghasilkan keputusan atau rekomendasi secara otomatis. Dalam proyek _Smart Budgeting Assistant_, agen menganalisis data keuangan pengguna, seperti pendapatan, pengeluaran, pendapatan, dan persentase alokasi dana, kemudian mencocokkannya dengan aturan-aturan yang telah ditentukan. Proses penalaran yang digunakan melibatkan dua pendekatan utama, yaitu **_Forward Chaining_** (penalaran maju) untuk menarik kesimpulan baru dari fakta awal, dan **_Backward Chaing_** (penalaran mundur) untuk memverifikasi kebenaran dari kesimpulan yang dihasilkan. Dengan jenis agen ini, sistem dapat meniru cara berpikir seorang pakar keuangan sederhana dalam memberikan rekomendasi yang logis dan relevan bagi pengguna.

---
## 🧠 Metode Reasoning

Sistem ini menggunakan dua metode penalaran utama, yaitu **_Forward Chaining_** dan **_Backward Chaining_**:
1. **_Forward Chaining_ (Penalaran Maju)**: Digunakan untuk mencari kesimpulan baru berdasarkan fakta-fakta awal yang dimasukkan oleh pengguna. Prosesnya dimulai dari data yang sudah diketahui (seperti pendapatan dan pengeluaran), kemudian sistem mencocokkan fakta tersebut dengan aturan yang ada untuk menghasilkan saran atau rekomendasi otomatis.
   
2. **_Backward Chaining_ (Penalaran Mundur)**: Digunakan untuk memverifikasi apakah suatu kesimpulan atau rekomendasi benar-benar didukung oleh fakta yang ada. Proses ini dimulai dari "tujuan" yang ingin dibuktikan, lalu sistem menelusuri aturan yang relevan untuk memastikan apakah kesimpulan tersebut dapat dipertanggungjawabkan.

---
## ⚙️ Aturan dan Fakta yang Digunakan

**1. Aturan yang Digunakan**

1.	Jika pendapatan tinggi dan pengeluaran rendah, sistem menyarankan investasi agresif.
2.	Jika pendapatan sedang dan pengeluaran tinggi, sistem menyarankan fokus pada tabungan stabil.
3.	Jika pendapatan rendah dan pengeluaran sangat tinggi, sistem menyarankan pemangkasan biaya.
4.	Jika sisa uang besar, sistem menyarankan meningkatkan alokasi investasi/tabungan.
5.	Jika sisa uang sangat kecil, sistem memberi peringatan potensi kekurangan kas.
6.	Jika persentase investasi kurang dari batas ideal, sistem menyarankan menambah investasi.
7.	Jika persentase tabungan terlalu kecil, sistem menyarankan meningkatkan tabungan.
8.	Jika dana darurat tidak mencukupi, sistem menyarankan menambah alokasi dana darurat.
9.	Jika pengeluaran sangat tinggi, sistem memberi peringatan untuk dikurangi.
10.	Jika pengeluaran rendah dengan pendapatan sedang, sistem merekomendasikan rencana keuangan moderat.

**2. Fakta yang Digunakan**

1.	`high_income`: Pendapatan tinggi
2.	`medium_income`: Pendapatan sedang
3.	`low_income`: Pendapatan rendah
4.	`very_high_expense`: Pengeluaran sangat tinggi
5.	`high_expense`: Pengeluaran tinggi
6.	`low_expense`: Pengeluaran rendah
7.	`large_remaining`: Sisa uang besar
8.	`small_remaining`: Sisa uang sangat kecil
9.	`low_investment_allocation`: Alokasi investasi di bawah ideal
10.	`low_saving_allocation` atau `low_emergency_allocation`: Alokasi tabungan/dana darurat rendah

---
## 📂 Struktur Project

---
## 🧩 Teknologi yang Digunakan

Proyek ini dikembangkan menggunakan bahasa pemrograman Python dengan beberapa library utama yang mendukung sistem pakar dan antarmuka pengguna:
1. **Streamlit**: Untuk membuat tampilan aplikasi web interaktif.
2. **Pandas**: Untuk mengelola dan menampilkan data pengeluaran pengguna.
3. **Python (_built-in functions_) 3.x**: Untuk proses inferensi, penalaran, serta pengolahan aturan dan fakta.
   
---
## 🚀 Cara Menjalankan Program


