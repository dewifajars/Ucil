#standart harga obat= RP10000, standar biaya jasa= RP30000
#standar harga tindakan khusus
   #a. pemberian suntikan = RP20000
   #b. medikasi=RP15000
   #c. penjahitan luka=RP25000
   #d. medikasi kesehatan gigi dan mulut = RP30000
def biaya1(): #obat+jasa
    x1= 10000+30000
    print("Total Biaya: Rp",x1)
    return x1
def biaya2(): #obat+jasa+tindakan khusus a
    x2= 10000+30000+20000
    print("Total Biaya: Rp", x2)
    return x2
def biaya3(): #obat+jasa+tindakan khusus b
    x3= 10000+30000+15000
    print("Total Biaya: Rp", x3)
    return x3
def biaya4(): #obat+jasa+tindakan khusus c
    x4= 10000+30000+25000
    print("Total Biaya: Rp", x4)
    return x4
def biaya5(): #obat+jasa+tindakan khusus a dan b
    x5= 10000+30000+20000+15000
    print("Total Biaya: Rp", x5)
    return x5
def biaya6(): #obat+jasa+tindakan khusus a dan c
    x6= 10000+30000+20000+25000
    print("Total Biaya: Rp", x6)
    return x6
def biaya7(): #obat+jasa+tindakan khusus b dan c
    x7= 10000+30000+15000+25000
    print("Total Biaya: Rp", x7)
    return x7
def biaya8(): #obat+jasa+tindakan khusus a, b, dan c
    x8= 10000+30000+20000+15000+25000

print ("PENDAFTARAN PASIEN")
print(" ")

print ("SILAKAN PILIH GOLONGAN PASIEN")

jenis_golongan = ["(Merah : Pasien Umum)", "(Hijau : Pasien BPJS)"]

for x in range (2):
    print (x+1, jenis_golongan [x])

import sys
try:
    Z = int(input("Golongan 1 atau 2?: "))
    kartu= input("Apakah pasien pernah berobat di sini? (y/t):")    
    if kartu == "t":
        print("Mohon maaf\nPasien dipersilakan menuju bagian administrasi  untuk mendapatkan nomor rekam medis")  
        print ("Masukkan nomor rekam medis pasien!", end=' ')
        no = input ()
        print ()
    else:
        kartu= input("Apakah pasien membawa kartu berobat? (y/t):")
        if kartu == "t" :
            print ("Silakan mencari di data pasien")
            print ("Masukkan nomor kartu berobat pasien!", end=' ')
            no = input ()
            print ()
        else :
            print ("Masukkan nomor kartu berobat pasien!", end=' ')
            no = input ()
            print ()
    if Z == 1:
        print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
            
        import time
        time.sleep (5)
        print ()
        print (f"Pasien dengan, \n Golongan         : Merah (Pasien Umum) \nNo. Kartu Berobat : {no} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan untuk mendapatkan penanganan\nTerimakasih")
    else:
        print("Masukkan nomor BPJS pasien:", end=' ')
        bpjs= input()
        print()
    
        print ("Mohon Tunggu Sebentar, data anda sedang kami proses...")
        import time
        time.sleep (5)
        print ()
        print (f"Pasien dengan, \n Golongan         : Hijau (Pasien BPJS) \nNo. Kartu Berobat : {no} \nNo. Kartu BPJS    : {bpjs} \n====TELAH TERDAFTAR====\nSilakan ambil rekam medis pasien \nPasien dimohon menuju ruang pelayanan untuk mendapatkan penanganan\nTerimakasih")
    print("")
    print("-------------------------------------")
    print("")
    print("Program telah selesai dijalankan.")
    
#cmd
#test
