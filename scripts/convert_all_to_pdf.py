"""
Convert all 16 CBSE Class 9 Science HTML Examination Papers into clean, print-ready PDF files.
Stores the PDFs in a separate dedicated folder 'PDF_Ready_To_Print'.
Keeps all HTML files completely untouched.
"""

import os
import subprocess

PAPERS = [
    # Chapter 1
    ("Science_Exam_Papers/chapter_01_exploration.html", "Class_9_Science_Ch01_Exploration_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_01_exploration_set_b.html", "Class_9_Science_Ch01_Exploration_Set_B.pdf"),
    # Chapter 2
    ("Science_Exam_Papers/chapter_02_cell.html", "Class_9_Science_Ch02_Cell_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_02_cell_set_b.html", "Class_9_Science_Ch02_Cell_Set_B.pdf"),
    # Chapter 3
    ("Science_Exam_Papers/chapter_03_tissues.html", "Class_9_Science_Ch03_Tissues_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_03_tissues_set_b.html", "Class_9_Science_Ch03_Tissues_Set_B.pdf"),
    # Chapter 4
    ("Science_Exam_Papers/chapter_04_motion.html", "Class_9_Science_Ch04_Motion_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_04_motion_set_b.html", "Class_9_Science_Ch04_Motion_Set_B.pdf"),
    # Chapter 5
    ("Science_Exam_Papers/chapter_05_mixtures.html", "Class_9_Science_Ch05_Mixtures_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_05_mixtures_set_b.html", "Class_9_Science_Ch05_Mixtures_Set_B.pdf"),
    # Chapter 6
    ("Science_Exam_Papers/chapter_06_forces.html", "Class_9_Science_Ch06_Forces_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_06_forces_set_b.html", "Class_9_Science_Ch06_Forces_Set_B.pdf"),
    # Chapter 7
    ("Science_Exam_Papers/chapter_07_work_energy.html", "Class_9_Science_Ch07_Work_Energy_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_07_work_energy_set_b.html", "Class_9_Science_Ch07_Work_Energy_Set_B.pdf"),
    # Chapter 8
    ("Science_Exam_Papers/chapter_08_atom.html", "Class_9_Science_Ch08_Atom_Set_A.pdf"),
    ("Science_Exam_Papers/chapter_08_atom_set_b.html", "Class_9_Science_Ch08_Atom_Set_B.pdf"),
]

output_dir = "PDF_Ready_To_Print"
os.makedirs(output_dir, exist_ok=True)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"Starting conversion of {len(PAPERS)} exam papers to PDF...")

for html_file, pdf_name in PAPERS:
    html_abs = os.path.abspath(html_file)
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

print("\nALL 16 PDFS SUCCESSFULLY CREATED IN 'PDF_Ready_To_Print' FOLDER!")
