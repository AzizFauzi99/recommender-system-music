# Sistem Rekomendasi Musik berdasarkan Lirik menggunakan TF-IDF dan Cosine Similarity 
####  Created by - Aziz F. Fauzi

## 1. Project Overview
### Latar Belakang
Musik adalah bagian penting dalam kehidupan sehari-hari banyak orang. Dengan adanya berbagai layanan streaming musik, pengguna memiliki akses ke jutaan lagu dari berbagai genre. Namun, seringkali pengguna kesulitan dalam menemukan lagu-lagu baru yang sesuai dengan selera mereka. Proyek ini bertujuan untuk memberikan solusi dengan memanfaatkan teks lirik lagu untuk merekomendasikan lagu-lagu yang mirip secara konten.
### Urgensi Permasalahan
Proyek ini penting karena dapat membantu pengguna menemukan lagu-lagu baru yang sesuai dengan selera mereka berdasarkan lirik lagu yang mereka sukai. Dengan demikian, proyek ini dapat meningkatkan pengalaman mendengarkan musik pengguna dan membantu mereka menemukan musik yang lebih bermakna bagi mereka.
### Referensi Riset
[Sistem Rekomendasi lagu dengan metode Content-Based Filtering berbasis Website](https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/article/view/17229/16940) 
[How to Build a Content-Based Song Recommender](https://georgepaskalev.medium.com/how-to-build-a-content-based-song-recommender-4346edbfa5cf)

## 2. Business Understanding
### Problem Statement
Pengguna layanan streaming musik sering kesulitan menemukan lagu-lagu baru yang sesuai dengan selera mereka berdasarkan lirik lagu yang mereka sukai.
### Goals
Membangun sistem rekomendasi musik berdasarkan lirik lagu yang dapat merekomendasikan lagu-lagu lain yang sesuai dengan selera pengguna.
### Solutions Approach
1. Preprocessing
    - Case Folding: Merubah semua teks lirik lagu menjadi huruf kecil untuk menghindari perbedaan yang tidak diperlukan karena perbedaan besar-kecil huruf.
    - Stemming: Menggunakan stemming untuk mengubah kata-kata dalam lirik lagu menjadi bentuk dasarnya. Contoh: "running" menjadi kata "run".
    - Hapus Stopwords: Menghapus kata-kata yang umum dan tidak memberikan informasi tambahan (stopwords) dalam bahasa Inggris.
2. Modeling
    - TF-IDF (Term Frequency-Inverse Document Frequency): Menggunakan TF-IDF untuk menghitung bobot kata-kata dalam lirik lagu. TF-IDF memberikan bobot yang lebih tinggi untuk kata-kata yang jarang muncul namun penting dalam dokumen tertentu.
    - Cosine Similarity: Menggunakan cosine similarity untuk mengukur kemiripan antara lirik lagu yang disukai pengguna dengan lirik lagu lainnya. Cosine similarity menghitung kesamaan arah antara dua vektor, di mana vektor mewakili bobot kata-kata dalam lirik lagu.

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
1. Info Data dan Cek Missing Value
2. Berapa banyak artist yang ada dalam dataset?
3. Visualisasi artis dengan lagu terbanyak (top 10) di dataset ini
4. Rata-rata jumlah kata dalam lirik

## 4. Data Preparation
### Teknik yang Dilakukan
1. Menghapus "\n" dalam Kolom Text (Lirik): Langkah ini dilakukan untuk menghilangkan karakter newline yang tidak diperlukan dalam teks lirik lagu.
2. Case Folding: Merubah semua teks lirik lagu menjadi huruf kecil untuk menghindari perbedaan yang tidak diperlukan karena perbedaan besar-kecil huruf.
3. Stemming (Bahasa Inggris) dengan PorterStemmer: Menggunakan algoritma PorterStemmer untuk mengubah kata-kata dalam lirik lagu menjadi bentuk dasarnya. Misalnya, "running" akan menjadi "run".
4. Menghapus Stopwords: Menghapus kata-kata yang umum dan tidak memberikan informasi tambahan (stopwords) dalam bahasa Inggris.
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
![image](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftowardsdatascience.com%2Fthe-abc-of-building-a-music-recommender-system-part-i-230e99da9cad&psig=AOvVaw1djpv-LgY5L3rWAu40bivf&ust=1711565554685000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCODms9nMkoUDFQAAAAAdAAAAABAE)
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

### Result

## 6. Evaluation
Untuk evaluasi, menggunakan metrik precision yang dirumuskan sebagai berikut:
<b> Precision = (Jumlah Rekomendasi Relevan) / (Jumlah Item yang Direkomendasikan)

Keterangan:
- Jumlah rekomendasi yang relevan: Jumlah item yang direkomendasikan oleh sistem yang benar-benar disukai atau dibutuhkan oleh pengguna.
- Jumlah item yang direkomendasikan: Jumlah total item yang direkomendasikan oleh sistem kepada pengguna.

Berdasarkan hasil rekomendasi Musik "Christmas Is Dead" dari Justin Bieber di atas, dapat dihitung nilai precision (P) sebagai berikut:

P = 5/5 = 1

Ini berarti bahwa dari 5 item yang direkomendasikan, semua di antaranya relevan, sehingga presisi adalah 100%.

Dengan demikian, tujuan dari pengembangan sistem rekomendasi musik menggunakan content-based filtering telah berhasil tercapai dengan baik.

