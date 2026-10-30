
def input_nilai():
    nilai = []

    print("=== ANALISIS NILAI SISWA ===")
    print("Masukkan nilai 0-100.")
    print("Ketik 'selesai' untuk mengakhiri.")

    while True:
        teks = input("Masukkan nilai: ").strip()

        if teks.lower() == "selesai":
            break

        try:
            angka = float(teks)
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if angka < 0 or angka > 100:
            print("Nilai harus antara 0-100!")
            continue

        nilai.append(angka)
        print("Nilai berhasil ditambahkan.")

    return nilai
