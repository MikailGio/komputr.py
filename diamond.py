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


# vvvvvvvvvv Tugas Diamond vvvvvvvvvv
n=5
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))