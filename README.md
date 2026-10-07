# CBSE Class 9 Examination & Practice Portal 📚

An enterprise-grade, comprehensive examination practice and paper generation system for CBSE Class 9 students preparing for Mid-Term (Half-Yearly) and Annual CBSE examinations.

## 🌐 Live Website (GitHub Pages)
👉 **[Open Online Examination Portal](https://ganeshchavan786.github.io/9th-Class/)**

---

## 🏛️ Professional Architecture & Project Structure

Organized following enterprise software engineering standards with clear separation of concerns:

```
9th-Class/
│
├── index.html                   # Master Central Exam Portal (All Subjects Landing)
├── exam-style.css               # Unified CBSE Design System & Print Typography
├── README.md                    # Project Architecture & Documentation
├── .gitignore                   # Enterprise-Grade Git Ignore Rules
│
├── Science_Exam_Papers/         # Subject Module 1: Science (Curiosity Curriculum)
│   ├── index.html               # Science Multi-Set Interactive Dashboard
│   ├── exam-style.css           # Local Print & Screen Styling
│   ├── chapter_01_..._set_a.html# Set A: Foundation Papers (8 Chapters)
│   ├── chapter_01_..._set_b.html# Set B: Advanced HOTS Papers (8 Chapters)
│   ├── chapter_01_..._set_c.html# Set C: NCERT Exemplar Papers (8 Chapters)
│   ├── chapter_01_..._set_d.html# Set D: Assertion-Reasoning Papers (8 Chapters)
│   └── PDF_Ready_To_Print/      # Production Ready Print PDFs (56 A4 PDFs)
│
├── scripts/                     # Build Automation, Data Pipelines & Compilers
│   ├── build_all_papers.py      # Set A Paper Generator
│   ├── build_set_b.py           # Set B Paper Generator
│   ├── build_set_c.py           # Set C Paper Generator
│   ├── build_set_d.py           # Set D Paper Generator
│   ├── data_set_d_part1.py      # Set D Question Bank (Ch 1-4)
│   ├── data_set_d_part2.py      # Set D Question Bank (Ch 5-8)
│   ├── convert_all_to_pdf.py    # Headless A4 PDF Compiler (Sets A & B)
│   ├── convert_set_c_to_pdf.py  # Headless A4 PDF Compiler (Set C)
│   ├── convert_set_d_to_pdf.py  # Headless A4 PDF Compiler (Set D)
│   └── update_portal_set_d.py   # Dashboard Synchronization Utility
│
└── raw_textbooks/               # Reference NCERT Textbooks (Git-Ignored)
    ├── iesc1dd/                 # Class 9 Science Source Modules
    └── iest1dd/                 # Class 9 Social Science Source Modules
```

---

## 🔬 Subject Portals & Status

### 1. Science (NCERT Class 9)
- **Science Portal URL:** `https://ganeshchavan786.github.io/9th-Class/Science_Exam_Papers/`
- **Chapters Covered (Chapters 1 to 8):**
  1. Exploration: Entering the World of Secondary Science
  2. Cell: The Building Block of Life
  3. Tissues in Action
  4. Describing Motion Around Us
  5. Exploring Mixtures and their Separation
  6. How Forces Affect Motion
  7. Work, Energy, and Simple Machines
  8. Journey Inside the Atom
- **Practice Sets Available:**
  - **Set A:** Foundation & Core Conceptual MCQs (8 papers $\times$ 25 = 200 MCQs)
  - **Set B:** Advanced HOTS, Numerical Kinematics & Assertion-Reasoning (200 MCQs)
  - **Set C:** NCERT Exemplar & Critical Application Questions (200 MCQs)
  - **Set D:** Assertion & Reasoning Special (200 MCQs)
  - **Set E:** Case Study & Practical Experiments (200 MCQs)
  - **Set F:** Rapid Fire Speed Test (200 MCQs)
  - **Set G:** Final Mastery & Grand Challenge Test (200 MCQs)
  - **Total Active:** **56 Exam Papers • 1,400 Unique MCQs • 56 Print-Ready PDFs**
- **Printable PDFs:** Available inside `Science_Exam_Papers/PDF_Ready_To_Print/`

### 2. Social Science (NCERT Class 9 Integrated)
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
  - **Set A:** Foundation & Core Concepts (9 papers $	imes$ 25 = 225 MCQs)
  - **Total Active:** **9 Exam Papers • 225 Unique MCQs • 9 Print-Ready PDFs**
- **Printable PDFs:** Available inside `Social_Science_Exam_Papers/PDF_Ready_To_Print/`

### 3. Upcoming Subjects
- **Mathematics:** `Maths_Exam_Papers/` (Scheduled)
- **English:** `English_Exam_Papers/` (Scheduled)

---

## 🌟 Key Features
- **CBSE Standard Layout:** Complete with school header, student roll number box, general instructions, and marking scheme.
- **Print-Ready A4 Format:** Clean typography, zero digital buttons on paper printout (`@media print`), automatic page-breaks.
- **OMR Response Sheet:** Realistic 25-bubble response grid for practicing pen darkening.
- **Full Answer Keys & Explanations:** Step-by-step conceptual rationale printed on a separate page.
- **Interactive Browser Mode:** Active 45-minute countdown clock with instant automated scoring.
- **Strict English Medium:** 100% standard CBSE English medium without regional fonts.

---
*Maintained with enterprise-grade modular architecture for Class 9 CBSE Students' Academic Excellence.*
