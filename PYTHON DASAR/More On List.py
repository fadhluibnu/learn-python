barang  = ['kunci','ember',' jaket','ban','mobil']
print(barang)

#method untuk menambah data
barang.append('sepeda')
print(barang)

barang.extend('dompet')
print(barang)

barang.insert(3,'sepeda')
print(barang)

#method untuk menghitung anggota
jumlahSepeda = barang.count('sepeda')
print("jumalh sepeda adalah : ",jumlahSepeda)

#meremove data
barang.remove('sepeda') #jika ada yang sama maka akan me remove yang pertama ditemukan
print(barang)

barang.reverse()
print(barang)

print('='*100)
#staff = barang #jagan gunakan seperti ini
staff = barang.copy()
staff.append('gelas')
print(staff)
print(barang)


