# Instalasi Pyspark di Google Collab

## Instalasi

### 1. Pastikan kalian mempunyai Google Account

### 2. Jalankan command di bawah ini untuk install pyspark di Google Collabnya

```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://downloads.apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
!tar xf spark-2.4.7-bin-hadoop2.7.tgz
!pip install -q findspark
```

### 3. Jalankan kodigan di bawah untuk mengatur path dari spark nya

```
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.7-bin-hadoop2.7"
```

### 4. Jalankan Kodingan ini untuk mengecek, apakah sudah benar-benar terinstall

```
import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
```
