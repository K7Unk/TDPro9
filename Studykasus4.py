"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""
def login(a):
    jumlah = a
    while True:
        if jumlah == 0:
            print(f"Salah {a} kali")
            return 

        user = input("\nMasukkan id: ")
        password = input("Masukkan password: ")

        if jumlah == 0:
            print("Kesempatan anda sudah habis: ")
            break

        else:
            if "FammRIOT" in user and "Fauzivalorant123" in password:
                print("Selamat datang User!")
                break
            
            else:
                print("\nMasukkan kembali id dan password")
                jumlah -=1
                print(f"Sisa pengulangan {jumlah}")
                
login(3)

def sapa(a):
    print(f"Halo ! {a}")

sapa("Fauzi")

