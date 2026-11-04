import streamlit as st
import pandas as pd

# --- KONFIGURASI ---
st.set_page_config(page_title="Simulasi TIK Profesional SMK", layout="wide", page_icon="💡")

# Menggunakan session_state untuk menyimpan progres siswa
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'modul_selesai' not in st.session_state:
    st.session_state.modul_selesai = []

# --- SIDEBAR ---
with st.sidebar:
    st.title("👨‍💻 Ruang Kerja TIK")
    menu = st.radio("Pilih Proyek Hari Ini:", 
                    ["1. Studi Kasus: Sekretaris Kewalahan", 
                     "2. Simulator Logika Excel", 
                     "3. Uji Pemikiran (HOTS)"])
    st.divider()
    st.progress(len(st.session_state.modul_selesai) / 3, text="Progres Belajarmu")

# --- HALAMAN 1: STUDI KASUS WORD (Konteks Dunia Nyata) ---
if menu == "1. Studi Kasus: Sekretaris Kewalahan":
    st.title("Kasus 1: Mengurus 500 Surat Undangan ✉️")
    
    st.markdown("""
    **Misi Kamu:**
    Bayangkan kamu adalah staf administrasi di sebuah perusahaan bergengsi. Bos memintamu mengirimkan surat undangan rapat tahunan kepada **500 investor berbeda** (nama dan alamat berbeda). 
    Acara dimulai *besok pagi*.
    """)
    
    st.info("💡 **Pertanyaan:** Apa strategi yang akan kamu gunakan?")
    
    strategi = st.radio(
        "Pilih langkah kerjamu:",
        ["[Pilih Strategi...]", 
         "A. Mengetik satu per satu nama dari awal sampai surat ke-500.", 
         "B. Membuat 1 format surat, di-copy-paste 500 kali, lalu mengubah nama secara manual.", 
         "C. Membuat 1 format surat di Word, membuat tabel daftar nama di Excel, lalu menghubungkan keduanya otomatis."]
    )
    
    if strategi != "[Pilih Strategi...]":
        if strategi == "C. Membuat 1 format surat di Word, membuat tabel daftar nama di Excel, lalu menghubungkan keduanya otomatis.":
            st.success("🎯 **Brilian! Pikiran seorang Profesional.**")
            st.markdown("""
            Strategi yang kamu pilih dikenal sebagai **Mail Merge (Surat Massal)**. 
            Alih-alih bekerja keras (*work hard*), kamu bekerja cerdas (*work smart*). 
            
            **Mengapa ini penting di dunia kerja?**
            - **Waktu:** Dari 3 hari kerja menjadi hanya 3 menit.
            - **Akurasi:** Nol *typo*. Apa yang ada di Excel, itu yang tercetak di Word.
            """)
            if 'kasus1' not in st.session_state.modul_selesai:
                st.session_state.modul_selesai.append('kasus1')
        elif strategi == "B. Membuat 1 format surat, di-copy-paste 500 kali, lalu mengubah nama secara manual.":
            st.warning("⚠️ **Masuk Akal, Tapi Berbahaya.**")
            st.markdown("""
            Cara ini lebih cepat dari mengetik manual, tapi bayangkan jika di surat ke-300 kamu salah meng-copy nama? Atau tiba-tiba bos meminta format tanggalnya diubah? Kamu harus mengedit 500 halaman satu per satu!
            
            Solusi yang dicari perusahaan adalah **Otomatisasi**, yaitu menggunakan **Mail Merge**.
            """)
        else:
            st.error("❌ **Kerja Keras yang Tidak Efisien.**")
            st.markdown("""
            Jika kamu menggunakan cara ini, kamu baru akan selesai lusa, dan bosmu pasti akan marah besar.
            Di era digital, kita menyerahkan tugas berulang kepada mesin. Solusinya adalah fitur **Mail Merge**.
            """)

# --- HALAMAN 2: SIMULATOR EXCEL (Learning by Doing) ---
elif menu == "2. Simulator Logika Excel":
    st.title("Kasus 2: Menjadi Analis Data HRD 📊")
    st.write("Perhatikan tabel gaji karyawan di bawah ini.")
    
    # Data Simulasi
    df = pd.DataFrame({
        "Nama Karyawan": ["Andi", "Budi", "Siti", "Dina"],
        "Target Penjualan (Juta)": [10, 5, 12, 8],
    })
    st.table(df)
    
    st.markdown("""
    **Aturan Perusahaan:** 
    Jika karyawan mencapai Target Penjualan **10 Juta atau lebih**, mereka mendapat status `"Bonus"`. Jika di bawah itu, statusnya `"Tidak Bonus"`.
    """)
    
    st.info("👨‍💻 **Tugasmu:** Ketikkan rumus logika Excel (Fungsi IF) untuk sel karyawan Andi secara tepat!")
    
    jawaban_excel = st.text_input("Ketik rumusmu di sini (Dimulai dengan =IF...):", placeholder='Contoh: =IF(B2>100, "Ya", "Tidak")')
    
    if jawaban_excel:
        jawaban_bersih = jawaban_excel.upper().replace(" ", "")
        
        # Validasi logika berlapis (meniru pola pikir siswa)
        if "=IF(" not in jawaban_bersih:
            st.error("Rumus Excel selalu dimulai dengan `=IF(` untuk pengujian logika. Coba lagi!")
        elif "10" not in jawaban_bersih:
            st.warning("Kamu belum memasukkan angka syarat targetnya, yaitu 10. Coba periksa lagi.")
        elif ">=" in jawaban_bersih and '"BONUS"' in jawaban_bersih and '"TIDAKBONUS"' in jawaban_bersih:
            st.success("✅ **Sempurna! Kamu memahami logika bersyarat.**")
            st.code('Jawaban Ideal: =IF(B2>=10, "Bonus", "Tidak Bonus")')
            st.markdown("""
            **Kenapa harus pakai `>=` (Lebih besar sama dengan)?**
            Karena aturan mengatakan "10 Juta **atau lebih**". Jika kamu hanya memakai `>`, maka orang yang mendapat pas 10 Juta (seperti Andi) tidak akan dapat bonus. Hal kecil ini sangat krusial dalam data keuangan!
            """)
            if 'kasus2' not in st.session_state.modul_selesai:
                st.session_state.modul_selesai.append('kasus2')
        else:
            st.error("Hampir. Perhatikan struktur penulisannya: `=IF(Logika_Pengujian, \"Nilai_Jika_Benar\", \"Nilai_Jika_Salah\")`")

# --- HALAMAN 3: EVALUASI HOTS ---
elif menu == "3. Uji Pemikiran (HOTS)":
    st.title("🧠 Uji Pemikiran Kritis (Pretest/Posttest)")
    st.write("Soal ini menguji apakah kamu memahami **konsep**, bukan sekadar menghafal tombol.")
    
    st.markdown("**Kasus:**")
    st.info("""
    Kamu sedang membuat Laporan PKL/Prakerin (Praktek Kerja Lapangan) yang tebalnya 100 halaman di Microsoft Word.
    Di halaman 95, kamu menyadari bahwa semua sub-judul Laporan harus diubah dari ukuran font 12 menjadi 14, dan ditebalkan (Bold). 
    """)
    
    jawaban_hots = st.radio(
        "Cara apa yang paling cepat dan tidak berisiko merusak format dokumen untuk mengubah semua sub-judul tersebut?",
        ["[Pilih Jawaban]",
         "A. Scroll perlahan, blok satu per satu setiap sub-judul dari halaman 1 sampai 100, lalu ubah font-nya.",
         "B. Menggunakan fitur CTRL+A (Select All) lalu ubah ukurannya menjadi 14.",
         "C. Mengubah pengaturan pada menu 'Heading 2' (Styles) yang sudah diterapkan, lalu pilih 'Update to Match Selection' otomatis.",
         "D. Membuka dokumen baru, menyalin teks perlahan, dan mengatur ulang semuanya dari awal."]
    )
    
    if jawaban_hots != "[Pilih Jawaban]":
        if jawaban_hots.startswith("C"):
            st.success("🎉 **Jawaban Tepat! Otak Analitis.**")
            st.markdown("""
            **Feedback:** 
            Inilah fungsi sejati dari fitur **Styles (Heading 1, Heading 2)** di Word. Selain untuk membuat Daftar Isi otomatis, fitur ini bertindak sebagai 'Tuan Rumah' bagi format teks. Jika Tuan Rumahnya diubah, seluruh teks di 100 halaman yang menggunakan status tersebut akan berubah dalam **1 detik**. 
            Siswa yang paham konsep ini siap menyusun skripsi atau laporan kerja tanpa menangis karena format yang berantakan!
            """)
            if 'kasus3' not in st.session_state.modul_selesai:
                st.session_state.modul_selesai.append('kasus3')
        elif jawaban_hots.startswith("A"):
            st.error("❌ **Terlalu Melelahkan.**")
            st.markdown("**Feedback:** Memblok teks satu per satu di dokumen 100 halaman butuh waktu berjam-jam, dan berisiko ada judul yang terlewat. Gunakan sistem *Styles* (Heading) agar Word yang bekerja untukmu, bukan sebaliknya.")
        elif jawaban_hots.startswith("B"):
            st.warning("⚠️ **Hati-hati!**")
            st.markdown("**Feedback:** CTRL+A akan memilih *seluruh isi dokumen*, termasuk isi paragraf biasa. Nanti isi laporanmu ikut-ikutan membesar dan menjadi Bold semua. Itu akan merusak laporanmu.")
        else:
            st.error("❌ **Jawaban Keliru.** Memulai dari awal hanya membuang waktu. Gunakan fitur *Styles*.")

# --- FOOTER & KESIMPULAN ---
if len(st.session_state.modul_selesai) == 3:
    st.balloons()
    st.sidebar.success("🏆 Selamat! Kamu sudah memiliki mindset seorang profesional TIK.")
