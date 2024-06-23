import pandas as pd

# Berikan jalur yang benar menuju file CSV Anda
file_path = 'C:/Users/ASUS/PycharmProjects/pythonProject4/hargalaptop.csv'

try:
    # Memuat file CSV dengan delimiter titik koma dan encoding yang sesuai
    laptop_data = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')

    # Menampilkan beberapa baris pertama dari dataframe untuk verifikasi
    print("Data berhasil dimuat. Berikut adalah beberapa baris pertama:")
    print(laptop_data.head())

    # Fungsi untuk mencari data berdasarkan nama produk menggunakan BFS
    def bfs_cari_laptop(data, nama_produk):
        queue = list(data.index)  # Inisialisasi queue dengan indeks dataframe
        visited = set()

        while queue:
            index = queue.pop(0)  # Ambil indeks pertama dari queue
            if index not in visited:
                visited.add(index)
                if nama_produk.lower() in str(data.at[index, 'Product']).lower():
                    print(f"Data yang cocok dengan nama produk '{nama_produk}':")
                    print(data.loc[index])
                    return
        print(f"Tidak ditemukan data yang cocok dengan nama produk '{nama_produk}'")

    # Meminta inputan pengguna
    nama_produk = input("Masukkan nama produk yang ingin dicari: ")

    # Pencarian data menggunakan BFS
    bfs_cari_laptop(laptop_data, nama_produk)

except FileNotFoundError:
    print(f"File di {file_path} tidak ditemukan. Silakan periksa jalurnya dan coba lagi.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
