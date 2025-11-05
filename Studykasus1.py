"""
============================
Nama : Muslihan Gio Suwanda
NIM : 2508126
Kelas : 1B
Materi : Function and Procedure
============================
"""

def deretfibonaci(n):
    deret = [0,1]
    for i in range(2, n):
        deret.append(deret[i-1] + deret[i-2])
    print(deret)
deretfibonaci(6)