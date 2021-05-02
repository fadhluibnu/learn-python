class mahasiswa():

     jumlah_mahasiswa = 0

     def __init__(self, input_nama, input_nim):
          self.nama = input_nama #public
          self.nim = input_nim #public
          mahasiswa.jumlah_mahasiswa += 1

#main program
otong = mahasiswa('otong surotong', 70128401)
ucup = mahasiswa('michel ucup', 8102108)
cassandra = mahasiswa('casandra aja', 8940921)

print(mahasiswa.jumlah_mahasiswa)