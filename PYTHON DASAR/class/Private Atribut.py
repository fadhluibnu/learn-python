#Private Attribut adalah untuk memprivasi agar tidak bisa di ubah
#class
class mahasiswa():

     jurusan = 'RPL'
     __nilai = 0 #private
     #jika ada __main maka itu adalah private

     def __init__(self, input_nama, input_nim):
          self.nama = input_nama #public
          self.nim = input_nim #public

     def uts(self, input_nilai):
          self.__nilai += input_nilai

     def uas(self, input_nilai):
          self.__nilai += input_nilai

     def check_status(self):
          if self.__nilai <= 50:
               print(self.nama,' tidak lulus')
          else:
               print(self.nama, 'lulus')

#main program
otong = mahasiswa('otong surotong', 70128401)
ucup = mahasiswa('michel ucup', 8102108)

otong.uts(10)
otong.uas(50)
otong.check_status()

ucup.uts(9)
ucup.uas(25)
ucup.check_status()
