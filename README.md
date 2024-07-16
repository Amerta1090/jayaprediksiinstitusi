# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan dengan reputasi yang baik, namun menghadapi tantangan serius terkait tingkat dropout yang tinggi di antara siswa-siswanya. Dropout tidak hanya mempengaruhi reputasi dan kualitas pendidikan institusi, tetapi juga potensi finansial dan keberlanjutan akademis siswa.

### Permasalahan Bisnis
- Tingkat Dropout Tinggi:
Dropout siswa menjadi isu utama yang mempengaruhi stabilitas akademis dan finansial institusi.

- Dampak Terhadap Reputasi:
Tingkat dropout yang tinggi dapat merusak reputasi institusi di mata masyarakat dan calon siswa.

- Potensi Kerugian Finansial:
Dropout dapat mengakibatkan kerugian pendapatan dari biaya pendidikan siswa yang keluar sebelum menyelesaikan program mereka.

- Kualitas Pendidikan yang Tidak Konsisten:
Tingkat dropout yang tinggi mengurangi efektivitas pengajaran dan pembelajaran di institusi.

- Kesempatan Belajar yang Terlewatkan:
Setiap siswa yang dropout kehilangan kesempatan untuk mengembangkan potensi mereka sepenuhnya.

### Cakupan Proyek
Analisis Data Historis:
- Melakukan analisis mendalam terhadap data historis mengenai tingkat dropout siswa.
- Mengidentifikasi pola-pola dan faktor-faktor yang berkaitan dengan siswa yang melakukan dropout.

Pengembangan Model Prediksi:
- Mengembangkan model prediksi menggunakan teknik machine learning untuk memprediksi kemungkinan siswa melakukan dropout.
- Model ini akan memanfaatkan data historis dan berbagai fitur terkait siswa seperti informasi pribadi, akademik, dan sosial.

Implementasi Dashboard Interaktif:
- Membangun dashboard interaktif menggunakan platform seperti Streamlit untuk visualisasi data dan hasil prediksi.
- Dashboard ini akan memberikan insight yang jelas kepada pengguna mengenai pola dropout dan faktor-faktor terkait.

Pengujian dan Validasi Model:
- Melakukan pengujian dan validasi model prediksi menggunakan data yang tidak terlihat (out-of-sample) untuk memastikan keandalan dan ketepatan prediksi.
- Memperbaiki dan meningkatkan model berdasarkan hasil pengujian.

### Persiapan
Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

*Setup Environment - Anaconda*
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

*Setup Environment - Shell/Terminal*
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

*Run steamlit app*
```
streamlit run dashboard.py
```
```
https://jayaprediksiinstitusi-nf6behprtsfmhuheubrjex.streamlit.app/
```


## Business Dashboard

Dashboard ini dikembangkan untuk Jaya Jaya Institut dengan tujuan utama untuk memprediksi kemungkinan siswa melakukan dropout berdasarkan berbagai faktor terkait. Berikut adalah beberapa fitur dan informasi penting terkait dashboard ini:

## Fitur Utama: Prediksi Dropout Mahasiswa

Dashboard ini dirancang untuk memprediksi kemungkinan siswa melakukan dropout berdasarkan berbagai fitur terkait. Berikut adalah beberapa fitur utama dan informasi penting terkait dashboard ini:

### Tujuan Utama

- **Mendeteksi Risiko Dropout**: Dashboard ini bertujuan untuk mendeteksi dini mahasiswa yang berpotensi melakukan dropout. Dengan pendekatan ini, Jaya Jaya Institut dapat memberikan bimbingan dan dukungan yang tepat waktu untuk meningkatkan retensi siswa.

### Cara Menggunakan

1. **Masukkan Data Mahasiswa**: Pengguna diminta untuk memasukkan beberapa fitur terkait mahasiswa pada formulir yang disediakan.
   
2. **Prediksi Dropout**: Model machine learning akan memproses input pengguna dan memberikan prediksi apakah seorang mahasiswa berisiko dropout atau tidak.
   
3. **Interpretasi Hasil**: Hasil prediksi berupa status "Ya" atau "Tidak" dropout ditampilkan, serta probabilitas masing-masing prediksi.

### Fitur-Fitur Input

Dashboard ini memungkinkan pengguna untuk memasukkan informasi berikut:

- **Mode Aplikasi**: Cara mahasiswa mendaftar ke institusi (misalnya, Online, Kertas, dll.).
- **Status Debitur**: Apakah mahasiswa adalah debitur atau bukan.
- **Status Pembayaran SPP**: Apakah pembayaran SPP mahasiswa sudah terbayar atau belum.
- **Jenis Kelamin**: Jenis kelamin mahasiswa (Laki-laki atau Perempuan).
- **Penerima Beasiswa**: Apakah mahasiswa menerima beasiswa atau tidak.
- **Usia saat Pendaftaran**: Usia mahasiswa ketika pertama kali mendaftar.
- **SKS Semester 1 yang Diakui**: Jumlah SKS yang diakui pada semester pertama.
- **Evaluasi Semester 1**: Evaluasi akademik pada semester pertama.
- **SKS Semester 1 yang Lulus**: Jumlah SKS yang berhasil diselesaikan pada semester pertama.
- **Nilai Semester 1**: Nilai rata-rata yang dicapai pada semester pertama.
- **SKS Semester 2 yang Diambil**: Jumlah SKS yang diambil pada semester kedua.
- **Evaluasi Semester 2**: Evaluasi akademik pada semester kedua.
- **SKS Semester 2 yang Lulus**: Jumlah SKS yang berhasil diselesaikan pada semester kedua.
- **Nilai Semester 2**: Nilai rata-rata yang dicapai pada semester kedua.

Pengguna dapat memilih atau menggeser nilai-nilai ini pada dashboard untuk melihat bagaimana nilai-nilai ini mempengaruhi prediksi dropout.

### Teknologi yang Digunakan

Dashboard ini dikembangkan menggunakan Streamlit, Python, dan berbagai pustaka seperti Pandas, Scikit-learn, serta Matplotlib dan Seaborn untuk visualisasi data. Model machine learning untuk prediksi dropout telah di-training menggunakan data historis dari Jaya Jaya Institut.

### Langkah-langkah Penggunaan

1. **Akses Dashboard**: Kunjungi https://jayaprediksiinstitusi-nf6behprtsfmhuheubrjex.streamlit.app/

2. **Masukkan Data Mahasiswa**: Isi formulir dengan informasi yang relevan terkait mahasiswa.

3. **Lihat Hasil Prediksi**: Dashboard akan menampilkan prediksi apakah mahasiswa tersebut berisiko dropout beserta probabilitas prediksinya.

### Menjalankan Prototype Sistem Machine Learning

Prototype sistem machine learning untuk prediksi dropout siswa di Jaya Jaya Institut dapat diakses dan dijalankan melalui platform Streamlit. Berikut langkah-langkah untuk menjalankannya:

1. **Akses Prototype:**
   - Kunjungi [Jaya Jaya Prediction Dashboard] (https://jayaprediksiinstitusi-nf6behprtsfmhuheubrjex.streamlit.app/).
   
2. **Langkah-langkah Penggunaan:**
- Isilah formulir dengan data mahasiswa yang ingin Anda prediksi.
- Lihatlah hasil prediksi yang ditampilkan oleh aplikasi, termasuk prediksi "Ya" atau "Tidak" serta probabilitas prediksi dropout.
Menguji dan Memvalidasi
- Gunakan aplikasi untuk memasukkan berbagai kombinasi data dan periksa apakah hasil prediksi masuk akal berdasarkan pengetahuan Anda tentang data dan domain masalah.

3. **Teknologi yang Digunakan:**
   - Prototype menggunakan teknologi Streamlit untuk membangun tampilan interaktif dan menampilkan hasil prediksi secara real-time.
   - Python digunakan untuk pemrosesan data, pengembangan model machine learning menggunakan pustaka seperti Scikit-learn, dan integrasi dengan visualisasi menggunakan Matplotlib dan Seaborn.

## Conclusion

### Karakteristik Umum Siswa yang Keluar dan Lulus

Berdasarkan analisis yang dilakukan menggunakan model machine learning, terdapat beberapa perbedaan karakteristik antara siswa yang keluar (dropout) dan siswa yang lulus di Jaya Jaya Institut. Berikut adalah beberapa temuan utama:

- **Mode Aplikasi**: Siswa yang cenderung dropout lebih sering mendaftar melalui agen pendaftaran atau pusat layanan pelanggan, sementara siswa yang lulus cenderung mendaftar secara langsung ke kampus atau melalui aplikasi mobile.
- **Status Debitur**: Siswa yang menjadi debitur cenderung memiliki risiko lebih tinggi untuk dropout.
- **Status Pembayaran SPP**: Siswa yang tidak membayar SPP tepat waktu memiliki kemungkinan dropout yang lebih tinggi.
- **Jenis Kelamin**: Tidak ada perbedaan signifikan dalam prediksi dropout berdasarkan jenis kelamin.
- **Penerima Beasiswa**: Siswa yang menerima beasiswa memiliki risiko dropout yang lebih rendah.
- **Usia saat Pendaftaran**: Tidak ada tren yang jelas terkait usia saat pendaftaran terhadap kemungkinan dropout.
- **Prestasi Akademik Semester Pertama**: Evaluasi rendah dan SKS yang tidak diakui pada semester pertama meningkatkan risiko dropout.
- **Prestasi Akademik Semester Kedua**: Hasil yang buruk pada semester kedua juga merupakan indikator potensial untuk dropout.

### Rekomendasi Action Items

Berdasarkan temuan di atas, berikut adalah beberapa rekomendasi tindakan yang dapat diambil untuk mengurangi tingkat dropout di Jaya Jaya Institut:

1. **Perbaiki Proses Pendaftaran**: Fokuskan untuk meningkatkan pendaftaran langsung ke kampus atau melalui aplikasi mobile, karena ini terkait dengan tingkat kelulusan yang lebih tinggi.
   
2. **Manajemen Keuangan Mahasiswa**: Sediakan dukungan lebih lanjut kepada mahasiswa yang mengalami kesulitan finansial, terutama dalam hal pembayaran SPP tepat waktu.

3. **Pemantauan dan Dukungan Akademik**: Tingkatkan sistem pemantauan dan dukungan untuk mahasiswa dengan kinerja akademik yang buruk, terutama pada semester pertama dan kedua.

4. **Program Beasiswa**: Perluas program beasiswa atau bantuan keuangan untuk merangsang motivasi akademik dan meminimalkan risiko dropout.

5. **Edukasi dan Kesadaran**: Lakukan edukasi dan meningkatkan kesadaran di antara mahasiswa tentang pentingnya kedisiplinan akademik dan pengaruhnya terhadap kelulusan.

Dengan mengimplementasikan rekomendasi ini, diharapkan Jaya Jaya Institut dapat memperbaiki tingkat kelulusan siswa dan mengurangi tingkat dropout secara signifikan.