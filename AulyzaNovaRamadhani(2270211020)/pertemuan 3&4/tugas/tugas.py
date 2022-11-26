from datetime import datetime
# #print ("date :", datetime.now().strftime("%Y-%m-%d %H:%M"))
# introduction
print("""--------------------------------------
        Marchandise Kpop
--------------------------------------""")


import time;
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)



nama    = input("Nama Pelanggan: ")
alamat  = input("Alamat: ")
notelp  = input("Nomor Telepon: ")

#product Object
class Product:
    def __init__(self,name,price,discountMinimum):
        self.name = name
        self.price = price
        self.discountMinimum = discountMinimum
    def printTotal(self,amount):
        self.harga = self.price * jumlahpesan
        self.ppn = self.harga * 1.0
        self.amount= amount
        if amount >= self.discountMinimum:
            self.discount = int(self.harga*0.2)
            self.totalHarga = int(self.harga-self.discount+self.ppn)
        print("""
        --------------------------
        Marchandise Kpop
        --------------------------
        Barang: {}
        Jumlah Pesan: {}
        Harga: {}
        Diskon: {}
        PPN: {}
        --------------------------
        Jumlah Bayar : {}
        --------------------------""".format(self.name,amount,self.harga,self.discount,self.ppn,self.totalHarga))


#products data
products = [
    Product("album", 300000, 5),
    Product("lighstick", 800000, 3),
    Product("photocard", 200000, 3),
    Product("kaos", 350000, 2)
]

# Printing the list
output = ""
c= 1
for product in products:
    output+=("{}) {: <10} {:>10}\n".format(str(c),product.name,"RP "+str(product.price)))
    c+=1

print("""
=====================================
|| Daftar produk
=====================================
{}=====================================
""".format(output))

# printing the check
pesan = int(input("memilih produk: "))
jumlahpesan = int(input("ketik jumlahnya: "))
product = products[pesan-1].printTotal(jumlahpesan)

print('=====================================')
text = ("TERIMAKASIH")
print(text.center(30))
print("=====================================")