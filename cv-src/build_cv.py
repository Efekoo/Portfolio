"""Efe Yılmaz CV'leri: tek stil, dört varyant (Backend / Gameplay x EN / TR).
Kullanım: python3 build_cv.py <çıktı_klasörü>
PDF'ler WeasyPrint ile üretilir; içerik değişince bu dosyayı düzenleyip yeniden çalıştırın.
"""
import sys
from pathlib import Path
from weasyprint import HTML

CSS = """
@page { size: A4; margin: 26pt 36.9pt 22pt 36.9pt; }
* { box-sizing: border-box; }
body { font-family: 'Liberation Sans', Arial, sans-serif; color: #1a1a1a; font-size: 9.4pt; line-height: 1.3; margin: 0; }
a { color: inherit; text-decoration: none; }
h1 { font-size: 19pt; text-align: center; margin: 0 0 2pt; }
.contact { text-align: center; font-size: 8.4pt; color: #333; margin-bottom: 6pt; }
h2 { font-size: 9.6pt; text-transform: uppercase; margin: 7pt 0 4pt; padding-bottom: 2pt; border-bottom: 0.75pt solid #555; }
p { margin: 0; }
.row { display: flex; justify-content: space-between; align-items: baseline; gap: 8pt; margin-bottom: 3.2pt; }
.when { font-size: 8.5pt; color: #555; white-space: nowrap; }
.meta { font-size: 8.8pt; font-style: italic; color: #444; }
.meta b { font-weight: bold; }
ul { margin: 1pt 0 3pt; padding-left: 12.4pt; }
li { margin-bottom: 2pt; }
.proj { margin-top: 3pt; }
.skills li { margin-bottom: 1.1pt; }
"""

CONTACT = {
    "en": "Istanbul, Türkiye",
    "tr": "İstanbul, Türkiye",
}


def contact(lang):
    return (f'{CONTACT[lang]} · <a href="mailto:efeylmz2612@gmail.com">efeylmz2612@gmail.com</a> · +90 530 011 0106 · '
            '<a href="https://github.com/Efekoo">github.com/Efekoo</a> · '
            '<a href="https://linkedin.com/in/efekoo">linkedin.com/in/efekoo</a> · '
            '<a href="https://efekoo.github.io/Portfolio">efekoo.github.io/Portfolio</a>')


GP = 'https://play.google.com/store/apps/details?id=com.devitapp.devit'
DEVIT_SITE = '<a href="https://devit-app.com/"><b>devit-app.com</b></a>'
GPLAY = f'<a href="{GP}"><b>Google Play</b></a>'
MF = '<a href="https://github.com/Efekoo/MatchForge">github.com/Efekoo/MatchForge</a>'
GSA = '<a href="https://github.com/Efekoo/Game_Services_API">github.com/Efekoo/Game_Services_API</a>'
GSA_DEMO = lambda t: f'<a href="https://gameservices-api.onrender.com/demo"><b>{t}</b></a>'


def project(title, meta, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="proj"><p><b>{title}</b> — <span class="meta">{meta}</span></p><ul>{lis}</ul></div>'


def edu(rows):
    return "".join(f'<div class="row"><span>{a}</span><span class="when">{b}</span></div>' for a, b in rows)


def skills(rows):
    return '<ul class="skills">' + "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in rows) + "</ul>"


def page(lang, sections):
    body = "".join(f"<h2>{h}</h2>{c}" for h, c in sections)
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>Efe Yılmaz CV</title>
<style>{CSS}</style></head><body><h1>Efe Yılmaz</h1><div class="contact">{contact(lang)}</div>{body}</body></html>"""


# ------------------------------------------------------------------ BACKEND EN
backend_en = page("en", [
    ("Summary", "<p>Backend-focused developer and Digital Game Design graduate, currently pursuing a non-thesis M.Sc. in Management "
     "Information Systems. Internship experience building REST APIs in C# / ASP.NET Core and a Unity mobile game; strong "
     "grounding in layered architecture, EF Core, PostgreSQL, Redis, JWT authentication, Docker, and automated testing with CI. "
     "Shipped DevIt's backend on Google Play; built matchmaking load-tested with 1,000 players. Seeking a "
     "junior backend role.</p>"),
    ("Education", edu([
        ("<b>Dokuz Eylül University</b> — Master's Degree, Management Information Systems (Non-Thesis)", "Online · 2026 – 2027 (Expected)"),
        ("<b>Istinye University</b> — Bachelor's Degree, Digital Game Design · GPA 3.21 / 4.00", "Istanbul · 2022 – 2026"),
    ])),
    ("Experience",
     '<div class="row" style="margin-bottom:0"><span><b>Software Developer Intern</b> · <i>KPlus Bilişim Teknolojileri A.Ş. / Asteri Game Studio</i></span>'
     '<span class="when">Istanbul · Jun 2025 – Oct 2025</span></div><ul>'
     "<li>Developed and tested backend features for business and application workflows using C#, ASP.NET Core, REST APIs, and SQL database operations.</li>"
     "<li>Built <b>Merge Vacuum</b>, a mobile casual puzzle game in Unity (C#, URP) for KPlus's in-house game studio, implementing the full gameplay loop and game-state UI across a 100+ script codebase.</li></ul>"),
    ("Projects",
     project("DevIt — Developer Team-Finding Platform", f"ASP.NET Core 9, EF Core, PostgreSQL, SignalR · {GPLAY} · {DEVIT_SITE}", [
         "Backend developer in a two-person team: four-layer ASP.NET Core 9 API with 10 controllers and 5 SignalR hubs (chat, notifications, admin) serving the Flutter app, web client, and admin panel.",
         "Production auth &amp; safety: JWT refresh-token rotation with reuse detection, Google OAuth, email verification, hashed reset codes with brute-force lockout, rate limiting, blocking, and account deletion.",
     ]) +
     project("MatchForge — Real-Time Matchmaking &amp; Lobby Service", f"ASP.NET Core, SignalR, Redis, PostgreSQL, RabbitMQ, nginx, k6, Docker, xUnit · {MF}", [
         "Built a real-time matchmaking &amp; lobby service closing the full player loop: JWT auth with refresh-token rotation, skill-based matchmaking with expanding Elo/MMR windows, SignalR lobbies, and hand-rolled Elo rating persisted to PostgreSQL.",
         "Solved race conditions with Redis distributed locks; load-tested with k6: <b>1,000 concurrent players matched, p95 match time 2.0 s, 0% failed requests</b> across 2 nginx load-balanced replicas with a SignalR Redis backplane.",
         "Added an event-driven stats service over RabbitMQ (MassTransit): transactional outbox, idempotent consumers via an inbox, retries and dead-letter queues; 42 tests with Testcontainers on GitHub Actions CI.",
     ]) +
     project("Game Services API", f"ASP.NET Core Web API, C#, EF Core, PostgreSQL, SignalR, Docker, xUnit · {GSA} · {GSA_DEMO('live demo')}", [
         "Designed a four-layer solution (API / Business / Core / DataAccess) exposing seven domain controllers: authentication, user management, currency, inventory, market economy, friends, and leaderboards.",
         "Implemented JWT authentication with BCrypt password hashing; used Entity Framework Core against PostgreSQL for all data access, with Swagger documentation for every endpoint.",
         "Built a SignalR real-time leaderboard broadcasting live standings; containerized with Docker Compose and covered by 24 xUnit tests on a GitHub Actions CI pipeline.",
     ]) +
     project("Investor — Algorithmic Trading Bot", 'Python, ccxt, pandas, SQLite, Optuna, Docker, pytest · <a href="https://github.com/Efekoo/Investor">github.com/Efekoo/Investor</a>', [
         "Built a modular trading bot: exchange abstraction over ccxt, eight pluggable strategies, and a risk module covering position sizing, stop-loss / trailing stop, and a daily circuit breaker.",
         "Developed a backtest engine simulating fees, slippage, and partial fills with Optuna optimization; designed a layered live-trading safety model (paper / live modes, kill switch); 19 pytest tests in GitHub Actions CI.",
     ])),
    ("Technical Skills", skills([
        ("Backend", "C#, ASP.NET Core, Entity Framework Core, REST APIs, PostgreSQL, Redis, SQL Server, SignalR, RabbitMQ / MassTransit, JWT Authentication, BCrypt, Swagger / OpenAPI, AutoMapper, FluentValidation"),
        ("Testing &amp; DevOps", "xUnit, Testcontainers, pytest, k6 Load Testing, Docker, Docker Compose, nginx, GitHub Actions CI"),
        ("Python", "pandas, ccxt, Optuna, LangGraph, Google Gemini API, Streamlit"),
        ("Game Development", "Unity, C#, Universal Render Pipeline"),
        ("Tools", "Git"),
    ])),
    ("Languages &amp; Certifications",
     "<p>Turkish (Native) · English (B2)</p><p><b>Foundational C# with Microsoft</b> — freeCodeCamp (Jul 2026) · <b>C# &amp; Python Intermediate</b> — Sololearn (Jan 2025)</p>"),
])

# ------------------------------------------------------------------ BACKEND TR
backend_tr = page("tr", [
    ("Özet", "<p>Dijital Oyun Tasarımı mezunu, backend odaklı bir geliştiriciyim; Yönetim Bilişim Sistemleri tezsiz yüksek lisansına devam "
     "ediyorum. Stajımda C# / ASP.NET Core ile REST API'ler ve Unity ile mobil bir oyun geliştirdim; katmanlı mimari, EF Core, "
     "PostgreSQL, Redis, JWT authentication, Docker ve CI'da otomatik test konularında sağlam bir temelim var. Google "
     "Play'deki DevIt'in backend'ini ve 1.000 oyuncuyla yük testli bir matchmaking servisi geliştirdim. Junior backend pozisyonu arıyorum.</p>"),
    ("Eğitim", edu([
        ("<b>Dokuz Eylül Üniversitesi</b> — Yüksek Lisans, Yönetim Bilişim Sistemleri (Tezsiz)", "Online · 2026 – 2027 (Beklenen)"),
        ("<b>İstinye Üniversitesi</b> — Lisans, Dijital Oyun Tasarımı · GNO 3,21 / 4,00", "İstanbul · 2022 – 2026"),
    ])),
    ("Deneyim",
     '<div class="row" style="margin-bottom:0"><span><b>Yazılım Geliştirici Stajyeri</b> · <i>KPlus Bilişim Teknolojileri A.Ş. / Asteri Game Studio</i></span>'
     '<span class="when">İstanbul · Haz 2025 – Eki 2025</span></div><ul>'
     "<li>C#, ASP.NET Core, REST API ve SQL veritabanı işlemleriyle iş ve uygulama akışlarına yönelik backend özellikleri geliştirdim ve test ettim.</li>"
     "<li>KPlus'ın kendi oyun stüdyosu için Unity (C#, URP) ile <b>Merge Vacuum</b> adlı mobil casual puzzle oyununu geliştirdim; 100+ script'lik kod tabanında oyun döngüsünün tamamını ve oyun durumu arayüzünü uyguladım.</li></ul>"),
    ("Projeler",
     project("DevIt — Yazılımcı Ekip Bulma Platformu", f"ASP.NET Core 9, EF Core, PostgreSQL, SignalR · {GPLAY} · {DEVIT_SITE}", [
         "İki kişilik ekipte backend geliştiricisi: Flutter uygulamasına, web istemcisine ve admin paneline hizmet veren, 10 controller ve 5 SignalR hub'ı (sohbet, bildirim, admin) içeren dört katmanlı ASP.NET Core 9 API.",
         "Production seviyesinde auth ve güvenlik: yeniden kullanım tespitli JWT refresh token rotasyonu, Google OAuth, e-posta doğrulama, brute-force kilitli hash'lenmiş sıfırlama kodları, rate limiting, engelleme ve hesap silme.",
     ]) +
     project("MatchForge — Gerçek Zamanlı Matchmaking &amp; Lobi Servisi", f"ASP.NET Core, SignalR, Redis, PostgreSQL, RabbitMQ, nginx, k6, Docker, xUnit · {MF}", [
         "Oyuncu döngüsünü uçtan uca kapatan matchmaking ve lobi servisi: refresh token rotasyonlu JWT authentication, genişleyen Elo/MMR aralıklarıyla skill-based matchmaking, SignalR lobileri ve PostgreSQL'de saklanan Elo puanı.",
         "Redis distributed lock ile race condition'ları çözdüm; k6 yük testi: 2 nginx load-balanced replika ve SignalR Redis backplane üzerinde <b>1.000 eşzamanlı oyuncu eşleştirildi, p95 eşleşme süresi 2,0 sn, %0 hatalı istek</b>.",
         "RabbitMQ (MassTransit) üzerinden olay güdümlü istatistik servisi ekledim: transactional outbox, inbox ile idempotent consumer'lar, retry ve dead-letter kuyrukları; GitHub Actions CI'da Testcontainers ile 42 test.",
     ]) +
     project("Game Services API", f"ASP.NET Core Web API, C#, EF Core, PostgreSQL, SignalR, Docker, xUnit · {GSA} · {GSA_DEMO('canlı demo')}", [
         "API / Business / Core / DataAccess olmak üzere dört katmanlı bir çözüm tasarladım; authentication, kullanıcı yönetimi, para birimi, envanter, market ekonomisi, arkadaşlar ve liderlik tablosu olmak üzere yedi domain controller sundum.",
         "BCrypt parola hash'leme ile JWT authentication uyguladım; tüm veri erişimini PostgreSQL üzerinde Entity Framework Core ile gerçekleştirdim ve her endpoint'i Swagger ile dokümante ettim.",
         "Canlı sıralamayı yayınlayan SignalR gerçek zamanlı liderlik tablosu geliştirdim; Docker Compose ile container'laştırdım ve GitHub Actions CI'da 24 xUnit testiyle kapsadım.",
     ]) +
     project("Investor — Algoritmik Alım-Satım Botu", 'Python, ccxt, pandas, SQLite, Optuna, Docker, pytest · <a href="https://github.com/Efekoo/Investor">github.com/Efekoo/Investor</a>', [
         "Modüler bir trading bot geliştirdim: ccxt üzerine exchange soyutlaması, sekiz takılabilir strateji ve pozisyon büyüklüğü, stop-loss / trailing stop ile günlük devre kesiciyi kapsayan risk modülü.",
         "Komisyon, slippage ve kısmi dolumları simüle eden, Optuna ile optimize edilen bir backtest motoru geliştirdim; katmanlı canlı işlem güvenlik modeli (paper / live mod, kill switch) tasarladım; GitHub Actions CI'da 19 pytest testi.",
     ])),
    ("Teknik Yetkinlikler", skills([
        ("Backend", "C#, ASP.NET Core, Entity Framework Core, REST API, PostgreSQL, Redis, SQL Server, SignalR, RabbitMQ / MassTransit, JWT Authentication, BCrypt, Swagger / OpenAPI, AutoMapper, FluentValidation"),
        ("Test &amp; DevOps", "xUnit, Testcontainers, pytest, k6 yük testi, Docker, Docker Compose, nginx, GitHub Actions CI"),
        ("Python", "pandas, ccxt, Optuna, LangGraph, Google Gemini API, Streamlit"),
        ("Oyun Geliştirme", "Unity, C#, Universal Render Pipeline"),
        ("Araçlar", "Git"),
    ])),
    ("Diller &amp; Sertifikalar",
     "<p>Türkçe (Ana dil) · İngilizce (B2)</p><p><b>Foundational C# with Microsoft</b> — freeCodeCamp (Tem 2026) · <b>C# &amp; Python Intermediate</b> — Sololearn (Oca 2025)</p>"),
])

# ------------------------------------------------------------------ GAMEPLAY EN
APOLLO = '<a href="https://github.com/Efekoo/APOLLO">github.com/Efekoo/APOLLO</a>'
SE7EN = '<a href="https://github.com/Efekoo/SE7EN">github.com/Efekoo/SE7EN</a>'

gameplay_en = page("en", [
    ("Summary", "<p>Gameplay programmer and Digital Game Design graduate with studio internship experience developing a mobile casual "
     "puzzle game in Unity. Hands-on with core gameplay systems across genres, including grid-based puzzles, platformer / "
     "shooter hybrids, and isometric action-RPG systems, plus backend skills (ASP.NET Core, REST APIs, real-time matchmaking) "
     "for game services. Seeking a junior gameplay / game developer role.</p>"),
    ("Education", edu([
        ("<b>Dokuz Eylül University</b> — Master's Degree, Management Information Systems (Non-Thesis)", "Online · 2026 – 2027 (Expected)"),
        ("<b>Istinye University</b> — Bachelor's Degree, Digital Game Design · GPA 3.21 / 4.00", "Istanbul · 2022 – 2026"),
    ])),
    ("Experience",
     '<div class="row" style="margin-bottom:0"><span><b>Game Developer Intern</b> · <i>Asteri Game Studio (KPlus Bilişim Teknolojileri A.Ş.)</i></span>'
     '<span class="when">Istanbul · Jun 2025 – Oct 2025</span></div><ul>'
     "<li>Developed <b>Merge Vacuum</b>, a mobile casual puzzle game in Unity (C#, URP), implementing the core puzzle loop: drag-and-drop grid interaction, match detection, and collapse / refill logic.</li>"
     "<li>Built level-objective systems (collector goals, multi-objective levels, ice obstacles), plus boosters and tutorial hints.</li>"
     "<li>Developed the full game-state UI flow (gameplay, victory, defeat, objective feedback) with Unity UI and TextMeshPro across a 100+ script codebase.</li>"
     "<li>Modeled missing 3D props (crates and other in-game objects) in Autodesk Maya and integrated them into the game to complete the existing 2D asset set.</li>"
     "<li>Additionally contributed to backend development at KPlus, building and testing REST API features with C#, ASP.NET Core, and SQL.</li></ul>"),
    ("Projects",
     project("Apollo", f"Unity, C#, URP, Unity Input System · {APOLLO}", [
         "Hybrid 2D platformer / space shooter with planet selection, mission phases, resource collection, and ship upgrades.",
         "Implemented global game-state and scene-transition systems, player movement, enemy spawning, and upgrade mechanics across a 100+ script codebase.",
     ]) +
     project("Seven Layers of Carnage", f"Unity, C#, URP, Unity Input System · {SE7EN}", [
         "2D isometric action-RPG inspired by Dante's Inferno, with layered level progression and boss encounters.",
         "Built inventory, hotbar, loot, crafting, shop, and quest-tracking systems along with the core combat and progression flow.",
     ]) +
     project("MatchForge — Real-Time Matchmaking &amp; Lobby Service", f"ASP.NET Core, SignalR, Redis, PostgreSQL, RabbitMQ, Docker · {MF}", [
         "The backend behind competitive multiplayer: skill-based matchmaking with expanding Elo/MMR windows, real-time SignalR lobbies with reconnect handling, Redis distributed locks, and an event-driven stats service over RabbitMQ; load-tested with <b>1,000 concurrent players (p95 match time 2.0 s, 0% failed requests)</b>.",
     ]) +
     project("Game Services API", f"ASP.NET Core Web API, C#, EF Core, PostgreSQL, SignalR, Docker · {GSA} · {GSA_DEMO('live demo')}", [
         "Backend API for game systems (authentication, player progression, inventory, market economy, friends, and leaderboards) with a SignalR real-time leaderboard, Docker Compose setup, and a CI-tested codebase (24 xUnit tests); directly applicable to live-service game backends.",
     ]) +
     project("DevIt — Developer Team-Finding Platform", f"ASP.NET Core 9, PostgreSQL, SignalR · {GPLAY} · {DEVIT_SITE}", [
         "Backend developer in a two-person team for an app <b>live on Google Play</b>: four-layer ASP.NET Core 9 API with real-time SignalR chat and notifications, JWT / Google OAuth authentication, and production hardening.",
     ])),
    ("Technical Skills", skills([
        ("Game Development", "Unity, C#, Universal Render Pipeline, Unity Input System, Unity UI, 2D gameplay systems (grid puzzles, platformers, isometric ARPG)"),
        ("Backend for Games", "ASP.NET Core, Entity Framework Core, REST APIs, PostgreSQL, Redis, SignalR, RabbitMQ, JWT Authentication, Docker"),
        ("AI &amp; Scripting", "Python, LangGraph, Google Gemini API"),
        ("Tools", "Git, Autodesk Maya (3D asset modeling)"),
    ])),
    ("Languages &amp; Certifications",
     "<p>Turkish (Native) · English (B2)</p><p><b>Foundational C# with Microsoft</b> — freeCodeCamp (Jul 2026) · <b>C# &amp; Python Intermediate</b> — Sololearn (Jan 2025)</p>"),
])

# ------------------------------------------------------------------ GAMEPLAY TR
gameplay_tr = page("tr", [
    ("Özet", "<p>Dijital Oyun Tasarımı mezunu bir gameplay programcısıyım; stüdyo stajımda Unity ile mobil bir casual puzzle oyunu "
     "geliştirdim. Grid tabanlı bulmaca, platformer / shooter melezi ve izometrik aksiyon-RPG gibi farklı türlerde temel gameplay "
     "sistemlerinde deneyimliyim; ayrıca oyun servisleri için backend (ASP.NET Core, REST API, gerçek zamanlı matchmaking) "
     "becerilerim var. Junior gameplay / oyun geliştirici pozisyonu arıyorum.</p>"),
    ("Eğitim", edu([
        ("<b>Dokuz Eylül Üniversitesi</b> — Yüksek Lisans, Yönetim Bilişim Sistemleri (Tezsiz)", "Online · 2026 – 2027 (Beklenen)"),
        ("<b>İstinye Üniversitesi</b> — Lisans, Dijital Oyun Tasarımı · GNO 3,21 / 4,00", "İstanbul · 2022 – 2026"),
    ])),
    ("Deneyim",
     '<div class="row" style="margin-bottom:0"><span><b>Oyun Geliştirici Stajyeri</b> · <i>Asteri Game Studio (KPlus Bilişim Teknolojileri A.Ş.)</i></span>'
     '<span class="when">İstanbul · Haz 2025 – Eki 2025</span></div><ul>'
     "<li>Unity (C#, URP) ile mobil casual puzzle oyunu <b>Merge Vacuum</b>'ı geliştirdim; sürükle-bırak grid etkileşimi, eşleşme tespiti ve çökme / yeniden doldurma mantığından oluşan temel bulmaca döngüsünü uyguladım.</li>"
     "<li>Seviye hedef sistemlerini (toplayıcı hedefler, çok hedefli seviyeler, buz engelleri), booster'ları ve ipucu akışını geliştirdim.</li>"
     "<li>Unity UI ve TextMeshPro ile oyun durumu arayüz akışının tamamını (oynanış, zafer, yenilgi, hedef geri bildirimi) 100+ script'lik kod tabanında geliştirdim.</li>"
     "<li>Eksik 3D prop'ları (sandıklar ve diğer oyun içi nesneler) Autodesk Maya'da modelleyip oyuna entegre ederek mevcut 2D varlık setini tamamladım.</li>"
     "<li>Ek olarak KPlus'ta C#, ASP.NET Core ve SQL ile REST API özellikleri geliştirip test ederek backend'e katkı verdim.</li></ul>"),
    ("Projeler",
     project("Apollo", f"Unity, C#, URP, Unity Input System · {APOLLO}", [
         "Gezegen seçimi, görev aşamaları, kaynak toplama ve gemi yükseltmeleri içeren hibrit 2D platformer / uzay shooter.",
         "100+ script'lik kod tabanında global oyun durumu ve sahne geçiş sistemlerini, oyuncu hareketini, düşman spawn'ını ve yükseltme mekaniklerini uyguladım.",
     ]) +
     project("Seven Layers of Carnage", f"Unity, C#, URP, Unity Input System · {SE7EN}", [
         "Dante'nin Cehennem'inden esinlenen, katmanlı seviye ilerleyişi ve boss karşılaşmaları içeren 2D izometrik aksiyon-RPG.",
         "Temel savaş ve ilerleme akışının yanı sıra envanter, hotbar, loot, crafting, dükkân ve görev takip sistemlerini geliştirdim.",
     ]) +
     project("MatchForge — Gerçek Zamanlı Matchmaking &amp; Lobi Servisi", f"ASP.NET Core, SignalR, Redis, PostgreSQL, RabbitMQ, Docker · {MF}", [
         "Rekabetçi çok oyunculunun arkasındaki backend: genişleyen Elo/MMR aralıklarıyla skill-based matchmaking, yeniden bağlanma destekli gerçek zamanlı SignalR lobileri, Redis distributed lock ve RabbitMQ üzerinden olay güdümlü istatistik servisi; <b>1.000 eşzamanlı oyuncuyla yük testi (p95 eşleşme süresi 2,0 sn, %0 hatalı istek)</b>.",
     ]) +
     project("Game Services API", f"ASP.NET Core Web API, C#, EF Core, PostgreSQL, SignalR, Docker · {GSA} · {GSA_DEMO('canlı demo')}", [
         "Oyun sistemleri (authentication, oyuncu ilerleyişi, envanter, market ekonomisi, arkadaşlar, liderlik tablosu) için backend API; SignalR gerçek zamanlı liderlik tablosu, Docker Compose kurulumu ve CI'da test edilen kod tabanıyla (24 xUnit testi) canlı servis oyun backend'lerine doğrudan uygulanabilir.",
     ]) +
     project("DevIt — Yazılımcı Ekip Bulma Platformu", f"ASP.NET Core 9, PostgreSQL, SignalR · {GPLAY} · {DEVIT_SITE}", [
         "İki kişilik ekipte <b>Google Play'de yayındaki</b> uygulamanın backend geliştiricisi: SignalR ile gerçek zamanlı sohbet ve bildirimler, JWT / Google OAuth ve production güvenlik önlemleri içeren ASP.NET Core 9 API.",
     ])),
    ("Teknik Yetkinlikler", skills([
        ("Oyun Geliştirme", "Unity, C#, Universal Render Pipeline, Unity Input System, Unity UI, 2D gameplay sistemleri (grid bulmacalar, platformer, izometrik ARPG)"),
        ("Oyunlar İçin Backend", "ASP.NET Core, Entity Framework Core, REST API, PostgreSQL, Redis, SignalR, RabbitMQ, JWT Authentication, Docker"),
        ("Yapay Zekâ &amp; Scripting", "Python, LangGraph, Google Gemini API"),
        ("Araçlar", "Git, Autodesk Maya (3D varlık modelleme)"),
    ])),
    ("Diller &amp; Sertifikalar",
     "<p>Türkçe (Ana dil) · İngilizce (B2)</p><p><b>Foundational C# with Microsoft</b> — freeCodeCamp (Tem 2026) · <b>C# &amp; Python Intermediate</b> — Sololearn (Oca 2025)</p>"),
])

VARIANTS = {
    "Efe_Yilmaz_Backend_CV": backend_en,
    "Efe_Yilmaz_Backend_CV_TR": backend_tr,
    "Efe_Yilmaz_Gameplay_CV": gameplay_en,
    "Efe_Yilmaz_Gameplay_CV_TR": gameplay_tr,
}

if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    for name, html in VARIANTS.items():
        doc = HTML(string=html).render()
        doc.write_pdf(out / f"{name}.pdf")
        (out / f"{name}.html").write_text(html, encoding="utf-8")
        print(f"{name}: {len(doc.pages)} page(s)")
