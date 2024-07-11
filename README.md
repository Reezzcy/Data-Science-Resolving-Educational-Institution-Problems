# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga mahasiswa yang tidak menyelesaikan pendidikannya alias dropout.

### Permasalahan Bisnis
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Tingkat dropout mahasiswa yang tinggi di Jaya Jaya Institut mengancam kualitas pendidikan dan keberlanjutan institusi. Fenomena ini tidak hanya mempengaruhi individu yang dropout, tetapi juga memiliki dampak luas pada kualitas pendidikan, reputasi institusi, serta aspek finansial dan operasional institusi. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin mahasiswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. 

### Cakupan Proyek
Proyek ini bertujuan untuk mendeteksi mahasiswa yang berisiko tinggi untuk dropout sedini mungkin dan memberikan intervensi yang tepat untuk membantu mereka menyelesaikan pendidikan mereka di Jaya Jaya Institut. Hasil akhirnya adalah dashboard visualisasi untuk memonitor performa mahasiswa dan prototype untuk memprediksi apakah mahasiswa akan berpotensi dropout.

### Persiapan

Sumber data: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

Setup environment:

1. Install pipenv
```
pip install pipenv
```

2. Create an environment 
```
pipenv install
```

3. Install dependencies
```
pipenv install -r requirements.txt
```

Menjalankan Dashboard:

1. Make sure Docker is installed, then run metabase.db.mv.db

2. Open a browser and run localhost:3000/setup

3. Enter email: xxxzuppasoupxxx@gmail.com password: 45464748

## Business Dashboard
Dashboard bisnis dibuat menggunkan Metabase, dashboard berisi metrik dari rata rata setiap nilai dari transkrip nilai mahasiswa pada semester 1&2. Selanjutnya pada bagian diagram, ada piechart yang menunjukan persentase kursus yang diambil oleh mahasiswa. Chart kedua berisi perbandingan jumlah mahasiswa yang mengambil kelas siang atau malam. Ketiga ada rata rata dari nilai kualifikasi sebelum masuk (PreviousQualificationGrade). Keempat ada barchart untuk tingkat pendidikan sebelum masuk (PreviousQualification). Kelima ada barchart untuk jumlah gender dari mahasiswa. Keenam ada piechart perbandingan dari mahasiswa internasional dan lokal. Terakhir ada barchart untuk melihat kewarganegaraan asal mahasiswa.

## Menjalankan Sistem Machine Learning
Prototype dapat dijalankan melalui terminal cmd/powershell melalui directory proyek.

Menjalankan Prototype:

1. Menjalankan secara lokal
```
streamlit run app.py
```
2. Akses melalui deploy streamlit
```
https://data-science-solving-educational-institution-problems.streamlit.app/
```

## Conclusion

Jika membandingkan dashboard yang menampilkan seluruh target dan target yang dropout, terdapat dua tanda utama yang menunjukkan mahasiswa yang berpotensi mengalami dropout. Pertama, penurunan nilai akademik secara signifikan. Mahasiswa yang mengalami dropout menunjukkan penurunan nilai yang jauh lebih rendah dibandingkan dengan mereka yang tidak dropout. Hal ini mengindikasikan bahwa mahasiswa tersebut mungkin mengalami kesulitan dalam mengikuti kurikulum atau memahami materi yang diajarkan. Kedua, faktor gender juga memainkan peran penting dalam tingkat dropout. Data menunjukkan bahwa mahasiswa laki-laki memiliki tingkat dropout yang lebih tinggi dibandingkan dengan mahasiswa perempuan.

Karakteristik Mahasiswa Mengalami Dropout:
- Mahasiswa memiliki rata rata nilai akademik yang rendah.
- Mahasiswa laki laki cenderung lebih sering mengalami dropout.

### Rekomendasi Action Items

- Mahasiswa mungkin mengalami kesulitan dalam mengikuti kurikulum atau memahami materi yang diajarkan. Untuk mengatasi masalah ini, institusi dapat mengimplementasikan program bimbingan akademik khusus serta sistem pemantauan nilai secara real-time untuk mendeteksi penurunan kinerja akademik lebih awal.
- Melakukan identifikasi alasan mengapa mahasiswa laki laki lebih sering mengalami dropout, indentifikasi dapat dilakukan melalui wawancara atau survey pada mahasiswa laki laki untuk memastikan apakah ada alasan khusus mahasiswa terkena dropout. Selanjutnya untuk mengatasi masalah tersebut lakukan diskusi bersama untuk memahami dan mamperbaiki masalah tersebut.
