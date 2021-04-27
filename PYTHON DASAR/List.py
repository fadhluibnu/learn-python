data = [1,4,9,16,25,36,49,64]

#mengakses list
subdata1 = data[0] #akan mengasilkan 1 mulai dari 0
subdata2 = data[-1] #akan mengasilkan 64 mulai dari -1

#memotong list
subdata3 = data[0:4] #akan menghasikan 0 sampai sebelum 4 angka = [1, 4, 9, 16]
subdata4 = data[-4:] #akan menghasilkan [25, 36, 49, 64] dihitung dari 4 angka dari belakang
subdata5 = data[:-4] #akan mengasilkan [1, 4, 9, 16] dihitung 4 angka dari depan
subdata6 = data[3:] #akan mengasilakn [16, 25, 36, 49, 64] dihitung dari 0 - 3 angka dan itu tidak di tampilkan

data2 = [100,200,300,400,500,600,700,800]

#menambah list
data3 = data + data2 #akan mengasilkan [1, 4, 9, 16, 25, 36, 49, 64, 100, 200, 300, 400, 500, 600, 700, 800]

#merubah content dari list
#print(data)
#data[4] = 87 #di indeks k4 4 (mulai dari 0) akan berubah dari [1, 4, 9, 16, 25, 36, 49, 64] ke [1, 4, 9, 16, 87, 36, 49, 64]

#menco[y list ke variabel
#a = data #jangan gunakan begini karena ini bukan mencopy tapi merubah dari akarnya
a = data[:] #jadi gunakanlah seperti ini
a[4] = 87

#merubah content list dengan metode slicing
data[3:5]= [11, 12] #akan merubah bilanganya menjadi [1, 4, 9, 11, 12, 36, 49, 64] dihitung mulai dari index ke 3 (tidak ikut di tampilakn ) dampai 5 (ikut di tampilakan)

#list dalam list
x = [data,data2] #akan menghasilkan [[1, 4, 9, 11, 12, 36, 49, 64], [100, 200, 300, 400, 500, 600, 700, 800]]

#megakses list di variabel x
y = x[1][4] #kurung pertama akan merubah "data" yang kedua akan mengubah "data2"

#method untuk list
data.append(30) #akan menambahkan 30 dan mengasikan [1, 4, 9, 11, 12, 36, 49, 64, 30]

#function yang bisa digunakan di list
panjang_list = len(data) #akan mengasilkan panjang data

print(data)
