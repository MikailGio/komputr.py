# VARIABLE

nama = "Mikail" # string
umur = 14 # integer
lakiLaki = True # boolean (true/false)
tinggi = 165 # float

daftarNama = ["Mikail", "Giovanni", "Mofsol", "Muhammad"] # array      

kalimat = "Nama saya " + nama + ". Umur saya " + str(umur) + " tahun." # type casting
# Nama saya Mikail. Umur saya 15 tahun.

if lakiLaki:
    print("saya laki-laki")
else:
    print("saya perempuan")

print(nama)
nama = 15
print(nama)

panjang = len(daftarNama)
# isi dari array jumlahnya berapa

daftarNama.append("tambahan")
# daftarNama = ["Mikail", "Giovanni", "Mofsol", "Muhammad", "tambahan"]

print(daftarNama[3])

# function
# function name
# function body
# parameter (0 =< N)
# return value (0 =< N)
def tambah(a, b):
    hasil = a + b
    return hasil

c = tambah(5, 4)
print ("hasilnya adalah "+ str(c))

# PERCABANGAN
# if
n = 9
if n < 10:
    print("n adalah satuan")

# if else
if n < 10 and n > 0:
    print("n adalah satuan " + str(n))
else:
    print("n bukan satuan")

# if else if
b = 10
if b < 0:
    print("b bukan negatif, b adalah " + str(b))
elif b < 10:
    print("b adalah satuan")
else: 
    print("b lebih dari atau sama dengan 10")

# PERULANGAN
# literasi
# for loop
i = 0
for nama in daftarNama:
    # nama = daftarNama[index]
    i += 1 # i = i + 1
    print(str(i) + " == " + nama)
    # i += 1

