import random

nama = [
    "Ridho Arjumal",
	"Rahmat Ramadhan Al Hais",
	"Harry Anshary",
	"Arwadi Setia Budi",
	"Muhammad Fadillah",
	"Tegar Ferdigantara",
	"Bayu Firmadi",
	"Giovany Kelvin Vatikan",
	"Muhamad Rafi H.W",
	"Devi Indah Wulandari",
	"Muhammad Pramudia Irvan",
	"Eraldo Jonathan Ramadhan",
	"Naufal Zahran Latif",
	"Andry Maulana",
	"Gusti Izza Maulana",
	"Ramadhan",
	"Alfredo Michael Alliandaw",
	"Faul Oliber Ms.",
	"Fernando Nestadianto",
	"Malekhiano Paskarian",
	"Ikhsan Putra",
	"Fachrul Ramadhanu",
	"Kristian Redondo",
	"Muhammad Aidil Rifaldi",
	"Ando Riswanto",
	"Indah Sridianti", 
	"Erwin Tampubolon",
	"Dhiya Ulhaq"
    ]

tim = int(input("Jumlah Kelompok: "))
member = len(nama)//tim
lebih = len(nama) % tim

keluar = []
cek = False

def tampilkanNama():
    nomor = random.randrange(len(nama)) #randomnya antara 0 sampai 27
    if len(keluar) == 0:
        print("\t\t", nama[nomor])
        keluar.append(nomor)
    else:
        for i in range(len(keluar)):
            if nomor == keluar[i]:
                cek = False
                break
            else:
                cek = True
        
        if cek:
            print("\t\t", nama[nomor])
            keluar.append(nomor)
        else:
            tampilkanNama()
        

for i in range(tim): #menampilkan kelompok
    print("Kelompok", i+1)
    if i < lebih:
        for j in range(member+1): #menampilkan nama
            tampilkanNama()
    else:
        for j in range(member): #menampilkan nama
            tampilkanNama()