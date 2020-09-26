

# Map Reduce

## Definisi 
Model pemrograman rilisan Google yang ditujukan untuk memproses data berukuran raksasa secara terdistribusi dan paralel dalam cluster yang terdiri atas ribuan komputer
[(baca sumber)](http://www.teknologi-bigdata.com/2013/02/mapreduce-besar-dan-powerful-tapi-tidak.html).

Anggap kita memiliki 1.000.000 data yang harus diproses, dan kita mem 100 komputer. Dengan metode MapReduce, kita akan membagi 1 juta proses tersebut ke dalam 100 komputer, jadi 1 komputer memproses 10.000 data.

## Proses Map Reduce
![Process](https://www.todaysoftmag.com/images/articles/tsm33/large/a11.png)

Process Map Reduce sebenarnya terbagi menjadi 2 bagian yaitu:
1. Mapping
2. Reducing

Tetapi ada beberapa proses di dalamnya lagi yang men*support* kedua proses tersebut.

### 1. Input

Ini adalah proses di mana data diinput ke dalam sistem, berdasarkan foto di atas, ada 3 buah inputan yaitu:
- Deer Bear River
- Car Car River
- Deer Car Bear

### 2. Splitting

Ini adalah proses di mana terjadi pembagian tugas. Kita asumsikan kita memiliki 3 buah komputer (berdasarkan gambar di atas), maka 1 komputer akan memproses 1 data

### 3. Mapping

Ini adalah proses di mana datanya dibuat menjadi *("key", 1)*. Lihat gambar di atas untuk contohnya.

### 4. Shuffling

Shuffling adalah proses penggabungan key dan valuenya dari semua data yang sudah di map berdasarkan key.

### 5. Reducing

Proses penggabungan hasil shuffling, dan hasil dari reducing akan menjadi *("key", sum(values))*

### 6. Final Result

Proses penggabungan hasil reducing

