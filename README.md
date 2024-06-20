# Rekomendasi Musik dengan Kemiripan Dokumen Berdasarkan lirik menggunakan TF-IDF dan Cosine Similarity


##  - Dataset -
Dataset dapat diunduh pada link berikut &#8594; [![kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019)

Dataset tersebut memiliki 31 kolom secara keseluruhan. Tetapi pada sistem rekomendasi ini hanya memerlukan beberapa kolom saja, antara lain: artist_name, track_name, dan lyrics

---

##  - Tujuan -
Tujuan dibuatnya sistem ini menggunakan dataset yang sudah disebutkan di atas adalah untuk memberikan pengalaman mendengarkan musik yang lebih personal dan sesuai dengan preferensi pengguna. Sistem ini menggunakan analisis teks untuk memahami makna dan emosi yang terkandung dalam lirik lagu, kemudian memadankan informasi tersebut dengan preferensi musik pengguna. Dengan demikian, sistem dapat meningkatkan kepuasan pengguna dan membantu mereka menemukan musik baru yang sesuai dengan selera mereka.

---

##  - Model dan tahapan -
- Data Collection :
  Pada tahapan ini dilakukan pencarian dataset yang cocok untuk menyelesaikan penelitian rekomendasi musik ini. Ditemukan dataset detail musik terkenal dari tahun 1950-2019.
- Preprocessing :
  Menyeleksi dataset dengan cara memilih atribut yang dibutuhkan pada penelitian dan mengabaikan atribut-atribut lain yang tidak digunakan. Normalisasi pada kolom "lyrics" (menyeragamkan menjadi lower, tokenisasi).
- Metode :
  - SKLearn digunakan untuk melakukan vektorisasi TF-IDF
  - SKLearn digunakan untuk menghitung similaritas (cosine similarity) berdasarkan matrix TF-IDF dari vektorisasi
  - Outputnya adalah 5 judul lagu yang memiliki lirik yang serupa dari input judul lagu yang dimasukkan pengguna
  
---

##  - Performa Uji -
Performa Uji dilakukan menggunakan K-Fold Cross-Validation yang sebelumnya penulis perlu membuat beberapa sampel rekomendasi pada judul game tertentu untuk mendapatkan hasil dari pengujian ini. Setelah dilakukan pengujian hasil Average Hit Ratio yang didapat: 0.224

---

##  - Deployment -
Sistem Rekomendasi Musik ini dapat dicoba pada link berikut &#8594; [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://widhibagoes-song-recommendation-app-1esqhr.streamlit.app/)
