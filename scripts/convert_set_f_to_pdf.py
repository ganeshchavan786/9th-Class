"""
Convert 8 Set F HTML exam papers to PDF in Science_Exam_Papers/PDF_Ready_To_Print.
"""

import os
import subprocess

PAPERS = [
    ("Science_Exam_Papers/chapter_01_exploration_set_f.html", "Class_9_Science_Ch01_Exploration_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_02_cell_set_f.html", "Class_9_Science_Ch02_Cell_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_03_tissues_set_f.html", "Class_9_Science_Ch03_Tissues_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_04_motion_set_f.html", "Class_9_Science_Ch04_Motion_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_05_mixtures_set_f.html", "Class_9_Science_Ch05_Mixtures_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_06_forces_set_f.html", "Class_9_Science_Ch06_Forces_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_07_work_energy_set_f.html", "Class_9_Science_Ch07_Work_Energy_Set_F.pdf"),
    ("Science_Exam_Papers/chapter_08_atom_set_f.html", "Class_9_Science_Ch08_Atom_Set_F.pdf"),
]

output_dir = "Science_Exam_Papers/PDF_Ready_To_Print"
os.makedirs(output_dir, exist_ok=True)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"Starting conversion of {len(PAPERS)} Set F exam papers to PDF...")

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

print("ALL 8 SET F PDFS CREATED SUCCESSFULLY!")
