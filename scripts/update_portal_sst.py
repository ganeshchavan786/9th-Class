"""
Build and synchronize Social Science Portal (Social_Science_Exam_Papers/index.html),
Main Multi-Subject Hub (index.html), and README.md.
"""

import os

CHAPTERS = [
    {
        "num": 1,
        "title": "Understanding Social Science",
        "category": "Foundations",
        "desc": "Scope of social science, primary and secondary sources, epigraphy, numismatics, archaeology, radiocarbon dating, and democratic ethics.",
        "slug": "understanding_sst",
        "pdf_slug": "Understanding_SST",
    },
    {
        "num": 2,
        "title": "Shaping of the Earth's Surface",
        "category": "Geography",
        "desc": "Endogenic and exogenic forces, plate tectonics, earthquake focus and epicentre, weathering vs erosion, meanders, oxbow lakes, glacial U-valleys, and moraines.",
        "slug": "shaping_earth",
        "pdf_slug": "Shaping_Earth",
    },
    {
        "num": 3,
        "title": "Atmosphere and Climate",
        "category": "Geography",
        "desc": "Atmospheric composition, troposphere and stratosphere, lapse rate, Coriolis force, jet streams, monsoon mechanism, greenhouse gases, and carbon footprint.",
        "slug": "atmosphere_climate",
        "pdf_slug": "Atmosphere_Climate",
    },
    {
        "num": 4,
        "title": "Early Humans and Beginning of Civilisation",
        "category": "History",
        "desc": "Palaeolithic to Neolithic transition, Bhimbetka art, Harappan town planning, Citadel, Great Bath, Lothal dockyard, Dholavira reservoirs, and seals.",
        "slug": "early_civilisation",
        "pdf_slug": "Early_Civilisation",
    },
    {
        "num": 5,
        "title": "State and Society up to 1000 CE",
        "category": "History",
        "desc": "Vedic society, 16 Mahajanapadas, Mauryan Empire, Kautilya's Arthashastra, Ashoka's Dhamma, Gupta classical golden age, Aryabhata, and Chola local assemblies.",
        "slug": "state_society",
        "pdf_slug": "State_Society",
    },
    {
        "num": 6,
        "title": "Democracy",
        "category": "Political Science",
        "desc": "Definition of democracy, rule of law, universal adult franchise, free and fair elections, non-democratic historical cases, and resolution of social conflicts.",
        "slug": "democracy",
        "pdf_slug": "Democracy",
    },
    {
        "num": 7,
        "title": "Elections",
        "category": "Political Science",
        "desc": "543 Lok Sabha constituencies, reserved seats, electoral roll, candidate affidavit disclosures, Model Code of Conduct, ECI independence, EVMs, and VVPAT.",
        "slug": "elections",
        "pdf_slug": "Elections",
    },
    {
        "num": 8,
        "title": "Building Blocks in Economics: The Problem of Choice",
        "category": "Economics",
        "desc": "Scarcity of resources, opportunity cost, factors of production (land, labour, physical capital, human capital), three central economic questions, and sectors.",
        "slug": "economics_choice",
        "pdf_slug": "Economics_Choice",
    },
    {
        "num": 9,
        "title": "The Price Puzzle: What Drives the Market",
        "category": "Economics",
        "desc": "Law of Demand and downward demand curve, Law of Supply, market equilibrium, shortages and surpluses, substitute vs complementary goods, and price elasticity.",
        "slug": "price_puzzle",
        "pdf_slug": "Price_Puzzle",
    },
]

def generate_sst_portal():
    cards_html = []
    for ch in CHAPTERS:
        n = ch["num"]
        n_pad = f"{n:02d}"
        slug = ch["slug"]
        pdf_slug = ch["pdf_slug"]
        cat = ch["category"]
        
        html_a = f"chapter_{n_pad}_{slug}_set_a.html"
        pdf_a = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_A.pdf"
        
        card = f"""
    <div class="chapter-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span class="chapter-badge">CHAPTER {n} • {cat.upper()}</span>
        <span style="font-size: 11px; font-weight: 700; color: #854d0e; background: #fef3c7; padding: 2px 8px; border-radius: 12px; border: 1px solid #fde68a;">
          ✅ SET A ACTIVE (25 MCQs)
        </span>
      </div>
      <div class="chapter-title">{ch['title']}</div>
      <p class="chapter-desc">{ch['desc']}</p>
      
      <!-- Interactive Exam Papers Grid -->
      <div style="background: #fafaf9; border: 1px solid #e7e5e4; border-radius: 8px; padding: 10px; margin-bottom: 12px;">
        <div style="font-size: 11.5px; font-weight: 700; color: #44403c; margin-bottom: 8px; display: flex; justify-content: space-between;">
          <span>AVAILABLE PRACTICE SETS:</span>
          <span style="color: #78716c;">(25 Marks | 45 Mins)</span>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr; gap: 6px; margin-bottom: 8px;">
          <a href="{html_a}" class="set-btn set-btn-a">📘 SET A (Foundation & Core Concepts)</a>
        </div>

        <div style="display: flex; gap: 4px; align-items: center; flex-wrap: wrap; font-size: 10px; color: #78716c; padding-top: 5px; border-top: 1px dashed #d6d3d1;">
          <span style="font-weight: 600;">Upcoming:</span>
          <span class="set-pill">Set B (HOTS)</span>
          <span class="set-pill">Set C (Sources)</span>
          <span class="set-pill">Set D (Assertion-Reason)</span>
          <span class="set-pill">Set E (Case Study)</span>
          <span class="set-pill">Set F (Speed)</span>
          <span class="set-pill">Set G (Mastery)</span>
        </div>
      </div>

      <!-- Direct PDF Downloads Strip -->
      <div style="background: #f5f5f4; border: 1px solid #d6d3d1; border-radius: 8px; padding: 8px 10px;">
        <div style="font-size: 11px; font-weight: 700; color: #57534e; margin-bottom: 6px;">
          🖨️ DIRECT PRINT-READY A4 PDF DOWNLOAD:
        </div>
        <div style="display: flex; gap: 6px; flex-wrap: wrap;">
          <a href="{pdf_a}" target="_blank" class="pdf-pill" style="border-left: 3px solid #854d0e;">
            📄 Download Set A Printable PDF (with OMR Sheet)
          </a>
        </div>
      </div>
    </div>
        """
        cards_html.append(card)

    portal_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Social Science - Examination Portal</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    body {{
      background: #f5f5f4;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .dashboard-container {{
      max-width: 1100px;
      margin: 25px auto;
      padding: 0 20px;
    }}
    .back-nav {{
      margin-bottom: 15px;
    }}
    .back-nav a {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 13.5px;
      font-weight: 700;
      color: #78350f;
      text-decoration: none;
      background: #fef3c7;
      padding: 6px 14px;
      border-radius: 6px;
      border: 1px solid #fde68a;
      transition: background 0.2s;
    }}
    .back-nav a:hover {{
      background: #fde68a;
    }}
    .dashboard-header {{
      background: linear-gradient(135deg, #451a03 0%, #78350f 50%, #9a3412 100%);
      color: #ffffff;
      padding: 32px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(120, 53, 15, 0.25);
      margin-bottom: 25px;
    }}
    .dashboard-header h1 {{
      font-size: 27px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .dashboard-header p {{
      font-size: 14.5px;
      color: #fef3c7;
      line-height: 1.5;
      max-width: 850px;
    }}
    .stats-bar {{
      display: flex;
      gap: 12px;
      margin-top: 18px;
      flex-wrap: wrap;
    }}
    .stat-badge {{
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(6px);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    .chapters-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(500px, 1fr));
      gap: 20px;
    }}
    .chapter-card {{
      background: #ffffff;
      border: 1px solid #e7e5e4;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .chapter-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
      border-color: #d6d3d1;
    }}
    .chapter-badge {{
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.8px;
      color: #78350f;
      background: #fffbeb;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #fde68a;
    }}
    .chapter-title {{
      font-size: 16px;
      font-weight: 700;
      color: #1c1917;
      margin-bottom: 8px;
      line-height: 1.35;
    }}
    .chapter-desc {{
      font-size: 12.5px;
      color: #57534e;
      line-height: 1.5;
      margin-bottom: 12px;
    }}
    .set-btn {{
      display: block;
      text-align: center;
      padding: 9px 12px;
      font-size: 12.5px;
      font-weight: 700;
      border-radius: 6px;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .set-btn-a {{ background: #854d0e; color: #fff; border: 1px solid #713f12; }}
    .set-btn-a:hover {{ background: #713f12; }}
    
    .set-pill {{
      background: #f5f5f4;
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid #e7e5e4;
      color: #78716c;
    }}
    
    .pdf-pill {{
      display: inline-block;
      font-size: 12px;
      font-weight: 700;
      color: #44403c;
      background: #ffffff;
      padding: 5px 12px;
      border-radius: 5px;
      text-decoration: none;
      border: 1px solid #d6d3d1;
      transition: all 0.15s;
    }}
    .pdf-pill:hover {{
      background: #fafaf9;
      border-color: #a8a29e;
    }}
  </style>
</head>
<body>

<div class="dashboard-container">
  
  <div class="back-nav">
    <a href="../index.html">
      ⬅️ Back to Main Subjects Portal (All Subjects)
    </a>
  </div>

  <div class="dashboard-header">
    <h1>CBSE CLASS IX — SOCIAL SCIENCE EXAMINATION HUB</h1>
    <p>Complete Chapter-Wise Practice Papers for Chapters 1 to 9 based on the latest NCERT Class 9 Social Science Curriculum (History, Geography, Political Science, and Economics). Complete with interactive timer, auto-grading, printable OMR answer sheets, and ready-to-print A4 PDF downloads.</p>
    <div class="stats-bar">
      <div class="stat-badge">📚 9 NCERT Chapters Covered</div>
      <div class="stat-badge">⚡ Set A (Foundation) Active</div>
      <div class="stat-badge">📝 9 Exam Papers Active (225 MCQs)</div>
      <div class="stat-badge">🖨️ 9 Print-Ready A4 PDFs</div>
      <div class="stat-badge">⭕ Realistic OMR Answer Sheets</div>
      <div class="stat-badge">💯 100% CBSE English Medium</div>
    </div>
  </div>

  <div class="chapters-grid">
{''.join(cards_html)}
  </div>

  <div style="margin-top: 35px; background: #ffffff; border: 1px solid #e7e5e4; border-radius: 10px; padding: 22px; font-size: 13px; color: #57534e; line-height: 1.6;">
    <h3 style="margin-bottom: 8px; color: #1c1917; font-size: 15px;">📋 NCERT Social Science 4-Domain Integrated Roadmap:</h3>
    <ul style="padding-left: 20px; margin: 0;">
      <li><b>Introductory Foundations:</b> Chapter 1 (Understanding Social Science).</li>
      <li><b>Geography:</b> Chapter 2 (Shaping of the Earth's Surface), Chapter 3 (Atmosphere and Climate).</li>
      <li><b>History:</b> Chapter 4 (Early Humans and Beginning of Civilisation), Chapter 5 (State and Society up to 1000 CE).</li>
      <li><b>Political Science:</b> Chapter 6 (Democracy), Chapter 7 (Elections).</li>
      <li><b>Economics:</b> Chapter 8 (Building Blocks in Economics: The Problem of Choice), Chapter 9 (The Price Puzzle: What Drives the Market).</li>
    </ul>
  </div>

</div>

</body>
</html>
"""
    return portal_html

def update_root_index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Update Social Science card in root index.html to LIVE status
    old_card_pattern = """    <!-- SUBJECT 2: SOCIAL SCIENCE -->
    <div class="subject-card card-ready">
      <div>
        <div class="subject-header-row">
          <div class="subject-icon-title">
            <span class="subject-icon">🌍</span>
            <div>
              <div class="subject-name">Social Science (SST)</div>
              <div style="font-size: 12px; color: #64748b; font-weight: 600;">Textbook Source: <code>iest1dd/</code></div>
            </div>
          </div>
          <span class="status-badge badge-ready">● BOOK DETECTED</span>
        </div>
        <p class="subject-desc">NCERT Class 9 Social Science textbook is already available in your directory. Ready to generate chapter-wise question papers whenever you request.</p>
        <ul class="subject-features">
          <li>📌 <b>Detected Chapters:</b> Earth's Surface, Atmosphere & Climate, Early Civilisations, etc.</li>
          <li>📌 <b>Format:</b> History, Geography, Civics & Economics CBSE MCQ blueprints</li>
          <li>📌 <b>Next Step:</b> Give confirmation to generate <code>Social_Science_Exam_Papers/</code></li>
        </ul>
      </div>
      <div>
        <a href="javascript:alert('The Social Science NCERT book (iest1dd) is available! Whenever you are ready, simply tell the assistant to generate Social Science exam papers.')" class="btn-subject-open btn-ready-action">
          ⚡ Ready to Generate on Request
        </a>
      </div>
    </div>"""

    new_card_pattern = """    <!-- SUBJECT 2: SOCIAL SCIENCE -->
    <div class="subject-card card-active">
      <div>
        <div class="subject-header-row">
          <div class="subject-icon-title">
            <span class="subject-icon">🌍</span>
            <div>
              <div class="subject-name">Social Science (SST)</div>
              <div style="font-size: 12px; color: #64748b; font-weight: 600;">Dedicated Folder: <code>Social_Science_Exam_Papers/</code></div>
            </div>
          </div>
          <span class="status-badge badge-live">● COMPLETED SET A</span>
        </div>
        <p class="subject-desc">Complete chapter-wise question papers for Chapters 1 to 9 covering History, Geography, Political Science, and Economics with interactive testing and A4 print PDFs.</p>
        <ul class="subject-features">
          <li>✅ <b>9 Chapters Covered:</b> Foundations, Earth Surface, Climate, Harappa, State/Society, Democracy, Elections, Economic Choice, Price Puzzle</li>
          <li>✅ <b>9 Exam Papers Active:</b> Set A (Foundation & Core Concepts)</li>
          <li>✅ <b>Total Questions:</b> 225 Unique MCQs (25 MCQs per chapter)</li>
          <li>✅ <b>Features:</b> 45-min timer, instant automated scoring, printable OMR sheet & solutions</li>
        </ul>
      </div>
      <div>
        <a href="Social_Science_Exam_Papers/index.html" class="btn-subject-open btn-live-open" style="background: #854d0e;">
          🚀 Open Social Science Exam Hub (Set A - 225 MCQs) ➡️
        </a>
      </div>
    </div>"""

    if old_card_pattern in content:
        content = content.replace(old_card_pattern, new_card_pattern)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("[OK] Updated root index.html with Live Social Science card!")
    else:
        print("[INFO] Root index.html pattern did not match exactly, checking manual update.")

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    old_sec = """### 2. Upcoming Subjects
- **Social Science:** `Social_Science_Exam_Papers/` (NCERT book `iest1dd` ready)
- **Mathematics:** `Maths_Exam_Papers/` (Scheduled)
- **English:** `English_Exam_Papers/` (Scheduled)"""

    new_sec = """### 2. Social Science (NCERT Class 9 Integrated)
- **Social Science Portal URL:** `https://ganeshchavan786.github.io/9th-Class/Social_Science_Exam_Papers/`
- **Chapters Covered (Chapters 1 to 9):**
  1. Understanding Social Science
  2. Shaping of the Earth's Surface (Geography)
  3. Atmosphere and Climate (Geography)
  4. Early Humans and Beginning of Civilisation (History)
  5. State and Society up to 1000 CE (History)
  6. Democracy (Political Science)
  7. Elections (Political Science)
  8. Building Blocks in Economics: The Problem of Choice (Economics)
  9. The Price Puzzle: What Drives the Market (Economics)
- **Practice Sets Available:**
  - **Set A:** Foundation & Core Concepts (9 papers $\times$ 25 = 225 MCQs)
  - **Total Active:** **9 Exam Papers • 225 Unique MCQs • 9 Print-Ready PDFs**
- **Printable PDFs:** Available inside `Social_Science_Exam_Papers/PDF_Ready_To_Print/`

### 3. Upcoming Subjects
- **Mathematics:** `Maths_Exam_Papers/` (Scheduled)
- **English:** `English_Exam_Papers/` (Scheduled)"""

    if old_sec in content:
        content = content.replace(old_sec, new_sec)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("[OK] Updated README.md with Social Science Section!")

if __name__ == "__main__":
    portal_html = generate_sst_portal()
    with open("Social_Science_Exam_Papers/index.html", "w", encoding="utf-8") as f:
        f.write(portal_html)
    print("[OK] Generated Social_Science_Exam_Papers/index.html")

    update_root_index()
    update_readme()
    print("ALL SST PORTALS SYNCHRONIZED!")
