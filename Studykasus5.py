"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""

def selisihwaktu():
    print("=====Mulai=====")
    jam = int(input("Masukkan waktu mulai, dalam jam: "))
    menit = int(input("Masukkan waktu mulai, dalam menit: "))
    detik = int(input("Masukkan waktu mulai, dalam detik: "))
    print("=====Selesai=====")
    jam1 = int(input("Masukkan waktu berhenti, dalam jam: "))
    menit1 = int(input("Masukkan waktu berhenti, dalam menit: "))
    detik1 = int(input("Masukkan waktu berhenti, dalam detik: "))

    print(f"Selisih waktu = {jam1 - jam} Jam, {menit1 - menit} Menit, {detik1-detik} Detik.")

selisihwaktu()
