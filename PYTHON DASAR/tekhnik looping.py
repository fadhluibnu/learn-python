
nama_band = ['payung teduh',
             'fourtwnty',
             'dialog dini hari',
             'parahena']
kumpulan_lagu = ['akad',
        'zona nyaman',
        'rumahku',
        'sang filsuf',
        'sindoro']

for band in nama_band:
     print(band)
print(100*'=')

#enumerate
for i,band in enumerate(nama_band):
     print(i,":",band)
print(100*'=')

#zip
for band,lagu in zip(nama_band,kumpulan_lagu):
     print(band,'menyayikan lagu yang berjudul',lagu)
print(100*'=')

playlist = {'baybay', 'ada apa dengan cinta', 'cenat - cenut', 'jaran goyang'}
for lagu in sorted(playlist):
     print(lagu)
print(100*'=')

playlist2 = {'payung teduh':'akad',
             'fourtwnty':'zona nyaman',
             'dialog dini hari':'rumahku'}
for i in playlist2.keys():
     print(i)
print(100*'=')

for i in playlist2.items():
     print(i)
