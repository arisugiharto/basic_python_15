## menghitung nilai kelulusan
ujian_teori = int(input("Nilai Ujian Teori: "))
ujian_praktek = int(input("Nilai Ujian Praktek: "))
if ujian_teori>=70 and ujian_praktek>=70:
    print("Selamat, anda lulus !")
elif ujian_teori >=70 and ujian_praktek <70:
    print("Anda  harus mengulang ujian Praktek")
elif ujian_teori <70 and ujian_praktek >=70:
    print("Anda harus mengulang ujian teori")
else:
    print ("Anda harus mengulang ujian teori dan praktek")