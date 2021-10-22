# TUGAS BUAT BENTUK DIAMOND DENGAN MENGGUNAKAN 
# PERULANGGAN DAN FUNGSI
#       *
#      ***
#     *****
#    *******
#   *********
#    *******
#     *****
#      ***
#       *

#def diamond(n):
#    i = 0
#    while i < n:
#        print("*", end='')
#        i = i + 1

# CONTOH MEMBUAT SEGITIGA
# def triangle(n):
#    i = 0
#    while i < n:
#        j = 0
#        while j < i:
#            print("*", end='')
#            j = j + 1
#        print('')
#        i = i + 1

#triangle(10)

#diamond(5) 

#n=int (input('Enter n value:'))
for i in range(5):
    print(' '*(-i-1)+'* '*(i+1))
for i in range(5-1):
    print(' '*(i+1)+'* '*(5-i-1))