"""
Update and synchronize all portals (Science index, root index, README) for all 7 sets (Sets A through G).
Total: 56 Exam Papers, 1,400 Unique MCQs, 56 Print-Ready A4 PDFs.
"""

import os

CHAPTERS = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "desc": "Scientific inquiry, SI units, variables, laboratory apparatus, vernier/screw gauge measurement, zero error, and experimental accuracy.",
        "slug": "exploration",
        "pdf_slug": "Exploration",
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "desc": "Cell theory, microscopy, prokaryotic vs eukaryotic cells, plant vs animal cells, plasma membrane, osmosis, diffusion, and cell organelles.",
        "slug": "cell",
        "pdf_slug": "Cell",
    },
    {
        "num": 3,
        "title": "Tissues: Plant & Animal Structures",
        "desc": "Meristematic tissues, simple permanent (parenchyma, collenchyma, sclerenchyma), complex permanent (xylem, phloem), epithelial, connective, muscular, and nervous tissues.",
        "slug": "tissues",
        "pdf_slug": "Tissues",
    },
    {
        "num": 4,
        "title": "Describing Motion & Kinematics",
        "desc": "Distance vs displacement, speed and velocity, uniform & non-uniform motion, acceleration, graphical representations, equations of motion, and uniform circular motion.",
        "slug": "motion",
        "pdf_slug": "Motion",
    },
    {
        "num": 5,
        "title": "Exploring Mixtures: Solution, Colloid & Suspension",
        "desc": "Pure substances vs mixtures, types of solutions, concentration, solubility, suspensions, colloidal properties, Tyndall effect, and separation methods.",
        "slug": "mixtures",
        "pdf_slug": "Mixtures",
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion & Laws of Motion",
        "desc": "Balanced and unbalanced forces, Newton's first, second, and third laws of motion, inertia and mass, momentum, and conservation of momentum.",
        "slug": "forces",
        "pdf_slug": "Forces",
    },
    {
        "num": 7,
        "title": "Work, Energy & Simple Machines",
        "desc": "Scientific concept of work, work done by constant force, kinetic and potential energy, law of conservation of energy, rate of doing work (power), and mechanical advantage.",
        "slug": "work_energy",
        "pdf_slug": "Work_Energy",
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom: Structure & Composition",
        "desc": "Charged particles in matter, Thomson's model, Rutherford's alpha particle scattering experiment, Bohr's atomic model, neutrons, distribution of electrons, valency, atomic number, and isotopes.",
        "slug": "atom",
        "pdf_slug": "Atom",
    },
]

def generate_science_portal():
    cards_html = []
    for ch in CHAPTERS:
        n = ch["num"]
        n_pad = f"{n:02d}"
        slug = ch["slug"]
        pdf_slug = ch["pdf_slug"]
        
        # HTML file names
        html_a = f"chapter_{n_pad}_{slug}.html"
        html_b = f"chapter_{n_pad}_{slug}_set_b.html"
        html_c = f"chapter_{n_pad}_{slug}_set_c.html"
        html_d = f"chapter_{n_pad}_{slug}_set_d.html"
        html_e = f"chapter_{n_pad}_{slug}_set_e.html"
        html_f = f"chapter_{n_pad}_{slug}_set_f.html"
        html_g = f"chapter_{n_pad}_{slug}_set_g.html"
        
        # PDF file names
        pdf_a = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_A.pdf"
        pdf_b = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_B.pdf"
        pdf_c = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_C.pdf"
        pdf_d = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_D.pdf"
        pdf_e = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_E.pdf"
        pdf_f = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_F.pdf"
        pdf_g = f"PDF_Ready_To_Print/Class_9_Science_Ch{n_pad}_{pdf_slug}_Set_G.pdf"
        
        card = f"""
    <div class="chapter-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span class="chapter-badge">CHAPTER {n}</span>
        <span style="font-size: 11px; font-weight: 700; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #86efac;">
          ✅ ALL 7 SETS ACTIVE (175 MCQs)
        </span>
      </div>
      <div class="chapter-title">{ch['title']}</div>
      <p class="chapter-desc">{ch['desc']}</p>
      
      <!-- Interactive Exam Papers Grid -->
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; margin-bottom: 12px;">
        <div style="font-size: 11.5px; font-weight: 700; color: #334155; margin-bottom: 8px; display: flex; justify-content: space-between;">
          <span>ONLINE INTERACTIVE EXAM PAPERS:</span>
          <span style="color: #64748b;">(Auto-Grading & Timer)</span>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-bottom: 6px;">
          <a href="{html_a}" class="set-btn set-btn-a">📘 SET A (Foundation)</a>
          <a href="{html_b}" class="set-btn set-btn-b">🔥 SET B (HOTS)</a>
          <a href="{html_c}" class="set-btn set-btn-c">🎯 SET C (Exemplar)</a>
          <a href="{html_d}" class="set-btn set-btn-d">⚡ SET D (Assertion-Reason)</a>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
          <a href="{html_e}" class="set-btn set-btn-e">🔬 SET E (Case Study)</a>
          <a href="{html_f}" class="set-btn set-btn-f">⚡ SET F (Rapid Fire)</a>
          <a href="{html_g}" class="set-btn set-btn-g">🏆 SET G (Mastery)</a>
        </div>
      </div>

      <!-- Direct PDF Downloads Strip -->
      <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 8px; padding: 8px 10px;">
        <div style="font-size: 11px; font-weight: 700; color: #475569; margin-bottom: 6px;">
          🖨️ DIRECT PRINT-READY A4 PDF DOWNLOADS:
        </div>
        <div style="display: flex; gap: 5px; flex-wrap: wrap;">
          <a href="{pdf_a}" target="_blank" class="pdf-pill" style="border-left: 3px solid #1e40af;">PDF A</a>
          <a href="{pdf_b}" target="_blank" class="pdf-pill" style="border-left: 3px solid #d97706;">PDF B</a>
          <a href="{pdf_c}" target="_blank" class="pdf-pill" style="border-left: 3px solid #047857;">PDF C</a>
          <a href="{pdf_d}" target="_blank" class="pdf-pill" style="border-left: 3px solid #6d28d9;">PDF D</a>
          <a href="{pdf_e}" target="_blank" class="pdf-pill" style="border-left: 3px solid #0284c7;">PDF E</a>
          <a href="{pdf_f}" target="_blank" class="pdf-pill" style="border-left: 3px solid #ea580c;">PDF F</a>
          <a href="{pdf_g}" target="_blank" class="pdf-pill" style="border-left: 3px solid #b91c1c;">PDF G</a>
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
  <title>CBSE Class 9 Science - Complete Multi-Set Examination Portal</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    body {{
      background: #f1f5f9;
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
      color: #1e40af;
      text-decoration: none;
      background: #e0e7ff;
      padding: 6px 14px;
      border-radius: 6px;
      transition: background 0.2s;
    }}
    .back-nav a:hover {{
      background: #c7d2fe;
    }}
    .dashboard-header {{
      background: linear-gradient(135deg, #0f172a 0%, #0369a1 50%, #0284c7 100%);
      color: #ffffff;
      padding: 32px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(2, 132, 199, 0.25);
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
      color: #e0f2fe;
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
      border: 1px solid #e2e8f0;
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
      border-color: #cbd5e1;
    }}
    .chapter-badge {{
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 1px;
      color: #0369a1;
      background: #f0f9ff;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #bae6fd;
    }}
    .chapter-title {{
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
      line-height: 1.35;
    }}
    .chapter-desc {{
      font-size: 12.5px;
      color: #64748b;
      line-height: 1.5;
      margin-bottom: 12px;
    }}
    .set-btn {{
      display: block;
      text-align: center;
      padding: 7px 6px;
      font-size: 11.5px;
      font-weight: 700;
      border-radius: 6px;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .set-btn-a {{ background: #1e40af; color: #fff; border: 1px solid #1e3a8a; }}
    .set-btn-a:hover {{ background: #1d4ed8; }}
    .set-btn-b {{ background: #d97706; color: #fff; border: 1px solid #b45309; }}
    .set-btn-b:hover {{ background: #b45309; }}
    .set-btn-c {{ background: #047857; color: #fff; border: 1px solid #065f46; }}
    .set-btn-c:hover {{ background: #065f46; }}
    .set-btn-d {{ background: #6d28d9; color: #fff; border: 1px solid #5b21b6; }}
    .set-btn-d:hover {{ background: #5b21b6; }}
    .set-btn-e {{ background: #0284c7; color: #fff; border: 1px solid #0369a1; }}
    .set-btn-e:hover {{ background: #0369a1; }}
    .set-btn-f {{ background: #ea580c; color: #fff; border: 1px solid #c2410c; }}
    .set-btn-f:hover {{ background: #c2410c; }}
    .set-btn-g {{ background: #b91c1c; color: #fff; border: 1px solid #991b1b; }}
    .set-btn-g:hover {{ background: #991b1b; }}
    
    .pdf-pill {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: #334155;
      background: #ffffff;
      padding: 3px 8px;
      border-radius: 4px;
      text-decoration: none;
      border: 1px solid #cbd5e1;
      transition: all 0.15s;
    }}
    .pdf-pill:hover {{
      background: #f8fafc;
      border-color: #94a3b8;
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
    <h1>CBSE CLASS IX — SCIENCE EXAMINATION HUB</h1>
    <p>Complete Chapter-Wise Practice Papers for Chapters 1 to 8 based on the NCERT Class 9 Science Curriculum. Complete 7-tier mastery roadmap (Foundation, HOTS, Exemplar, Assertion-Reason, Case Study, Rapid Fire, and Grand Challenge) with interactive timer, auto-grading, printable OMR sheets, and ready-to-print A4 PDF downloads.</p>
    <div class="stats-bar">
      <div class="stat-badge">📚 8 NCERT Chapters Covered</div>
      <div class="stat-badge">⚡ 7 Complete Practice Sets (A, B, C, D, E, F & G)</div>
      <div class="stat-badge">📝 56 Exam Papers Active (1,400 MCQs)</div>
      <div class="stat-badge">🖨️ 56 Print-Ready A4 PDFs</div>
      <div class="stat-badge">⭕ Realistic OMR Answer Sheets</div>
      <div class="stat-badge">💯 100% CBSE English Medium</div>
    </div>
  </div>

  <div class="chapters-grid">
{''.join(cards_html)}
  </div>

  <div style="margin-top: 35px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; font-size: 13px; color: #475569; line-height: 1.6;">
    <h3 style="margin-bottom: 8px; color: #0f172a; font-size: 15px;">📋 CBSE Examination System Tier Guide:</h3>
    <ul style="padding-left: 20px; margin: 0;">
      <li><b>Set A (Foundation):</b> Fundamental NCERT Curiosity definitions, standard SI units, basic organelle/formula recall.</li>
      <li><b>Set B (HOTS & Numericals):</b> Mathematical multi-step calculations, graphical slopes, kinematics equations, momentum recoil.</li>
      <li><b>Set C (NCERT Exemplar):</b> Critical thinking, higher-order reasoning, non-intuitive tricky questions, experimental controls.</li>
      <li><b>Set D (Assertion - Reasoning Special):</b> Rigorous two-statement causality analysis with standard CBSE A/R 4-option framework.</li>
      <li><b>Set E (Case Study & Practical Experiments):</b> Lab experiments, data tables, observations, real-world case scenarios.</li>
      <li><b>Set F (Rapid Fire Speed Test):</b> 30-minute high-speed recall exam targeting quick intuition and instant accuracy.</li>
      <li><b>Set G (Final Mastery & Grand Challenge):</b> Comprehensive 60-minute Olympiad/NTSE-grade multi-step synthesis for 100/100 mastery.</li>
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

    # Update Science Card badge and statistics
    old_target = """<span class="status-badge badge-live">● COMPLETED</span>"""
    if "40 Exam Papers Active" in content:
        content = content.replace("40 Exam Papers Active: Set A (Foundation) + Set B (HOTS) + Set C (Exemplar) + Set D (A/R) + Set E (Case Study)",
                                  "56 Exam Papers Active: Sets A, B, C, D, E, F & G (Complete 7-Tier Mastery)")
        content = content.replace("1,000 Unique MCQs (125 MCQs per chapter)",
                                  "1,400 Unique MCQs (175 MCQs per chapter • 56 Print-Ready PDFs)")
        content = content.replace("Open Science Exam Papers (Sets A, B, C, D & E - 1,000 MCQs) ➡️",
                                  "🚀 Open Complete Science Exam Hub (56 Papers • 1,400 MCQs) ➡️")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Updated root index.html")

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    old_sec = """  - **Set E:** Case Study & Practical Experiments (200 MCQs)
  - **Total Active:** **40 Exam Papers • 1,000 Unique MCQs • 40 Print-Ready PDFs**"""

    new_sec = """  - **Set E:** Case Study & Practical Experiments (200 MCQs)
  - **Set F:** Rapid Fire Speed Test (200 MCQs)
  - **Set G:** Final Mastery & Grand Challenge Test (200 MCQs)
  - **Total Active:** **56 Exam Papers • 1,400 Unique MCQs • 56 Print-Ready PDFs**"""

    if old_sec in content:
        content = content.replace(old_sec, new_sec)
        content = content.replace("Production Ready Print PDFs (32 A4 PDFs)", "Production Ready Print PDFs (56 A4 PDFs)")
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content)
        print("[OK] Updated README.md")

if __name__ == "__main__":
    portal_html = generate_science_portal()
    with open("Science_Exam_Papers/index.html", "w", encoding="utf-8") as f:
        f.write(portal_html)
    print("[OK] Updated Science_Exam_Papers/index.html with all 7 Sets!")
    
    update_root_index()
    update_readme()
    print("ALL PORTALS SYNCHRONIZED SUCCESSFULLY!")
