GPS Tracker Application
Deskripsi

Aplikasi GPS Tracker adalah solusi berbasis perangkat keras dan lunak untuk melacak lokasi secara real-time. Sistem ini dirancang untuk memantau kapal berukuran kecil yang terdaftar di aplikasi "e-pass kecil" menggunakan modul GPS yang terhubung ke perangkat Anda. Data lokasi dikirimkan ke server melalui jaringan lora-wan dan dapat diakses melalui aplikasi web atau seluler.
Fitur Utama

    Pelacakan Real-Time: Memantau lokasi objek secara langsung melalui peta interaktif.
    Riwayat Perjalanan: Menyimpan dan menampilkan data rute perjalanan sebelumnya.
    Geofencing: Memberikan notifikasi saat objek keluar atau masuk ke area yang ditentukan.
    Notifikasi: Pemberitahuan instan melalui SMS, email, atau aplikasi saat ada peringatan.
    Laporan Lengkap: Menyediakan laporan berbasis waktu terkait lokasi dan aktivitas.

Komponen

    Perangkat Keras
        Modul GPS NEO-8M
        Modul Lora-Wan SX1206
        Mikrokontroler ESP32C
        Power supply, Solar Panel dan baterai cadangan

    Perangkat Lunak
        Aplikasi untuk pengolahan data GPS dan pengiriman data ke server
        Backend server untuk menyimpan data lokasi
        Frontend web atau aplikasi seluler untuk antarmuka pengguna

Cara Kerja

    Perangkat Keras menangkap data lokasi dari satelit GPS.
    Modul Lora=Wan mengirimkan data ke server melalui jaringan Lora.
    Server Backend menerima, menyimpan, dan mengolah data lokasi.
    Aplikasi Frontend menampilkan data lokasi secara real-time kepada pengguna.

Instalasi
Frontend

    Clone repositori ini:

git clone https://github.com/yanyan-handayani/gps-tracker.git  

Instal dependensi:

cd gps-tracker/  
buat virtual environtment
    python3 -m venv env
    source env/bin/activate

    pip install -c requirement.txt

Install database:
    Database yang digunakan adalah postgresql v16 dengan ektensi postgis
    python3 manage.py migrate 
    python3 manage.py createsuperuser

Jalankan server:
    python3 manage.py runserver  


Perangkat Keras

    Rakit perangkat sesuai skema wiring pada Dokumentasi.
    Unggah kode sumber ke mikrokontroler menggunakan Arduino IDE atau platform yang relevan.

Penggunaan

    Buka aplikasi frontend atau web.
    Login menggunakan akun yang telah terdaftar.
    Lihat lokasi perangkat GPS pada peta.
    Atur fitur seperti geofencing atau laporan sesuai kebutuhan.

Kontribusi

Kontribusi sangat kami apresiasi! Silakan buat pull request atau ajukan issue jika menemukan bug atau memiliki ide untuk pengembangan.
Lisensi

Aplikasi ini dilisensikan di bawah MIT License.