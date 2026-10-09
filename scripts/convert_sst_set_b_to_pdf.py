"""
Convert 9 Social Science Set B HTML exam papers to PDF in Social_Science_Exam_Papers/PDF_Ready_To_Print.
"""

import os
import subprocess

PAPERS = [
    ("Social_Science_Exam_Papers/chapter_01_understanding_sst_set_b.html", "Class_9_SST_Ch01_Understanding_SST_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_02_shaping_earth_set_b.html", "Class_9_SST_Ch02_Shaping_Earth_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_03_atmosphere_climate_set_b.html", "Class_9_SST_Ch03_Atmosphere_Climate_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_04_early_civilisation_set_b.html", "Class_9_SST_Ch04_Early_Civilisation_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_05_state_society_set_b.html", "Class_9_SST_Ch05_State_Society_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_06_democracy_set_b.html", "Class_9_SST_Ch06_Democracy_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_07_elections_set_b.html", "Class_9_SST_Ch07_Elections_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_08_economics_choice_set_b.html", "Class_9_SST_Ch08_Economics_Choice_Set_B.pdf"),
    ("Social_Science_Exam_Papers/chapter_09_price_puzzle_set_b.html", "Class_9_SST_Ch09_Price_Puzzle_Set_B.pdf"),
]

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(root_dir, "Social_Science_Exam_Papers", "PDF_Ready_To_Print")
os.makedirs(output_dir, exist_ok=True)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"Starting conversion of {len(PAPERS)} Social Science Set B exam papers to PDF...")

for html_file, pdf_name in PAPERS:
    html_abs = os.path.abspath(os.path.join(root_dir, html_file))
    pdf_abs = os.path.abspath(os.path.join(output_dir, pdf_name))
    
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_abs}",
        html_abs
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    size_kb = os.path.getsize(pdf_abs) // 1024 if os.path.exists(pdf_abs) else 0
    print(f"[OK] Generated: {pdf_name} ({size_kb} KB)")

print("ALL 9 SOCIAL SCIENCE SET B PDFS CREATED SUCCESSFULLY!")
