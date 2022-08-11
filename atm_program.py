from customer import Customer
import random
import datetime

atm = Customer(id)

while True:
    id = int(input('Masukan Pin Anda:' ))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silakan masukan lagi: "))
        trial += 1

        if trial == 3:
            print("Pin telah salah sebanyak 3 kali")
            exit()

    while True:
        print("Selamat Datang di ATM ...")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 -Simpan \t 4 - Ganti Pin \t 5 - Keluar")
        selectMenu = int(input("\n Silakan Pilih Menu: "))


        if selectMenu == 1 :
            print("Saldo Anda " + str(atm.checkBal()))

        elif selectMenu == 2:
            nominal = int(input("Masukan nominal saldo "))
            verify = input("Konfirmasi: Anda akan melakukan debet dengan nomninal berikut ? (y/n) " + str(nominal) + " ")

            if verify == 'y' or verify == 'Y':
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBal()) + " ")
            else:
                break

            if nominal < atm.checkBal():
                atm.withdrawBal(nominal)
                print("Transaksi debet berhasil")
                print("Sisa saldo anda sebesar Rp." + str(atm.checkBal()) + " ")
            else:
                print('Maaf saldo anda tidak mencukupi')
                print('Silakan lakukan penyimpanan uang ')
                break

        elif selectMenu == 3:
            nominal = int(input('Masukan nominal yang anda ingin simpan : Rp.'))
            verify = verify = input("Konfirmasi: Anda akan melakukan debet dengan nomninal berikut ? (y/n) " + str(nominal) + " ")

            if verify == 'y' or verify == 'Y':
                atm.depositBal(nominal)
                print('Saldo anda sekarang adalah Rp.' + str(atm.checkBal()) + '\n')
            else : break
        elif selectMenu == 4:
            old_pin = int(input('Masukan pin anda: '))

            if old_pin != int(atm.checkPin()):
                print('Pin anda salah, silakan masukan pin:' )
            else:
                new_pin = int(input('Silakan masukan pin baru: '))
                verify_pin = int(input('Konfirmasi pin anda: '))

                if verify_pin == new_pin:
                    print('Pin berhasil diperbaharui')
                else:
                    print('Maaf pin anda salah')
                    break

        elif selectMenu == 5:
            print('Resi tercetak otomatis saat anda keluar. \n harap simpan tanda terima ini sebagai bukti transaksi anda.')
            print('No. Record: ', random.randint(10000,100000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBal())
            print('Terima Kasih telah menggunakan ATM')
            exit()
        else:
            print('Tidak ada pilihan di menu')
            break
