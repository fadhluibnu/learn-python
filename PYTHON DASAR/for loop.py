#list sebagai interable
print('list sebagai interable')
gorengan = ['bakwan', 'cireng','tahu isi', 'tempe goreng', 'ubi goreng']
for i in gorengan:
     print(i) #maka akan menggakses komoponen dalam gorengan
     print(len(i)) #akan menghitung huruf setiap komponen
print(50*'=')
print('\n')

#string sebagai interable
print('string sebagai interable')
bakwan = 'bakwan'
for i in bakwan:
     print(i)
print(50*'=')
print('\n')

#for di dalam for
print('for di dalam for')

buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

daftarBelanja = [gorengan,buah, sayur]
for subDaftarBelanja in daftarBelanja:
     print(subDaftarBelanja)
     for komponen in subDaftarBelanja:
          print(komponen)




