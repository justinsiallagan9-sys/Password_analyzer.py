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
# 2. DATA MATERI (DIPERLUAS & DIREVISI)
# ==========================================
def get_materi_data():
    return {
        "1. Pengertian Komputer": {
            "tipe": "standar",
            "teks": "Komputer adalah alat elektronik yang dapat menerima input data, mengolah data tersebut secara terstruktur, memberikan informasi berupa output yang bermanfaat, serta menyimpannya dalam media penyimpanan sekunder. Secara etimologis, kata komputer berasal dari bahasa Latin *\"computare\"* yang berarti menghitung. Pada awalnya, komputer memang dirancang khusus untuk melakukan proses perhitungan matematika yang rumit.\n\nNamun, seiring dengan pesatnya perkembangan zaman dan teknologi modern, fungsi komputer telah meluas secara signifikan. Komputer kini menjadi mesin serbaguna yang mampu menyelesaikan berbagai tugas kompleks, mulai dari administrasi perkantoran, desain grafis, pengelolaan basis data, hingga menjalankan sistem kecerdasan buatan (AI). Sistem komputer modern dapat bekerja dengan optimal karena adanya kolaborasi yang erat dan tidak terpisahkan antara tiga pilar utama: perangkat keras (hardware), perangkat lunak (software), dan pengguna (brainware).",
            "gambar": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Gambar Komputer utuh
        },
        "2. Fungsi Komputer": {
            "tipe": "standar",
            "teks": "Secara operasional, komputer memiliki empat fungsi dasar yang saling berkesinambungan dan membentuk sebuah siklus pengolahan data:\n\n"
                    "1. **Fungsi Input (Memasukkan Data):** Ini adalah tahap awal di mana komputer menerima instruksi, perintah, atau data mentah dari pengguna melalui perangkat masukan (input devices) seperti keyboard, mouse, mikrofon, atau scanner. Tanpa adanya input, tidak ada data yang bisa diolah.\n"
                    "2. **Fungsi Process (Mengolah Data):** Merupakan inti dari sistem komputer. Data mentah yang telah dimasukkan akan dikirim ke Central Processing Unit (CPU) untuk diproses, dihitung, dianalisis, atau dimanipulasi secara logis sehingga berubah menjadi informasi yang bermakna dan terstruktur.\n"
                    "3. **Fungsi Output (Menghasilkan Informasi):** Setelah data selesai diproses, komputer akan menyajikan hasil olahan tersebut ke dalam bentuk yang dapat dilihat, dibaca, didengar, atau dipahami oleh manusia (informasi). Penyajian ini dilakukan melalui perangkat keluaran seperti layar monitor (visual), printer (cetak), atau speaker (audio).\n"
                    "4. **Fungsi Storage (Menyimpan Data):** Komputer menyediakan ruang untuk menyimpan data dan informasi yang telah diproses ke dalam media penyimpanan permanen. Fungsi ini sangat krusial agar file atau dokumen dapat dibuka kembali, diedit, atau diproses di lain waktu tanpa harus memulai dari awal.",
            "gambar": "https://images.unsplash.com/photo-1555680202-c86f0e12f086?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Gambar alur sistem/komputer yang sesuai
        },
        "3. Perangkat Keras (Hardware)": {
            "tipe": "komponen_detail",
            "teks_pengantar": "Hardware (Perangkat Keras) adalah semua bagian dari struktur komputer yang memiliki wujud fisik, sehingga dapat dilihat dengan mata telanjang dan disentuh secara langsung. Komponen ini adalah mesin nyata yang merakit sistem komputer. Berikut adalah komponen-komponen esensial pembangun komputer beserta fungsinya secara mendalam:",
            "komponen": [
                {
                    "nama": "Motherboard (Papan Induk)",
                    "teks": "Motherboard adalah papan sirkuit cetak (Printed Circuit Board) utama di dalam komputer. Fungsinya layaknya sistem saraf pusat pada manusia, menghubungkan seluruh komponen komputer lainnya agar dapat saling berkomunikasi. Prosesor, RAM, kartu grafis, dan penyimpanan semuanya dipasang atau terhubung ke papan ini.",
                    "gambar": "https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "nama": "CPU / Prosesor",
                    "teks": "Central Processing Unit (CPU) sering disebut sebagai 'otak' dari komputer. Komponen kecil ini bertanggung jawab untuk mengeksekusi semua perintah dan perhitungan matematis yang masuk. Kecepatan kinerja sebuah komputer sangat bergantung pada seberapa canggih dan cepat prosesor yang dimilikinya (biasanya diukur dalam satuan Gigahertz atau GHz).",
                    "gambar": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "nama": "RAM (Random Access Memory)",
                    "teks": "RAM adalah ruang memori penyimpanan sementara yang sangat cepat, digunakan oleh komputer untuk menyimpan data dari program yang sedang berjalan saat itu juga. Semakin besar kapasitas RAM, semakin banyak aplikasi yang bisa dijalankan secara bersamaan tanpa membuat komputer menjadi lambat (multitasking). Perlu diingat, data pada RAM akan hilang seketika jika komputer dimatikan.",
                    "gambar": "https://images.unsplash.com/photo-1562976540-1502c2145186?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "nama": "HDD & SSD (Penyimpanan Permanen)",
                    "teks": "Hard Disk Drive (HDD) dan Solid State Drive (SSD) adalah media penyimpanan data permanen. Di sinilah sistem operasi, dokumen, video, dan foto-foto Anda tersimpan. HDD menggunakan piringan magnetik yang berputar (mekanik), sedangkan SSD menggunakan chip memori flash yang jauh lebih cepat, ringan, dan tahan terhadap guncangan dibandingkan HDD.",
                    "gambar": "https://images.unsplash.com/photo-1531492746076-161ca9bcad58?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "nama": "VGA Card (Kartu Grafis)",
                    "teks": "Video Graphics Array (VGA) atau sering disebut GPU (Graphics Processing Unit) adalah komponen yang khusus bertugas memproses data grafis untuk ditampilkan ke layar monitor. Komponen ini sangat krusial bagi pekerjaan desain grafis, editing video, dan bermain game 3D, karena membebaskan CPU dari beban kerja rendering gambar.",
                    "gambar": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                }
            ]
        },
        "4. Perangkat Lunak (Software)": {
            "tipe": "standar",
            "teks": "Software (Perangkat Lunak) adalah sekumpulan instruksi, data, atau program elektronik yang disimpan, diatur, dan dieksekusi oleh sistem komputer untuk menjalankan tugas-tugas spesifik. Berbeda dengan hardware, software sama sekali tidak memiliki bentuk fisik dan hanya berupa baris-baris kode tak kasatmata yang menjadi 'ruh' penyala mesin.\n\nSoftware bertindak sebagai jembatan komunikasi antara pengguna dengan perangkat keras. Secara luas, perangkat lunak dibagi menjadi tiga kategori utama:\n\n"
                    "1. **Sistem Operasi (Operating System):** Merupakan perangkat lunak paling dasar dan vital yang mengelola seluruh sumber daya perangkat keras dan menyediakan layanan umum untuk aplikasi lain. Tanpa sistem operasi, kita tidak bisa menggunakan program apa pun. Contoh populer adalah **Microsoft Windows** (banyak digunakan di perkantoran), **Linux** (sistem operasi sumber terbuka/open source), dan **macOS** (milik Apple).\n"
                    "2. **Perangkat Lunak Aplikasi:** Program yang dirancang khusus untuk memfasilitasi kebutuhan sehari-hari pengguna. Mulai dari Microsoft Word untuk menyusun makalah, Excel untuk mengolah angka, hingga Google Chrome untuk berselancar di dunia maya.\n"
                    "3. **Perangkat Lunak Utilitas:** Program pembantu yang memastikan komputer berjalan dengan aman dan efisien, contohnya program antivirus, alat backup data, dan alat manajemen partisi disk.",
            "gambar": "https://images.unsplash.com/photo-1629654291663-b91ad427698f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Gambar layar/sistem operasi
        },
        "5. Brainware (Pengguna)": {
            "tipe": "standar",
            "teks": "Brainware merujuk pada elemen intelektual manusia yang terlibat secara langsung dalam merancang, mengoperasikan, mengarahkan, dan mengatur sistem komputer. Sehebat, secanggih, dan semahal apa pun perangkat keras dan perangkat lunak yang dirakit, komputer hanyalah benda mati yang tidak akan berfungsi secara maksimal tanpa adanya campur tangan logika manusia.\n\nBrainware adalah otak utama yang memberikan inisiatif dan tujuan. Tingkatan pengguna komputer (Brainware) sangat bervariasi bergantung pada penguasaan teknologinya:\n\n"
                    "- **System Analyst (Analis Sistem):** Pakar yang bertugas menganalisis kebutuhan, merancang arsitektur jaringan, dan merencanakan sistem teknologi informasi yang akan diterapkan pada sebuah perusahaan atau sekolah.\n"
                    "- **Programmer:** Ahli yang memiliki keahlian menuliskan kode menggunakan bahasa pemrograman tertentu. Mereka adalah para kreator pembuat perangkat lunak, aplikasi, dan website.\n"
                    "- **Administrator Jaringan/Database:** Individu yang bertanggung jawab mengelola, mengamankan, dan merawat sistem operasi, server, atau pusat data agar tetap beroperasi tanpa gangguan (downtime).\n"
                    "- **User / Operator:** Pengguna akhir (end-user) seperti pelajar, pekerja kantoran, atau masyarakat umum yang menggunakan komputer sehari-hari untuk mengetik laporan, mengirim email, mendengarkan musik, dan aktivitas komputasi praktis lainnya.",
            "gambar": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" # Gambar orang sedang fokus menggunakan komputer
        }
    }

# ==========================================
# 3. DATA LATIHAN SOAL (TIDAK BERUBAH DARI SEBELUMNYA)
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
# 5. BAGIAN MATERI (DIREVISI UNTUK MENAMPUNG KOMPONEN HARDWARE)
# ==========================================
def render_materi():
    st.title("📚 Materi Dasar Komputer")
    materi_dict = get_materi_data()
    
    tabs = st.tabs(list(materi_dict.keys()))
    
    for i, (judul, konten) in enumerate(materi_dict.items()):
        with tabs[i]:
            st.header(judul)
            
            # Jika materi standar
            if konten.get("tipe") == "standar":
                col_text, col_img = st.columns([2, 1])
                with col_text:
                    st.markdown(konten["teks"])
                with col_img:
                    st.image(konten["gambar"], use_container_width=True)
            
            # Jika materi berisi eksplorasi list komponen (seperti Hardware)
            elif konten.get("tipe") == "komponen_detail":
                st.markdown(konten["teks_pengantar"])
                st.divider()
                
                # Looping setiap sub-komponen hardware
                for item in konten["komponen"]:
                    st.subheader(item["nama"])
                    c_text, c_img = st.columns([2, 1])
                    with c_text:
                        st.markdown(item["teks"])
                    with c_img:
                        st.image(item["gambar"], use_container_width=True)
                    st.write("") # Memberi jarak tiap komponen

# ==========================================
# 6. BAGIAN LATIHAN SOAL
# ==========================================
def render_latihan_soal():
    st.title("📝 Latihan Soal Interaktif")
    st.info("Pilih jawaban yang paling tepat! Sistem akan langsung memberikan tanggapan begitu kamu menekan tombol 'Cek Jawaban'.")
    
    soal_data = get_soal_data()
    
    for i, item in enumerate(soal_data):
        st.markdown(f"**{item['soal']}**")
        
        jawaban_user = st.radio("Pilih opsi:", item['opsi'], key=f"radio_{i}", label_visibility="collapsed")
        
        if st.button("Cek Jawaban", key=f"btn_{i}"):
            if jawaban_user == item['jawaban_benar']:
                st.success(f"✅ **BENAR!** {item['pujian']}")
                st.balloons()
            else:
                st.error(f"❌ **SALAH.** {item['alasan_salah']}")
        st.divider()

# ==========================================
# 7. ROUTING / MENU NAVIGASI UTAMA
# ==========================================
def main():
    apply_custom_css()
    
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Microsoft_Office_Word_%282019%E2%80%93present%29.svg/512px-Microsoft_Office_Word_%282019%E2%80%93present%29.svg.png", width=60)
    st.sidebar.title("Navigasi Modul")
    menu = st.sidebar.radio("Pilih Halaman:", ["🏠 Beranda", "📚 Materi", "📝 Latihan Soal"])
    
    st.sidebar.divider()
    st.sidebar.caption("Pengembangan Media Pembelajaran Interaktif Berbasis Website (Informatika SMK Kelas X)")
    
    if menu == "🏠 Beranda":
        render_beranda()
    elif menu == "📚 Materi":
        render_materi()
    elif menu == "📝 Latihan Soal":
        render_latihan_soal()

if __name__ == "__main__":
    main()
