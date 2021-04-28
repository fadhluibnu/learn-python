nilai = 80
nilai1 = 75
nilai2 = 80

# if nilai == 75:
#      print("nilai anda = ", nilai)
# if nilai == 80:
#      print('nilai anda = ', nilai)

#nesting
# if nilai1 == 75:
#      print('nilai anda :', nilai1)
#      print('step 1')
#      if nilai2 == 80:
#           print('nilai anda : ', nilai2)
#           print('step 2')

#dengan bahasa
# if nilai is 80:
#      print('nilai anda : ', nilai)
# if nilai is not 60:
#      print('nilai anda : ', nilai1)

#elif
nilai = 73
if 80 <= nilai <= 100:
     print('nilai anda adalah A')
elif 70 <= nilai < 80:
     print('nilai anda adalah B')
elif 60 <= nilai < 70:
     print('nilai anda adalah C')
elif 50 <= nilai < 60:
     print('nilai anda adalah T, lakukan perbaikan')
else:
     print('maaf anfa tidak lulus mata pelajaran ini')
print(100*"=")
print('operator logika untuk list dan string')
print(' ')
gorengan = ['bakwan','cireng','bala - bala','tahu','combro','pisang goreng','pukis','risoles']
beli = 'laptop'

if beli in gorengan:
     print('mamang "ya saya jual ',beli,'"')
elif not beli in gorengan:
     print('mamang "saya tidak jual ',beli,'"')

karakter = 'z'
if karakter in beli:
     print('ada z di ', beli)
else:
     print('tidak ada karakter z di ', beli)





