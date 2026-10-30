
from src.input_data import input_nilai
from src.proses import ringkasan
from src.output import tampilkan_hasil, simpan_hasil


def main():
    nilai = input_nilai()
    hasil = ringkasan(nilai)

    tampilkan_hasil(hasil)

    try:
        simpan_hasil(hasil)
    except OSError as error:
        print(f"Gagal menyimpan hasil: {error}")


if __name__ == "__main__":
    main()
