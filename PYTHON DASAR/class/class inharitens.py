class ojek():

     def __init__(self, nama, transmisi, daerah):
          self.nama = nama
          self.transmisi = transmisi
          self.daerah = daerah

     def cek_id_abang(self):
          print('nama :', self.nama,'\nmotor : ',self.transmisi,'\ndaerah : ',self.daerah)

class Gojek(ojek): #disebut inharitens atau turunan

     def cek_id_abang(self):
          print('cek aplikasi gojek')

ojek1 = ojek('mario','manual','bandung selaatan')
ojek2 = Gojek('jakson','automatic','tasikmalaya')

ojek1.cek_id_abang()
ojek2.cek_id_abang()