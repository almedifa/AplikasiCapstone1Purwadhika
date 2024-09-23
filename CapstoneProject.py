
PASIEN_DATA_LOGIN = {"Rizal": "123", "Davis": "123",  "Ali": "123"}
DOKTER_DATA_LOGIN = {"paimo": "123", "paire": "123", "aya": "123"}
ADMIN_DATA_LOGIN = {"paimo": "123", "paire": "123", "aya": "123"}
REKAM_MEDIS = [{
        "nama_lengkap": "Ali",
        "jenis_kelamin": "L",
        "usia": 54,
        "identitas": 1123,
        "penyakit": [
            "Radang Tenggorokan"
        ],
        "nama_obat": [
            "Panadol 1 mg",
            "Ultraflu 3 mg"
        ]
    },
    {
        "nama_lengkap": "Amar",
        "jenis_kelamin": "L",
        "usia": 27,
        "identitas": 15,
        "penyakit": [
            "Radang Tenggorokan"
        ],
        "nama_obat": [
            "Panadol 1 mg",
            "Ultraflu 3 mg"
        ]
    },
    {
        "nama_lengkap": "Davis ",
        "jenis_kelamin": "L",
        "usia": 24,
        "identitas": 1122
    }]
KUOTA_IGD = [{
        "nama_lengkap": "Ali bin Abi",
        "identitas": 1123
    }]
ANTRIAN_OBAT = []
kuota_igd = 2
ANTRIAN_DOKTER = {
    "Dokter Umum": [],
    "Dokter Jantung": [],
    "Penyakit Dalam": []
}

# Fungsi untuk meregister pengguna baru
def registerPasien(username, password):
    if username in PASIEN_DATA_LOGIN:
        print("Congratulation.. Your Username is already registered..")
    else:
        PASIEN_DATA_LOGIN[username] = password
        print(f"Account User {username}, Successful to registered... ")

# Fungsi untuk login pasien
def loginPasien(username, password):
    if username in PASIEN_DATA_LOGIN and PASIEN_DATA_LOGIN[username] == password:
        print(f"====Login is Successful! Welcome, {username}!====")
        MenuPasien(username)
    else:
        print("====Username or password is Wrong!!====")

# Fungsi untuk login dokter
def loginDokter(username, password):
    if username in DOKTER_DATA_LOGIN and DOKTER_DATA_LOGIN[username] == password:
        print(f"====Login is Successful! Welcome, {username}!====")
        MenuDokter(username)
    else:
        print("====Username or password is Wrong!!====")

# Fungsi untuk login Admin
def loginAdmin(username, password):
    if username in ADMIN_DATA_LOGIN and ADMIN_DATA_LOGIN[username] == password:
        print(f"====Login is Successful! Welcome, {username}!====")
        MenuAdmin (username)
    else:
        print("====Username or password is Wrong!!====")

# Fungsi untuk menyimpan data pasien IGD
def SimpanDataPasienIGD(pasienIGD):
    # Cek apakah identitas sudah ada
    for p in REKAM_MEDIS:
        if p['identitas'] == pasienIGD['identitas']:
            print("Identity already exists... Data is not saved!!")
            return
    # Tambahkan data pasien ke dalam list
    REKAM_MEDIS.append(pasienIGD)
    print("====Data saved successfully!====")

def SimpanKuotaIGD(kuotaIGD):

    # Tambahkan data pasien ke dalam list
    KUOTA_IGD.append(kuotaIGD)
    print("====Data saved successfully!====")

def tambah_pasien_igd(kuota_pasien_igd):
    global KUOTA_IGD
    if len(KUOTA_IGD) >= kuota_igd:
        print("IGD is full... Cannot add any more patients!!")
        return
    
    # Cek apakah pasien sudah ada di IGD
    for pasien in KUOTA_IGD:
        if pasien['identitas'] == kuota_pasien_igd['identitas']:
            print("====The patient is registered at IGD====")
            return

    KUOTA_IGD.append(kuota_pasien_igd)
    print("====Data Patient successfully added to ke IGD====")

def TambahAntrianObat(Tambah_Antrian_Obat):
    # Cek apakah pasien sudah ada di IGD
    for pasien in ANTRIAN_OBAT:
        if pasien['identitas'] == Tambah_Antrian_Obat['identitas']:
            print("====The patient is registered at IGD====")
            return

        KUOTA_IGD.append(Tambah_Antrian_Obat)
    print("====Data Patient successfully added to Antrian====")


# Fungsi untuk melihat daftar antrian
def lihat_antrian():
    if len(KUOTA_IGD) == 0:
        print("There are no patients in IGD.....")
        return

    print(f'| {"No.":<4} | {"Nama Pasien":<15} | {"No. Identitas":<15} |')
    for i, pasien in enumerate(KUOTA_IGD, 1):
        nama_lengkap = pasien.get('nama_lengkap', 'Tidak ada data')
        identitas = pasien.get('identitas', 'Tidak ada data')
        print(f"| {i:<4} | {nama_lengkap:<15} | {identitas:<15} |")
      

# Fungsi untuk menambah penyakit dan obat ke data pasien
def tambah_penyakit_dan_obat():
    identitas = int(input("Enter the patient identity you want to change: "))

    # Cari pasien berdasarkan identitas
    for pasien in REKAM_MEDIS:
        if pasien['identitas'] == identitas:
            penyakit = input("Enter the patient's disease: ")
            nama_obat = input("Enter the names of the medications given (separate them with commas if more than one): ")
            list_obat = [obat.strip() for obat in nama_obat.split(",")]

            # Pastikan 'penyakit' adalah list
            if isinstance(pasien.get('penyakit'), str):
                pasien['penyakit'] = [pasien['penyakit']]  # Ubah string menjadi list
            elif 'penyakit' not in pasien:
                pasien['penyakit'] = []

            # Pastikan 'nama_obat' adalah list
            if isinstance(pasien.get('nama_obat'), str):
                pasien['nama_obat'] = [pasien['nama_obat']]  # Ubah string menjadi list
            elif 'nama_obat' not in pasien:
                pasien['nama_obat'] = []

            # Tambahkan data penyakit dan obat
            pasien['penyakit'].append(penyakit)
            pasien['nama_obat'].extend(list_obat)
            print("====Disease and medicine successfully added====")
            return

    print("Identity not found in the data....")

# Fungsi untuk mencari data berdasarkan identitas
def cari_data(identitas):
    for pasien in REKAM_MEDIS:
        if pasien['identitas'] == identitas:
            return format_data(pasien)
    return "Data not found...."

# Fungsi untuk format data pasien
def format_data(pasien):
    return ( f'\n\n| {"Nama Pasien":<15} | {"Jenis Kelamin":<15} | {"Usia":<7} | {"No. Identitas":<15} | {"Penyakit":<30} | {"Nama Obat":<30} |\n'
             f'| {pasien["nama_lengkap"]:<15} | {pasien["jenis_kelamin"]:<15} | {pasien["usia"]:<7} | {pasien["identitas"]:<15} '
             f'| {", ".join(pasien.get("penyakit", ["Tidak ada data"])):<30} | {", ".join(pasien.get("nama_obat", ["Tidak ada data"])):<30} |\n'
                '---')

# Fungsi untuk menyimpan antrian dokter
def SimpanAntrianDokter(antriandokter, dokter_periksa):
# Tambahkan antrian baru ke dalam list sesuai dengan dokter_periksa
    ANTRIAN_DOKTER[dokter_periksa].append(antriandokter)
    print(f"====Data saved successfully for {dokter_periksa}!====")

# Fungsi untuk melihat rincian antrian pasien tertentu
def LihatAntrianPasien():
    identitas = int(input("Enter your ID to see queue details: "))
    
    # Cari pasien di seluruh daftar antrian berdasarkan nama
    ditemukan = False
    for dokter, antrian in ANTRIAN_DOKTER.items():
        for index, pasien in enumerate(antrian):
            if pasien['identitas'] == identitas:
                # solving queue of patient
                posisi = index+1
                antrian_tersisa = len(antrian) - posisi
                print(f"\n===={pasien['nama_lengkap']}, You are registered in the queue for {dokter}====")
                if posisi == 0:
                    print(f"Now it's your turn to be examined...")
                #  not implemented
                elif posisi != 0:
                    print(f"There still is {posisi} patient before your turn!!")
                ditemukan = True
                break

    if not ditemukan:
        print(f"\nThe patient was not found in the queue.....")

def  LihatAntrianObatku(): 
    identitas = int(input("Enter your ID to see queue details: "))
    
    ditemukan = False  # Flag untuk menentukan apakah pasien ditemukan
    
    # Cari pasien di seluruh daftar antrian berdasarkan identitas
    for i, pasien in enumerate(ANTRIAN_OBAT):
        if pasien['identitas'] == identitas:
            posisi = i + 1
            ditemukan = True
            print(f"\n===={pasien['nama_lengkap']}, You are registered in the queue for Medicine====")
            if posisi == 1:
                print(f"Now it's your turn to be examined..")
            else:
                print(f"There still is {posisi - 1} patient before your turn!!")
            break
    
    if not ditemukan:
        print("Sorry, queue data not found....")

def LihatKuotaIGD():
    if len(KUOTA_IGD) == 0:
        print("====There are no patients in IGD====")
        return

    print("\nList of Patients in IGD:")
    print(f'| {"No.":<4} | {"Nama Pasien":<15} | {"No. Identitas":<15} |')
    for i, pasien in enumerate(KUOTA_IGD, 1):
        nama_lengkap = pasien.get('nama_lengkap', 'Tidak ada data')
        identitas = pasien.get('identitas', 'Tidak ada data')
        print(f"| {i:<4} | {nama_lengkap:<15} | {identitas:<15} |")

# Fungsi untuk menghapus pasien dari IGD
def UpdatePasienIGD():
    if len(KUOTA_IGD) == 0:
        print("====There are no patients in IGD====")
        return
    elif len(KUOTA_IGD) != 0:
        LihatKuotaIGD()
        nomor_pasien = int(input("\nEnter the patient number you want to delete: "))

            # Validasi input
        if 1 <= nomor_pasien <= len(KUOTA_IGD):
            pasien_dihapus = KUOTA_IGD.pop(nomor_pasien - 1)
            print(f"====Pasien {pasien_dihapus['nama_lengkap']} successfully removed from IGD====")


def UpdateDataRekamMedis():
    if len(REKAM_MEDIS) == 0:
        print("No patient data....")
        return

    LihatDataRekamMedis()
    identitas = int(input("\nEnter the patient ID number you want to update: "))

    # Cari pasien berdasarkan identitas
    for pasien in REKAM_MEDIS:
        if pasien['identitas'] == identitas:
            # Meminta input data baru
            pasien['nama_lengkap'] = str(input("Enter the patient's new full name:  "))
            pasien['jenis_kelamin'] = str(input("Enter the patient's new Gender: "))
            pasien['usia'] = int(input("Enter the patient's new age: "))
            pasien['penyakit'] = input("Enter a list of new diseases (separate them with commas): ").split(',')
            pasien['nama_obat'] = input("Enter a list of new medicines names (separate them with commas): ").split(',')
            print("\n====Patient data updated successfully====\n")
            return

    print("The patient with this identity was not found.....")  

def LihatDataRekamMedis():
    if len(REKAM_MEDIS) == 0:
        print("No patient data in Rekam Medis....")
        return

    print("\nData Rekam Medis Patient:")
    print(f'| {"No.":<4} | {"Name Patient":<15} | {"Gender":<15} | {"Age":<7} | {"No. Identity":<15} | {"Diseases":<30} | {"Medicine Name":<30} |')
    for i, pasien in enumerate(REKAM_MEDIS, 1):
        nama_lengkap = pasien.get('nama_lengkap', 'Tidak ada data')
        jenis_kelamin = pasien.get('jenis_kelamin', 'Tidak ada data')
        usia = pasien.get('usia', 'Tidak ada data')
        identitas = pasien.get('identitas', 'Tidak ada data')
        penyakit = ', '.join(pasien.get('penyakit', ['Tidak ada data']))
        nama_obat = ', '.join(pasien.get('nama_obat', ['Tidak ada data']))

        print(f"| {i:<4} | {nama_lengkap:<15} | {jenis_kelamin:<15} | {usia:<7} | {identitas:<15} | {penyakit:<30} | {nama_obat:<30} |")

# Fungsi Sorting data rekam medis
def LihatDataSorting():
    if len(REKAM_MEDIS) == 0:
        print("No patient data in Rekam Medis....")
        return

    # Mengurutkan data berdasarkan usia pasien
    sorted_rekam_medis = sorted(REKAM_MEDIS, key=lambda pasien: pasien.get('usia', 0))

    print("\n\nData Rekam Medis Patient (sorted by age):")
    print(f'| {"No.":<4} | {"Name Patient":<15} | {"Gender":<15} | {"Age":<7} | {"No. Identity":<15} | {"Diseases":<30} | {"Medicine Name":<30} |')
    
    for i, pasien in enumerate(sorted_rekam_medis, 1):
        nama_lengkap = pasien.get('nama_lengkap', 'Tidak ada data')
        jenis_kelamin = pasien.get('jenis_kelamin', 'Tidak ada data')
        usia = pasien.get('usia', 'Tidak ada data')
        identitas = pasien.get('identitas', 'Tidak ada data')
        penyakit = ', '.join(pasien.get('penyakit', ['Tidak ada data']))
        nama_obat = ', '.join(pasien.get('nama_obat', ['Tidak ada data']))

        print(f"| {i:<4} | {nama_lengkap:<15} | {jenis_kelamin:<15} | {usia:<7} | {identitas:<15} | {penyakit:<30} | {nama_obat:<30} |")

def LihatAntrianDokter():
    for dokter, antrian in ANTRIAN_DOKTER.items():
        print(f"\nQueue for {dokter}:")
        print(f'| {"No.":<4} | {"Name Patient":<15} |')
        if antrian:
            for i, pasien in enumerate(antrian, 1):
                print(f"| {i:<4} | {pasien['nama_lengkap']:<15} |\n")
        else:
            print("....there is no queue....")

def  HapusAntrianDokter():
    dokter_periksa = int(input(f"\nEnter the number of the examining doctor whose queue you want to delete"
                               f"\n1. Dokter Umum"
                               f"\n2. Dokter Jantung"
                               f"\n3. Penyakit Dalam"
                               f"\nPlease enter: "))

    # Mapping pilihan dokter ke nama dokter
    daftar_dokter = {
        1: "Dokter Umum",
        2: "Dokter Jantung",
        3: "Penyakit Dalam"
    }

    if dokter_periksa in daftar_dokter:
        dokter = daftar_dokter[dokter_periksa]
        if ANTRIAN_DOKTER[dokter]:
            LihatAntrianDokter()

            nomor_antrian = int(input("Enter the queue number you want to delete: "))

            # Validasi nomor antrian
            if 1 <= nomor_antrian <= len(ANTRIAN_DOKTER[dokter]):
                pasien_dihapus = ANTRIAN_DOKTER[dokter].pop(nomor_antrian - 1)
                print(f"Antrian {nomor_antrian} ({pasien_dihapus['nama_lengkap']}) deleted successfully.")
            else:
                print("Invalid queue number....")
        else:
            print(f"There are no queues for {dokter}....")
    else:
        print("Invalid doctor number. Please try again!!!")

def LihatAntrianObat():
    if len(ANTRIAN_OBAT) == 0:
        print("There are no patients in the Medicine Queue....")
        return

    print("\nList patient in Farmasi:")
    print(f'| {"No.":<4} | {"Name Patient":<15} | {"No. Identity":<15} |')
    for i, pasien in enumerate(ANTRIAN_OBAT, 1):
        print(f"| {i:<4} | {pasien['nama_lengkap']:<15} | {pasien['identitas']:<15} |")



# Menu utama
def main():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Pasien \n2. Admin \n3. Dokter \n4. Keluar")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            pasien()
        elif pilihan == '2':
            Admin()
        elif pilihan == '3':
            Dokter()
        elif pilihan == '4':
            print("\n-----Program complete-----")
            break
        else:
            print("\nInvalid choice....")


# Menu Login Dokter
def Admin():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Login \n2. Exit")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            loginAdmin(username, password)
        elif pilihan == '2':
            print("\n-----Program complete-----")
            break
        else:
            print("\nInvalid choice....")

def MenuAdmin(username):
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print(f"\nWelcome {username} in Panti Rini!")
        print("1. Data Pasien Berobat")
        print("2. Data Pasien IGD")
        print("3. Data Rekam Medis")
        print("4. Logout")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            DataAdminBerobat()
        elif pilihan == '2':
            DataAdminIGD()
        elif pilihan == '3':
            DataAdminRekamMedis()
        elif pilihan == '4':
            print("\nThanks.. See you...")
            break
        else:
            print("Invalid choice....")

#  Menu admin untuk pasien IGD
def DataAdminBerobat():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Antrian Dokter \n2. Obat \n3. Exit")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            AntrianDokterPeriksa()
        elif pilihan == '2':
            Obat()
        elif pilihan == '3':
            print("\n-----Program complete-----")
            break
        else:
            print("\nInvalid choice....")

def Obat():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("\n1. add Antrian Obat")
        print("2. Delete Antrian Obat")
        print("3. Exit")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            TambahAntrianObat()
        elif pilihan == '2':
            HapusAntrianObat()
        elif pilihan == '3':
            print("\n-----Program complete-----")
            break
        else:
            print("\nInvalid choice....")

def TambahAntrianObat():
    nama_lengkap = str(input("Enter the patient's full name: "))
    identitas = int(input("Enter the patient's identity card (KTP) number: "))

    # Cek apakah pasien sudah ada di IGD
    for pasien in ANTRIAN_OBAT:
        if pasien['identitas'] == identitas:
            print("------The patient has been registered in the Medicine Queue-----")
            return

    # Tambahkan pasien ke database IGD
    pasien_igd = {
        'nama_lengkap': nama_lengkap,
        'identitas': identitas
    }

    ANTRIAN_OBAT.append(pasien_igd)
    print("-----The patient was successfully added to the Medication Queue-----")

def HapusAntrianObat():
    if len(ANTRIAN_OBAT) == 0:
        print("-----There are no patients in the Medicine Queue-----")
        return

    LihatAntrianObat()
    nomor_pasien = int(input("\nEnter the patient number you want to delete: "))

    # Validasi input
    if 1 <= nomor_pasien <= len(ANTRIAN_OBAT):
        pasien_dihapus = ANTRIAN_OBAT.pop(nomor_pasien - 1)
        print(f"Patient {pasien_dihapus['nama_lengkap']} successfully removed from IGD....")
    else:
        print("Invalid patient number.....")

def AntrianDokterPeriksa():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Lihat Antrian Dokter \n2. Hapus Antrian Dokter \n3. Exit")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            LihatAntrianDokter()
        elif pilihan == '2':
            HapusAntrianDokter()
        elif pilihan == '3':
            print("-----Program completed-----")
            break
        else:
            print("Invalid choice.....")

#  Menu admin untuk pasien IGD
def DataAdminIGD():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Lihat Pasien IGD \n2. Hapus Pasien IGD \n3. Keluar")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            LihatKuotaIGD()
        elif pilihan == '2':
            UpdatePasienIGD()
        elif pilihan == '3':
            print("-----Program completed-----")
            break
        else:
            print("Invalid choice.....")

def DataAdminRekamMedis():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("\n1. Show Data Rekam Medis Patient \n2. Update Data Rekam Medis \n3. Exit")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            LihatDataRekamMedis()
        elif pilihan == '2':
            UpdateDataRekamMedis()
        elif pilihan == '3':
            print("-----Program completed-----")
            break
        else:
            print("Invalid choice.....")


# Menu Login Dokter
def Dokter():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Login \n2. Exit")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            loginDokter(username, password)
        elif pilihan == '2':
            print("-----Program completed-----")
            break
        else:
            print("Invalid choice.....")

# Menu Dokter
def MenuDokter(username):
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print(f"\nWelcome {username} in Panti Rini")
        print("1. Input Penyakit dan Obat")
        print("2. Search Data Rekam Medis")
        print("3. Logout")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            tambah_penyakit_dan_obat()
        elif pilihan == '2':
            LihatDataRekamMedis()
            identitas = int(input("Enter the patient's identity card (KTP) number: "))
            hasil_cari = cari_data(identitas)
            print(hasil_cari)

            print("\n\n"+10*'='+" Sorting Data Patient "+10*'=')
            sort = input("Do you want to sorting this data base on age (Y/T) :")
            if sort == 'Y':
                LihatDataSorting()

        elif pilihan == '3':
            print("Thanks! See you.....")
            break
        else:
            print("Invalid choice.....")

# Menu login register Pasien
def pasien():
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print("1. Register \n2. Login \n3. Exit")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            registerPasien(username, password)
        elif pilihan == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            loginPasien(username, password)
        elif pilihan == '3':
            print("Program completed....")
            break
        else:
            print("Invalid choice.....")

# Menu Pasien
def MenuPasien(username):
    while True:
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print(f"Welcome {username} in Panti Rini")
        print("1. IGD")
        print("2. Berobat")
        print("3. Rekam Medis")
        print("4. Show Antrian Periksa")
        print("5. Show Antrian Obat")
        print("6. Logout")
        pilihan = input("Select an option: ")

        if pilihan == '1':
            IGD(username)
        elif pilihan == '2':
            Berobat(username)
        elif pilihan == '3':
            identitas = int(input("Enter your identity card (KTP) number: "))
            hasil_cari = cari_data(identitas)
            print(hasil_cari)
        elif pilihan == '4':
            LihatAntrianPasien()
        elif pilihan == '5':
            LihatAntrianObatku()
        elif pilihan == '6':
            print("Thanks! see you.....")
            break
        else:
            print("Invalid Choice.....")

# Menu IGD
def IGD(username):
    user_response = input("Have you already filled in your personal data (Y/T): ")

    if user_response == 'Y':
        print("---We will use your medical records as a data reference. Please input your name and identity according to the medical record---\n")
        nama_lengkap = str(input(f"Enter your full name: "))
        identitas = int(input("Enter your identity card (KTP) number: "))
        for pasien in REKAM_MEDIS:
            if pasien['identitas'] == identitas:
                kuota_IGD_Terdaftar = {
                    'nama_lengkap': nama_lengkap,
                    'identitas': identitas
                }

                data_diri = input("\n\nAre you sure you want to go to IGD (Y/T): ")
                if data_diri == 'Y':
                    tambah_pasien_igd(kuota_IGD_Terdaftar) 

      

    elif user_response == 'T':
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        print(f"\nHalo {username}, Please fill in your personal data completely")
        nama_lengkap = str(input(f"your full name:"))
        jenis_kelamin = str(input(f"your gender (L/P) : "))
        usia = int(input("Enter your age: "))
        identitas = int(input("Enter your identity card (KTP) number: "))

        pasienIGD = {
            'nama_lengkap': nama_lengkap,
            'jenis_kelamin': jenis_kelamin,
            'usia': usia,
            'identitas': identitas
        }

        SimpanDataPasienIGD(pasienIGD)

        kuota_pasien_igd = {
            'nama_lengkap': nama_lengkap,
            'identitas': identitas
        }

        data_diri = input("\n\nAre you sure you want to go to IGD (Y/T): ")
        if data_diri == 'Y':
            tambah_pasien_igd(kuota_pasien_igd)

    else:
        print("Please input correctly... Thank you...")

# Menu Berobat
def Berobat(username):
    print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
    print(f"\nHalo {username},Please fill in your personal data completely")

    user_response = input("Have you already filled in your personal data (Y/T): ")  

    if user_response == 'T':
        # Implementasi tambahan untuk menu berobat
        print('\n\n'+6*'='+" Welcome to the Panti Rini Hospital Information System "+6*'=')
        nama_Lengkap = str(input(f"your full name: "))
        jenis_Kelamin = str(input(f"your gender (L/P): "))
        usia = int(input(f"Enter your age:"))
        identitas = int(input(f"Enter your identity card (KTP) number: "))

        pasienBerobat = {
            'nama_lengkap': nama_Lengkap,
            'jenis_kelamin': jenis_Kelamin,
            'usia': usia,
            'identitas': identitas
        }

        # Memilih dokter yang ingin diperiksa
        dokter_periksa = int(input(f"\nEnter the number of the doctor you want to examine"
                               f"\n1. Dokter Umum"
                               f"\n2. Dokter Jantung"
                               f"\n3. Penyakit Dalam"
                               f"\nPlease enter: "))

        # Mapping pilihan dokter ke nama dokter
        daftar_dokter = {
            1: "Dokter Umum",
            2: "Dokter Jantung",
            3: "Penyakit Dalam"
        }

        # Pastikan input valid
        if dokter_periksa in daftar_dokter:
            # Buat dictionary antrian
            antriandokter = {
                'nama_lengkap': nama_Lengkap,
                'identitas': identitas
            }

            # Simpan data antrian
            SimpanAntrianDokter(antriandokter, daftar_dokter[dokter_periksa])
        else:
            print("Invalid doctor number... Please try again...")

        SimpanDataPasienIGD(pasienBerobat)


    elif user_response == 'Y':
        nama_Lengkap = str(input(f"\nEnter your full name: "))
        identitas = int(input(f"Enter your identity card (KTP) number: ")) # Memilih dokter yang ingin diperiksa
        for pasien in REKAM_MEDIS:
            if pasien['identitas'] == identitas:
                dokter_periksa = int(input(f"\nEnter the number of the doctor you want to examine"
                               f"\n1. Dokter Umum"
                               f"\n2. Dokter Jantung"
                               f"\n3. Penyakit Dalam"
                               f"\nPlease enter: "))

                # Mapping pilihan dokter ke nama dokter
                daftar_dokter = {
                        1: "Dokter Umum",
                        2: "Dokter Jantung",
                        3: "Penyakit Dalam"
                }

                # Pastikan input valid
                if dokter_periksa in daftar_dokter:
                    # Buat dictionary antrian
                    antriandokter = {
                        'nama_lengkap': nama_Lengkap,
                        'identitas': identitas
                    }

                    # Simpan data antrian
                    SimpanAntrianDokter(antriandokter, daftar_dokter[dokter_periksa])

           

# Jalankan program utama
main()