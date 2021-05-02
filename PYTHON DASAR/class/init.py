#class
class mahasiswa():
     def __init__(self, input_nama, input_nilai):
          self.nama = input_nama
          self.nilai = input_nilai

     def belajar(self, kondisi):
          print(self.nama,'sedang belajar', kondisi)

     def tidur(self):
          print(self.nama,'tidur di kelas')

#main program
otong = mahasiswa('otong surotong', 80)
print(otong.nama)
print(otong.nilai)
otong.belajar('dengan giat')
