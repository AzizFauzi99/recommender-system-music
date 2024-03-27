# Sistem Rekomendasi Musik berdasarkan Lirik menggunakan TF-IDF dan Cosine Similarity 
####  Created by - Aziz F. Fauzi

## 1. Project Overview
### Latar Belakang
Musik adalah bagian penting dalam kehidupan sehari-hari banyak orang. Dengan adanya berbagai layanan streaming musik, pengguna memiliki akses ke jutaan lagu dari berbagai genre. Namun, seringkali pengguna kesulitan dalam menemukan lagu-lagu baru yang sesuai dengan selera mereka [1]. Proyek ini bertujuan untuk memberikan solusi dengan memanfaatkan teks lirik lagu untuk merekomendasikan lagu-lagu yang mirip secara konten.
### Urgensi Permasalahan
Proyek ini penting karena dapat membantu pengguna menemukan lagu-lagu baru yang sesuai dengan selera mereka berdasarkan lirik lagu yang mereka sukai. Dengan demikian, proyek ini dapat meningkatkan pengalaman mendengarkan musik pengguna dan membantu mereka menemukan musik yang lebih bermakna bagi mereka.

## 2. Business Understanding
### Problem Statement
    1. Bagaimana mengembangkan sistem rekomendasi musik yang dapat memberikan rekomendasi lagu yang sesuai dengan preferensi musik pengguna?
    2. Bagaimana tingkat akurasi dan relevansi rekomendasi lagu yang diberikan kepada pengguna?
    3. Bagaimana tahapan dalam membuat rekomendasi musik berdasarkan lirik lagu?
### Goals
    1. Mengembangkan sistem rekomendasi musik yang dapat memberikan rekomendasi lagu yang sesuai dengan preferensi musik pengguna
    2. Mengetahui tingkat akurasi dan relevansi rekomendasi lagu yang diberikan kepada pengguna
    3. Mengethaui tahapan dalam membuat rekomendasi musik berdasarkan lirik lagu
### Manfaat/Impact
    1. Meningkatkan Penjualan atau Stream Musik: Dengan memperkenalkan lagu-lagu baru/lain kepada pengguna berdasarkan lirik, sistem ini dapat membantu meningkatkan penjualan atau stream musik bagi para artis atau label musik.
    2. Meningkatkan Retensi Pengguna: Dengan memberikan pengalaman yang memuaskan dalam menemukan lagu-lagu yang disukai, sistem ini dapat membantu meningkatkan retensi pengguna terhadap platform musik tersebut.
    3. Meningkatkan Pengalaman Pengguna: Dengan memberikan rekomendasi lagu yang sesuai dengan preferensi musik pengguna, sistem ini dapat meningkatkan pengalaman mendengarkan musik pengguna.
### Solutions Approach
1. Preprocessing
    - Case Folding: Merubah semua teks lirik lagu menjadi huruf kecil untuk menghindari perbedaan yang tidak diperlukan karena perbedaan besar-kecil huruf.
    - Stemming: Menggunakan stemming untuk mengubah kata-kata dalam lirik lagu menjadi bentuk dasarnya. Contoh: "running" menjadi kata "run".
    - Hapus Stopwords: Menghapus kata-kata yang umum dan tidak memberikan informasi tambahan (stopwords) dalam bahasa Inggris.
2. Modeling
    - TF-IDF (Term Frequency-Inverse Document Frequency): Menggunakan TF-IDF untuk menghitung bobot kata-kata dalam lirik lagu. TF-IDF memberikan bobot yang lebih tinggi untuk kata-kata yang jarang muncul namun penting dalam dokumen tertentu.
    - Cosine Similarity: Menggunakan cosine similarity untuk mengukur kemiripan antara lirik lagu yang disukai pengguna dengan lirik lagu lainnya. Cosine similarity menghitung kesamaan arah antara dua vektor, di mana vektor mewakili bobot kata-kata dalam lirik lagu.
3. Evaluasi
    - Mengukur tingkat relevansi dengan menggunakan metrik precision

## 3. Data Understanding
### Informasi Umum tentang Data
Dataset ini merupakan kumpulan data berisi informasi tentang lagu-lagu berbahasa Inggris. Dataset ini memiliki 57650 baris dan 4 kolom, yaitu:
- Artist: Nama artis atau penyanyi yang menyanyikan lagu.
- Song: Judul lagu.
- Link: Link atau URL yang mengarahkan ke informasi lebih lanjut tentang lagu.
- Text: Teks lirik dari lagu tersebut.

Dataset ini terbatas pada lagu-lagu berbahasa Inggris, sehingga cocok untuk digunakan dalam pembuatan sistem rekomendasi musik berdasarkan lirik menggunakan metode seperti TF-IDF dan cosine similarity. Dengan memanfaatkan dataset ini, kita dapat melakukan analisis teks pada lirik lagu untuk menghasilkan rekomendasi lagu yang lebih baik sesuai dengan preferensi pengguna.
### Sumber Data
[Dataset Lagu](https://github.com/GrayRobert/big-data-project/blob/master/src/main/resources/temp/data/songdata.csv)

### Exploratory Data Analysis
1. Info Data dan Cek Missing Value <br>

<div align="center">
Tabel 1. Info Data

| # 	| Column 	| Non-Null Count 	| Dtype  	|
|---	|--------	|----------------	|--------	|
| 0 	| artist 	| 57650 non-null 	| object 	|
| 1 	| song   	| 57650 non-null 	| object 	|
| 2 	| link   	| 57650 non-null 	| object 	|
| 3 	| text   	| 57650 non-null 	| object 	|

</div>

    - Semua kolom bertipe object dan tidak missing value dalam dataset ini
    
2. Berapa banyak artist yang ada dalam dataset? <br>
<div align="center">

![image](https://github.com/AzizFauzi99/recommender-system-music/assets/92005833/293f0118-2d71-44d8-a93d-8661354296e6) <br>

</div>
3. Visualisasi artis dengan lagu terbanyak (top 10) di dataset ini <br>

<div align="center">

Tabel 2. Artist dengan lagu terbanyak di dataset

| Artist           	| Total Lagu 	|
|------------------	|------------	|
| Donna Summer     	| 191        	|
| Gordon Lightfoot 	| 189        	|
| Bob Dylan        	| 188        	|
| George Strait    	| 188        	|
| Loretta Lynn     	| 187        	|
| Cher             	| 187        	|
| Alabama          	| 187        	|
| Reba Mcentire    	| 187        	|
| Chaka Khan       	| 186        	|
| Dean Martin      	| 186        	|


![image](https://github.com/AzizFauzi99/recommender-system-music/assets/92005833/701e456e-0ccf-484a-802a-6d47035a8a6c) <br>

</div>

4. Rata-rata jumlah kata dalam lirik <br>

<div align="center">

Tabel 3. Describe Data
    
| Metrik 	| Hasil        	|
|--------	|--------------	|
| count  	| 57650.000000 	|
| mean   	| 219.486262   	|
| std    	| 108.814619   	|
| min    	| 37.000000    	|
| 25%    	| 145.000000   	|
| 50%    	| 196.000000   	|
| 75%    	| 264.000000   	|
| max    	| 827.000000   	|

</div>

    - Diketahui, Rata-rata dalam 1 lagu terdapat 219 kata

## 4. Data Preparation
### Teknik yang Dilakukan
1. Menghapus "\n" dalam Kolom Text (Lirik): Langkah ini dilakukan untuk menghilangkan karakter newline yang tidak diperlukan dalam teks lirik lagu.
2. Case Folding: Merubah semua teks lirik lagu menjadi huruf kecil untuk menghindari perbedaan yang tidak diperlukan karena perbedaan besar-kecil huruf [1].
3. Stemming (Bahasa Inggris) dengan PorterStemmer: Menggunakan algoritma PorterStemmer untuk mengubah kata-kata dalam lirik lagu menjadi bentuk dasarnya. Misalnya, "running" akan menjadi "run" [1].
4. Menghapus Stopwords: Menghapus kata-kata yang umum dan tidak memberikan informasi tambahan (stopwords) dalam bahasa Inggris [1].
### Proses Data Preparation
1. Langkah pertama adalah menghapus karakter "\n" dari kolom teks lirik lagu.
2. Selanjutnya, dilakukan case folding untuk mengubah semua huruf menjadi huruf kecil.
3. Kemudian, dilakukan proses stemming dengan menggunakan algoritma PorterStemmer untuk mengubah kata-kata dalam lirik lagu menjadi bentuk dasarnya.
4. Terakhir, dilakukan penghapusan stopwords untuk membersihkan teks lirik lagu dari kata-kata yang umum dan tidak relevan.
### Alasan Data Preparation
1. Menghapus karakter "\n" dan mengubah huruf menjadi huruf kecil membuat teks lirik lagu menjadi lebih bersih dan mudah diproses.
2. Stemming membantu dalam mengurangi variasi kata-kata dalam teks lirik lagu, sehingga mempermudah dalam proses pencocokan kata-kata.
3. Penghapusan stopwords membantu menghilangkan kata-kata yang tidak memberikan informasi tambahan dalam analisis teks lirik lagu, sehingga meningkatkan kualitas rekomendasi lagu.

## 5. Modeling and Result
### Content-Based Filtering
![1_MnedC576EFf7dfeKmPBkiQ](https://github.com/AzizFauzi99/recommender-system-music/assets/92005833/1e6c0867-8123-4a00-a727-25f9830362ab)

Content-based filtering adalah salah satu teknik dalam sistem rekomendasi yang menggunakan informasi tentang item (konten) yang disukai oleh pengguna untuk melakukan rekomendasi item serupa.

Dalam konteks rekomendasi musik berdasarkan lirik lagu, content-based filtering akan menganalisis lirik lagu yang disukai oleh pengguna untuk mencari lagu-lagu lain yang memiliki kesamaan dalam konten (lirik) dengan lagu-lagu tersebut. Misalnya, jika pengguna menyukai lagu dengan lirik yang mengandung kata-kata seperti "love", "heartbreak", dan "romance", maka content-based filtering akan merekomendasikan lagu-lagu dengan lirik yang mirip.

### Pemilihan Content-Based Filtering untuk Rekomendasi Musik
- Dalam kasus sistem rekomendasi musik berdasarkan lirik lagu, alasan menggunakan content-based filtering adalah karena fokus pada kesamaan konten (lirik) dengan lagu-lagu yang disukai oleh pengguna. Berikut adalah beberapa alasan mengapa content-based filtering dipilih:
    1. Tidak Memerlukan Data Pengguna Lain: Content-based filtering tidak memerlukan informasi tentang pengguna lain atau preferensi mereka. Hal ini membuatnya cocok untuk digunakan dalam situasi di mana data pengguna terbatas atau sulit didapatkan.
    2. Rekomendasi yang Personalisasi: Dengan menganalisis lirik lagu yang disukai oleh pengguna, content-based filtering dapat memberikan rekomendasi yang lebih personalisasi sesuai dengan selera musik pengguna.
    3. Pemahaman yang Lebih Baik tentang Preferensi Pengguna: Dengan menganalisis konten lirik lagu, sistem dapat memahami lebih baik tentang preferensi pengguna dalam hal tema, emosi, atau pesan yang ingin disampaikan dalam lagu.

- Kelebihan dari content-based filtering antara lain:
    1. Tidak memerlukan data pengguna lain atau kolaborasi antar pengguna.
    2. Mampu memberikan rekomendasi yang sesuai dengan preferensi pengguna secara personal.
- Namun, content-based filtering juga memiliki beberapa kelemahan, seperti:
    1. Rentan terhadap kesenjangan informasi (information gap) karena hanya merekomendasikan item yang mirip dengan item yang sudah disukai pengguna.
    2. Kurang mampu memberikan rekomendasi yang mengeksplorasi atau mendekati preferensi baru pengguna karena hanya berfokus pada kesamaan dengan item yang sudah diketahui.

### TF-IDF (Term Frequency-Inverse Document Frequency)
- TF-IDF adalah metode yang digunakan untuk mengukur pentingnya kata dalam sebuah dokumen relatif terhadap koleksi dokumen.
- Pada tahap ini, kita menggunakan TfidfVectorizer dari scikit-learn untuk menghitung bobot TF-IDF dari setiap kata dalam lirik lagu.
- TfidfVectorizer akan mengubah teks (lirik lagu) menjadi matriks di mana setiap baris mewakili sebuah lagu dan setiap kolom mewakili kata dalam lirik lagu.
### Cosine Similarity
- Cosine similarity adalah metode untuk mengukur kesamaan antara dua vektor berdasarkan sudut kosinus antara vektor-vektor tersebut.
- Pada tahap ini, kita menggunakan cosine_similarity dari scikit-learn untuk menghitung similarity score antara setiap pasangan lagu berdasarkan bobot TF-IDF dari kata-kata dalam lirik lagu.
- Setiap elemen dalam matriks cosine similarity akan menunjukkan seberapa mirip dua lagu berdasarkan liriknya.
### Hasil setelah TF-IDF dan hitung Cosine Similarity
![image](https://github.com/AzizFauzi99/recommender-system-music/assets/92005833/a366759d-a00d-4b38-a4ce-9a476b3035f5)

### Result
Sebagai contoh, akan diinputkan judul lagu berikut:
<div align="center">

Tabel 4. Data Input
    
| Artist        	| Judul             	|
|---------------	|-------------------	|
| Justin Bieber 	| Christmas is Dead 	|

</div>

Dan keluar 5 rekomendasi teratas berdasarkan similarity score paling tinggi <br>

<div align="center">
    
Tabel 5. Data Output

| Artist             	| Judul                           	|
|--------------------	|---------------------------------	|
| Harry Connick, Jr. 	| Please Come Home for Christmas  	|
| Cyndi Lauper       	| Three Ships                     	|
| Glee               	| Do They Know It's Christmas     	|
| Christmas Songs    	| I Believe in Christmas          	|
| Demi Lovato        	| All I Want for Christmas Is You 	|

</div> 

Jika dilihat pada tabel hasil, model berhasil menghasilkan rekomendasi yang sesuai, yakni yang berkaitan dengan christmas

## 6. Evaluation
Untuk evaluasi, menggunakan metrik precision yang dirumuskan sebagai berikut: <br>

$$ x = \frac{\text{Jumlah Rekomendasi Relevan}}{\text{Jumlah Item yang Direkomendasikan}} $$

Keterangan:
- Jumlah rekomendasi relevan: Jumlah item yang direkomendasikan oleh sistem yang benar-benar disukai atau dibutuhkan oleh pengguna.
- Jumlah item yang direkomendasikan: Jumlah total item yang direkomendasikan oleh sistem kepada pengguna.

Berdasarkan hasil rekomendasi Musik "Christmas Is Dead" dari Justin Bieber di atas, dapat dihitung nilai precision (P) sebagai berikut:

$$ P = \frac{5}{5} = 1 $$

Ini berarti bahwa dari 5 item yang direkomendasikan, semua di antaranya relevan, sehingga presisi adalah 100%.

Dengan demikian, tujuan dari pengembangan sistem rekomendasi musik menggunakan content-based filtering telah berhasil tercapai dengan baik.

## Sumarry
1. Dalam proyek ini, berhasil dikembangkan sistem rekomendasi musik yang menggunakan metode content-based filtering berdasarkan lirik lagu. Sistem ini memanfaatkan teknik TF-IDF untuk menganalisis dan memahami makna dari lirik lagu. Dengan demikian, model dapat merekomendasikan lagu-lagu yang memiliki kesamaan dalam konten liriknya dengan lagu yang disukai oleh pengguna.
2. Dalam mengukur tingkat akurasi dan relevansi rekomendasi lagu yang diberikan kepada pengguna, digunakan metrik precision (P). Precision mengukur proporsi dari item yang direkomendasikan yang relevan bagi pengguna. Dalam contoh kasus "Christmas Is Dead" dari Justin Bieber, nilai precision yang dihitung adalah 100%, yang berarti semua lagu yang direkomendasikan relevan bagi pengguna.
3. Tahapan dalam membuat rekomendasi musik berdasarkan lirik lagu meliputi:

    - Preprocessing Data: Tahapan ini melibatkan menghapus karakter khusus, mengubah teks menjadi lowercase, dan melakukan proses stemming pada lirik lagu untuk menghasilkan kata-kata dasar.
    - Menggunakan TF-IDF: Teknik ini digunakan untuk menghitung bobot kata-kata dalam lirik lagu, di mana kata-kata yang jarang muncul tetapi muncul dalam beberapa lirik lagu dapat dianggap penting.
    - Menggunakan Cosine Similarity: Kami menggunakan cosine similarity untuk mengukur sejauh mana kemiripan antara lirik lagu yang satu dengan yang lainnya. Semakin tinggi nilai cosine similarity, semakin mirip kedua lirik lagu tersebut.
    - Rekomendasi Lagu: Berdasarkan nilai cosine similarity, kami dapat merekomendasikan lagu-lagu yang memiliki kemiripan lirik dengan lagu yang disukai oleh pengguna.

### Referensi
1. Ula, N., Setianingsih, C., & Nugrahaeni, R. A. (2021). Sistem Rekomendasi Lagu dengan Metode Content-based Filtering Berbasis Website. E-Proceeding of Engineering, 8(6), 12193–12199.
2. Paskalev, G. (2021, February 4). How to build a content-based song recommender. Medium. https://georgepaskalev.medium.com/how-to-build-a-content-based-song-recommender-4346edbfa5cf 
