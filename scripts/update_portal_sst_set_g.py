"""
Update and synchronize Social Science Portal (Social_Science_Exam_Papers/index.html),
Main Multi-Subject Hub (index.html), and README.md for Sets A, B, C, D, E, F, and G.
100% Curriculum Completion: 63 Exam Papers, 1,575 Unique MCQs, 63 Print-Ready A4 PDFs.
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
        html_b = f"chapter_{n_pad}_{slug}_set_b.html"
        html_c = f"chapter_{n_pad}_{slug}_set_c.html"
        html_d = f"chapter_{n_pad}_{slug}_set_d.html"
        html_e = f"chapter_{n_pad}_{slug}_set_e.html"
        html_f = f"chapter_{n_pad}_{slug}_set_f.html"
        html_g = f"chapter_{n_pad}_{slug}_set_g.html"
        
        pdf_a = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_A.pdf"
        pdf_b = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_B.pdf"
        pdf_c = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_C.pdf"
        pdf_d = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_D.pdf"
        pdf_e = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_E.pdf"
        pdf_f = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_F.pdf"
        pdf_g = f"PDF_Ready_To_Print/Class_9_SST_Ch{n_pad}_{pdf_slug}_Set_G.pdf"
        
        card = f"""
    <div class="chapter-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span class="chapter-badge">CHAPTER {n} • {cat.upper()}</span>
        <span style="font-size: 11px; font-weight: 700; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #86efac;">
          ✅ 100% COMPLETE (ALL 7 SETS • 175 MCQs)
        </span>
      </div>
      <div class="chapter-title">{ch['title']}</div>
      <p class="chapter-desc">{ch['desc']}</p>
      
      <!-- Interactive Exam Papers Grid -->
      <div style="background: #fafaf9; border: 1px solid #e7e5e4; border-radius: 8px; padding: 10px; margin-bottom: 12px;">
        <div style="font-size: 11.5px; font-weight: 700; color: #44403c; margin-bottom: 8px; display: flex; justify-content: space-between;">
          <span>AVAILABLE PRACTICE SETS:</span>
          <span style="color: #78716c;">(25 Marks each)</span>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
          <a href="{html_a}" class="set-btn set-btn-a">📘 SET A (Foundation)</a>
          <a href="{html_b}" class="set-btn set-btn-b">🔥 SET B (HOTS)</a>
          <a href="{html_c}" class="set-btn set-btn-c">📜 SET C (Sources)</a>
          <a href="{html_d}" class="set-btn set-btn-d">⚖️ SET D (Assertion-Reason)</a>
          <a href="{html_e}" class="set-btn set-btn-e">📑 SET E (Case Study)</a>
          <a href="{html_f}" class="set-btn set-btn-f">⚡ SET F (Speed Test - 30m)</a>
        </div>
        <div>
          <a href="{html_g}" class="set-btn set-btn-g">🏆 SET G (Final Mastery & Grand Challenge - 60m)</a>
        </div>
      </div>

      <!-- Direct PDF Downloads Strip -->
      <div style="background: #f5f5f4; border: 1px solid #d6d3d1; border-radius: 8px; padding: 8px 10px;">
        <div style="font-size: 11px; font-weight: 700; color: #57534e; margin-bottom: 6px;">
          🖨️ DIRECT PRINT-READY A4 PDF DOWNLOADS:
        </div>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          <a href="{pdf_a}" target="_blank" class="pdf-pill" style="border-left: 3px solid #854d0e;">
            📄 Set A
          </a>
          <a href="{pdf_b}" target="_blank" class="pdf-pill" style="border-left: 3px solid #d97706;">
            🔥 Set B
          </a>
          <a href="{pdf_c}" target="_blank" class="pdf-pill" style="border-left: 3px solid #059669;">
            📜 Set C
          </a>
          <a href="{pdf_d}" target="_blank" class="pdf-pill" style="border-left: 3px solid #9a3412;">
            ⚖️ Set D
          </a>
          <a href="{pdf_e}" target="_blank" class="pdf-pill" style="border-left: 3px solid #0f766e;">
            📑 Set E
          </a>
          <a href="{pdf_f}" target="_blank" class="pdf-pill" style="border-left: 3px solid #ea580c;">
            ⚡ Set F
          </a>
          <a href="{pdf_g}" target="_blank" class="pdf-pill" style="border-left: 3px solid #b91c1c;">
            🏆 Set G
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
  <title>CBSE Class 9 Social Science - Examination Portal (100% Curriculum Complete)</title>
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
      padding: 8px 6px;
      font-size: 11px;
      font-weight: 700;
      border-radius: 6px;
      text-decoration: none;
      transition: all 0.2s;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .set-btn-a {{ background: #854d0e; color: #fff; border: 1px solid #713f12; }}
    .set-btn-a:hover {{ background: #713f12; }}
    .set-btn-b {{ background: #d97706; color: #fff; border: 1px solid #b45309; }}
    .set-btn-b:hover {{ background: #b45309; }}
    .set-btn-c {{ background: #059669; color: #fff; border: 1px solid #047857; }}
    .set-btn-c:hover {{ background: #047857; }}
    .set-btn-d {{ background: #9a3412; color: #fff; border: 1px solid #7c2d12; }}
    .set-btn-d:hover {{ background: #7c2d12; }}
    .set-btn-e {{ background: #0f766e; color: #fff; border: 1px solid #115e59; }}
    .set-btn-e:hover {{ background: #115e59; }}
    .set-btn-f {{ background: #ea580c; color: #fff; border: 1px solid #c2410c; }}
    .set-btn-f:hover {{ background: #c2410c; }}
    .set-btn-g {{ background: linear-gradient(135deg, #b91c1c, #991b1b); color: #fff; border: 1px solid #7f1d1d; margin-top: 2px; }}
    .set-btn-g:hover {{ background: #7f1d1d; }}
    
    .pdf-pill {{
      display: inline-block;
      font-size: 10.5px;
      font-weight: 700;
      color: #44403c;
      background: #ffffff;
      padding: 3px 8px;
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
      <div class="stat-badge">🏆 100% Curriculum Completed (Sets A to G)</div>
      <div class="stat-badge">📝 63 Exam Papers Active (1,575 MCQs)</div>
      <div class="stat-badge">🖨️ 63 Print-Ready A4 PDFs</div>
      <div class="stat-badge">⭕ Realistic OMR Answer Sheets</div>
      <div class="stat-badge">💯 100% CBSE English Medium</div>
    </div>
  </div>

  <div class="chapters-grid">
{''.join(cards_html)}
  </div>

  <div style="margin-top: 35px; background: #ffffff; border: 1px solid #e7e5e4; border-radius: 10px; padding: 22px; font-size: 13px; color: #57534e; line-height: 1.6;">
    <h3 style="margin-bottom: 8px; color: #1c1917; font-size: 15px;">📋 NCERT Social Science Multi-Tier Roadmap (100% Complete):</h3>
    <ul style="padding-left: 20px; margin: 0;">
      <li><b>Set A (Foundation):</b> Core definitions, basic terminology, constitutional articles, and foundational historical facts.</li>
      <li><b>Set B (Advanced HOTS):</b> High-order analytical reasoning, geomorphic mechanics, institutional checks, and market disequilibrium.</li>
      <li><b>Set C (NCERT Sources & Tricky Questions):</b> Primary historical inscriptions, geographic cross-sections, statutory provisions, and economic decision matrices.</li>
      <li><b>Set D (Assertion - Reasoning Special):</b> Causal assertions, logical deductions, constitutional checks, geodynamic drivers, and microeconomic laws.</li>
      <li><b>Set E (Case Study & Source Scenarios):</b> Real-world evidentiary case studies, archaeological excavation profiles, synoptic meteorological models, and public policy interventions.</li>
      <li><b>Set F (Rapid Fire Speed Test):</b> 30-minute rapid recall challenge testing instant memory of constitutional provisions, geographic terms, historical dates, and market laws.</li>
      <li><b>Set G (Final Mastery & Grand Challenge Test):</b> 60-minute Olympiad and NTSE level grand challenge testing deep multi-disciplinary analytical rigor and constitutional jurisprudence.</li>
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

    # Update Social Science card stats
    content = content.replace("● SETS A, B, C, D, E & F ACTIVE", "● COMPLETED (SETS A TO G)")
    content = content.replace("● SETS A, B, C, D & E ACTIVE", "● COMPLETED (SETS A TO G)")
    content = content.replace("9 Exam Papers Active: Set A (Foundation & Core Concepts)",
                              "63 Exam Papers Active: Sets A to G (Foundation, HOTS, Sources, A/R, Case Study, Speed & Mastery)")
    content = content.replace("54 Exam Papers Active: Sets A to F (Foundation, HOTS, Sources, A/R, Case Study & Speed)",
                              "63 Exam Papers Active: Sets A to G (Foundation, HOTS, Sources, A/R, Case Study, Speed & Mastery)")
    content = content.replace("1,350 Unique MCQs (150 MCQs per chapter • 54 Print-Ready PDFs)",
                              "1,575 Unique MCQs (175 MCQs per chapter • 63 Print-Ready PDFs)")
    content = content.replace("🚀 🚀 Open Social Science Exam Hub (Sets A to F - 1,350 MCQs) ➡️",
                              "🚀 🚀 Open Complete Social Science Exam Hub (63 Papers • 1,575 MCQs) ➡️")
    content = content.replace("Open Social Science Exam Hub (Sets A to F - 1,350 MCQs) ➡️",
                              "Open Complete Social Science Exam Hub (63 Papers • 1,575 MCQs) ➡️")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated root index.html with Sets A to G (100% Complete)!")

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    old_sec = """  - **Set A:** Foundation & Core Concepts (9 papers $\\times$ 25 = 225 MCQs)
  - **Set B:** Advanced HOTS & Analytical Thinking (9 papers $\\times$ 25 = 225 MCQs)
  - **Set C:** NCERT In-Text Sources & Tricky Questions (9 papers $\\times$ 25 = 225 MCQs)
  - **Set D:** Assertion & Reasoning Special (9 papers $\\times$ 25 = 225 MCQs)
  - **Set E:** Case Study & Source-Based Scenarios (9 papers $\\times$ 25 = 225 MCQs)
  - **Set F:** Rapid Fire Speed Test (9 papers $\\times$ 25 = 225 MCQs)
  - **Total Active:** **54 Exam Papers • 1,350 Unique MCQs • 54 Print-Ready PDFs**"""

    new_sec = """  - **Set A:** Foundation & Core Concepts (9 papers $\\times$ 25 = 225 MCQs)
  - **Set B:** Advanced HOTS & Analytical Thinking (9 papers $\\times$ 25 = 225 MCQs)
  - **Set C:** NCERT In-Text Sources & Tricky Questions (9 papers $\\times$ 25 = 225 MCQs)
  - **Set D:** Assertion & Reasoning Special (9 papers $\\times$ 25 = 225 MCQs)
  - **Set E:** Case Study & Source-Based Scenarios (9 papers $\\times$ 25 = 225 MCQs)
  - **Set F:** Rapid Fire Speed Test (9 papers $\\times$ 25 = 225 MCQs)
  - **Set G:** Final Mastery & Grand Challenge Test (9 papers $\\times$ 25 = 225 MCQs)
  - **Total Active:** **63 Exam Papers • 1,575 Unique MCQs • 63 Print-Ready PDFs (100% Curriculum Complete)**"""

    if old_sec in content:
        content = content.replace(old_sec, new_sec)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("[OK] Updated README.md with Sets A to G!")
    else:
        print("[WARN] Could not find old_sec in README.md")

if __name__ == "__main__":
    portal_html = generate_sst_portal()
    with open("Social_Science_Exam_Papers/index.html", "w", encoding="utf-8") as f:
        f.write(portal_html)
    print("[OK] Generated Social_Science_Exam_Papers/index.html with Sets A to G (100% Complete)")

    update_root_index()
    update_readme()
    print("ALL SST PORTALS SYNCHRONIZED FOR SET G!")
