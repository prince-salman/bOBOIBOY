import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from pathlib import Path

doc = docx.Document()

# Set standard 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Title
title_p = doc.add_paragraph()
title_run = title_p.add_run("PANDUAN LENGKAP PENJELASAN CODE")
title_run.font.size = Pt(22)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(255, 87, 34)
title_p.paragraph_format.space_after = Pt(4)

sub_p = doc.add_paragraph()
sub_run = sub_p.add_run("Proyek Web Programming & Design — BoBoiBoy Universe Portal")
sub_run.font.size = Pt(13)
sub_run.font.color.rgb = RGBColor(100, 116, 139)
sub_p.paragraph_format.space_after = Pt(18)

def add_h1(text):
    h = doc.add_heading(text, level=1)
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    for r in h.runs:
        r.font.size = Pt(15)
        r.font.color.rgb = RGBColor(15, 23, 42)
    return h

def add_qa(question, answer):
    qp = doc.add_paragraph()
    q_lbl = qp.add_run("Tanya: ")
    q_lbl.bold = True
    q_lbl.font.color.rgb = RGBColor(220, 38, 38)
    q_txt = qp.add_run(f'"{question}"')
    q_txt.italic = True
    qp.paragraph_format.space_before = Pt(8)
    qp.paragraph_format.space_after = Pt(3)

    ap = doc.add_paragraph()
    a_lbl = ap.add_run("Jawab: ")
    a_lbl.bold = True
    a_lbl.font.color.rgb = RGBColor(37, 99, 235)
    ap.add_run(answer)
    ap.paragraph_format.space_after = Pt(10)

def add_code_snippet(code_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    # Add border/shading
    pPr = p._element.get_or_add_pPr()
    shd = parse_xml(r'<w:shd {} w:fill="F1F5F9"/>'.format(nsdecls('w')))
    pPr.append(shd)

# 1. Master Frame
add_h1("1. Konsep Arsitektur Master Frame (index.html)")
add_qa(
    "Bagaimana arsitektur website ini dibangun dan apa fungsi index.html?",
    "Website ini menggunakan arsitektur Master Frame sesuai ketentuan rubrik Resident University. File index.html bertindak sebagai bingkai induk (master shell) yang menampung header navigasi di bagian luar, dan sebuah tag <iframe> di bagian tengah untuk menampilkan 5 halaman konten utama."
)
add_qa(
    "Bagaimana cara kerja tombol navigasi saat diklik agar tidak me-refresh seluruh halaman?",
    "Di tag <iframe>, kita berikan atribut name=\"mainFrame\". Kemudian di setiap tag link navigasi <a>, kita tambahkan atribut target=\"mainFrame\". Ketika pengguna mengklik link, browser secara otomatis membuka file halaman yang dituju di dalam iframe tersebut, sementara header dan footer di index.html tetap diam di tempat."
)
add_code_snippet(
'''<!-- Header navigasi di luar frame -->
<a href="home.html" target="mainFrame" class="nav-link">Home</a>
<a href="characters.html" target="mainFrame" class="nav-link">Characters</a>

<!-- Frame utama penampung konten -->
<iframe name="mainFrame" id="mainFrame" src="home.html"></iframe>'''
)

# 2. 5 Pages
add_h1("2. Struktur 5 Halaman Interkoneksi")
p2 = doc.add_paragraph(
    "Kelima halaman saling terhubung penuh dengan navigasi dan memiliki peran masing-masing:\n"
    "1. home.html: Beranda utama dengan Hero Section, statistik, callout box, dan alur pendaftaran kadet (Ordered List <ol>).\n"
    "2. characters.html: Profil 6 pahlawan TAPOPS dengan avatar bulat (border-radius: 50%) dan bilah meteran kemampuan tempur (stat meters).\n"
    "3. elements.html: Eksplorasi 7 kekuatan elemen dasar, hierarki 3 tingkatan evolusi (Ordered List <ol>), dan 4 elemen fusi, dilengkapi tabel matriks komparasi.\n"
    "4. series.html: Kronologi petualangan BoBoiBoy dari musim klasik hingga film bioskop, dilengkapi tabel master kanon rilis dan roadmap nonton maraton.\n"
    "5. contact.html: Cadet Hub yang memuat formulir pendaftaran 7 jenis kontrol lengkap dengan validasi HTML5, profil mahasiswa, dan FAQ accordion."
)
p2.paragraph_format.space_after = Pt(10)

# 3. 3 CSS Methods
add_h1("3. Penjelasan 3 Metode CSS yang Diterapkan")
add_qa(
    "Di mana saja Anda menerapkan ketiga metode CSS (External, Internal, Inline)?",
    "1. External CSS: Di file css/style.css, dihubungkan dengan tag <link rel=\"stylesheet\" href=\"css/style.css\"> di dalam tag <head> seluruh halaman.\n"
    "2. Internal CSS: Menggunakan tag <style> yang disematkan di dalam tag <head> masing-masing file HTML untuk styling spesifik halaman tersebut.\n"
    "3. Inline CSS: Diterapkan langsung pada atribut style=\"...\" pada elemen tertentu, misalnya pada kartu preview di hero section."
)

# 4. 4 CSS Categories
add_h1("4. Penjelasan 4 Kategori Properti CSS Wajib")
add_qa(
    "Sebutkan properti CSS apa saja yang Anda gunakan di masing-masing dari 4 kategori wajib!",
    "1. Background Properties (6): background-color, background-image, background-position, background-repeat, background-size, background-attachment.\n"
    "2. Text & Font Properties (7): font-family, font-size, font-weight, line-height, text-align, color, text-transform.\n"
    "3. Dimension Properties (5): width, min-width, max-width, height, min-height.\n"
    "4. Positioning Properties (6): position, top, bottom, left, right, z-index."
)

# 5. Box Model & Shadows
add_h1("5. Penjelasan Box Model, Border, dan Box-Shadow")
add_qa(
    "Bagaimana cara kerja box-shadow pada kartu di website Anda?",
    "Format CSS box-shadow adalah: box-shadow: offset-x offset-y blur color;\n"
    "Pada kartu website ini, saya menggunakan: box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);\n"
    "- 0: Bayangan lurus di tengah (tidak geser horizontal).\n"
    "- 2px: Bayangan turun 2px ke bawah.\n"
    "- 4px: Keburaman (blur) bayangan sebesar 4px agar lembut.\n"
    "- rgba(0, 0, 0, 0.06): Warna hitam dengan transparansi 6% sehingga terlihat natural dan bersih."
)
add_qa(
    "Bagaimana cara membuat kartu elemen berbeda-beda warnanya?",
    "Setiap kartu elemen diberi class tersendiri, lalu ditambahkan properti border-top: 3px solid <warna_elemen>;. Misalnya border-top: 3px solid #dc2626; untuk kartu elemen Api. Cara ini sangat rapi, simpel, dan tidak memerlukan efek bayangan neon yang rumit."
)

# 6. Form & Validation
add_h1("6. Penjelasan Form & Validasi (contact.html)")
add_qa(
    "Jelaskan 7 kontrol form yang Anda buat dan bagaimana validasinya!",
    "Formulir TAPOPS Cadet Enlistment memuat 7 kontrol wajib:\n"
    "1. Text Input: Untuk Nama Kadet dan Callsign (dengan atribut required dan placeholder).\n"
    "2. Password Input: Untuk Passcode Keamanan (type=\"password\", required, minlength=\"6\").\n"
    "3. Textarea: Tag <textarea rows=\"4\"> untuk Pesan Transmisi.\n"
    "4. Radio Buttons: Pilihan divisi dengan name=\"division\" agar bersifat mutually exclusive (hanya 1 yang bisa dipilih).\n"
    "5. Checkbox: Persetujuan kode etik kadet (type=\"checkbox\", required).\n"
    "6. Selection Dropdown: Tag <select> dengan <option> pilihan 7 elemen afinitas.\n"
    "7. Submit Button: Tag <button type=\"submit\"> untuk mengirim formulir."
)

doc.save("PANDUAN_PENJELASAN_CODE.docx")
print("PANDUAN_PENJELASAN_CODE.docx generated successfully!")
