import json
import time


data_pengguna = []

# File name to store user data
file_name = "user_data.json"

#i used chatgpt for the data saving method using json because idk how to do it
#Load user data from a file if it exists
try:
    with open(file_name, "r") as file:
        data_pengguna = json.load(file)
    print("Data loaded successfully.")
except (FileNotFoundError, json.JSONDecodeError):
    print("File not found or data is corrupted. Using an empty list.")

email = ['@gmail.com', '@outlook.com', '@yahoo.com', '@std.trisakti.ac.id', '@mail.com']

isValid = True

while True:
    print("Masuk ke akun")
    print("1.) Register")
    print("2.) Login")
    print("3.) Ganti Password")
    print("4.) Hapus akun")
    print("5.) List User")
    print("6.) Edit User")

    pilihan = input("Masukan pilihan opsi (1/2/3/4/5/6) : ")

    if pilihan == "1":
        print("\nMendaftarkan pengguna baru\n")
        nama_pengguna = input("Masukan Username : ")
        email_pengguna = input(r"Masukan Email : ")
        for ending in email:
            if email_pengguna.endswith(ending):
                isValid = True
                break
        if not isValid:
            print("email tidak valid!")
        else:
            password_pengguna = input("Masukan Password : ")
            existing_user = None
            for user in data_pengguna:
                if user['nama'] == nama_pengguna:
                    existing_user = user
                    break
                elif user['email'] == email_pengguna:
                    existing_user = user
                    break
            if existing_user:
                print("Pengguna dengan username atau email yang sama sudah terdaftar.")
            else:
                user = {'nama': nama_pengguna, 'email': email_pengguna, 'password': password_pengguna}
                data_pengguna.append(user)
                print("Berhasil mendaftarkan pengguna {}!".format(nama_pengguna))
                print("Selamat Datang!")

    elif pilihan == "2":
        print("\nLogin ke akun\n")
        nama_pengguna = input("Masukan Username : ")
        password_pengguna = input("Masukan Password : ")
        login_berhasil = False
        for user in data_pengguna:
            if user['nama'] == nama_pengguna and user['password'] == password_pengguna:
                print("Berhasil Login!")
                print("Selamat Datang {}".format(nama_pengguna))
                login_berhasil = True
                break

        if not login_berhasil:
            print("Username atau Password tidak valid! atau User tidak ada di data list")
            keluar = input("Ulangi dari program ini? y/n : ")
            if keluar.lower() != "y":
                break
            else:
                continue

    elif pilihan == "3":
        email_pengguna = input("Masukan Email : ")
        password_ditemukan = False
        for user in data_pengguna:
            if user['email'] == email_pengguna:
                print("Email ditemukan!")
                passwordBaru = input("Masukan password baru : ")
                user['password'] = passwordBaru
                print("Password pengguna {} dengan email {} telah diganti!".format(user['nama'], email_pengguna))
                password_ditemukan = True
                break

        if not password_ditemukan:
            print("User yang memiliki Email tersebut tidak ditemukan!")
            keluar = input("Keluar dari program ini? y/n : ")
            if keluar.lower() == "y":
                break
    elif pilihan == "4":
        print("\nMenghapus akun\n")
        nama_pengguna = input("Masukan Nama : ")
        email_pengguna = input("Masukan Email : ")
        password_pengguna = input("Masukan Password : ")
        akunDitemukan = False
        for user in data_pengguna:
            if user['nama'] == nama_pengguna and user['email'] == email_pengguna and user['password'] == password_pengguna:
                print("Akun ditemukan")
                akunDitemukan = True
                hapusAkun = input("Apakah Anda yakin ingin menghapus akun ini? (y/n) : ")
                if hapusAkun.lower() == "y":
                    data_pengguna.remove(user)
                    print("Akun Telah dihapus")
                else:
                    print("Akun tidak jadi dihapus")
                break

        if not akunDitemukan:
            print("Akun tidak ditemukan")
            keluar = input("Keluar dari program ini? y/n : ")
            if keluar.lower() == "y":
                break
    elif pilihan == "5":
        if len(data_pengguna) == 0:
            print("User tidak ditemukan")
        else:
            print("Daftar User : ")
            for idx, user in enumerate(data_pengguna, start=1):
                print("{}.Nama : {} = aktif".format(idx, user['nama']))
    
    elif pilihan == "6":
        print("Edit Akun")
        
        nama_pengguna = input("Masukan Username : ")
        password_pengguna = input("Masukan Password : ")
        dataValid = False    
        
        for user in data_pengguna:
            if user['nama'] == nama_pengguna and user['password'] == password_pengguna:
                dataValid = True
                opsi1 = input("silahkan pilih, apa yang ingin di ganti (username/email/password) = ")
                if opsi1 == "email":
                        newEmail = input("Masukan email baru : ")
                        user['email'] = newEmail
                        for ending in email:
                            if newEmail.endswith(ending):
                                    isValid = True
                                    print("email berhasil diganti!")
                                    break
                            if not isValid:
                                    print("masukan email yang valid!")
                                    break
                elif opsi1 == "username":
                                newUsername = input("Masukan Username yang baru : ")
                                user['nama'] = newUsername
                                print("username telah diperbarui")
                                userNameBaru = True
                                break

                            
                elif opsi1 == "password":
                                newPass = input("Masukan password baru : ")   
                                user['password'] = newPass
                                print("password telah diperbarui")
                                passwordNew = True
                                break
                else:
                                print("opsi tidak valid")
                                break
                break
        if not dataValid:
             print("Data tidak valid")
        
    ulangi = input("Ulangi Proses? (y/n) : ")
    if ulangi.lower() != "y":
        # Save user data to a file before exiting
        with open(file_name, "w") as file:
            json.dump(data_pengguna, file)
        print("Data saved successfully.")
        print("sistem akan mati otomatis dalam 5 detik")
        time.sleep(5)
        break
