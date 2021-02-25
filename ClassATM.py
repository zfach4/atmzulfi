class ATM:
    def __init__(self):
        self.saldo = 1000000
        self.resi = ["Saldo awal Rp. 1000000"]

    def getCetakAwal(self):
        print("Selamat datang di ATM Halusin Nasi")
        print("Layanan Apa yang ingin Anda Pilih:")
        self.setPilihan()

    def setPilihan(self):
        print("1. Stor Tunai")
        print("2. Tarik Tunai")
        print("3. Lihat Saldo")
        print("4. Cetak Resi")
        print("5. Transfer")
        print("0. Kembali")
        a = int(input("Masukkan Pilihan Anda: "))
        if a == 0:
            print("Terimakasih...")
        elif a == 1:
            self.setorTunai()
        elif a == 2:
            self.tarikTunai()
        elif a == 3:
            self.lihatSaldo()
        elif a == 4:
            self.cetakResi()
        elif a == 5:
            self.transfer()
        else:
            print("Pilihan Tidak tersedia")
            print("Pilihan:")
            self.setPilihan()

    def setorTunai(self):
        print("")
        print("Anda memasuki layanan Stor Tunai")
        print("")
        print("Silahkan masukkan uang Anda")
        b = int(input("Rp. "))
        self.saldo += b
        print("Saldo anda menjadi Rp. " + str(self.saldo))
        self.resi.append("Stor tunai Rp. " + str(b))
        self.lanjutTransaksi()

    def tarikTunai(self):
        print("")
        print("Anda memasuki layanan Tarik Tunai")
        print("")
        print("Silahkan masukkan uang yang ingin ditarik")
        d = int(input("Rp. "))
        if d > (self.saldo - 100000):
            print("Maaf sisa saldo anda tidak mencukupi")
            self.lanjutTransaksi()
        else:
            self.saldo -= d
            print("")
            print("Anda Berhasil menarik Uang")
            print("sisa saldo anda Rp. " + str(self.saldo))
            self.resi.append("Penarikan Uang Rp. " + str(d))
            print("")
            self.lanjutTransaksi()

    def lihatSaldo(self):
        print("Saldo anda Rp. " + str(self.saldo))
        self.lanjutTransaksi()

    def cetakResi(self):
        print("")
        for i in self.resi:
            print(i)
        print("")
        print("Sisa saldo anda Rp. " + str(self.saldo))
        print("")
        self.lanjutTransaksi()

    def transfer(self):
        print("")
        print("Anda Akan mentransfer uang")
        print("")
        to = int(input("Silahkan Masukan No Rekening Tujuan anda: "))
        uang = int(input("Silahkan Masukan Banyak uang yang ditransfer: Rp. "))
        print("")
        if uang > (self.saldo - 100000):
            print("Maaf, saldo anda tidak cukup")
            self.setPilihan()
        else:
            print("Tujuan  : " + str(to))
            print("Nominal : Rp. " + str(uang))
            print("")
            print("Apakah anda yakin:")
            print("1. Ya")
            print("2. Tidak")
            yakin = int(input("Pilihan: "))
            if yakin == 1:
                self.saldo -= uang
                self.resi.append("Transfer Rp. " + str(uang))
                print("")
                print("Anda Telah sukses mentransfer Uang")
                print("Sisa saldo anda Rp. " + str(self.saldo))
                print("")
                self.lanjutTransaksi()
            elif yakin == 2:
                print("")
                self.transfer()

    def lanjutTransaksi(self):
        print("")
        print("Apakah anda masih ingin bertransaksi:")
        print("")
        print("1. Ya")
        print("2. Tidak")
        c = int(input("Masukkan pilihan anda: "))
        if c == 1:
            print("Silahkan pilih layanan:")
            self.setPilihan()
        elif c == 2:
            print("Terimakasih sudah Menggunakan jasa kami")
        else:
            print("Pilihan Tidak tersedia")
            self.lanjutTransaksi()

atm = ATM()
atm.getCetakAwal()

