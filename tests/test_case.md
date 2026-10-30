# Dokumentasi Test Case - Proyek Analisis Nilai Siswa

| ID | Fitur | Jenis | Input | Expected | Actual Awal | Status Awal | Actual Akhir | Status Akhir |
|---|---|---|---|---|---|---|---|---|
| TC01 | Rata-rata | Normal | [70, 80, 90] | 80.0 | 80.0 | PASS | 80.0 | PASS |
| TC02 | Kelulusan | Boundary | 60 | True | False | FAIL | True | PASS |
| TC03 | Kelulusan | Di bawah batas | 59 | False | False | PASS | False | PASS |
| TC04 | Rata-rata | Kosong | [] | 0 | ZeroDivisionError | FAIL | 0 | PASS |
| TC05 | Validasi | Invalid | 'abc' | ValueError | ValueError | PASS | ValueError | PASS |
| TC06 | Validasi | Invalid | '120' | ValueError | ValueError | PASS | ValueError | PASS |
| TC07 | Validasi | Invalid | '-1' | ValueError | ValueError | PASS | ValueError | PASS |
| TC08 | Validasi | Normal | '85,5' | 85.5 | 85.5 | PASS | 85.5 | PASS |
| TC09 | File | File tidak ada | tidak_ada.txt | (0 nilai, 1 pesan) | (0, 1) | PASS | (0, 1) | PASS |
| TC10 | File | Normal | contoh_data.txt | 8 nilai | 8 | PASS | 8 | PASS |
| TC11 | Median | Normal | [80, 60, 90, 75] | 75.0 | 75.0 | PASS | 75.0 | PASS |