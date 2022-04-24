#existing contact
kontak = {
    'nama': ('Farhan', 'Joko', 'Anwar'),
    'telp': ('08123456789', '08987654321', '08195643587')
    }

nama = list(kontak['nama'])
telp = list(kontak['telp'])

def main():
    #start program
    print("Selamat Datang !")
    print(f"\n---Menu---")
    print(f"1. Daftar Kontak")
    print(f"2. Tambah Kontak")
    print(f"3. Keluar")
    pilih= int(input("Masukkan pilihan: "))
    option(pilih)

def option(pilih):
    if pilih == 1:
    #menampilan daftar kontak
        print("\nDaftar Kontak: ")
        for a, b in zip(nama, telp):
            print(f"Nama: {a}\nNo.Telp: {b}\n")
        main()    
    elif pilih == 2:
        #menambahkan kontak baru
        print(f"\nMasukkan nama dan nomor telp yang ingin ditambahkan:")
        nama_baru = input("Nama: ")
        telp_baru = input("No. Telp: ")
        nama.append(nama_baru)
        telp.append(telp_baru)
        print(f"\nData berhasil di tambahkan")
        main()    
    elif pilih == 3:
        #program selesai
        print(f"Program selesai!\nSampai jumpa!")
    else:
        print(f"\nMenu tidak tersedia")
        print(f"\nSilahkan pilih menu yg lainnya")
        main()
main()