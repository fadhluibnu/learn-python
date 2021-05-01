list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}

print(type(list))
print(type(tuple))
print(type(set))

#dictionaru
member1 =  {'ID':101,
            'nama':"fadhlu ibnu",
            'status member':'gold',
            }



def nota ():
     member2 = {'id': input("masukkan id : "),
                'nama': input("masukkan nama : "),
                'status member': input("masukkan status : ")
                }
     print("Peminjam Buku :")
     print("ID : ",member2['id'])
     print("Nama : ", member2['nama'])
     print("Status Member : ", member2['status member'])

nota()











# print(member1['ID'])
# print(member1['nama'])
# print(member1['status member'])
# print(member1.keys())
# print(member1.values())
# print(member1.items())
