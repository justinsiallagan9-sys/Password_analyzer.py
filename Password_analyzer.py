import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN & CSS (WARNA & ANIMASI)
# ==========================================
st.set_page_config(page_title="Modul Pembelajaran Informatika", page_icon="💻", layout="wide")

def apply_custom_css():
    st.markdown("""
        <style>
        /* Warna utama biru ala Microsoft Word */
        :root {
            --primary-blue: #185ABD;
            --hover-blue: #2B579A;
        }
        
        /* Animasi interaktif pada tombol */
        div.stButton > button {
            background-color: var(--primary-blue);
            color: white;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        div.stButton > button:hover {
            background-color: var(--hover-blue);
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            color: white;
        }
        
        /* Styling untuk Header Beranda */
        .hero-title {
            color: var(--primary-blue);
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-bottom: 0;
        }
        .hero-subtitle {
            text-align: center;
            color: #555;
            font-size: 1.2em;
            margin-bottom: 2em;
        }
        
        /* Styling Kartu Fitur di Beranda */
        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid var(--primary-blue);
            transition: 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 15px rgba(24, 90, 189, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. DATA MATERI (DARI SUMBER REFERENSI)
# ==========================================
def get_materi_data():
    # Materi diambil dari file referensi
    return {
        "1. Pengertian Komputer": {
            "teks": "Komputer adalah alat elektronik yang digunakan untuk menerima, mengolah, menyimpan, dan menghasilkan informasi[cite: 1]. Komputer membantu manusia dalam menyelesaikan berbagai pekerjaan, seperti mengetik, menghitung, belajar, dan mencari informasi[cite: 1].",
            "gambar": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Placeholder Gambar PC
        },
        "2. Fungsi Komputer": {
            "teks": "Komputer memiliki empat fungsi utama, yaitu input, process, output, dan storage[cite: 1]. Input adalah proses memasukkan data ke komputer, Process adalah proses mengolah data, Output merupakan hasil pengolahan, dan Storage adalah tempat menyimpan data[cite: 1].",
            "gambar": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        "3. Perangkat Keras (Hardware)": {
            "teks": "Hardware adalah semua bagian komputer yang memiliki bentuk fisik sehingga dapat dilihat dan disentuh[cite: 1].\n\n"
                    "- **Input**: Perangkat untuk memasukkan data (contoh: Keyboard, Mouse, Scanner)[cite: 1].\n"
                    "- **Process**: Mengolah data. Komponen utamanya CPU (otak komputer) dan memori seperti RAM[cite: 1].\n"
                    "- **Output**: Menampilkan hasil (contoh: Monitor, Printer, Speaker)[cite: 1].\n"
                    "- **Storage**: Menyimpan data permanen (contoh: Hard disk, SSD, Flashdisk)[cite: 1].",
            "gambar": "https://images.unsplash.com/photo-1591488320449-011701bb6704?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Placeholder Hardware/RAM
        },
        "4. Perangkat Lunak (Software)": {
            "teks": "Software adalah program atau aplikasi yang digunakan untuk menjalankan perintah pada komputer[cite: 1]. Software tidak memiliki bentuk fisik[cite: 1].\n\n"
                    "Contohnya:\n"
                    "- **Windows**: sistem operasi[cite: 1].\n"
                    "- **Microsoft Word & Excel**: pengolah dokumen dan angka[cite: 1].\n"
                    "- **Google Chrome**: mengakses internet[cite: 1].",
            "gambar": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        },
        "5. Brainware (Pengguna)": {
            "teks": "Brainware adalah manusia yang menggunakan atau mengoperasikan komputer[cite: 1]. Contohnya:\n"
                    "- **User**: pengguna sehari-hari[cite: 1].\n"
                    "- **Programmer**: pembuat aplikasi[cite: 1].\n"
                    "- **Administrator**: pengelola sistem[cite: 1].",
            "gambar": "https://images.unsplash.com/photo-1573164713988-8665fc963095?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
        }
    }

# ==========================================
# 3. DATA LATIHAN SOAL (10 SOAL PG)
# ==========================================
def get_soal_data():
    return [
        {
            "soal": "1. Apa pengertian dari komputer?",
            "opsi": ["A. Alat mekanik untuk mencetak", "B. Alat elektronik untuk mengolah informasi", "C. Program tanpa bentuk fisik", "D. Manusia pengelola sistem"],
            "jawaban_benar": "B. Alat elektronik untuk mengolah informasi",
            "pujian": "Luar biasa! Benar sekali, komputer memang bekerja secara elektronik untuk memproses informasi.",
            "alasan_salah": "Kurang tepat. Coba ingat kembali sifat dasar komponen komputer yang menggunakan arus listrik untuk memproses data, bukan mekanik atau manusia."
        },
        {
            "soal": "2. Di bawah ini yang merupakan 4 fungsi utama komputer adalah...",
            "opsi": ["A. Mengetik, Menghitung, Bermain, Belajar", "B. Input, Process, Output, Storage", "C. Hardware, Software, Brainware, CPU", "D. Windows, Word, Excel, Chrome"],
            "jawaban_benar": "B. Input, Process, Output, Storage",
            "pujian": "Tepat sekali! Keempat fungsi ini adalah pilar utama cara kerja sistem komputer.",
            "alasan_salah": "Jawabanmu belum tepat. Fungsi utama sistem berkaitan dengan bagaimana alur data masuk, diolah, dikeluarkan, dan disimpan."
        },
        {
            "soal": "3. Hardware yang digunakan untuk memasukkan data atau perintah ke dalam komputer disebut perangkat...",
            "opsi": ["A. Output", "B. Process", "C. Input", "D. Storage"],
            "jawaban_benar": "C. Input",
            "pujian": "Sangat bagus! 'In' berarti masuk, sehingga alat masukannya disebut perangkat Input.",
            "alasan_salah": "Oops, salah. Pikirkan tentang arti kata 'memasukkan', pilih istilah bahasa Inggris yang maknanya paling sesuai dengan 'masuk'."
        },
        {
            "soal": "4. Komponen yang sering disebut sebagai otak dari sebuah komputer adalah...",
            "opsi": ["A. RAM", "B. Monitor", "C. Hard disk", "D. CPU (Central Processing Unit)"],
            "jawaban_benar": "D. CPU (Central Processing Unit)",
            "pujian": "Hebat! CPU memang bertugas memproses semua logika dan perintah layaknya otak.",
            "alasan_salah": "Masih keliru. Meskipun memori atau layar itu penting, 'otak' yang memproses setiap instruksi bukanlah media penyimpanan atau penampil."
        },
        {
            "soal": "5. Manakah dari kelompok berikut yang termasuk perangkat output (keluaran)?",
            "opsi": ["A. Monitor, Printer, Speaker", "B. Keyboard, Mouse, Scanner", "C. Hard disk, SSD, Flashdisk", "D. CPU, RAM, Motherboard"],
            "jawaban_benar": "A. Monitor, Printer, Speaker",
            "pujian": "Jawaban sempurna! Alat-alat ini menampilkan visual, cetakan, dan suara sebagai hasil.",
            "alasan_salah": "Bukan itu jawabannya. Perangkat output fungsinya 'mengeluarkan' atau 'menampilkan' hasil yang bisa dilihat, didengar, atau dipegang oleh pengguna."
        },
        {
            "soal": "6. Program atau aplikasi yang digunakan untuk menjalankan perintah pada komputer dan tidak memiliki bentuk fisik disebut...",
            "opsi": ["A. Hardware", "B. Brainware", "C. Software", "D. Storage"],
            "jawaban_benar": "C. Software",
            "pujian": "Benar! 'Soft' menandakan tidak ada wujud fisik yang bisa diraba secara langsung.",
            "alasan_salah": "Sayang sekali, salah. Kalau hardware memiliki wujud fisik, maka aplikasi yang berjalan di dalamnya memiliki sebutan kebalikannya."
        },
        {
            "soal": "7. Microsoft Word merupakan salah satu contoh perangkat lunak yang berfungsi untuk...",
            "opsi": ["A. Mengolah angka dan data", "B. Membuat dan mengedit dokumen", "C. Mengatur seluruh sistem komputer", "D. Menjelajahi internet"],
            "jawaban_benar": "B. Membuat dan mengedit dokumen",
            "pujian": "Mantap! Word memang dirancang khusus untuk mempermudah penulisan dokumen.",
            "alasan_salah": "Jawabanmu kurang tepat. Ingat-ingat aplikasi apa yang biasa kamu gunakan untuk mengetik surat atau laporan teks."
        },
        {
            "soal": "8. Manusia yang mengoperasikan, menggunakan, atau mengatur sistem komputer disebut...",
            "opsi": ["A. Hardware", "B. Software", "C. Malware", "D. Brainware"],
            "jawaban_benar": "D. Brainware",
            "pujian": "Cerdas! 'Brain' merujuk pada kecerdasan manusia yang mengendalikan mesin.",
            "alasan_salah": "Masih salah. Perangkat keras adalah hardware, perangkat lunak adalah software. Lalu apa sebutan untuk penggunanya?"
        },
        {
            "soal": "9. Ketika kita mengetik tugas menggunakan keyboard, tahap kerja komputer yang sedang berlangsung adalah tahap...",
            "opsi": ["A. Process", "B. Output", "C. Storage", "D. Input"],
            "jawaban_benar": "D. Input",
            "pujian": "Benar sekali! Mengetik adalah proses memberikan perintah atau data mentah ke dalam sistem.",
            "alasan_salah": "Belum tepat. Coba bayangkan, saat kamu mengetik, data sedang 'dimasukkan' ke dalam komputer sebelum diolah."
        },
        {
            "soal": "10. Di bidang komunikasi, salah satu manfaat keberadaan komputer dan internet adalah...",
            "opsi": ["A. Memudahkan manusia berkomunikasi melalui email dan video call", "B. Membantu mencetak dokumen dalam jumlah banyak", "C. Menyimpan ribuan foto di dalam Flashdisk", "D. Merakit komponen robotika secara otomatis"],
            "jawaban_benar": "A. Memudahkan manusia berkomunikasi melalui email dan video call",
            "pujian": "Sempurna! Kamu telah memahami manfaat langsung komputer untuk komunikasi modern.",
            "alasan_salah": "Kurang tepat. Pastikan kamu memilih opsi yang berhubungan langsung dengan aktivitas 'berkomunikasi' antar manusia."
        }
    ]

# ==========================================
# 4. BAGIAN BERANDA
# ==========================================
def render_beranda():
    st.markdown('<p class="hero-title">Selamat Datang di Modul Informatika 🚀</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Belajar Dasar Komputer Jadi Lebih Mudah dan Menyenangkan untuk Siswa SMK!</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📖 Materi Lengkap</h3>
            <p>Penjelasan komprehensif mulai dari Hardware, Software, hingga Brainware dengan visualisasi menarik.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Latihan Interaktif</h3>
            <p>Uji pemahamanmu dengan kuis pilihan ganda yang memberikan umpan balik langsung secara real-time.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Tingkatkan Nilai</h3>
            <p>Modul didesain khusus berdasarkan metode pembelajaran efektif untuk meningkatkan hasil belajar siswa.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 5. BAGIAN MATERI
# ==========================================
def render_materi():
    st.title("📚 Materi Dasar Komputer")
    materi_dict = get_materi_data()
    
    # Menampilkan materi menggunakan Tabs agar rapi
    tabs = st.tabs(list(materi_dict.keys()))
    
    for i, (judul, konten) in enumerate(materi_dict.items()):
        with tabs[i]:
            st.header(judul)
            col_text, col_img = st.columns([2, 1])
            with col_text:
                st.write(konten["teks"])
            with col_img:
                # PENANDA: Silakan ubah link gambar pada dictionary `get_materi_data()` dengan URL foto spesifik komponen jika diinginkan
                st.image(konten["gambar"], use_container_width=True)

# ==========================================
# 6. BAGIAN LATIHAN SOAL
# ==========================================
def render_latihan_soal():
    st.title("📝 Latihan Soal Interaktif")
    st.info("Pilih jawaban yang paling tepat! Sistem akan langsung memberikan tanggapan begitu kamu menekan tombol 'Cek Jawaban'.")
    
    soal_data = get_soal_data()
    
    # Loop untuk membuat 10 soal
    for i, item in enumerate(soal_data):
        st.markdown(f"**{item['soal']}**")
        
        # Inisialisasi session state untuk setiap soal agar jawaban tersimpan
        state_key = f"soal_{i}"
        
        # Radio button untuk pilihan (hilangkan label agar clean)
        jawaban_user = st.radio("Pilih opsi:", item['opsi'], key=f"radio_{i}", label_visibility="collapsed")
        
        # Tombol interaktif untuk cek jawaban per soal
        if st.button("Cek Jawaban", key=f"btn_{i}"):
            if jawaban_user == item['jawaban_benar']:
                st.success(f"✅ **BENAR!** {item['pujian']}")
                st.balloons() # Animasi tambahan yang menyenangkan
            else:
                # Jika salah, berikan error + alasan TANPA memberi tahu jawaban yang benar
                st.error(f"❌ **SALAH.** {item['alasan_salah']}")
        st.divider()

# ==========================================
# 7. ROUTING / MENU NAVIGASI UTAMA
# ==========================================
def main():
    apply_custom_css()
    
    # Sidebar menu dengan tampilan rapi
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Microsoft_Office_Word_%282019%E2%80%93present%29.svg/512px-Microsoft_Office_Word_%282019%E2%80%93present%29.svg.png", width=60) # Logo placeholder ala biru
    st.sidebar.title("Navigasi Modul")
    menu = st.sidebar.radio("Pilih Halaman:", ["🏠 Beranda", "📚 Materi", "📝 Latihan Soal"])
    
    st.sidebar.divider()
    st.sidebar.caption("Pengembangan Media Pembelajaran Interaktif Berbasis Website (Informatika SMK Kelas X)")
    
    # Routing antar halaman
    if menu == "🏠 Beranda":
        render_beranda()
    elif menu == "📚 Materi":
        render_materi()
    elif menu == "📝 Latihan Soal":
        render_latihan_soal()

# Eksekusi Aplikasi
if __name__ == "__main__":
    main()
