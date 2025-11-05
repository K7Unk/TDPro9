"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""
def jawaban():

    while True:
        try:
            berapaangka = int(input("Mau memasukkan berapa angka?"))
            break
        except ValueError:
            print("Harap masukkan angka")
        
    kotak_angka = []

    for i in range(berapaangka):
        while True:
            try:
                angkainputan = int(input("Masukkan angka : "))
                kotak_angka.append(angkainputan)
                break
            except ValueError:
                print("Tolong masukkan angka")

    total = sum(kotak_angka)
    rata2 = total/len(kotak_angka)
    print(f"Total angka adalah : {total}\nRata-ratanya adalah: {rata2}")


jawaban()
