import csv
import os
from models import Buku


FILE_BUKU = "buku.csv"


def tambah_buku():
    print("\n=== TAMBAH DATA BUKU ===")

    judul = input("Judul   : ").strip()
    penulis = input("Penulis : ").strip()
    isbn = input("ISBN    : ").strip()

    if not judul or not penulis or not isbn:
        print("\nSemua kolom harus diisi!")
        return

    buku = Buku(judul, penulis, isbn)

    file_baru = not os.path.exists(FILE_BUKU)

    with open(FILE_BUKU, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_baru:
            writer.writerow(["Judul", "Penulis", "ISBN", "Status"])

        writer.writerow(buku.to_list())

    print("\nBuku berhasil ditambahkan!")


def tampilkan_buku():
    print("\n=== DAFTAR BUKU ===")

    if not os.path.exists(FILE_BUKU):
        print("Belum ada data buku.")
        return

    daftar_buku = []

    with open(FILE_BUKU, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Lewati header
        next(reader, None)

        for row in reader:
            if len(row) >= 4:
                buku = Buku(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )
                daftar_buku.append(buku)

    if not daftar_buku:
        print("Belum ada data buku.")
        return

    print("-" * 80)
    print(f"{'Judul':25}{'Penulis':20}{'ISBN':20}{'Status'}")
    print("-" * 80)

    for buku in daftar_buku:
        print(
            f"{buku.judul[:24]:25}"
            f"{buku.penulis[:19]:20}"
            f"{buku.isbn[:19]:20}"
            f"{buku.status}"
        )

    print("-" * 80)
    print(f"Total buku: {len(daftar_buku)}")


def menu_utama():

    while True:
        print("\n" + "=" * 40)
        print("       SISTEM PERPUSTAKAAN")
        print("=" * 40)
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_buku()

        elif pilihan == "2":
            tampilkan_buku()

        elif pilihan == "0":
            print("\nTerima kasih!")
            break

        else:
            print("\nPilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()