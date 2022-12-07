import csv
import os 

nama_csv = 'tugas akhir.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print("=== BIT COUNT ===")
    print("Selamat Datang Di aplikasi Kami \nYang memaksimalkan lahan anda\nuntuk pertanian")
    print("=================")
    print("")
    print("[1] Lihat Data ")
    print("[2] Buat Data Baru")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        Tampilan()
    elif(selected_menu == "2"):
        inputan()
    elif(selected_menu == "3"):
        Edit()
    elif(selected_menu == "4"):
        Hapus()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
def Tampilan():
    clear_screen()
    contacts = []
    with open(nama_csv, mode="r") as data_csv:
        csv_reader = csv.DictReader(data_csv)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t LUAS \t\t JENIS TANAMAN \t\t TANAMAN YANG DAPAT DITANAM")
    print("-"*100)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['LUAS']} \t\t {data['JENIS TANAMAN']} \t\t\t {data['TANAMAN YANG DAPAT DITANAM']}")
        
    back_to_menu()

        
def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali Ke Menu...")
    menu()
    
def inputan_salah():
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu...")
    inputan()
    
def inputan():
    clear_screen()
    contacts = []
    nomor = input("masukkan nomor urutan = ")
    with open(nama_csv, mode="r") as data_csv:
        csv_reader = csv.DictReader(data_csv)
        for row in csv_reader:
            contacts.append(row)
    for data in contacts:
        if nomor == data['NO']:
            print("maaf nomor urutan sudah ada silahkan input nomor yang berbeda")
            inputan_salah()
        else:
            pass
    nama = input("masukkan nama anda : ")
    luas = int(input("masukkan luas lahan anda (m^2): "))
    jenis_tanaman = input("masukkan jenis tanaman yang ingin ditanam : ")
    jarak_antar_tanaman = int(input("masukkan jarak lebar antar tanaman(cm) : "))
    jarak_antar_tanaman1 = int(input("masukkan jarak panjang antar tanaman(cm) : "))
    jarak_antar_tanaman = jarak_antar_tanaman / 100
    jarak_antar_tanaman1 = jarak_antar_tanaman1 / 100
    jarak_antar_tanaman = jarak_antar_tanaman*jarak_antar_tanaman1
    jumlah_maksimal = luas/jarak_antar_tanaman
    
    with open(nama_csv, mode='a') as data_csv:
        fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'TANAMAN YANG DAPAT DITANAM']
        writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
        nomor = nomor
        nama = nama 
        luas = luas
        jenis_tanaman = jenis_tanaman
        jumlah_maksimal = int(jumlah_maksimal)

        writer.writerow({'NO': nomor, 'NAMA': nama, 'LUAS': luas , 'JENIS TANAMAN' : jenis_tanaman , 'TANAMAN YANG DAPAT DITANAM' : jumlah_maksimal})    
    back_to_menu()
    
def Hapus():
    clear_screen()
    contacts = []

    with open(nama_csv, mode="r") as data_csv:
        csv_reader = csv.DictReader(data_csv)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t LUAS \t\t JENIS TANAMAN \t\t TANAMAN YANG DAPAT DITANAM")
    print("-"*100)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['LUAS']} \t\t\t {data['JENIS TANAMAN']} \t \t {data['TANAMAN YANG DAPAT DITANAM']}")

    print("-"*100)
    nomor = input("Hapus nomer> ")
    indeks = 0
    for data in contacts:
        if (data['NO'] == nomor):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1
    with open(nama_csv, mode="w") as data_csv:
        fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'TANAMAN YANG DAPAT DITANAM']
        writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'LUAS': new_data['LUAS'] , 'JENIS TANAMAN':new_data['JENIS TANAMAN'] , 'TANAMAN YANG DAPAT DITANAM':new_data['TANAMAN YANG DAPAT DITANAM']}) 

    print("Data sudah terhapus")
    back_to_menu()
    
def Edit():
    clear_screen()
    contacts = []

    with open(nama_csv, mode="r") as data_csv:
        csv_reader = csv.DictReader(data_csv)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t LUAS \t\t JENIS TANAMAN \t\t TANAMAN YANG DAPAT DITANAM")
    print("-"*100)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['LUAS']} \t\t\t {data['JENIS TANAMAN']} \t \t {data['TANAMAN YANG DAPAT DITANAM']}")

    print("-"*100)
    nomor = input("masukkan nomor urutan = ")   
    for data in contacts:
        if nomor == data['NO']:
            nama = input("masukkan nama anda : ")
            luas = int(input("masukkan luas lahan anda (m^2): "))
            jenis_tanaman = input("masukkan jenis tanaman yang ingin ditanam : ")
            jarak_antar_tanaman = int(input("masukkan jarak lebar antar tanaman(cm) : "))
            jarak_antar_tanaman1 = int(input("masukkan jarak panjang antar tanaman(cm) : "))
            jarak_antar_tanaman = jarak_antar_tanaman / 100
            jarak_antar_tanaman1 = jarak_antar_tanaman1 / 100
            jarak_antar_tanaman = jarak_antar_tanaman*jarak_antar_tanaman1
            jumlah_maksimal = luas/jarak_antar_tanaman 
            jumlah_maksimal = int(jumlah_maksimal)    
            indeks = 0
            for data in contacts:
                if (data['NO'] == nomor):
                    contacts[indeks]['NAMA'] = nama
                    contacts[indeks]['LUAS'] = luas 
                    contacts[indeks]['JENIS TANAMAN'] = jenis_tanaman
                    contacts[indeks]['TANAMAN YANG DAPAT DITANAM'] = jumlah_maksimal
                indeks = indeks + 1
            with open(nama_csv, mode="w") as data_csv:
                fieldnames = ['NO', 'NAMA', 'LUAS' , 'JENIS TANAMAN' , 'TANAMAN YANG DAPAT DITANAM']
                writer = csv.DictWriter(data_csv, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in contacts:
                    writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'LUAS': new_data['LUAS'] , 'JENIS TANAMAN':new_data['JENIS TANAMAN'] , 'TANAMAN YANG DAPAT DITANAM':new_data['TANAMAN YANG DAPAT DITANAM']}) 
            back_to_menu()
    print("maaf nomor anda tidak ada di database kita")
    back_to_menu()
    
menu()
