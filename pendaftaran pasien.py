# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:16:09 2020

@author: User
"""

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
