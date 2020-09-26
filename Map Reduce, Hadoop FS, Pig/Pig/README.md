# Pig

## Apa itu Pig?

Klik [di sini](https://pig.apache.org/) untuk lebih detail. Untuk dokumentasinya bisa dilihat (di sini)[https://pig.apache.org/docs/r0.15.0/basic.html]

## Mengapa dinamakan Pig?

Karena Pig memang seperti babi yang suka makan semuanya, Pig juga bisa memproses semua data.

## Contoh Kasus
Di sini, kita menggunakan data yang ada di folder [ml-100k]('../ml-100k') yaitu [u.data](../ml-100k/u.data) dan [u.item](../ml-100k/u.item). Sekarang, kita akan menampilkan data **movies** yang ratingnya lebih dari 3.0 

## Step

1. Buka terminal terlebih dahulu
   
2. import data [u.data](../ml-100k/u.data) dan [u.item](../ml-100k/u.item)

    ```
    data = LOAD '/user/cloudera/big_data/training/ml-100k/u.data'
    AS (userID:int, movieID:int, rating:int, ratingTime:int);

    movies = LOAD '/user/cloudera/big_data/training/p1 & p2/ml-100k/u.item'
    USING PigStorage('|') AS (movieID:int, movieTitle: chararray, releaseDate:chararray, 
    videoRelease:chararray, imdblink:chararray)
    ```
    **LOAD** adalah sebuah syntax yang digunakan untuk mengimport data dan memasukkannya ke dalam sebuah variabel dengan atribut yang terdapat di dalam **AS**

    **USING PigStorage** berguna untuk memberitahu "character" apa yang memisahkan semua atribut.


3. Untuk melihat isinya kita jalankan command di bawah
    ```
    dump data;
    ```

4. Untuk melihat struktur dari variabel yang sudah dibuat
    ```
    describe data;

    # Output:
    # {userID: int, movieID: int, rating: int, ratingTime: int}
    ```

5. Sekarang kita kelompokkan datanya berdasarkan movieId
    ```
    groupMovie = GROUP data BY MovieID;
    ```

6. Kalau kita describe, datanya akan menjadi seperti ini
    ```
    describe groupMovie;
    
    # Output:
    #{group: int, data: {userID: int, movieID: int, rating: int, ratingTime: int}}
    ```

7. Sekarang cari rata-rata ratingnya, karena 1 movie bisa di*rate* lebih dari 1 orang
   ```
   avgMovie = FOREACH groupMovie GENERATE group as MovieID, AVG(ratings.rating) AS avg_rating;
   ```

   **FOREACH** digunakan untuk looping data <br>
   **GENERATE** digunakan untuk membuat atribut dari variabel tersebut

8. Kita filter data yang rata-rata ratingnya lebih dari 3.0
   ```
   filterAvg = FILTER avgMovie BY avg_rating > 3.0;
   ```

9. Kita sort datanya berdasarkan ratingnya dari yang tertinggi ke terendah
    ```
    ordered = ORDERED filtered BY avg_rating DESC
    ```

10. Kita join u.data dan u.item
    ```
    joined = JOIN movies BY movieID, ratings by movieID;
    ```

11. Kalau kita ingin limit datanya, kita bisa menggunakan syntax ini
    ```
    limited = LIMIT joined 10;
    ```