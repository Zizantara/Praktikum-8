class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, nama, nilai):
        """Menambahkan data mahasiswa."""
        if nama in self.data_mahasiswa:
            print(f"Mahasiswa dengan nama {nama} sudah ada.")
        else:
            self.data_mahasiswa[nama] = nilai
            print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        """Menampilkan semua data mahasiswa."""
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.data_mahasiswa.items():
                print(f"Nama: {nama}, Nilai: {nilai}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"Data mahasiswa {nama} berhasil dihapus.")
        else:
            print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        """Mengubah data mahasiswa berdasarkan nama."""
        if nama in self.data_mahasiswa:
            self.data_mahasiswa[nama] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.")
        else:
            print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")


# Contoh penggunaan:
daftar = DaftarNilaiMahasiswa()
daftar.tambah("Andi", 85)
daftar.tambah("Budi", 90)
daftar.tampilkan()
daftar.ubah("Andi", 95)
daftar.tampilkan()
daftar.hapus("Budi")
daftar.tampilkan()
