# Hadoop

## Apa itu Hadoop?
Silahkan baca [di sini](http://www.teknologi-bigdata.com/2013/02/hdfs-berawal-dari-google-untuk-big-data.html)

## /user/cloudera

[HUE (Hadoop User Experience)]([https://link](https://www.dataideology.com/data/hadoop-user-experience-hue)) menggunakan directory /user/cloudera sebagai default directorynya. Jikalau kita ingin menggunakan Impala atau Hive, maka semua data tersebut diambil dari /user/cloudera. Oleh sebab itu, setiap kali kita melakukan *-copyFromLocal* kita harus mengcopynya ke /user/cloudera

## Syntax Dasar

Untuk menggunakan Hadoop FS, kita harus memulai command dengan syntax 

```
hadoop fs [arguments]
```

Berikut adalah argument-argument yang akan kita gunakan di project ini

| Argumen       | Keterangan                          | Contoh                                                     |
| ------------- | ----------------------------------- | ---------------------------------------------------------- |
| mkdir         | Membuat folder                      | hadoop fs -mkdir folder1                                   |
| rm            | Menghapus file / folder             | hadoop fs -rm *                                            |
| copyFromLocal | Mengcopy file local ke dalam hadoop | hadoop fs -copyFromLocal source /user/cloudera/destination |
| ls            | Menampilkan isi dari sebuah folder  | hadoop fs -ls /user/cloudera                               |