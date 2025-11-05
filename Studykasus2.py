"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""


def volume_tabung(jari_jari,tinggi):
    volume = jari_jari*jari_jari*22/7*tinggi
    print(f"Volume tabung adalah: {volume}")
    return volume

print(volume_tabung(7,10))