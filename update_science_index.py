"""
Update Science_Exam_Papers/index.html to display both Set A and Set B exam papers,
along with badges for upcoming Sets C, D, E, F, G.
"""

CHAPTERS = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "desc": "Scientific inquiry, SI units, variables, laboratory apparatus, vernier/screw gauge measurement, zero error, and experimental accuracy.",
        "file_a": "chapter_01_exploration.html",
        "file_b": "chapter_01_exploration_set_b.html"
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "desc": "Cell discovery, plasma membrane fluidity, osmosis & plasmolysis, endomembrane system, mitochondria & plastids bioenergetics, and cell division.",
        "file_a": "chapter_02_cell.html",
        "file_b": "chapter_02_cell_set_b.html"
    },
    {
        "num": 3,
        "title": "Tissues in Action",
        "file_a": "chapter_03_tissues.html",
        "file_b": "chapter_03_tissues_set_b.html",
        "desc": "Plant tissues (meristematic, collenchyma, sclerenchyma, xylem, phloem) and Animal tissues (epithelial brush borders, bone Haversian canals, cardiac gap junctions, neurons)."
    },
    {
        "num": 4,
        "title": "Describing Motion Around Us",
        "file_a": "chapter_04_motion.html",
        "file_b": "chapter_04_motion_set_b.html",
        "desc": "Distance vs displacement, harmonic mean velocity, equations of motion, reaction time stopping distances, graphical v-t analysis, and uniform circular motion."
    },
    {
        "num": 5,
        "title": "Exploring Mixtures and their Separation",
        "file_a": "chapter_05_mixtures.html",
        "file_b": "chapter_05_mixtures_set_b.html",
        "desc": "Homogeneous & heterogeneous systems, solubility crystallization thermodynamics, fractional distillation of liquid air, chromatography Rf factors, and colloids."
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion",
        "file_a": "chapter_06_forces.html",
        "file_b": "chapter_06_forces_set_b.html",
        "desc": "Balanced forces, inertia & mass, Newton's laws, multi-body contact forces, apparent weight in elevators, impulse-momentum theorem, and rocket thrust."
    },
    {
        "num": 7,
        "title": "Work, Energy, and Simple Machines",
        "file_a": "chapter_07_work_energy.html",
        "file_b": "chapter_07_work_energy_set_b.html",
        "desc": "Work done by constant and variable forces, kinetic & elastic potential energy, conservation of mechanical energy, power and pump efficiency, levers and block & tackle systems."
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom",
        "file_a": "chapter_08_atom.html",
        "file_b": "chapter_08_atom_set_b.html",
        "desc": "Subatomic e/m ratios, Rutherford nuclear scattering geometry, Bohr-Bury electronic configurations, octet valencies, isotopes, isobars, and nuclear medicine applications."
    }
]

short_names = {
    1: "Exploration",
    2: "Cell",
    3: "Tissues",
    4: "Motion",
    5: "Mixtures",
    6: "Forces",
    7: "Work_Energy",
    8: "Atom"
}

cards_html = []
for ch in CHAPTERS:
    sname = short_names[ch['num']]
    ch['pdf_a'] = f"PDF_Ready_To_Print/Class_9_Science_Ch{ch['num']:02d}_{sname}_Set_A.pdf"
    ch['pdf_b'] = f"PDF_Ready_To_Print/Class_9_Science_Ch{ch['num']:02d}_{sname}_Set_B.pdf"
    card = f"""
    <div class="chapter-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <span class="chapter-badge">CHAPTER {ch['num']}</span>
        <span style="font-size: 11px; font-weight: 700; color: #166534; background: #dcfce7; padding: 2px 8px; border-radius: 12px; border: 1px solid #86efac;">
          ✅ 2 SETS ACTIVE (50 MCQs)
        </span>
      </div>
      <div class="chapter-title">{ch['title']}</div>
      <p class="chapter-desc">{ch['desc']}</p>
      
      <!-- Set Selector Grid -->
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; margin-bottom: 12px;">
        <div style="font-size: 11.5px; font-weight: 700; color: #334155; margin-bottom: 8px; display: flex; justify-content: space-between;">
          <span>AVAILABLE PRACTICE SETS:</span>
          <span style="color: #64748b;">(25 Marks each | 45 Mins)</span>
        </div>
        
        <!-- Active Sets -->
        <div style="display: flex; gap: 8px; margin-bottom: 8px;">
          <a href="{ch['file_a']}" class="set-btn set-btn-a">
            📘 SET A (Foundation)
          </a>
          <a href="{ch['file_b']}" class="set-btn set-btn-b">
            🔥 SET B (Advanced HOTS)
          </a>
        </div>
        
        <!-- Upcoming Sets Badges -->
        <div style="display: flex; gap: 4px; align-items: center; flex-wrap: wrap; font-size: 10.5px; color: #64748b; padding-top: 4px; border-top: 1px dashed #cbd5e1;">
          <span style="font-weight: 600;">Next Sets:</span>
          <span class="set-pill">Set C (Exemplar)</span>
          <span class="set-pill">Set D (Assertion)</span>
          <span class="set-pill">Set E (Case Study)</span>
          <span class="set-pill">Set F (Speed)</span>
          <span class="set-pill">Set G (Mastery)</span>
        </div>
      </div>
      
        <!-- Direct PDF Download / Open Actions -->
        <div style="display: flex; gap: 8px;">
          <a href="{ch['pdf_a']}" target="_blank" class="btn-portal btn-outline" style="font-size: 11.5px; padding: 6px 8px;">
            📄 Open Set A (PDF)
          </a>
          <a href="{ch['pdf_b']}" target="_blank" class="btn-portal btn-outline" style="font-size: 11.5px; padding: 6px 8px; color: #b45309; border-color: #fde68a; background: #fffbeb;">
            📄 Open Set B (PDF)
          </a>
        </div>
      </div>
      """
    cards_html.append(card)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Science - Multi-Set Examination Portal</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    body {{
      background: #f1f5f9;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .dashboard-container {{
      max-width: 1050px;
      margin: 25px auto;
      padding: 0 20px;
    }}
    .back-nav {{
      margin-bottom: 18px;
    }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      font-weight: 700;
      color: #1e3a8a;
      background: #e0e7ff;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      border: 1px solid #c7d2fe;
      transition: all 0.2s;
    }}
    .back-btn:hover {{
      background: #c7d2fe;
    }}
    .hero-banner {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
      color: #ffffff;
      padding: 35px 40px;
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.25);
      margin-bottom: 30px;
    }}
    .hero-banner h1 {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .hero-banner p {{
      font-size: 14.5px;
      color: #cbd5e1;
      line-height: 1.6;
    }}
    .badge-grid {{
      display: flex;
      gap: 12px;
      margin-top: 15px;
      flex-wrap: wrap;
    }}
    .badge-item {{
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(5px);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}
    .chapters-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(470px, 1fr));
      gap: 20px;
    }}
    .chapter-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 22px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .chapter-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
      border-color: #93c5fd;
    }}
    .chapter-badge {{
      display: inline-block;
      background: #e0e7ff;
      color: #3730a3;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }}
    .chapter-title {{
      font-size: 16.5px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 6px;
    }}
    .chapter-desc {{
      font-size: 12.5px;
      color: #475569;
      line-height: 1.45;
      margin-bottom: 12px;
      flex-grow: 1;
    }}
    .set-btn {{
      flex: 1;
      padding: 8px 10px;
      text-align: center;
      border-radius: 6px;
      font-weight: 700;
      font-size: 12px;
      text-decoration: none;
      transition: all 0.2s;
      display: block;
    }}
    .set-btn-a {{
      background: #1e40af;
      color: #ffffff;
    }}
    .set-btn-a:hover {{
      background: #1e3a8a;
    }}
    .set-btn-b {{
      background: #d97706;
      color: #ffffff;
    }}
    .set-btn-b:hover {{
      background: #b45309;
    }}
    .set-pill {{
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 1px 6px;
      border-radius: 10px;
      font-size: 10px;
    }}
    .btn-portal {{
      flex: 1;
      text-align: center;
      border-radius: 6px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
    }}
    .btn-outline {{
      background: #ffffff;
      color: #1e293b;
      border: 1.5px solid #cbd5e1;
    }}
    .btn-outline:hover {{
      background: #f8fafc;
      border-color: #94a3b8;
    }}
    .guide-box {{
      margin-top: 35px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 24px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }}
    .guide-box h3 {{
      font-size: 16px;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    .guide-box ul {{
      padding-left: 20px;
      font-size: 13px;
      color: #334155;
      line-height: 1.7;
    }}
  </style>
</head>
<body>

<div class="dashboard-container">
  
  <div class="back-nav">
    <a href="../index.html" class="back-btn">
      🏠 ⬅️ Return to All Subjects Master Portal
    </a>
  </div>

  <div class="hero-banner">
    <h1>CBSE CLASS IX SCIENCE — MULTI-SET EXAMINATION PORTAL</h1>
    <p>Comprehensive Chapter-Wise Examination Question Papers for Chapters 1 to 8 based on the NCERT Class 9 Science Curriculum. Features graduated difficulty with <b>Set A (Foundation & Core Concepts)</b> and <b>Set B (Advanced HOTS & Numericals)</b>, complete with printable OMR bubble sheets and detailed solutions.</p>
    <div class="badge-grid">
      <div class="badge-item">🎯 400 Total Unique MCQs (16 Papers Active)</div>
      <div class="badge-item">📘 Set A: Foundation & Core Concepts</div>
      <div class="badge-item">🔥 Set B: Advanced HOTS & Numericals</div>
      <div class="badge-item">📄 Standard A4 Black-and-White Print Layout</div>
      <div class="badge-item">⭕ Printable OMR Bubble Grids</div>
    </div>
  </div>

  <div class="chapters-grid">
    {''.join(cards_html)}
  </div>

  <div class="guide-box">
    <h3>💡 How to Use Set A & Set B for Highest Exam Marks:</h3>
    <ul>
      <li><b>Step 1 — Foundation (Set A):</b> Have the student solve <b>Set A</b> first immediately after reading the NCERT chapter to master core definitions, fundamental concepts, and essential facts.</li>
      <li><b>Step 2 — Challenge & Numericals (Set B):</b> After scoring 80%+ on Set A, administer <b>Set B</b>. It contains challenging Higher Order Thinking Skills (HOTS), multi-step formulas, velocity-time graph analysis, and critical Assertion-Reason questions designed to prepare the student for full marks (100%) in school exams.</li>
      <li><b>Direct Printing:</b> Click <b>"Print Set A"</b> or <b>"Print Set B"</b> to open a pre-formatted school examination question paper on A4 size with student details and instructions box.</li>
      <li><b>Upcoming Sets:</b> Sets C, D, E, F, and G can be unlocked and generated anytime for further mega-practice!</li>
    </ul>
  </div>

</div>

<script>
function openAndPrint(url) {{
  let w = window.open(url, '_blank');
  w.onload = function() {{
    setTimeout(function() {{
      w.print();
    }}, 600);
  }};
}}
</script>

</body>
</html>
"""

with open("Science_Exam_Papers/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Updated Science_Exam_Papers/index.html successfully!")
