import pandas as pd
import os

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
                  sum(int(self.data_all_item['Total Harga']) - (sum(self.data_all_item["Total Harga"]) * 0.05))))
