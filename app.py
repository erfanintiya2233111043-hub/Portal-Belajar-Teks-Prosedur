from pathlib import Path
import mimetypes
import streamlit as st
import streamlit.components.v1 as components

# PORTAL BELAJAR TEKS PROSEDUR - simpan sebagai app.py
BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"

st.set_page_config(page_title="Portal Belajar Teks Prosedur", page_icon="📚", layout="wide")

LINKS = {
    "Presensi": [("Form Presensi", "https://docs.google.com/forms/d/e/1FAIpQLSfxP_VxR9j-FxgkbjNGGhLGPsE9NxV6bNDyUuyP60r0jcNAIg/viewform?usp=publish-editor", "Isi kehadiran sebelum belajar.")],
    "Ice Breaking": [("Video Ice Breaking", "https://youtu.be/PV9WzWksz0c?feature=shared", "Segarkan pikiran sebelum mulai belajar.")],
    "LKPD": [("LKPD Teks Prosedur", "https://www.educaplay.com/learning-resources/22297713-lk_kelas_c.html", "Kerjakan aktivitas interaktif.")],
}

MENUS = [
    "Beranda", "Presensi", "Ice Breaking", "Modul Pembelajaran", 
    "Materi", "Analisis Teks", "LKPD", "Tugas Praktik", 
    "Tanya Biografika", "Media Belajar", "Refleksi"
]

# Style CSS untuk Menyesuaikan Tampilan dengan Gambar Desain
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background-color: #f4f7fc;
}

/* Sidebar Dark Navy */
[data-testid="stSidebar"] {
    background-color: #17253d !important;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Menu Radio Sidebar Active Item */
[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding: 10px 16px;
    border-radius: 12px;
    margin-bottom: 4px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background-color: #fde047 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] span {
    color: #17253d !important;
    font-weight: 800 !important;
}

/* Header Top */
.top-user-bar {
    text-align: right;
    font-weight: 700;
    color: #1e293b;
    padding-bottom: 15px;
}

/* Hero Banner Style */
.hero-banner {
    background: linear-gradient(135deg, #e0f2fe 0%, #dbeafe 60%, #eff6ff 100%);
    border-radius: 20px;
    padding: 35px 40px;
    border: 1px solid #bfdbfe;
    margin-bottom: 25px;
}

.hero-banner h1 {
    color: #1e3a8a;
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 10px;
}

.hero-banner p {
    color: #334155;
    font-size: 15px;
    max-width: 70%;
    margin-bottom: 18px;
}

.hero-btn {
    background-color: #facc15;
    color: #713f12;
    padding: 8px 18px;
    border-radius: 20px;
    font-weight: 800;
    font-size: 14px;
    display: inline-block;
}

/* 6 Card Feature Grid */
.card-box {
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    min-height: 150px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    border: 1px solid rgba(0,0,0,0.04);
}

.card-box .icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    margin: 0 auto 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    color: white;
}

.card-box h4 {
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 6px;
    color: #1e293b;
}

.card-box p {
    font-size: 12px;
    color: #64748b;
    margin: 0;
    line-height: 1.3;
}

.bg-materi { background-color: #ffebee; }
.bg-materi .icon { background-color: #ef4444; }

.bg-media { background-color: #e0f2fe; }
.bg-media .icon { background-color: #06b6d4; }

.bg-modul { background-color: #f3e8ff; }
.bg-modul .icon { background-color: #a855f7; }

.bg-game { background-color: #e0f2fe; }
.bg-game .icon { background-color: #3b82f6; }

.bg-lkpd { background-color: #fef9c3; }
.bg-lkpd .icon { background-color: #eab308; }

.bg-tugas { background-color: #fce7f3; }
.bg-tugas .icon { background-color: #ec4899; }

/* Info Section & Sticky Note */
.info-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    border: 1px solid #e2e8f0;
    height: 100%;
}

.quote-bubble {
    background-color: #fef9c3;
    border-radius: 12px;
    padding: 12px 16px;
    color: #854d0e;
    font-weight: 700;
    font-size: 13px;
    margin-top: 15px;
}

.sticky-note {
    background-color: #fef9c3;
    border-radius: 16px;
    padding: 24px;
    border: 1px solid #fef08a;
    text-align: center;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Footer Style */
.custom-footer {
    background-color: #e0f2fe;
    border-radius: 10px;
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 25px;
    font-weight: 700;
    color: #1e3a8a;
    font-size: 13px;
}

div.stButton>button, div.stLinkButton>a {
    border-radius: 10px;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)


def files_in(folder, exts=None):
    if not folder.exists() or not folder.is_dir():
        return []
    result = [p for p in folder.iterdir() if p.is_file()]
    if exts:
        result = [p for p in result if p.suffix.lower() in exts]
    return sorted(result, key=lambda p: p.name.lower())


def download_file(path):
    try:
        st.download_button("⬇️ Unduh file", path.read_bytes(), file_name=path.name,
                           mime=mimetypes.guess_type(path.name)[0] or "application/octet-stream",
                           key="download_" + str(path.resolve()), use_container_width=True)
    except OSError:
        st.warning("File tidak dapat dibaca.")


def show_folder(folder, exts=None, read_text=False):
    if not folder.exists():
        st.info(f"Folder **{folder.name}** belum ditemukan. Periksa nama folder di VS Code.")
        return
    items = files_in(folder, exts)
    if not items:
        st.info(f"Belum ada file di folder **{folder.name}**.")
        return
    for p in items:
        with st.container(border=True):
            a, b = st.columns([4, 1])
            with a:
                st.markdown(f"**📄 {p.name}**")
                if read_text and p.suffix.lower() in (".txt", ".md"):
                    try:
                        text = p.read_text(encoding="utf-8-sig")
                    except UnicodeDecodeError:
                        text = p.read_text(encoding="latin-1")
                    st.markdown(text)
                elif p.suffix.lower() == ".html":
                    with st.expander("Tampilkan halaman HTML"):
                        try:
                            components.html(p.read_text(encoding="utf-8"), height=650, scrolling=True)
                        except Exception:
                            st.caption("HTML tidak dapat ditampilkan; silakan unduh file.")
                elif p.suffix.lower() in (".ppt", ".pptx", ".pdf", ".doc", ".docx"):
                    st.caption("Unduh file untuk membukanya dengan aplikasi yang sesuai.")
            with b:
                download_file(p)


def show_links(menu):
    items = LINKS.get(menu, [])
    if not items:
        st.info("Tautan untuk menu ini belum ditambahkan. URL dapat dimasukkan ke daftar LINKS di bagian atas kode.")
        return
    for title, url, desc in items:
        with st.container(border=True):
            st.markdown(f"#### 🔗 {title}")
            st.write(desc)
            st.link_button("Buka tautan", url, use_container_width=True)


def show_qr(folders, heading="Pindai QR Code"):
    found = []
    for folder in folders:
        found += [p for p in files_in(folder, {".png", ".jpg", ".jpeg", ".webp"}) if "qr" in p.stem.lower()]
    found = list({str(p.resolve()): p for p in found}.values())
    if found:
        st.markdown(f"### {heading}")
        cols = st.columns(min(3, len(found)))
        for i, p in enumerate(found):
            with cols[i % len(cols)]:
                st.image(str(p), caption=p.stem.replace("_", " ").title(), use_container_width=True)
    else:
        st.caption("QR belum ditemukan. Letakkan gambar QR di folder assets atau folder kegiatan.")


# Sidebar Header Layout
with st.sidebar:
    st.markdown("## 📖 Portal Belajar\nTeks Prosedur")
    st.caption("Belajar • Berlatih • Berkarya")
    st.divider()
    menu = st.radio("Navigasi", MENUS, label_visibility="collapsed")
    st.divider()
    st.caption("Langkah kecil hari ini, untuk masa depan yang lebih baik 📚")

# Top User Profile Header
st.markdown('<div class="top-user-bar">👤 Halo, Siswa! ▾</div>', unsafe_allow_html=True)

if menu == "Beranda":
    # Hero Banner
    st.markdown("""
    <div class="hero-banner">
        <h1>Selamat Datang di<br>Portal Belajar Teks Prosedur!</h1>
        <p>Di sini kamu bisa belajar materi, menonton video, bermain game, menyelesaikan LKPD, dan mengumpulkan tugas praktik.</p>
        <div class="hero-btn">Yuk, jadi pembelajar yang aktif dan kreatif!</div>
    </div>
    """, unsafe_allow_html=True)

    # 6 Feature Cards Grid
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    
    with c1:
        st.markdown('<div class="card-box bg-materi"><div class="icon">📖</div><h4>Materi</h4><p>Pahami konsep dasar teks prosedur</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-box bg-media"><div class="icon">▶️</div><h4>Media Belajar</h4><p>Video, gambar, dan bahan pendukung</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card-box bg-modul"><div class="icon">📄</div><h4>Modul Pembelajaran</h4><p>Unduh modul dalam berbagai format</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="card-box bg-game"><div class="icon">🎮</div><h4>Game</h4><p>Belajar sambil bermain</p></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="card-box bg-lkpd"><div class="icon">📝</div><h4>LKPD</h4><p>Latihan dan uji pemahaman</p></div>', unsafe_allow_html=True)
    with c6:
        st.markdown('<div class="card-box bg-tugas"><div class="icon">📹</div><h4>Tugas Praktik</h4><p>Buat video dan kumpulkan tugas</p></div>', unsafe_allow_html=True)

    st.write("")

    # Lower Info Section Grid
    col_a, col_b, col_c = st.columns([1.2, 1.2, 1])

    with col_a:
        st.markdown("""
        <div class="info-card">
            <h3>📣 Selamat Datang!</h3>
            <p>Portal ini dirancang khusus untuk membantu kamu mempelajari teks prosedur dengan cara yang mudah, menyenangkan, dan interaktif.</p>
            <div class="quote-bubble">
                "Belajar teks prosedur, langkah demi langkah menuju hasil yang tepat!" 💬
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="info-card">
            <h3>📅 Fitur Utama</h3>
            <div style="font-size: 14px; line-height: 1.8;">
                ✅ Materi lengkap dan terstruktur<br>
                ✅ Game interaktif: Roda Seru & Dapur Prosedur<br>
                ✅ Akses modul pembelajaran (PPT, PDF, Word)<br>
                ✅ Media belajar (video, gambar, dll)<br>
                ✅ LKPD interaktif<br>
                ✅ Tugas praktik dengan QR code<br>
                ✅ Tanya Biografika untuk diskusi dan refleksi
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div class="sticky-note">
            <div style="font-size:24px; margin-bottom:10px;">📌</div>
            <div style="font-size:16px; font-weight:800; color:#1e293b;">
                "Jangan takut mencoba, karena dari mencoba kita belajar."
            </div>
            <div style="font-size:20px; margin-top:10px;">🙂</div>
        </div>
        """, unsafe_allow_html=True)

    # Footer Row
    st.markdown("""
    <div class="custom-footer">
        <div>📖 Teks Prosedur | SMP</div>
        <div>💙 Belajar dengan hati, menghasilkan karya</div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Presensi":
    st.markdown("## 🗓️ Presensi Kehadiran")
    st.caption("Isi presensi sebelum mengikuti kegiatan pembelajaran.")
    show_links(menu)
    show_qr([ASSETS, BASE], "QR Presensi")

elif menu == "Ice Breaking":
    st.markdown("## 🎈 Ice Breaking")
    st.caption("Segarkan pikiran sebelum masuk ke materi.")
    show_links(menu)
    st.video("https://youtu.be/PV9WzWksz0c?feature=shared")

elif menu == "Modul Pembelajaran":
    st.markdown("## 📘 Modul Pembelajaran")
    st.caption("Modul dapat berupa PDF, PPT, Word, atau HTML.")
    show_folder(BASE / "MODUL AJAR", {".pdf", ".ppt", ".pptx", ".doc", ".docx", ".html"})
    show_folder(ASSETS, {".pdf", ".ppt", ".pptx", ".doc", ".docx", ".html"})

elif menu == "Materi":
    st.markdown("## 📖 Materi Teks Prosedur")
    st.caption("Pilih materi untuk membaca penjelasan yang sudah disiapkan.")
    show_folder(BASE / "MATERI", {".txt", ".md", ".pdf", ".ppt", ".pptx"}, read_text=True)
    root_txt = files_in(BASE, {".txt", ".md"})
    if root_txt:
        st.markdown("### Materi lain di folder utama")
        for p in root_txt:
            with st.expander(p.name):
                try: 
                    st.markdown(p.read_text(encoding="utf-8-sig"))
                except UnicodeDecodeError: 
                    st.markdown(p.read_text(encoding="latin-1"))

elif menu == "Analisis Teks":
    st.markdown("## 🔍 Analisis Teks Prosedur")
    st.write("Panduan Pertanyaan:\n- Apa tujuan teks tersebut?\n- Alat dan bahan apa yang diperlukan?\n- Apa saja langkah-langkahnya?\n- Apakah urutannya sudah logis?\n- Kata kerja atau kata urutan apa yang digunakan?")
    
    teks = st.text_area("Tempelkan teks prosedur yang ingin dianalisis", height=180)
    if st.button("Buat lembar analisis", use_container_width=True):
        if teks.strip():
            st.session_state["teks_analisis"] = teks
            st.success("Teks tersimpan sementara pada halaman ini. Isi lembar analisis berikut.")
        else: 
            st.warning("Tempelkan teks terlebih dahulu.")
            
    if st.session_state.get("teks_analisis"):
        st.text_area("Tujuan teks", key="analisis_tujuan")
        st.text_area("Alat dan bahan", key="analisis_bahan")
        st.text_area("Urutan langkah", key="analisis_langkah")
        st.text_area("Ciri kebahasaan", key="analisis_bahasa")

elif menu == "LKPD":
    st.markdown("## 📋 Lembar Kerja Peserta Didik")
    st.caption("Kerjakan aktivitas untuk menguji pemahamanmu.")
    show_links(menu)
    show_qr([ASSETS, BASE / "MATERI"], "QR LKPD")

elif menu == "Tugas Praktik":
    st.markdown("## 🎥 Proyek Video Teks Prosedur")
    st.caption("Pilih kegiatan yang aman, tulis langkahnya, lalu rekam saat mempraktikkannya.")
    st.markdown("### Petunjuk proyek")
    steps = [
        "Pilih kegiatan sederhana dan aman.", 
        "Siapkan alat dan bahan.", 
        "Jelaskan tujuan kegiatan di awal video.", 
        "Rekam setiap langkah dengan gambar dan suara yang jelas.", 
        "Gunakan urutan yang runtut.", 
        "Tonton ulang video sebelum dikumpulkan.", 
        "Unggah video melalui QR Code pengumpulan."
    ]
    for i, step in enumerate(steps, 1): 
        st.write(f"{i}. {step}")
    
    st.warning("⚠️ Pilih kegiatan yang aman. Minta bantuan orang dewasa untuk kegiatan yang memerlukan pengawasan.")
    show_qr([BASE / "PENGUMPULAN TUGAS PRAKTIK", ASSETS], "📤 QR Pengumpulan Video")
    show_folder(BASE / "PENGUMPULAN TUGAS PRAKTIK")

elif menu == "Tanya Biografika":
    st.markdown("## 💬 Tanya Biografika")
    st.caption("Tuliskan hal yang ingin kamu ketahui tentang teks prosedur.")
    st.info("Kotak ini membantu menyusun pertanyaan, tetapi belum terhubung ke AI yang menjawab otomatis.")
    question = st.text_area("Apa yang ingin kamu tanyakan?", placeholder="Contoh: Apa perbedaan tujuan dan langkah dalam teks prosedur?")
    if st.button("Tampilkan panduan", use_container_width=True):
        if question.strip():
            st.write("1. Periksa kembali materi.\n2. Tandai kata kunci pertanyaan.\n3. Susun jawaban dengan bahasamu sendiri dan sertakan contoh.")
        else: 
            st.warning("Tuliskan pertanyaan terlebih dahulu.")

elif menu == "Media Belajar":
    st.markdown("## 🎧 Media Belajar")
    st.caption("Tonton, amati, dan gunakan media interaktif yang tersedia.")
    st.markdown("### 🎬 Video")
    st.video("https://youtu.be/PV9WzWksz0c?feature=shared")
    st.markdown("### 🧩 Aktivitas interaktif")
    show_links("LKPD")
    st.markdown("### 📁 File media")
    show_folder(BASE / "MEDIA BELAJAR", {".pdf", ".ppt", ".pptx", ".mp4", ".mov", ".png", ".jpg", ".jpeg", ".webp", ".mp3", ".wav", ".html", ".txt"})

elif menu == "Refleksi":
    st.markdown("## 🌱 Refleksi Pembelajaran")
    st.caption("Jawab dengan jujur agar kamu tahu hal yang sudah dikuasai.")
    r1 = st.text_area("1. Apa hal baru yang kamu pelajari hari ini?")
    r2 = st.text_area("2. Bagian mana yang paling mudah dipahami?")
    r3 = st.text_area("3. Bagian mana yang masih membingungkan?")
    r4 = st.text_area("4. Apa yang ingin kamu perbaiki berikutnya?")
    if st.button("Lihat Ringkasan Refleksi", use_container_width=True):
        st.markdown("### Ringkasan Refleksi")
        for label, answer in [("Hal baru", r1), ("Bagian yang mudah", r2), ("Masih membingungkan", r3), ("Rencana perbaikan", r4)]:
            st.markdown(f"**{label}:** {answer or 'Belum diisi.'}")