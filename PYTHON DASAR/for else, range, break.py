#range
for i in range(0,10): #dibaca 0 sampai 10
     print(i)
print(50*'=')
print('\n')

#range dengan kelipatan
for i in range(0,10,2): #dibaca 0 sampai 10 kelipatan 2
     print(i)
print(50*'=')
print('\n')

#break
# number = 25
# for i in range(0,40):
#      print(i)
#
#      if i is 25:
#           print('angka di temukan', i)
#           print(50 * '=')
#           print('\n')
#           break #keluar dari looping

#for else
number = 25
for i in range(0, 40):
     print(i)
     if i is number:
          print('angka di temukan', i)
          break #keluar dari looping
else:
     print('angka tidak di temukan')

