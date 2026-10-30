
BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)


def status_lulus(nilai):
    return [angka for angka in nilai if angka >= BATAS_LULUS]


def ringkasan(nilai):
    jumlah_lulus = len(status_lulus(nilai))

    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": len(nilai) - jumlah_lulus,
    }
