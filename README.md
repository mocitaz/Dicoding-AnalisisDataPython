# 🚲 Dashboard Analisis Penyewaan Sepeda

## 📧 Informasi Kontak
- **Nama**: mocitaz
- **Email**: luthfafiwork@gmail.com

## 📊 Pendahuluan
Dashboard ini memungkinkan analisis data penyewaan sepeda berdasarkan variabel cuaca dan waktu. Analisis ini bertujuan untuk mengidentifikasi pola utama yang memengaruhi jumlah penyewaan sepeda, dengan menyoroti dampak suhu, kelembapan, kecepatan angin, serta tren musiman dan harian. Selain itu, dashboard ini menggunakan teknik klastering K-Means untuk mengelompokkan penyewaan sepeda berdasarkan suhu dan jumlah penyewaan.

### Dataset yang Digunakan:
- **Dataset Harian (day.csv)**: Berisi data penyewaan sepeda harian, termasuk variabel terkait cuaca dan waktu.
- **Dataset Per Jam (hour.csv)**: Berisi data penyewaan sepeda per jam, memberikan tingkat granularitas waktu yang lebih tinggi serta variabel cuaca per jam.

Tujuan utama proyek ini adalah memahami bagaimana faktor cuaca seperti suhu, kelembapan, dan kecepatan angin memengaruhi penyewaan sepeda serta mengeksplorasi tren penyewaan berdasarkan waktu (bulanan dan harian).

## 🎯 Tujuan Proyek
1. **Menilai Hubungan Cuaca dan Penyewaan Sepeda**: Menganalisis pengaruh suhu, kelembapan, dan kecepatan angin terhadap jumlah penyewaan sepeda.
2. **Tren Penyewaan Sepeda Berdasarkan Waktu**: Menyajikan tren penyewaan sepeda berdasarkan bulan dan hari dalam seminggu.
3. **Klastering Penyewaan Sepeda**: Menggunakan klastering K-Means untuk mengidentifikasi pola dalam data penyewaan sepeda berdasarkan suhu dan jumlah penyewaan.

## 🔧 Persyaratan Sistem
- **Python**: Versi 3.7 atau lebih tinggi
- **Pustaka**: Streamlit, Pandas, Seaborn, Matplotlib, scikit-learn

### Penyiapan Lingkungan dengan virtualenv di macOS
1. **Membuat Lingkungan Virtual**:
   Buka terminal di macOS dan jalankan:
   ```bash
   python3 -m venv bike-sharing-analysis
   ```
2. **Mengaktifkan Lingkungan**:
   ```bash
   source bike-sharing-analysis/bin/activate
   ```
3. **Menginstal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

### Alternatif: Penyiapan Lingkungan dengan pipenv
1. **Membuat Folder Proyek dan Masuk**:
   ```bash
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   ```
2. **Menginstal pipenv dan Membuat Lingkungan Virtual**:
   ```bash
   pipenv install
   pipenv shell
   ```
3. **Menginstal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

## 📥 Instalasi dan Menjalankan Dashboard
1. **Menyiapkan Data**:
   Pastikan file `day.csv` dan `hour.csv` diletakkan di folder `data/` dalam direktori proyek.
2. **Menjalankan Dashboard**:
   Setelah dependensi terinstal dan data tersedia, jalankan aplikasi dengan:
   ```bash
   streamlit run dashboard.py
   ```
   *Catatan*: Ganti `dashboard.py` dengan nama file aplikasi utama jika berbeda.

## 🖥️ Fitur Dashboard
- **Distribusi Cuaca**: Visualisasi distribusi suhu, kelembapan, dan kecepatan angin.
- **Tren Penyewaan**: Menampilkan tren penyewaan sepeda per bulan dan per hari dalam seminggu untuk menggambarkan pola musiman dan harian.
- **Klastering**: Mengelompokkan penyewaan sepeda berdasarkan suhu dan jumlah penyewaan menggunakan K-Means untuk memahami pola permintaan.
- **Fitur Interaktif**:
  - **Filter Berdasarkan Tanggal**: Memungkinkan pengguna untuk memilih rentang tanggal yang diinginkan untuk analisis.
  - **Filter Berdasarkan Musim**: Pengguna dapat memilih musim (musim panas, gugur, dingin, atau semi) untuk memfokuskan analisis pada periode tertentu.
  - **Filter Berdasarkan Cuaca**: Memungkinkan pengguna untuk memilih jenis cuaca (cerah, hujan, berawan, dll.) dan melihat bagaimana cuaca memengaruhi penyewaan sepeda.
  - **Filter Berdasarkan Waktu (Bulanan/Harian)**: Pengguna dapat memilih untuk melihat tren penyewaan sepeda berdasarkan bulan atau hari dalam seminggu.

## 📝 Kesimpulan dan Rekomendasi
### Temuan Utama:
- **Suhu**: Terdapat korelasi kuat antara suhu dan penyewaan sepeda. Suhu yang lebih tinggi meningkatkan jumlah penyewaan, dengan tren yang jelas pada bulan-bulan musim panas.
- **Kelembapan dan Kecepatan Angin**: Faktor-faktor ini menunjukkan korelasi yang lebih lemah terhadap penyewaan sepeda, tetapi tetap memengaruhi variabilitas permintaan.
- **Tren Musiman**: Penyewaan sepeda meningkat signifikan pada bulan-bulan musim panas, terutama Juni, Juli, dan Agustus.
- **Tren Harian**: Akhir pekan (Sabtu dan Minggu) menunjukkan permintaan yang lebih tinggi dibandingkan hari kerja, menandakan pengguna lebih aktif di akhir pekan.

### Rekomendasi:
- **Penambahan Armada di Musim Panas**: Mengingat hubungan positif antara suhu dan permintaan, tingkatkan ketersediaan sepeda pada musim panas untuk memenuhi permintaan yang lebih tinggi.
- **Promosi Akhir Pekan**: Terapkan program promosi atau diskon pada akhir pekan untuk meningkatkan penyewaan sepeda selama hari libur.
- **Distribusi Sepeda yang Efisien**: Berdasarkan hasil klastering, optimalkan distribusi sepeda dengan menyesuaikan ketersediaan berdasarkan suhu di berbagai wilayah.

## 🔗 URL Streamlit Cloud
[https://ouapjjt5hpqhxxqjpoxcty.streamlit.app/](https://ouapjjt5hpqhxxqjpoxcty.streamlit.app/)

## 📌 Catatan
- Pastikan semua paket yang tercantum dalam `requirements.txt` telah terinstal untuk menjalankan aplikasi dengan lancar.
- Visualisasi dan analisis dapat disesuaikan berdasarkan kebutuhan analitik lebih lanjut atau eksplorasi data tambahan.
- **Fitur Interaktif**: Dashboard ini telah dilengkapi dengan fitur interaktif seperti filter berdasarkan tanggal, musim, cuaca, dan waktu untuk memungkinkan eksplorasi data secara langsung.
