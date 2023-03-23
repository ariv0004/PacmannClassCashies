# Super Cashier

![image](https://user-images.githubusercontent.com/88027268/213964997-b79e6193-dfeb-4eb8-9a81-d33a35810d89.png)

Gambar 1. Illustrasi super cashier

## Proyek overview

Kasir adalah salah satu profesi yang bertugas mengurus transaksi dan menyimpan pembayaran seperti uang tunai maupun giro. Kasir sendiri memiliki beberapa *job desk* seperti mencatat data penjualan, Melakukan proses transaksi penjualan, Membuat laporan rutin dan Merekap laporan transaksi penjualan. Proyek ini bertujuan agar supermarket dapat menimalisir cost yang harus dibayarkan kepada pekerjaan kasir sehingga uang tersebut dapat dialokasikan ke bagian yang lebih penting, seperti meningkatkan kualitas produk yang dijual, menjual produk yang lebih beragam dan memaksimalkan *campaign* produk.

## Business Understanding

Bagian ini akan menjelaskan proses klarifikasi masalah.

### Problem Statements

- Bagaimana menurunkan cost dari biaya pekerjaan kasir bagi pemilik supermarket?
- Bagaimana sebuah supermarket dapat menjangkau customer dari luar daerah?

### Goals

- Meminimalisir terjadinya error atau bug pada program sehingga customer dapat berbelanja dengan lancar.
- Menghasilkan sebuah program yang dapat dijangkau hanya menggunakan internet saja tanpa harus secara langsung pergi ke supermarket tersebut.

    ### Solution statement
    - Menggunakan bahasa pemrograman *python* dengan konsep *object oriented programming, Modular code, Error handling dan clean code*.

## Objectives

Membuat sebuah program yang dapat melakukan *Create, Read, Update dan Delete*(CRUD). 

- <b>Create</b>
    - Customer dapat memasukkan ID transaksi pada sistem.
    - Customer dapat menambahkan nama item, jumlah item, harga per item dan sistem otomatis akan menghitung total harga berdasarkan jumlah item * harga per item.
- <b>Read</b>
    - Customer dapat melihat sebuah data tabular dari item order transaksi yang telah dilakukan.
    - Customer dapat melakukan *sanity check* dari item order transaksi yang telah masuk kedalam sistem.
    - Customer dapat melihat total biaya yang harus dibayar dari seluruh total biaya yang telah customer input dan melihat apakah mendapatkan sebuah potongan harga. 
- <b>Update</b>
    - Customer dapat mengubah nama item yang telah diinput sebelumnya berdasarkan nama item yang dimasukkan. 
    - Customer dapat mengubah jumlah item yang telah diinput sebelumnya berdasarkan nama item yang dimasukkan dan total harga akan dapat menyesuaikan jumlah item terbaru.
    - Customer dapat mengubah harga per item yang telah diinput sebelumnya berdasarkan nama item yang dimasukkan dan total harga akan dapat menyesuaikan harga per item terbaru.
- <b>Delete</b>
    - Customer dapat menghapus salah satu item yang telah diinput berdasarkan nama item yang dimasukkan.
    - Customer dapat menghapus seluruh item yang telah masuk kedalam order transaksi.
    
## Flowchart

![flowchart drawio](https://user-images.githubusercontent.com/88027268/214074845-c78a2005-3d83-4864-918d-97f3a7ab1cd5.png)

Gambar 2. Flowchart super cashier

## Technical explain

proyek ini terdiri dari 2 file yaitu main.py dan modul.py yang masing-masing memiliki kegunaan.
- file main.py digunakan sebagai file utama untuk menjalankan program *super cashier* dan hanya berisi object dari class Transaction.
- file modul.py digunakan sebagai modul yang berisi *class, function dan attributes*. penjelasan dari isi file sebagai berikut:

```
import pandas as pd
import os

"""
Sebuah code untuk memanggil library pandas dan os. library pandas digunakan untuk melakukan visualisasi data dalam bentuk tabular sedangkan os digunakan untuk melakukan exit program.
"""
```


```
class Transaction:
    """
    Sebuah class untuk kasir self-service disupermarket

    ...

    Attributes
    ----------
    id_transaksi : int
        id_transaksi berjenis input untuk hasil transaksi customer
    data_all_item : dict
        data_all_item adalah tempat penyimpanan data order transaksi yang berhasil diinput oleh customer kedalam sistem
    """

    data_all_item = {"Nama item": [], "Jumlah item": [], "Harga per item": [], "Total Harga": []}
```

```
def __init__(self):
    """
    Constructor untuk sebuah class Transaction

    Parameters
    ----------
    Tidak terdapat parameter pada fungsi Constructor

    Attributes
    ----------
    id_transaksi : int
      id_transaksi berjenis input untuk hasil transaksi customer
    """

    print("<-----------------Welcome to Super Cashier----------------->")
    while 1:
      try:
          id_transaksi = int(input("Masukkan ID Transaksi anda: "))
          print("ID Transaksi anda {}".format(id_transaksi))
          print("\n")
          break
      except ValueError:
          print("ID Transaksi tidak valid!")
          continue
    while 1:
      print("<-----------------------list perintah----------------------->")
      print("- tambah order transaksi ketik: add_item")
      print("- ubah nama item order transaksi ketik: update_item_name")
      print("- ubah jumlah item order transaksi ketik: update_item_qty")
      print("- ubah harga per item order transaksi ketik: update_item_price")
      print("- validasi order transaksi ketik: check_order_item")
      print("- hapus salah satu order transaksi ketik: delete_item")
      print("- hapus seluruh order transaksi ketik: reset_transaction")
      print("- tampilkan biaya untuk seluruh order transaksi ketik: total_price")
      print("- keluar dari program ketik: keluar")
      print("\n")
      perlu = input("Masukkan perintah sesuai keperluan: ")
      if perlu.lower() == "add_item":
          self.add_item()
          print("\n")
      elif perlu.lower() == "update_item_name":
          self.update_item_name()
          print("\n")
      elif perlu.lower() == "update_item_qty":
          self.update_item_qty()
          print("\n")
      elif perlu.lower() == "update_item_price":
          self.update_item_price()
          print("\n")
      elif perlu.lower() == "check_order_item":
          self.check_order_item()
          print("\n")
      elif perlu.lower() == "delete_item":
          self.delete_item()
          print("\n")
      elif perlu.lower() == "reset_transaction":
          self.reset_transaction()
          print("\n")
      elif perlu.lower() == "total_price":
          self.total_price()
          print("\n")
      elif perlu.lower() == "keluar":
          # break
          os._exit(0)
      else:
          print("Mohon masukkan perintah dengan benar dan sesuai!")
          print("\n")
```

```
def add_item(self):
  """
  Sebuah fungsi untuk menambahkan item baru kedalam keranjang

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi add_item

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang dimasukkan kedalam keranjang
  jumlah_item : int
      jumlah_item berjenis input untuk jumlah item yang dimasukkan kedalam keranjang
  harga : int
      harga berjenis input untuk harga per item yang dimasukkan kedalam keranjang
  total_harga : int
      Penghitung total_harga dengan melakukan perkalian terhadap jumlah item dan harga per item

  Return
  ------
  Menyimpan seluruh data yang berhasil diinput oleh customer kedalam database
  """

  nama_item = input("Nama item yang dibeli: ")

  while 1:
      try:
          jumlah_item = int(input("Jumlah item yang dibeli: "))
          break
      except ValueError:
          print("Input berupa angka!")
          continue

  while 1:
      try:
          harga = int(input("Harga per item yang dibeli: "))
          break
      except ValueError:
          print("Input berupa angka!")
          continue

  self.data_all_item["Nama item"].append(nama_item)
  self.data_all_item["Jumlah item"].append(jumlah_item)
  self.data_all_item["Harga per item"].append(harga)
  self.data_all_item["Total Harga"].append(jumlah_item * harga)
```

```
def update_item_name(self):
  """
  Sebuah fungsi untuk mengubah data nama item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_name

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada nama item
  update_nama_item : int
      update_nama_item berjenis input untuk nama item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada nama item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item sebelum diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          update_nama_item = input("Update nama item yang ingin diubah: ")
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Nama item'][idx_item] = update_nama_item
          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def update_item_qty(self):
  """
  Sebuah fungsi untuk mengubah data jumlah item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_qty

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada jumlah item
  update_jumlah_item : int
      update_jumlah_item berjenis input untuk jumlah item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada jumlah item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item yang ingin diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          while 1:
              try:
                  update_jumlah_item = int(input("Update jumlah item yang dibeli: "))
                  break
              except ValueError:
                  print("Input berupa angka!")
                  continue
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Jumlah item'][idx_item] = update_jumlah_item

          self.data_all_item["Total Harga"][idx_item] = (
                      update_jumlah_item * self.data_all_item["Harga per item"][idx_item])

          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def update_item_price(self):
  """
  Sebuah fungsi untuk mengubah data harga per item pada order transaksi yang telah diinput oleh customer

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi update_item_price

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada harga per item
  update_harga_item : int
      update_harga_item berjenis input untuk harga per item terbaru
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menyimpan seluruh data perubahan pada harga per item yang berhasil diinput oleh customer kedalam database
  """

  while 1:
      nama_item = input("Nama item yang ingin diubah: ")

      if nama_item in self.data_all_item.get("Nama item"):
          while 1:
              try:
                  update_harga_item = int(input("Update harga per item yang dibeli: "))
                  break
              except ValueError:
                  print("Input berupa angka!")
                  continue
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          self.data_all_item['Harga per item'][idx_item] = update_harga_item

          self.data_all_item["Total Harga"][idx_item] = (
                      update_harga_item * self.data_all_item["Jumlah item"][idx_item])

          print("Berhasil dirubah!")
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def check_order_item(self):
  """
  Sebuah fungsi untuk melihat apakah terdapat kesalahan penginputan data pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi check_order_item

  Attributes
  ----------
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular

  Return
  ------
  Menampilkan apakah terdapat kesalahan dalam penginputan data pada transaksi dan data yang berhasil diinput oleh customer
  """

  if not any(self.data_all_item.values()):
      print("Tidak ada data transaksi!")
  elif '' in self.data_all_item['Nama item']:
      print("Mohon mengisi nama item yang kosong!")
      print("<--------List order item-------->")
      df = pd.DataFrame(self.data_all_item)
      print(df)
  else:
      print("Data transaksi sudah benar!")
      print("<--------List order item-------->")
      df = pd.DataFrame(self.data_all_item)
      print(df)
```

```
def delete_item(self):
  """
  Sebuah fungsi untuk menghapus salah satu item yang berhasil diinput oleh customer pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi delete_item

  Attributes
  ----------
  nama_item : str
      nama_item berjenis input untuk nama item yang ingin dilakukan penghapusan order transaksi
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular
  idx_item : int
      idx_item untuk menyimpan posisi index dari nama item yang customer input

  Return
  ------
  Menghapus salah satu order transaksi pada data database
  """

  while 1:
      nama_item = input("Nama item yang ingin dihapus: ")

      if nama_item in self.data_all_item.get("Nama item"):
          idx_item = self.data_all_item['Nama item'].index(nama_item)
          for key in list(self.data_all_item.keys()):
              del self.data_all_item[key][idx_item]

          print("Berhasil dihapus!")
          if not any(self.data_all_item.values()):
              print("Tidak ada data transaksi!")
          else:
              df = pd.DataFrame(self.data_all_item)
              print(df)
          break

      else:
          print("Tidak terdapat nama item tersebut!")
```

```
def reset_transaction(self):
  """
  Sebuah fungsi untuk menghapus seluruh item yang berhasil diinput oleh customer pada transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi reset_transaction

  Attributes
  ----------
  Tidak terdapat attribute pada fungsi reset_transaction

  Return
  ------
  Menghapus seluruh order transaksi pada data database
  """

  for key in list(self.data_all_item.keys()):
      del self.data_all_item[key][:]

  print("Berhasil menghapus seluruh transaksi!")
```

```
def total_price(self):
  """
  Sebuah fungsi untuk menghitung total biaya yang harus dibayarkan customer dari item-item pada data transaksi

  Parameters
  ----------
  Tidak terdapat parameter pada fungsi total_price

  Attributes
  ----------
  df : dataframe
      df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular

  Return
  ------
  Menampilkan total biaya yang harus dibayar oleh customer tersebut dengan beberapa kriteria yaitu
  - diatas Rp. 500.000 akan mendapatkan potongan biaya sebesar 10% dari total biaya yang harus dibayarkan
  - diatas Rp. 300.000 akan mendapatkan potongan biaya sebesar 8% dari total biaya yang harus dibayarkan
  - diatas Rp. 200.000 akan mendapatkan potongan biaya sebesar 5% dari total biaya yang harus dibayarkan
  """

  if not any(self.data_all_item.values()):
      print("Tidak ada data transaksi!")
  else:
      df = pd.DataFrame(self.data_all_item)
      print(df)
      if sum(self.data_all_item["Total Harga"]) > 500000:
          print("Sebelum mendapatkan diskon 10%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 10%: Rp.{}".format(
              int(sum(self.data_all_item["Total Harga"]) - (sum(self.data_all_item["Total Harga"]) * 0.10))))
      elif sum(self.data_all_item["Total Harga"]) > 300000:
          print("Sebelum mendapatkan diskon 8%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 8%: Rp.{}".format(
              sum(int(self.data_all_item["Total Harga"]) - (sum(self.data_all_item["Total Harga"]) * 0.08))))
      elif sum(self.data_all_item["Total Harga"]) > 200000:
          print("Sebelum mendapatkan diskon 5%: Rp.{}".format(sum(self.data_all_item["Total Harga"])))
          print("Setelah mendapatkan diskon 5%: Rp.{}".format(
              sum(int(self.data_all_item['Total Harga']) - (sum(self.data_all_item["Total Harga"]) * 0.0
```

## Test Case

Pada bagian ini program akan dilakukan beberapa testing berbeda untuk memastikan bahwa program berjalan dengan lancar.

1. Test pertama
    Customer ingin menambahkan dua item baru menggunakan *method add_item()*. item yang ditambahkan adalah sebagai berikut:
    - Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
    - Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

    Hasil:
    
    ![image](https://user-images.githubusercontent.com/88027268/214100635-9de049a5-b2d0-4efe-8244-b2ccdded61c7.png)
    
    Gambar 3. Output test pertama
 
2. Test kedua
    Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan *method delete_item()* untuk menghapus item.   Item yang ingin dihapus adalah <b>Pasta Gigi</b>.

    Hasil:
    
    ![image](https://user-images.githubusercontent.com/88027268/214100819-a2761058-cfcb-445e-91b4-253187db33e1.png)
    
    Gambar 4. Output test kedua

3. Test ketiga
    Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan *method reset_transaction()* untuk menghapus semua item yang sudah ditambahkan.

    Hasil:
    
    ![image](https://user-images.githubusercontent.com/88027268/214104723-2a73cecb-4692-4b2a-a956-4f0e4fb6a8a8.png)
    
    Gambar 5. Output test ketiga

3. Test keempat
    Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan *method total_price()*. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

    Hasil:
    
    ![image](https://user-images.githubusercontent.com/88027268/214104472-cd46e89f-79d0-4874-b597-cb8b0eae5fd7.png)
    
    Gambar 6. Output test keempat

## Conclusion: 

Kebanyakan manusia sangat terbantu dengan adanya supermarket untuk membeli barang atau makanan yang dibutuhkan. Pada supermarket banyak barang-barang yang dibutuhkan sehingga manusia dapat membeli barang tersebut dengan efisien karena barang-barang tersebut berada disatu tempat yaitu supermarket. Dengan adanya program ini akan menambah efisiensi dari customer dan pihak supermarket karena tidak bergantung pada *physical transcation*, cukup dengan smartphone dan internet sudah dapat membeli barang atau makanan di supermarket tersebut. 

Harapan saya pada program ini kedepannya adalah dapat mengimplementasikan program ini menjadi sebuah aplikasi mobile atau website yang memiliki tampilan interaktif dan menarik. Menambahkan beberapa fitur, salah satunya seperti setiap transaksi customer akan mendapatkan point dan point tersebut dapat digunakan untuk membeli barang di supermarket tersebut secara gratis. Menyimpan seluruh data customer, transaksi dan barang ke sebuah database.

## References: 
- [apa itu kasir?](https://www.ekrut.com/media/kasir-adalah)
- [tips membuat dokumentasi ekstensi .md](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
