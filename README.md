# Analisis Nilai Siswa

Nama: Mafatihun Nabila  
NIM: 2225250918  
Kelas: 3B

## Deskripsi Proyek

Program Analisis Nilai Siswa merupakan program Python yang digunakan untuk mengolah dan menganalisis nilai siswa. Program ini dapat menghitung rata-rata nilai, mencari nilai tertinggi dan terendah, serta menentukan jumlah siswa yang lulus dan tidak lulus.

## Tujuan

1. Menerapkan konsep pemrograman Python.
2. Membuat program dengan beberapa modul.
3. Mengolah dan menganalisis data nilai siswa.
4. Melakukan pengujian untuk memastikan program berjalan dengan baik.

## Fitur Program

1. Memasukkan nilai siswa.
2. Memvalidasi input nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata nilai.
4. Menampilkan nilai tertinggi dan terendah.
5. Menghitung jumlah siswa yang lulus dan tidak lulus.
6. Menyimpan hasil analisis ke dalam file.

## Ketentuan Kelulusan

Nilai minimal untuk dinyatakan lulus adalah 60.

- Nilai >= 60: Lulus.
- Nilai < 60: Tidak Lulus.

## Struktur Folder

```text
Mafatihun Nabila-proyek/
├── data/
│   ├── contoh_data.txt
│   └── hasil_rekap.txt
├── docs/
│   └── screenshot/
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── tests/
│   └── test_case.md
├── .gitignore
├── main.py
└── README.md
```

## Cara Menjalankan Program

Pastikan Python sudah terpasang, kemudian buka terminal pada folder proyek dan jalankan perintah:

```bash
python main.py
```

Masukkan nilai siswa satu per satu. Jika semua nilai sudah dimasukkan, ketik `selesai` untuk mengakhiri input dan menampilkan hasil analisis.

## Pengujian

Pengujian dilakukan menggunakan beberapa kondisi, yaitu:

1. Menghitung rata-rata dari beberapa nilai.
2. Memeriksa nilai tepat 60 sebagai batas kelulusan.
3. Memasukkan teks yang bukan angka.
4. Menguji data nilai kosong.
5. Memasukkan nilai di luar rentang 0–100.

Hasil pengujian dicatat dalam folder `tests`.

## Kesimpulan

Program ini dibuat untuk menerapkan materi Python, khususnya penggunaan fungsi, modul, validasi input, pengolahan data, dan pengujian program. Dengan adanya program ini, proses analisis nilai siswa dapat dilakukan secara lebih mudah dan terstruktur.

## Referensi

Bahan Ajar Algoritma dan Pemrograman Pertemuan 15.
