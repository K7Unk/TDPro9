"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""

def jualan(a):
    harga_total = []
    """
    while True:
        try:
            a = int(input("Masukkan jumlah barang yang sudah terjual: "))
            break
        except ValueError:
            print("Mohon masukkan angka :)")
            """

    for i in range(a):
        print(f"\nBarang ke {i+1}")
        while True:
            try:
                harga = int(input("Masukkan harga barang: "))
                if harga <= 0:
                    print("Harap masukkan angka positif")
                    continue
                break
            except ValueError:
                print("Tolong masukkan angka")
        harga_total.append(harga)


    def statistik():
        total_pendapatan = sum(harga_total)
        rata_rata = total_pendapatan/len(harga_total)
        print(f"\nTotal pendapatan: {total_pendapatan}\nRata-rata pendapatan: {rata_rata}")
    statistik()
    
jualan(4)