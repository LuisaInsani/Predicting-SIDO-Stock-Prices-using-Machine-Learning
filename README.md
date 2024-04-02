# Prediksi Harga Saham SIDO menggunakan Machine Learning
Repository ini berisi kode dan sumber daya terkait dengan pengembangan model machine learning untuk memprediksi harga saham perusahaan SIDO. Dengan menggunakan data historis harga saham SIDO selama beberapa tahun terakhir, proyek ini bertujuan untuk mengembangkan model yang dapat memprediksi harga saham di masa depan dengan akurasi yang tinggi.

## Domain Proyek
Saham adalah tanda kepemilikan seseorang dalam suatu perusahaan atau perseroan terbatas. Harga saham menunjukkan besaran uang yang harus dikeluarkan oleh calon investor untuk memperoleh satu lembar saham emiten [[1](https://www.researchgate.net/publication/366715917_Pengaruh_Dividen_Terhadap_Harga_Saham_Pada_Bursa_Efek_Indonesia_Periode_Tahun_2018-2020)]. Investor membeli saham dengan harapan mendapatkan keuntungan dari harga saham dan/atau dividen yang dibayarkan oleh perusahaan.

Perusahaan Sidomuncul dengan kode saham SIDO merupakan produsen jamu terbesar dan termodern di Indonesia dengan pangsa pasar terbesar untuk kategori produk jamu tradisional [[2](https://investor.sidomuncul.co.id/id/home.html)]. Oleh karena itu, investasi dalam saham SIDO dapat dianggap sebagai partisipasi dalam pertumbuhan dan keberhasilan perusahaan Sidomuncul di industri jamu tradisional Indonesia. Dengan demikian, pergerakan harga saham SIDO juga mencerminkan kinerja dan prospek perusahaan Sidomuncul dalam pasar yang berkembang ini. Para investor mungkin tertarik untuk memantau dan berinvestasi dalam saham SIDO sebagai bagian dari strategi portofolio mereka dalam industri kesehatan dan produk konsumen di Indonesia. 

Machine learning akan digunakan untuk memprediksikan harga saham SIDO dengan menggunakan algoritma Long Short-Term Memory (LSTM). 

## Business Understanding
Pengembangan model prediksi harga saham memiliki potensi untuk memberikan manfaat dalam membantu pengambilan keputusan bagi para investor. Salah satu manfaat potensial dari prediksi harga saham yang akurat adalah membantu pembeli dan penjual dalam membuat keputusan lebih bijaksana terkait aksi jual atau beli.

### Problem Statements
- Berdasarkan eksplorasi dataset, fitur apa saja yang mempengaruhi prediksi harga saham SIDO?
- Bagaimana mengembangkan model machine learning yang dapat memprediksi harga penutupan saham SIDO berdasarkan data historis *open*, *low*, *high*, *volume*, *adj close*, dan *close*? 
- Bagaimana mengolah *dataset* agar dapat dibuat model prediksi harga saham SIDO?

### Goals
- Mengeksplorasi fitur yang tersedia pada *dataset* kemudian melihat korelasi dari fitur yang tersedia untuk melihat faktor apa yang paling mempengaruhi harga saham SIDO.
- Mengembangkan model machine learning yang dapat memprediksi harga penutupan saham SIDO dengan akurat berdasarkan data historis *open*, *low*, *high*, *volume*, *adj close*, dan *close*.
- Melakukan proses *data preparation* terhadap *dataset* agar dapat dibuat model predksi harga saham SIDO.

## Data Understanding
Data yang digunakan dalam pembuatan model merupakan data sekunder. Data diambil dari Yahoo! Finance dengan nama *dataset* adalah SIDO.JK. *dataset* yang digunakan adalah record harga saham PT Sidomuncul selama kurun waktu April 2019 – April 2024 (5 tahun).

URL: https://finance.yahoo.com/quote/SIDO.JK?.tsrc=fin-srch

-	*Dataset* berupa CSV.
-	*Dataset* terdiri atas 7308 *records* dengan 7 buah fitur yang diukur.
-	*Dataset* terdiri atas 7 data numerik.
-	*Dataset* memiliki missing value sejumlah 10 *records*.

# Variabel-variabel pada dataset:
-	_Date_: Date adalah tanggal perdagangan saham. Meskipun tidak langsung digunakan untuk memprediksi harga saham, tanggal bisa menjadi penting untuk menganalisis tren seiring waktu, musim, atau pola berulang dalam perilaku pasar.
-	_Open_: Harga pembukaan saham adalah harga perdagangan pertama pada suatu hari perdagangan. Ini memberikan informasi tentang bagaimana pasar bereaksi terhadap berita dan peristiwa ekonomi yang muncul sejak perdagangan terakhir.
-	_High_: Harga tertinggi yang dicapai selama hari perdagangan. Informasi ini penting karena mencerminkan tingkat kepercayaan dan minat pembeli yang kuat pada suatu saham.
-	_Low_: Harga terendah yang dicapai selama hari perdagangan. Ini mencerminkan tingkat kekhawatiran dan ketidakpastian di pasar.
-	_Adj Close_: Harga penutupan yang disesuaikan dengan faktor seperti dividen, pembagian saham, dan peristiwa korporat lainnya. Ini adalah harga penutupan yang paling penting untuk dianalisis karena mencerminkan nilai aktual dari saham pada akhir hari perdagangan.
-	_Volume_: Jumlah saham yang diperdagangkan selama hari perdagangan. Tingkat volume dapat memberikan petunjuk tentang seberapa aktifnya pasar dan seberapa besar minat investor dalam saham tersebut.
-	Close: Harga terakhir pada suatu hari perdagangan. Ini juga merupakan variabel penting dalam analisis teknikal karena mencerminkan harga yang diterima oleh investor pada akhir hari perdagangan.

