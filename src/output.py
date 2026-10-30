
def tampilkan_hasil(hasil):
    print("\n=== HASIL ANALISIS ===")
    print(f"Jumlah siswa       : {hasil['jumlah']}")
    print(f"Rata-rata nilai    : {hasil['rata_rata']:.2f}")
    print(f"Jumlah lulus       : {hasil['jumlah_lulus']}")
    print(f"Jumlah tidak lulus : {hasil['jumlah_tidak_lulus']}")

    if hasil["jumlah"] > 0:
        print(f"Nilai minimum      : {hasil['minimum']}")
        print(f"Nilai maksimum     : {hasil['maksimum']}")
    else:
        print("Belum ada data nilai.")


def simpan_hasil(hasil):
    with open("data/hasil_rekap.txt", "w", encoding="utf-8") as file:
        file.write("HASIL ANALISIS NILAI SISWA\n")
        file.write(f"Jumlah siswa: {hasil['jumlah']}\n")
        file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")
        file.write(f"Nilai minimum: {hasil['minimum']}\n")
        file.write(f"Nilai maksimum: {hasil['maksimum']}\n")
        file.write(f"Jumlah lulus: {hasil['jumlah_lulus']}\n")
        file.write(
            f"Jumlah tidak lulus: {hasil['jumlah_tidak_lulus']}\n"
        )

    print("Hasil berhasil disimpan.")
