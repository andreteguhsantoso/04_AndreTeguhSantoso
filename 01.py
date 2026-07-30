def soal1():
    while True:
        try:
            print("\n--- Cek Angka Genap / Ganjil ---")
            angka = int(input("Masukkan angka: "))

            if angka % 2 == 0:
                print(f"{angka} adalah angka genap.")
            else:
                print(f"{angka} adalah angka ganjil.")
                
            while True:
                out = input("\nApakah kamu mau lanjut ? [ lanjut / keluar ] : ")
                if out == "keluar":
                    break
                elif out == "lanjut":
                    break
                else :
                    print ("\nmasukkan perintah yang benar [ lanjut / keluar ]")
                                    
            if out == "keluar":
                break
                    

        except ValueError:
            print("Input!!! Harap masukkan angka.")
            
def soal2():
    while True:
        try:
            print("\n--- Cek Luas Persegi ---")
            print(" == masukkan angka [0] untuk keluar")
            panjang = int(input("Masukkan panjang persegi : "))
            lebar = int(input("Masukkan lebar persegi : "))
            luas = panjang * lebar
            print("Luas persegi anda adalah :", luas)
          
            while True:
                keluar = input("\nApakah kamu mau lanjut ? [ lanjut / keluar ] : ")
                if keluar == "keluar":
                    break
                elif keluar == "lanjut":
                    break
                else :
                    print ("\nmasukkan perintah yang benar [ lanjut / keluar ]")
                    
            if keluar == "keluar":
                break
                
        except ValueError:
            print("Input salah!!! Harap masukkan angka.")
            

while True:
    try:
        print("\n=== MENU UTAMA ===")
        print("1. Jalankan Soal 1")
        print("2. Jalankan soal 2")
        print("0. Keluar Aplikasi")
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            soal1()
        if pilihan == 2:
            soal2()
        elif pilihan == 0:
            print("Terima kasih, program selesai!")
            break
        else:
            print("Pilihan menu tidak tersedia. Silakan pilih 1 atau 0.")

    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")