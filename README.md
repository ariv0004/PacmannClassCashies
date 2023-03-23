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
import sqlite3

"""
Sebuah code untuk memanggil library sqlite3.
"""
```


```
import sqlite3

class Transaction:
    """
    Sebuah class untuk kasir self-service disupermarket

    """

    def __init__(self):
      """
      Constructor untuk sebuah class Transaction

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi Constructor

      """
      self.items = {}
      self.total_belanja = 0
      while 1:
          print("<-----------------------list perintah----------------------->")
          print("- tambah order transaksi ketik: add_item")
          print("- ubah nama item order transaksi ketik: update_item_name")
          print("- ubah jumlah item order transaksi ketik: update_item_qty")
          print("- ubah harga per item order transaksi ketik: update_item_price")
          print("- validasi order transaksi ketik: check_order")
          print("- hapus salah satu order transaksi ketik: delete_item")
          print("- hapus seluruh order transaksi ketik: reset_transaction")
          print("- tampilkan biaya untuk seluruh order transaksi ketik: check_out")
          print("- keluar dari program ketik: keluar")
          print("\n")
          perlu = input("Masukkan perintah sesuai keperluan: ")

          if perlu.lower() == "add_item":
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
              self.add_item([nama_item, jumlah_item, harga])
              print("\n")

          elif perlu.lower() == "update_item_name":
              while 1:
                nama_item = input("Nama item sebelum diubah: ")
                if nama_item in self.items:
                    update_nama_item = input("Update nama item yang ingin diubah: ")
                    self.update_item_name(nama_item, update_nama_item)
                    break
                else:
                    print("Tidak terdapat nama item tersebut!")
              print("\n")

          elif perlu.lower() == "update_item_qty":
              while 1:
                nama_item = input("Nama item sebelum diubah: ")
                if nama_item in self.items:
                    update_quantity_item = input("Update quantity item yang ingin diubah: ")
                    self.update_item_qty(nama_item, update_quantity_item)
                    break
                else:
                    print("Tidak terdapat nama item tersebut!")
              print("\n")

          elif perlu.lower() == "update_item_price":
              while 1:
                nama_item = input("Nama item sebelum diubah: ")
                if nama_item in self.items:
                    update_price_item = input("Update price item yang ingin diubah: ")
                    self.update_item_price(nama_item, update_price_item)
                    break
                else:
                    print("Tidak terdapat nama item tersebut!")
              print("\n")

          elif perlu.lower() == "check_order":
              self.check_order()
              print("\n")

          elif perlu.lower() == "delete_item":
              while 1:
                nama_item = input("Nama item dihapus: ")
                if nama_item in self.items:
                    self.delete_item(nama_item)
                    break
                else:
                    print("Tidak terdapat nama item tersebut!")

          elif perlu.lower() == "reset_transaction":
              self.reset_transaction()
              print("Semua Item berhasil di Delete")
              print("\n")

          elif perlu.lower() == "check_out":
              self.check_out()
              print("\n")

          elif perlu.lower() == "keluar":
              break

          else:
              print("Mohon masukkan perintah dengan benar dan sesuai!")
              print("\n")
      print(self.items)
 ```
 ```
    def add_item(self, item):
      """
      Sebuah fungsi untuk menambahkan item baru kedalam keranjang

      Parameters
      ----------
      terdapat parameter pada fungsi item

      Return
      ------
      Menyimpan seluruh data yang berhasil diinput oleh customer kedalam database
      """
      if item[0] in self.items:
          self.items[item[0]][0] += item[1]
      else:
          self.items[item[0]] = [item[1], item[2]]
```
```
    def update_item_name(self, old_name, new_name):
      """
      Sebuah fungsi untuk mengubah data nama item pada order transaksi yang telah diinput oleh customer

      Parameters
      ----------
      terdapat parameter pada fungsi old_name, new_name

      Return
      ------
      Menyimpan seluruh data perubahan pada nama item yang berhasil diinput oleh customer kedalam database
      """
      if old_name in self.items:
          self.items[new_name] = self.items.pop(old_name)
```
```
    def update_item_qty(self, name, qty):
      """
      Sebuah fungsi untuk mengubah data jumlah item pada order transaksi yang telah diinput oleh customer

      Parameters
      ----------
      terdapat parameter pada fungsi name, qty

      Return
      ------
      Menyimpan seluruh data perubahan pada jumlah item yang berhasil diinput oleh customer kedalam database
      """

      if name in self.items:
          self.items[name][0] = qty
```
```
    def update_item_price(self, name, price):
      """
      Sebuah fungsi untuk mengubah data harga per item pada order transaksi yang telah diinput oleh customer

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi name, price

      Return
      ------
      Menyimpan seluruh data perubahan pada harga per item yang berhasil diinput oleh customer kedalam database
      """

      if name in self.items:
          self.items[name][1] = price
```
```
    def check_order(self):
      """
      Sebuah fungsi untuk melihat apakah terdapat kesalahan penginputan data pada transaksi

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi check_order_item

      Return
      ------
      Menampilkan apakah terdapat kesalahan dalam penginputan data pada transaksi dan data yang berhasil diinput oleh customer
      """

      print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
      print("|----|-----------|-------------|------------|-------------|")
      i = 0
      for item in self.items:
          i += 1
          if not item or self.items[item][0] < 1 or self.items[item][1] < 1:
              return "Terdapat kesalahan input data"
          else:
              total_price = self.items[item][0] * self.items[item][1]
              print(
                  f"| {i}  | {item}     |{self.items[item][0]}            |{self.items[item][1]}      |   {total_price}    |")
      return "Pemesanan sudah benar"
```
```
    def delete_item(self, name):
      """
      Sebuah fungsi untuk menghapus salah satu item yang berhasil diinput oleh customer pada transaksi

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi delete_item

      Return
      ------
      Menghapus salah satu order transaksi pada data database
      """

      if name in self.items:
          del self.items[name]
```
```
    def reset_transaction(self):
      """
      Sebuah fungsi untuk menghapus seluruh item yang berhasil diinput oleh customer pada transaksi

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi reset_transaction

      Return
      ------
      Menghapus seluruh order transaksi pada data database
      """

      self.items = {}

      print("Berhasil menghapus seluruh transaksi!")
```
```
        def check_out(self):
      check_out_item = {}
      """
      Sebuah fungsi untuk menghitung total biaya yang harus dibayarkan customer dari item-item pada data transaksi

      Parameters
      ----------
      Tidak terdapat parameter pada fungsi total_price

      Return
      ------
      Menampilkan total biaya yang harus dibayar oleh customer tersebut dengan beberapa kriteria yaitu
      - diatas Rp. 500.000 akan mendapatkan potongan biaya sebesar 7% dari total biaya per Item yang harus dibayarkan
      - diatas Rp. 300.000 akan mendapatkan potongan biaya sebesar 6% dari total biaya per Item  yang harus dibayarkan
      - diatas Rp. 200.000 akan mendapatkan potongan biaya sebesar 5% dari total biaya per Item  yang harus dibayarkan
      """
      print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga | Diskon | Harga Diskon |")
      print("|----|-----------|-------------|------------|-------------|--------|--------------|")
      i = 0
      total_belanja = 0
      for item in self.items:
          total = self.items[item][0] * self.items[item][1]
          if total > 500000:
              discount = 0.07
              diskon_str = "7%"
          elif total > 300000:
              discount = 0.06
              diskon_str = "6%"
          elif total > 200000:
              discount = 0.05
              diskon_str = "5%"
          else:
              discount = 0
              diskon_str = "-"
          discounted_total = total - (total * (discount))
          check_out_item[item] = [self.items[item][0], self.items[item][1], discount, discounted_total]
          i += 1
          if not item or self.items[item][0] < 1 or self.items[item][1] < 1:
              return "Terdapat kesalahan input data"
          else:
              total_price = self.items[item][0] * self.items[item][1]
              total_diskon = round(total_price * (1 - discount))
              print(
                  f"| {i}  | {item}     |{self.items[item][0]}            |{self.items[item][1]}      |   {total_price}    |    {diskon_str}   |    {total_diskon}    |")
          self.insert_to_table(check_out_item)
          total_belanja += total_diskon
      print("Total Belanja",total_belanja)
```                 
```
        def insert_to_table(self, check_out_item):
        conn = sqlite3.connect('transaction.db')
        c = conn.cursor()
        c.execute(
            """ DROP TABLE IF EXISTS transactions; """)
        c.execute(
            """
            CREATE TABLE transactions (
                no_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_item DATATYPE, 
                jumlah_item INTERGER, 
                harga INTERGER, 
                total_harga INTERGER, 
                diskon INTERGER, 
                harga_diskon INTERGER
            ); """)
        for item in check_out_item:
            jumlah_item = check_out_item[item][0]
            harga = check_out_item[item][1]
            total_harga = jumlah_item * harga
            diskon = total_harga * check_out_item[item][2]
            harga_diskon = total_harga - diskon
            list_item = [item, jumlah_item, harga, total_harga, diskon, round(harga_diskon)]
            c.execute(
                "INSERT INTO transactions (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES (?, ?, ?, ?, ?, ?)",
                (list_item))
        conn.commit()
        conn.close()
```

## Test Case

Pada bagian ini program akan dilakukan beberapa testing berbeda untuk memastikan bahwa program berjalan dengan lancar.

1. Test pertama
    Customer ingin menambahkan dua item baru menggunakan *method add_item()*. item yang ditambahkan adalah sebagai berikut:
    - Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
    - Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

    Hasil:
    
    ![Test 1](https://user-images.githubusercontent.com/53809969/227107772-c6701035-1a18-4657-8ef0-d4528e92e3d9.png)
    
    Gambar 3. Output test pertama
 
2. Test kedua
    Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan *method delete_item()* untuk menghapus item.   Item yang ingin dihapus adalah <b>Pasta Gigi</b>.

    Hasil:
    
    ![Test 2](https://user-images.githubusercontent.com/53809969/227108401-c7fdfc18-7c09-4c47-b248-35bd7de529b1.png)
    
    Gambar 4. Output test kedua

3. Test ketiga
    Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan *method reset_transaction()* untuk menghapus semua item yang sudah ditambahkan.

    Hasil:
    
    ![Test 3](https://user-images.githubusercontent.com/53809969/227108890-a6d9ff96-63dd-4e1a-a932-24ff45785920.png)
    
    Gambar 5. Output test ketiga

4. Test keempat
    Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan *method total_price()*. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

    Hasil:
    
    ![Test 4](https://user-images.githubusercontent.com/53809969/227120917-099e4219-5530-49f5-9065-bdcc0500267e.png)
    
    Gambar 6. Output test keempat

## Conclusion: 

Kebanyakan manusia sangat terbantu dengan adanya supermarket untuk membeli barang atau makanan yang dibutuhkan. Pada supermarket banyak barang-barang yang dibutuhkan sehingga manusia dapat membeli barang tersebut dengan efisien karena barang-barang tersebut berada disatu tempat yaitu supermarket. Dengan adanya program ini akan menambah efisiensi dari customer dan pihak supermarket karena tidak bergantung pada *physical transcation*, cukup dengan smartphone dan internet sudah dapat membeli barang atau makanan di supermarket tersebut. 

Harapan saya pada program ini kedepannya adalah dapat mengimplementasikan program ini menjadi sebuah aplikasi mobile atau website yang memiliki tampilan interaktif dan menarik. Menambahkan beberapa fitur, salah satunya seperti setiap transaksi customer akan mendapatkan point dan point tersebut dapat digunakan untuk membeli barang di supermarket tersebut secara gratis. Menyimpan seluruh data customer, transaksi dan barang ke sebuah database.

## References: 
- [apa itu kasir?](https://www.ekrut.com/media/kasir-adalah)
- [tips membuat dokumentasi ekstensi .md](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
