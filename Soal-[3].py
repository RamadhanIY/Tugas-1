Nilai_Teori = int(input("Nilai Teori Anda: "))
Nilai_Praktek = int(input("Nilai Praktek Anda: "))
KKM = 70
if Nilai_Teori >= KKM and Nilai_Praktek >= KKM:
    print("Selamat, anda lulus!")
elif Nilai_Teori >= KKM and Nilai_Praktek <= KKM:
    print("Anda harus mengulang ujian praktek.")
elif Nilai_Teori <= KKM and Nilai_Praktek >=KKM:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")