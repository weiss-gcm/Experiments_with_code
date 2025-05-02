# Class
# Array
# Looping
# Stack/Queue

class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def subtotal(self):
        return self.harga * self.jumlah

list_belanja = [] #<-- Array bentuk List untuk menyimpan barang belanjaan
history_stack = [] #<-- Stack untuk menyimpan riwayat transaksi

def tampilkan_menu():
    print("\n--- MENU MINIMARKET ---")
    print("1. Tambah Barang")
    print("2. Lihat Daftar Belanja")
    print("3. Hitung Total & Bayar")
    print("4. Keluar")
    return input("Pilih menu (1-4): ")

def tambah_barang():
    nama = input("Nama barang: ")
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    barang = Barang(nama, harga, jumlah)
    list_belanja.append(barang)
    history_stack.append(f"Tambah {nama} x{jumlah}")

def tampilkan_belanja():
    if not list_belanja:
        print("Belum ada belanjaan.")
        return
    print("\n--- Daftar Belanja ---")
    print(f"{'Nama':<15}{'Harga':<10}{'Jumlah':<10}{'Subtotal':<10}")
    for b in list_belanja:
        print(f"{b.nama:<15}{b.harga:<10}{b.jumlah:<10}{b.subtotal():<10}")
        
def hitung_total_dan_bayar():
    if not list_belanja:
        print("Tidak ada belanjaan.")
        return
    total = sum(b.subtotal() for b in list_belanja)
    tampilkan_belanja()
    print(f"\nTotal Belanja: Rp {total}")
    bayar = int(input("Masukkan jumlah uang: Rp "))
    if bayar < total:
        print("Uang tidak cukup!")
    else:
        print(f"Kembalian: Rp {bayar - total}")
        history_stack.append("Transaksi selesai")

while True:
    pilihan = tampilkan_menu()
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        tampilkan_belanja()
    elif pilihan == '3':
        hitung_total_dan_bayar()
        break
    elif pilihan == '4':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
