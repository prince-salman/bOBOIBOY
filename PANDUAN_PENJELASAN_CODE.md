# PANDUAN LENGKAP PENJELASAN CODE (PRESENTASI & UJIAN PRAKTIK)
## Proyek Web Programming: BoBoiBoy Universe Portal

Dokumen ini disiapkan khusus agar Anda dapat **menjelaskan seluruh kode proyek dengan lancar, percaya diri, dan mudah dipahami** saat dosen bertanya. Bahasa yang digunakan sederhana dan langsung ke inti konsep.

---

## 1. Konsep Arsitektur Master Frame (`index.html`)

### Pertanyaan Dosen:
> *"Bagaimana arsitektur website ini dibangun dan apa fungsi `index.html`?"*

### Jawaban Anda:
> *"Pak/Bu, website ini menggunakan arsitektur **Master Frame** sesuai ketentuan rubrik. File `index.html` bertindak sebagai bingkai induk (master shell) yang menampung header navigasi di bagian luar, dan sebuah tag `<iframe>` di bagian tengah untuk menampilkan 5 halaman konten utama."*

### Penjelasan Kodenya di `index.html`:
```html
<!-- Navigasi berada di luar iframe -->
<nav class="nav-menu">
  <ul class="nav-list">
    <li><a href="home.html" target="mainFrame" class="nav-link active">Home</a></li>
    <li><a href="characters.html" target="mainFrame" class="nav-link">Characters</a></li>
    <li><a href="elements.html" target="mainFrame" class="nav-link">Elements</a></li>
    <li><a href="series.html" target="mainFrame" class="nav-link">Series & Movies</a></li>
    <li><a href="contact.html" target="mainFrame" class="nav-link">Cadet Hub</a></li>
  </ul>
</nav>

<!-- Konten halaman dibuka di dalam iframe ini -->
<div class="main-frame-container">
  <iframe name="mainFrame" id="mainFrame" src="home.html"></iframe>
</div>
```

### Kunci yang Harus Diingat:
1. `name="mainFrame"` pada tag `<iframe>`: Memberikan nama unik pada frame target.
2. `target="mainFrame"` pada tag `<a>`: Menginstruksikan browser agar ketika link diklik, halaman yang dituju dibuka **di dalam iframe**, bukan me-refresh seluruh halaman web.

---

## 2. Struktur 5 Halaman Utama (Interconnected Pages)

Semua 5 halaman saling terhubung melalui menu navigasi yang sama:

1. **`home.html` (Beranda & Overview)**:
   - **Hero Section**: Judul besar promosi portal TAPOPS, deskripsi singkat, tombol CTA (*Explore Heroes* dan *Discover Elements*), serta kartu preview elemen.
   - **Stats Strip**: Menampilkan 4 kotak statistik (7 Elemental Tiers, 5 Core Heroes, 3 Feature Films, 100+ Galactic Episodes).
   - **Callout Box**: Kotak info dengan aksen garis oranye di sebelah kiri (`border-left: 4px solid var(--primary-orange)`).
   - **Cadet Protocol**: Menggunakan **Ordered List (`<ol>`)** untuk langkah-langkah bergabung menjadi kadet TAPOPS.
   - **Highlights & Lore**: Kartu ringkasan cerita BoBoiBoy dan Ochobot.

2. **`characters.html` (Dossier Karakter)**:
   - Menampilkan kartu profil 6 karakter utama: BoBoiBoy, Yaya, Ying, Gopal, Fang, dan Ochobot.
   - Avatar berbentuk lingkaran menggunakan `border-radius: 50%` dan `object-fit: cover`.
   - Bilah meteran kekuatan (*stat meters*) menggunakan `<div>` bertingkat: wadah abu-abu (`stat-bar`) dan isi warna (`stat-fill`) dengan lebar persentase.
   - Kartu mentor: Tok Aba dan Papa Zola.

3. **`elements.html` (7 Kekuatan Elemen & Fusi)**:
   - **Tingkatan Evolusi**: Menjelaskan Tier 1 (Dasar), Tier 2 (Evolusi), dan Tier 3 (Fusi) menggunakan Ordered List kedua (`<ol>`).
   - **7 Elemen**: Petir, Angin, Tanah, Api, Air, Daun, Cahaya. Masing-masing kartu dibedakan warna aksennya dengan garis tepi atas 3px (`border-top: 3px solid ...`).
   - **4 Elemen Fusi**: FrostFire, Glacier, Supra, dan SORI.
   - **Tabel Komparasi Elemen**: Menggunakan tag `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, dan `<td>`.

4. **`series.html` (Kronologi Serial & Film)**:
   - Garis waktu rilis mulai dari BoBoiBoy Klasik Season 1–3, BoBoiBoy The Movie 1, BoBoiBoy Galaxy Season 1–2, dan Movie 2.
   - **Tabel Urutan Nonton Resmi**: Memuat kolom Season, Tahun Rilis, Jumlah Episode, Format, dan Status Kanon.
   - Menggunakan Ordered List ketiga (`<ol>`) untuk panduan maraton menonton.

5. **`contact.html` (Cadet Hub & Formulir)**:
   - **Formulir Pendaftaran Kadet**: Memuat **7 jenis kontrol form** lengkap dengan validasi semantik HTML5.
   - **Tabel Metadata Mahasiswa**: Memuat NIM, Nama Ketua Kelompok, Program Studi, dan Anggota Kelompok.
   - **Accordion FAQ**: Tanya jawab seputar semesta BoBoiBoy menggunakan teknik CSS murni (checkbox toggle).

---

## 3. Penjelasan 3 Metode CSS yang Digunakan

### Pertanyaan Dosen:
> *"Di mana saja kamu menerapkan 3 metode penggunaan CSS (External, Internal, Inline)?"*

### Jawaban Anda:
1. **External CSS (File Terpisah)**:
   - Disimpan di file `css/style.css`.
   - Dihubungkan di dalam `<head>` setiap file HTML menggunakan:
     ```html
     <link rel="stylesheet" href="css/style.css">
     ```
   - Berisi seluruh aturan desain global: warna variabel, font, tata letak grid, navbar, tombol, dan footer.

2. **Internal CSS (Tag `<style>` di Head)**:
   - Diletakkan di dalam tag `<head>` masing-masing halaman HTML:
     ```html
     <style>
       .portal-announcement-banner {
         background-color: #f8fafc;
         border-left: 4px solid var(--primary-orange);
       }
     </style>
     ```
   - Berisi styling khusus komponen halaman tersebut (misal kotak pengumuman atau daftar bernomor khusus).

3. **Inline CSS (Atribut `style=""` pada elemen)**:
   - Diterapkan langsung pada tag HTML tertentu untuk memberikan gaya spesifik tanpa membuat class baru, contohnya:
     ```html
     <div style="background-color: #ffffff; width: 100%; max-width: 380px;">...</div>
     ```

---

## 4. Penjelasan 4 Kategori Properti CSS Wajib

Rubrik mewajibkan minimal 5 properti untuk setiap kategori berikut:

### Kategori 1: Background Properties
| Properti CSS | Fungsi yang Dijelaskan ke Dosen |
| :--- | :--- |
| `background-color` | Mengatur warna dasar latar belakang elemen (misal: `#ffffff`). |
| `background-image` | Menentukan gambar latar belakang (atau `none` jika polos). |
| `background-position` | Menentukan posisi awal gambar latar (misal: `center top`). |
| `background-repeat` | Mengatur perulangan gambar latar (`no-repeat` agar tidak berulang). |
| `background-size` | Mengatur ukuran gambar latar (`cover`, `contain`, atau `auto`). |
| `background-attachment` | Menentukan apakah background ikut digulir (`scroll`) atau tetap (`fixed`). |

### Kategori 2: Text and Font Properties
| Properti CSS | Fungsi yang Dijelaskan ke Dosen |
| :--- | :--- |
| `font-family` | Menentukan jenis rupa huruf (misal: Segoe UI, sans-serif). |
| `font-size` | Mengatur ukuran huruf (misal: `1rem`, `1.25rem`, `24px`). |
| `font-weight` | Mengatur ketebalan huruf (`400` normal, `600` semi-bold, `700` bold). |
| `line-height` | Mengatur jarak spasi antar baris teks (misal: `1.5` atau `1.6`). |
| `text-align` | Mengatur perataan teks (`left`, `center`, `right`, `justify`). |
| `color` | Menentukan warna teks (misal: `#0f172a` hitam pekat atau `#ff5722` oranye). |
| `text-transform` | Mengubah format huruf kapital (`uppercase`, `lowercase`, `capitalize`). |

### Kategori 3: Dimension Properties
| Properti CSS | Fungsi yang Dijelaskan ke Dosen |
| :--- | :--- |
| `width` | Menentukan lebar elemen (misal: `100%` atau `380px`). |
| `min-width` | Batas lebar terkecil agar elemen tidak terlalu menciut (misal: `280px`). |
| `max-width` | Batas lebar terbesar agar elemen tidak terlalu melar (misal: `1200px`). |
| `height` | Menentukan tinggi elemen (misal: `auto` atau `250px`). |
| `min-height` | Batas tinggi minimal elemen (misal: `100vh` atau `70px`). |

### Kategori 4: Positioning Properties
| Properti CSS | Fungsi yang Dijelaskan ke Dosen |
| :--- | :--- |
| `position` | Menentukan metode penempatan elemen (`relative`, `absolute`, `fixed`, `sticky`). |
| `top` | Mengatur jarak pergeseran dari tepi atas. |
| `bottom` | Mengatur jarak pergeseran dari tepi bawah. |
| `left` | Mengatur jarak pergeseran dari tepi kiri. |
| `right` | Mengatur jarak pergeseran dari tepi kanan. |
| `z-index` | Mengatur urutan tumpukan elemen di sumbu Z (angka lebih besar berada di atas). |

---

## 5. Penjelasan Box Model, Border, dan Shadow

### Pertanyaan Dosen:
> *"Bagaimana Anda mengatur kotak kartu dan bayangannya di CSS?"*

### Jawaban Anda:
1. **Konsep CSS Box Model**:
   - **Content**: Isi teks/gambar di dalam kartu.
   - **Padding**: Jarak bagian dalam antara konten dan garis tepi kotak (`padding: 1.5rem`).
   - **Border**: Garis tepi pembatas kotak (`border: 1px solid #e2e8f0`).
   - **Margin**: Jarak bagian luar kotak ke elemen lain (`margin-bottom: 2rem`).

2. **Mengapa sudutnya melengkung?**
   - Menggunakan `border-radius: 8px;` agar sudut tidak runcing dan tampil modern.

3. **Cara Kerja `box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);`**:
   - `0` (offset-x): Tidak bergeser ke kiri/kanan.
   - `2px` (offset-y): Bayangan jatuh 2px ke arah bawah.
   - `4px` (blur): Keburaman bayangan selebar 4px agar lembut.
   - `rgba(0, 0, 0, 0.06)`: Warna hitam dengan tingkat transparansi 6% sehingga terlihat natural dan bersih.

4. **Warna pembeda elemen di kartu:**
   - Dibuat sederhana dan elegan menggunakan garis aksen di bagian atas:
     ```css
     .glow-fire { border-top: 3px solid #dc2626; }
     .glow-wind { border-top: 3px solid #0284c7; }
     ```

---

## 6. Penjelasan Form & Validasi (Halaman `contact.html`)

### Pertanyaan Dosen:
> *"Formulir apa yang Anda buat dan bagaimana validasinya dilakukan?"*

### Jawaban Anda:
> *"Di halaman `contact.html`, terdapat formulir **TAPOPS Cadet Enlistment** yang memuat seluruh 7 jenis input sesuai ketentuan rubrik tanpa menggunakan JavaScript, melainkan memanfaatkan fitur validasi semantik HTML5 bawaan browser."*

### Rincian 7 Kontrol Form:
1. **Text Input**:
   - `id="cadet-name"` untuk Nama Lengkap kadet (`required`, `placeholder="Enter your full name"`).
   - `id="cadet-callsign"` untuk Nama Panggilan / Callsign.
2. **Password Input**:
   - `id="cadet-password"` dengan atribut `type="password"`, `required`, dan `minlength="6"`.
3. **Textarea**:
   - `id="transmission-message"` menggunakan tag `<textarea rows="4">` untuk pesan transmisi.
4. **Radio Buttons**:
   - Memilih Divisi Kadet (Recon, Defense, Heavy Artillery) dengan atribut `name="division"` agar hanya bisa memilih salah satu opsi.
5. **Checkbox**:
   - `id="honor-pledge"` dengan `type="checkbox"` dan `required` sebagai persetujuan kode etik kadet.
6. **Selection Dropdown**:
   - Tag `<select id="elemental-affinity">` dengan `<option>` pilihan 7 elemen.
7. **Submit Button**:
   - `<button type="submit">Submit Enlistment</button>` untuk mengeksekusi pengiriman formulir.

---

## 7. Rangkuman Bukti Kepatuhan Rubrik (Quick Recap)

Bila dosen menanyakan poin-poin kelengkapan rubrik secara cepat:
- **Master Frame**: Ada di `index.html` dengan `<iframe name="mainFrame">`.
- **5 Halaman Interkoneksi**: `home.html`, `characters.html`, `elements.html`, `series.html`, `contact.html`.
- **3 Metode CSS**: File terpisah (`style.css`), tag `<style>`, dan atribut inline `style=""`.
- **4 Kategori Properti CSS**: Background (6 properti), Text/Font (9 properti), Dimensi (5 properti), Posisi (6 properti).
- **Struktur Tambahan**: 4 Tabel, 4 Ordered List (`<ol>`), 24 Unordered List (`<ul>`).
- **Laporan Word**: File `Project_1_Web_Programming_Salman_Report.docx` (lengkap dengan screenshot dan pembahasan).
