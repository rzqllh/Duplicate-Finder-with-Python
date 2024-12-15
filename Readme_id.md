# Duplicate Finder (Bahasa Indonesia)

Duplicate Finder adalah sebuah skrip Python untuk mendeteksi gambar serupa dalam sebuah folder menggunakan kombinasi metode **hash perceptual** dan **SIFT feature matching**. Skrip ini dirancang untuk membantu Anda menemukan file gambar duplikat atau hampir serupa berdasarkan toleransi yang dapat diatur.

---

## 🎯 Fitur Utama

- **Hash Perceptual**
  - Menggunakan algoritma perceptual hash untuk mendeteksi kesamaan gambar dengan cepat dan efisien.
- **SIFT Feature Matching**
  - Membandingkan fitur visual gambar menggunakan metode **Scale-Invariant Feature Transform (SIFT)** untuk hasil yang lebih mendetail.
- **Toleransi yang Dapat Diatur**
  - Anda dapat menyesuaikan tingkat kesamaan melalui parameter hash dan threshold SIFT agar sesuai dengan kebutuhan spesifik Anda.
- **Umpan Balik Real-Time**
  - Proses pencarian memberikan pembaruan progres sehingga Anda tahu file mana yang sedang diproses.

---

## ⚙️ Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal:

- Python 3.6 atau lebih baru
- Library berikut:
  - `opencv-python`
  - `imagehash`
  - `Pillow`

Untuk menginstal dependensi, gunakan perintah berikut:

```bash
pip install opencv-python imagehash Pillow
```

---

## 🚀 Cara Penggunaan

1. Simpan file `Duplicate_finder.py` ke dalam direktori lokal Anda.
2. Jalankan skrip menggunakan terminal atau command prompt:

```bash
python Duplicate_finder.py
```

3. Masukkan path gambar sumber yang ingin Anda cari duplikasinya.
4. Masukkan path folder tempat pencarian gambar dilakukan.
5. Skrip akan mencari gambar serupa dan menampilkan hasilnya di terminal.

---

## 📝 Contoh Input dan Output

**Input:**

```
Masukkan path gambar sumber: ./example/source.jpg
Masukkan path folder yang akan dicari: ./example/folder_to_search
```

**Output:**

```
Menghitung hash untuk gambar sumber...
Memulai pencarian gambar serupa...
Memproses file 1/10: ./example/folder_to_search/img1.jpg
...

Gambar serupa ditemukan:
./example/folder_to_search/duplicate1.jpg
./example/folder_to_search/duplicate2.jpg
```

---

## ⚡ Parameter yang Dapat Disesuaikan

Anda dapat mengatur parameter berikut dalam fungsi `find_duplicates`:

- `threshold`: Toleransi perbedaan hash (default: 5). Semakin kecil nilai ini, semakin ketat pencarian.
- `sift_threshold`: Minimum jumlah "good matches" untuk metode SIFT (default: 10).

---

## 🚧 Keterbatasan

- **Kualitas Gambar**
  - Metode ini bergantung pada kualitas gambar. Jika gambar buram atau mengalami transformasi besar, hasilnya mungkin kurang akurat.
- **Format File Terbatas**
  - Hanya mendukung format gambar umum seperti PNG, JPEG, BMP, GIF, dan TIFF. File non-gambar akan diabaikan secara otomatis.
- **Kecepatan Proses**
  - Proses dapat memakan waktu jika jumlah file sangat banyak, terutama saat menggunakan threshold SIFT yang tinggi.

---

## 🤝 Kontribusi

Kami terbuka untuk kontribusi dari komunitas. Jika Anda memiliki ide untuk meningkatkan skrip ini, jangan ragu untuk:

1. Membuat fork repository ini.
2. Melakukan perbaikan atau penambahan fitur.
3. Mengirimkan pull request.

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Anda bebas menggunakan dan memodifikasi proyek ini sesuai kebutuhan.

---

## 🎉 Penutup

Semoga skrip ini bermanfaat untuk kebutuhan Anda. Jangan ragu untuk membagikan saran atau umpan balik!

Happy Coding! 😊
