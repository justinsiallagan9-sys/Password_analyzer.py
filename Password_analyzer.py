import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Media Pembelajaran Perangkat Keras", layout="centered", page_icon="💻")

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🖥️ Menu Navigasi")
    menu = st.radio("Pilih Halaman:", 
                    ["1. Beranda", 
                     "2. Materi Komputer", 
                     "3. Latihan Evaluasi"])
    st.divider()
    st.info("Media Pembelajaran Interaktif berbasis Website - Informatika SMK")

# ==========================================
# HALAMAN 1: BERANDA
# ==========================================
if menu == "1. Beranda":
    st.title("Selamat Datang di Portal Informatika! 🚀")
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_column_width=True)
    
    st.markdown("""
    ### Belajar Perangkat Keras Komputer (Hardware)
    Website ini dikembangkan sebagai media pembelajaran interaktif untuk membantu Anda memahami dasar-dasar perangkat keras komputer. 
    
    **Apa yang akan Anda dapatkan di sini?**
    * 📖 **Materi Terstruktur:** Penjelasan ringkas dan mudah dipahami mengenai konsep dasar komputer dan komponen-komponennya.
    * 📝 **Latihan Interaktif:** Uji pemahaman Anda melalui 10 soal pilihan berganda.
    * 💡 **Umpan Balik Langsung:** Anda tidak hanya mengetahui apakah jawaban Anda benar atau salah, tetapi juga akan mendapatkan penjelasan (feedback) langsung mengenai alasan di baliknya.
    
    👈 *Silakan klik menu **2. Materi Komputer** pada panel di sebelah kiri untuk mulai belajar!*
    """)

# ==========================================
# HALAMAN 2: MATERI PEMBELAJARAN
# ==========================================
elif menu == "2. Materi Komputer":
    st.title("Materi: Pengenalan Komputer & Komponennya 📖")
    
    st.header("1. Apa Itu Komputer?")
    st.write("""
    Secara sederhana, **Komputer** adalah perangkat elektronik yang dapat menerima data masukan (Input), memproses data tersebut (Process), dan menghasilkan informasi berupa keluaran (Output), serta dapat menyimpan data (Storage). 
    Siklus dasar komputer selalu berputar pada: **Input ➡️ Proses ➡️ Output**.
    """)
    
    st.divider()
    
    st.header("2. Tiga Elemen Utama Sistem Komputer")
    st.write("Agar komputer dapat menyala dan digunakan, ia membutuhkan 3 elemen yang tidak bisa dipisahkan:")
    
    # Elemen 1: Hardware
    with st.expander("🖥️ 1. Hardware (Perangkat Keras) - Klik untuk detail", expanded=True):
        st.write("Komponen fisik komputer yang bisa dilihat dan diraba. Dibagi menjadi 4 bagian:")
        st.markdown("""
        * **Input Device (Perangkat Masukan):** Alat untuk memasukkan data ke komputer. 
          * *Contoh:* Keyboard, Mouse, Microphone, Scanner.
        * **Processing Device (Perangkat Pemroses):** Otak komputer yang mengolah data.
          * *CPU (Processor):* Mengeksekusi semua perintah.
          * *RAM (Random Access Memory):* Penyimpanan sementara yang sangat cepat. Data di RAM akan hilang jika komputer dimatikan.
        * **Output Device (Perangkat Keluaran):** Menampilkan hasil pemrosesan data.
          * *Contoh:* Monitor (visual), Printer (cetak kertas), Speaker (suara).
        * **Storage Device (Perangkat Penyimpanan):** Menyimpan data secara permanen.
          * *Contoh:* Hardisk (HDD), SSD, Flashdisk. (SSD jauh lebih cepat daripada HDD).
        """)
        
    # Elemen 2: Software
    with st.expander("💿 2. Software (Perangkat Lunak)"):
        st.write("""
        Program atau aplikasi tidak berwujud fisik yang memberikan instruksi kepada *hardware* agar bisa bekerja.
        * *Contoh Sistem Operasi:* Windows, macOS, Linux, Android.
        * *Contoh Aplikasi:* Microsoft Word, Google Chrome, Game.
        """)

    # Elemen 3: Brainware
    with st.expander("👤 3. Brainware (Pengguna)"):
        st.write("""
        Manusia yang mengoperasikan, menggunakan, atau mengendalikan komputer. Tanpa manusia, komputer hanyalah mesin mati.
        * *Contoh:* Programmer, Teknisi, Operator (Anda sendiri).
        """)

# ==========================================
# HALAMAN 3: LATIHAN SOAL & FEEDBACK
# ==========================================
elif menu == "3. Latihan Evaluasi":
    st.title("Latihan Pilihan Berganda 📝")
    st.write("Kerjakan 10 soal di bawah ini. Sistem akan langsung memberikan penjelasan (feedback) saat Anda memilih jawaban.")
    st.divider()

    # Dictionary Soal untuk efisiensi kode
    soal_latihan = [
        {
            "id": 1,
            "pertanyaan": "Secara definisi, apa yang dimaksud dengan komputer?",
            "opsi": ["Mesin ketik modern yang canggih", "Perangkat elektronik yang menerima input, memproses data, dan menghasilkan output", "Alat penyimpanan data berkapasitas besar", "Perangkat lunak untuk membuat dokumen"],
            "jawaban_benar": "Perangkat elektronik yang menerima input, memproses data, dan menghasilkan output",
            "alasan_benar": "Tepat sekali. Esensi dari komputer adalah kemampuannya menjalankan siklus Input, Proses, dan Output.",
            "alasan_salah": "Kurang tepat. Komputer tidak hanya sekadar menyimpan data atau mesin ketik, melainkan memiliki siklus pemrosesan data (Input -> Proses -> Output)."
        },
        {
            "id": 2,
            "pertanyaan": "Komponen fisik pada komputer yang dapat dilihat dan diraba secara langsung disebut...",
            "opsi": ["Software", "Brainware", "Hardware", "Malware"],
            "jawaban_benar": "Hardware",
            "alasan_benar": "Benar! 'Hard' berarti keras/fisik, dan 'ware' berarti perangkat. Contohnya adalah monitor, keyboard, dan CPU.",
            "alasan_salah": "Salah. Software adalah perangkat lunak (tidak bisa disentuh), Brainware adalah penggunanya, dan Malware adalah virus/program jahat."
        },
        {
            "id": 3,
            "pertanyaan": "Berikut ini yang merupakan contoh dari perangkat masukan (Input Device) adalah...",
            "opsi": ["Monitor dan Printer", "Keyboard dan Mouse", "CPU dan RAM", "Hardisk dan Flashdisk"],
            "jawaban_benar": "Keyboard dan Mouse",
            "alasan_benar": "Benar. Keyboard untuk memasukkan data teks, dan mouse untuk memasukkan instruksi pergerakan kursor.",
            "alasan_salah": "Keliru. Monitor/Printer adalah Output, CPU/RAM adalah Process, sedangkan Hardisk/Flashdisk adalah Storage."
        },
        {
            "id": 4,
            "pertanyaan": "Komponen yang bertindak sebagai 'Otak' dari sebuah sistem komputer dan bertugas mengeksekusi semua instruksi adalah...",
            "opsi": ["RAM", "Motherboard", "CPU (Processor)", "SSD"],
            "jawaban_benar": "CPU (Processor)",
            "alasan_benar": "Tepat! CPU (Central Processing Unit) adalah otak utama yang melakukan semua perhitungan dan pengambilan keputusan di dalam mesin.",
            "alasan_salah": "Salah. RAM hanya meja kerja sementara, motherboard adalah papan sirkuit tempat komponen menempel, dan SSD adalah gudang penyimpanan."
        },
        {
            "id": 5,
            "pertanyaan": "Karakteristik utama dari RAM (Random Access Memory) adalah...",
            "opsi": ["Menyimpan data secara permanen", "Hanya bisa digunakan untuk menyimpan video", "Menyimpan data sementara dan datanya hilang saat komputer dimatikan", "Membantu monitor menampilkan warna"],
            "jawaban_benar": "Menyimpan data sementara dan datanya hilang saat komputer dimatikan",
            "alasan_benar": "Benar sekali. Sifat RAM adalah 'Volatile', artinya ia membutuhkan arus listrik untuk menyimpan data sementara saat aplikasi sedang berjalan.",
            "alasan_salah": "Salah. Penyimpanan permanen adalah tugas Hardisk/SSD, bukan RAM."
        },
        {
            "id": 6,
            "pertanyaan": "Perangkat keluaran (Output Device) yang berfungsi untuk menampilkan informasi berupa gambar atau antarmuka visual adalah...",
            "opsi": ["Scanner", "Printer", "Monitor", "Speaker"],
            "jawaban_benar": "Monitor",
            "alasan_benar": "Benar. Monitor berfungsi menerjemahkan sinyal digital dari komputer menjadi tampilan visual di layar.",
            "alasan_salah": "Keliru. Scanner adalah alat input, Printer mengeluarkan data ke kertas (fisik), dan Speaker mengeluarkan bentuk suara (audio)."
        },
        {
            "id": 7,
            "pertanyaan": "Apa perbedaan utama antara HDD (Hard Disk Drive) dan SSD (Solid State Drive)?",
            "opsi": ["HDD digunakan untuk Input, SSD untuk Output", "SSD memiliki kecepatan baca/tulis data yang jauh lebih cepat daripada HDD", "HDD adalah software, SSD adalah hardware", "HDD bentuknya cair, SSD bentuknya padat"],
            "jawaban_benar": "SSD memiliki kecepatan baca/tulis data yang jauh lebih cepat daripada HDD",
            "alasan_benar": "Tepat! SSD menggunakan memori flash tanpa komponen bergerak mekanik, sehingga jauh lebih cepat dan tahan guncangan dibanding HDD.",
            "alasan_salah": "Kurang tepat. Keduanya sama-sama hardware perangkat penyimpanan (Storage), perbedaannya terletak pada kecepatan dan teknologi pembacaan datanya."
        },
        {
            "id": 8,
            "pertanyaan": "Windows, Linux, dan aplikasi seperti Microsoft Word merupakan kelompok dari...",
            "opsi": ["Hardware", "Software", "Brainware", "Freeware"],
            "jawaban_benar": "Software",
            "alasan_benar": "Benar. Windows/Linux adalah Software Sistem Operasi, sedangkan Microsoft Word adalah Software Aplikasi.",
            "alasan_salah": "Salah. Karena wujudnya berupa program (tidak bisa disentuh fisik), mereka masuk kategori Software, bukan Hardware atau Brainware."
        },
        {
            "id": 9,
            "pertanyaan": "Manusia yang bertindak sebagai pembuat, pengontrol, atau pengguna sistem komputer disebut sebagai...",
            "opsi": ["Software", "Hardware", "Brainware", "Spyware"],
            "jawaban_benar": "Brainware",
            "alasan_benar": "Tepat sekali. 'Brain' berarti otak manusia. Secanggih apapun hardware dan software, mereka membutuhkan manusia (brainware) untuk mengarahkannya.",
            "alasan_salah": "Salah. Hardware itu fisik mesin, software itu aplikasinya. Penggunanya adalah Brainware."
        },
        {
            "id": 10,
            "pertanyaan": "Urutan siklus pemrosesan informasi pada komputer yang benar adalah...",
            "opsi": ["Output -> Proses -> Input", "Proses -> Input -> Output", "Input -> Output -> Proses", "Input -> Proses -> Output"],
            "jawaban_benar": "Input -> Proses -> Output",
            "alasan_benar": "Sempurna! Kita memasukkan perintah (Input), kemudian CPU mengolahnya (Proses), dan hasilnya ditampilkan ke layar/speaker (Output).",
            "alasan_salah": "Keliru. Komputer tidak bisa memproses sesuatu yang belum dimasukkan, dan tidak bisa mengeluarkan hasil (output) sebelum diproses. Urutan mutlaknya adalah: Masuk (Input) -> Olah (Proses) -> Keluar (Output)."
        }
    ]

    # Iterasi untuk merender 10 soal
    for idx, item in enumerate(soal_latihan):
        st.markdown(f"**{item['id']}. {item['pertanyaan']}**")
        
        opsi_jawaban = ["[Pilih Jawaban]"] + item['opsi']
        jawaban_user = st.radio(f"Jawaban No {item['id']}:", opsi_jawaban, label_visibility="collapsed", key=f"soal_{item['id']}")
        
        # Logika Feedback Langsung
        if jawaban_user != "[Pilih Jawaban]":
            if jawaban_user == item['jawaban_benar']:
                st.success(f"✅ **BENAR!**\n\n**Penjelasan:** {item['alasan_benar']}")
            else:
                st.error(f"❌ **SALAH!**\n\n**Penjelasan:** {item['alasan_salah']}")
        st.markdown("---")
