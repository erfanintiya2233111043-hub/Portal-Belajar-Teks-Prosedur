import streamlit as st
import google.generativeai as genai
import os

# 1. Configuration & Styling
st.set_page_config(
    page_title="Portal Belajar Teks Prosedur",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Sidebar Navigation
st.sidebar.title("Teks Prosedur")
st.sidebar.caption("Belajar • Berlatih • Berkarya")

menu = st.sidebar.radio(
    "Navigasi Portal",
    [
        "Beranda",
        "Presensi",
        "Ice Breaking",
        "Modul Pembelajaran",
        "Materi",
        "Analisis Teks",
        "LKPD",
        "Tugas Praktik",
        "Tanya Biografika",
        "Media Belajar"
    ]
)

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

# 3. Pages

# --- BERANDA ---
if menu == "Beranda":
    # Custom CSS Background Polkadot Ceria & Pastel
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f7f9fc;
        background-image: radial-gradient(#ffb6c1 2px, transparent 2px), radial-gradient(#87cefa 2px, #f7f9fc 2px);
        background-size: 40px 40px;
        background-position: 0 0, 20px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("✏️📚 Portal Belajar Teks Prosedur 🎨🔤")
    st.caption("✨ Media Pembelajaran Bahasa Indonesia Interaktif untuk Siswa/i SMP ✨")
    
    # Header Gambar Canva Hasil Desainmu
    st.image(
        "header_beranda.png",
        use_container_width=True
    )
    
    st.markdown("---")
    
    # Fitur Utama Warna-Warni
    st.markdown("### 🎒 Apa Saja yang BISA Kamu Pelajari di Sini?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📚 **1. Pahami Struktur & Ciri**\nPelajari langkah-langkah membuat teks prosedur yang runtut, lengkap dari tujuan sampai penutup!")
        st.success("✏️ **2. Latihan Praktis & LKPD**\nAsah keterampilan menulis teks prosedur dengan tugas interaktif yang siap dikerjakan.")
        
    with col2:
        st.warning("✒️ **3. Kaidah Kebahasaan**\nKuasai penggunaan kata kerja imperatif, konjungsi urutan, dan kalimat perintah.")
        st.error("🤖 **4. Tanya Biografika AI**\nBingung buat teks prosedur? Tanya langsung ke AI tutor pintar yang siap bantu 24/7!")

    st.markdown("""
    ---
    ### 🏫 Yuk, Mulai Belajar!
    Pilih menu navigasi di **sidebar sebelah kiri** 👈 untuk mulai menjelajahi materi, melakukan *ice breaking*, atau bertanya langsung pada **Tanya Biografika**!
    """)

# --- PRESENSI ---
elif menu == "Presensi":
    st.header("📋 Presensi Kehadiran Siswa")
    st.write("Silakan isi formulir kehadiran di bawah ini sebelum memulai kegiatan pembelajaran.")
    
    with st.form("presensi_form"):
        nama = st.text_input("Nama Lengkap:")
        kelas = st.selectbox("Kelas", ["VII-1", "VII-2", "VII-3", "VII-4", "VII-5", "Lainnya"])
        nisn = st.text_input("NISN / Nomor Absen")
        keterangan = st.radio("Keterangan Kehadiran", ["Hadir", "Izin", "Sakit"])
        submitted = st.form_submit_button("Kirim Presensi")
        
        if submitted:
            if nama and nisn:
                st.success(f"Presensi berhasil dicatat untuk {nama} ({kelas}) - Status: {keterangan}")
            else:
                st.error("Mohon lengkapi Nama dan NISN/Nomor Absen!")

# --- ICE BREAKING ---
elif menu == "Ice Breaking":
    st.header("🎮 Ice Breaking: Kuis Tebak Kata Teks Prosedur")
    st.write("Segarkan pikiranmu sebelum belajar!")
    
    q1 = st.radio("1. Kata kerja yang berisi perintah atau ajakan disebut...", ["Imperatif", "Deklaratif", "Interogatif", "Pasif"])
    if q1 == "Imperatif":
        st.success("Benar! 🎉 Kata kerja imperatif adalah kata kerja perintah.")
    
    q2 = st.radio("2. Kata penghubung yang menyatakan urutan waktu (seperti *kemudian, setelah itu*) disebut...", ["Konjungsi Temporal", "Konjungsi Kausalitas", "Kata Benda", "Kata Sifat"])
    if q2 == "Konjungsi Temporal":
        st.success("Tepat sekali! 👍")

# --- MODUL PEMBELAJARAN ---
elif menu == "Modul Pembelajaran":
    st.header("📘 Modul Pembelajaran")
    st.write("Unduh dan pelajari modul ajar resmi Teks Prosedur.")
    
    modul_path = "MODUL AJAR/MODUL AJAR TEKS PROSEDUR.docx"
    if os.path.exists(modul_path):
        with open(modul_path, "rb") as file:
            st.download_button(
                label="📥 Unduh Modul Ajar (DOCX)",
                data=file,
                file_name="MODUL_AJAR_TEKS_PROSEDUR.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.info("File Modul Ajar dapat diakses dari menu repositori GitHub kamu.")

# --- MATERI ---
elif menu == "Materi":
    st.header("📚 Materi Pembelajaran Teks Prosedur")
    
    sub_materi = st.tabs([
        "A. Pengertian",
        "B. Tujuan",
        "C. Ciri-ciri",
        "D. Kebahasaan",
        "E. Struktur",
        "F. Contoh"
    ])
    
    files = [
        ("MATERI/A. PENGERTIAN TEKS PROSEDUR.txt", "Pengertian Teks Prosedur"),
        ("MATERI/B. TUJUAN TEKS PROSEDUR.txt", "Tujuan Teks Prosedur"),
        ("MATERI/C. CIRI-CIRI TEKS PROSEDUR.txt", "Ciri-ciri Teks Prosedur"),
        ("MATERI/D. UNSUR KEBAHASAAN TEKS PROSEDUR.txt", "Unsur Kebahasaan Teks Prosedur"),
        ("MATERI/E. STRUKTUR TEKS PROSEDUR.txt", "Struktur Teks Prosedur"),
        ("MATERI/F. CONTOH TEKS PROSEDUR.txt", "Contoh Teks Prosedur")
    ]
    
    for tab, (path, title) in zip(sub_materi, files):
        with tab:
            st.subheader(title)
            content = read_file(path)
            if content:
                st.markdown(content)
            else:
                st.write(f"Materi {title} siap dipelajari.")

# --- ANALISIS TEKS ---
elif menu == "Analisis Teks":
    st.header("🔍 Analisis Teks Prosedur")
    st.write("Lakukan analisis struktur dan unsur kebahasaan pada teks prosedur yang kamu pilih.")
    
    sample_text = st.text_area("Tempelkan Teks Prosedur di sini untuk dianalisis:", height=200)
    if st.button("Mulai Analisis Mandiri"):
        if sample_text:
            st.subheader("Hasil Panduan Analisis:")
            st.write("1. **Struktur**: Pastikan memuat Tujuan, Material/Bahan, dan Langkah-langkah.")
            st.write("2. **Ciri Kebahasaan**: Periksa apakah terdapat kata kerja imperatif (misal: *masukkan, aduklah*) dan konjungsi temporal (misal: *selanjutnya, lalu*).")
        else:
            st.warning("Masukkan teks prosedur terlebih dahulu.")

# --- LKPD ---
elif menu == "LKPD":
    st.header("📝 Lembar Kerja Peserta Didik (LKPD)")
    st.write("Kerjakan tugas lembar kerja untuk menguji pemahamanmu.")
    
    st.markdown("""
    ### Tugas LKPD:
    1. Bacalah salah satu teks prosedur yang ada di menu **Materi**.
    2. Identifikasilah **Struktur** (Tujuan, Bahan/Alat, Langkah-langkah, Penutup) dari teks tersebut!
    3. Tentukan 3 kalimat yang memuat **Kata Kerja Imperatif**!
    """)

# --- TUGAS PRAKTIK ---
elif menu == "Tugas Praktik":
    st.header("📤 Pengumpulkan Tugas Praktik")
    st.write("Unggah hasil karya teks prosedur atau scan QR Code di bawah ini.")
    
    qr_path = "PENGUMPULAN TUGAS PRAKTIK/qr_proyek.png.png"
    if os.path.exists(qr_path):
        st.image(qr_path, caption="Scan QR Code untuk Mengumpulkan Tugas Praktik", width=300)
    
    st.subheader("Atau Kirimkan Draf Teks Praktikmu di Sini:")
    tugas_text = st.text_area("Tuliskan Teks Prosedur buatanmu:")
    if st.button("Kirim Tugas"):
        if tugas_text:
            st.success("Tugas berhasil dikirim! Guru akan memeriksa karya kamu.")
        else:
            st.warning("Isi draf teks prosedurmu terlebih dahulu.")

# --- TANYA BIOGRAFIKA (AI INTEGRATED) ---
elif menu == "Tanya Biografika":
        # Desain Header Full Warna Gradasi
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FF5E7E, #A060FF, #4DE1FF); padding: 25px; border-radius: 20px; color: white; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
            <h1 style="color: white; margin: 0; font-size: 32px;">🤖🎨 Tanya Biografika AI 📚✨</h1>
            <p style="font-size: 18px; margin-top: 8px; font-weight: bold;">Asisten Pintar Pembelajaran Teks Prosedur SMP!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Kartu Rekomendasi Pertanyaan Warna-Warni
        st.markdown("##### 💡 **Coba Tanyakan Hal Ini:**")
        col_a, col_b = st.columns(2)
        with col_a:
            st.success("📌 *Apa saja struktur utama Teks Prosedur?*")
            st.info("📌 *Buatkan contoh Teks Prosedur membuat jus buah!*")
        with col_b:
            st.warning("📌 *Apa bedanya kata kerja imperatif dan deklaratif?*")
            st.error("📌 *Koreksi teks prosedur yang sudah kubuat dong!*")
            
        st.markdown("---")

        # Configure Gemini API Key
        api_key = None
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
        elif "GEMINI_API_KEY" in os.environ:
            api_key = os.environ["GEMINI_API_KEY"]

        if not api_key:
            with st.sidebar.expander("🔑 Input API Key (Opsional)"):
                user_api_key = st.text_input("Masukkan Gemini API Key:", type="password")
                if user_api_key:
                    api_key = user_api_key

        if not api_key:
            st.warning("⚠️ **API Key Gemini belum terpasang.** Silakan atur Secrets di Streamlit Cloud.")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(
                    'gemini-3.8-flash',
                    system_instruction="""
                    Kamu adalah Biografika AI, tutor pembelajaran Bahasa Indonesia untuk anak SMP yang sangat ramah, ceria, interaktif, dan penuh semangat!
                    Tugas utamamu adalah membantu siswa memahami Teks Prosedur dengan contoh yang mudah dipahami anak SMP.
                    Gunakan emoji yang ramai dan bahasa yang santai namun tetap edukatif.
                    """
                )

                # Initialize Chat History
                if "messages" not in st.session_state:
                    st.session_state.messages = [
                        {"role": "assistant", "content": "Halo! Saya **Biografika AI** 🤖✨ Siap bantu kamu belajar Teks Prosedur! Ada yang mau ditanyakan hari ini? ✏️📚"}
                    ]

                # Display Chat History
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                # Chat Input
                if prompt := st.chat_input("Tanyakan sesuatu tentang Teks Prosedur..."):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    with st.chat_message("user"):
                        st.markdown(prompt)

                    with st.chat_message("assistant"):
                        message_placeholder = st.empty()
                        message_placeholder.markdown("🎨 *Biografika AI sedang berpikir...*")
                        
                        formatted_history = []
                        for msg in st.session_state.messages[:-1]:
                            role = "user" if msg["role"] == "user" else "model"
                            formatted_history.append({"role": role, "parts": [msg["content"]]})

                        chat = model.start_chat(history=formatted_history)
                        response = chat.send_message(prompt)
                        
                        message_placeholder.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"Gagal mendapatkan respons AI: {e}")

# --- MEDIA BELAJAR ---
elif menu == "Media Belajar":
    st.header("🖼️ Media Belajar Interaktif")
    st.write("Unduh media presentasi dan materi visual pendukung.")
    
    media_path = "MEDIA BELAJAR/Teks Prosedur Presentasi Pendidikan Krem dan Kuning Sederhana dan Lucu.pptx"
    if os.path.exists(media_path):
        with open(media_path, "rb") as file:
            st.download_button(
                label="📊 Unduh Presentasi Pembelajaran (PPTX)",
                data=file,
                file_name="Presentasi_Teks_Prosedur.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
    else:
        st.info("Materi presentasi dapat diakses langsung dari folder Media Belajar.")
