import csv
import os
from models import Buku


def muat_data():
    daftar_buku = []

    if not os.path.exists("buku.csv"):
        print("File buku.csv tidak ditemukan.")
        return daftar_buku

    with open("buku.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Lewati header
        next(reader, None)

        for row in reader:
            # Pastikan data lengkap
            if len(row) < 4:
                continue

            buku = Buku(
                judul=row[0],
                penulis=row[1],
                isbn=row[2],
                status=row[3]
            )

            daftar_buku.append(buku)

    return daftar_buku


def tampilkan_buku():
    daftar_buku = muat_data()

    if not daftar_buku:
        print("\nTidak ada data buku.\n")
        return

    print("\n" + "=" * 80)
    print("DAFTAR BUKU PERPUSTAKAAN".center(80))
    print("=" * 80)

    print(
        f"{'Judul':25}"
        f"{'Penulis':20}"
        f"{'ISBN':20}"
        f"{'Status'}"
    )

    print("-" * 80)

    for buku in daftar_buku:
        print(
            f"{buku.judul[:24]:25}"
            f"{buku.penulis[:19]:20}"
            f"{buku.isbn[:19]:20}"
            f"{buku.status}"
        )

    print("-" * 80)
    print(f"Total Buku: {len(daftar_buku)}")
    print("=" * 80)


def main():
    while True:
        print("\n=== MENU TAMPIL BUKU ===")
        print("1. Tampilkan Buku")
        print("2. Refresh Data")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_buku()

        elif pilihan == "2":
            print("\nData berhasil dimuat ulang.")
            tampilkan_buku()

        elif pilihan == "0":
            print("Kembali ke menu utama...")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()