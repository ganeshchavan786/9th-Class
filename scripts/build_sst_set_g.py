"""
Build script for CBSE Class 9 Social Science - SET G (Final Mastery & Grand Challenge Test)
Generates 9 chapter-wise exam papers (25 Grand Challenge MCQs each = 225 questions).
Curriculum: NCERT Class 9 Social Science (Latest Edition)
Strictly 100% CBSE English Medium.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_sst_set_g_part1 import (
    CHAPTER_01_QUESTIONS,
    CHAPTER_02_QUESTIONS,
    CHAPTER_03_QUESTIONS,
    CHAPTER_04_QUESTIONS,
)
from data_sst_set_g_part2 import (
    CHAPTER_05_QUESTIONS,
    CHAPTER_06_QUESTIONS,
    CHAPTER_07_QUESTIONS,
    CHAPTER_08_QUESTIONS,
    CHAPTER_09_QUESTIONS,
)

CHAPTERS_DATA = [
    {
        "num": 1,
        "title": "Understanding Social Science",
        "file": "Social_Science_Exam_Papers/chapter_01_understanding_sst_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Radiocarbon calibration curves, Harris matrix, stable isotope dietary analysis, and structural epigraphy.",
        "questions": CHAPTER_01_QUESTIONS
    },
    {
        "num": 2,
        "title": "Shaping of the Earth's Surface",
        "file": "Social_Science_Exam_Papers/chapter_02_shaping_earth_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Plate tectonics kinematics, seismic moment Mw, Mohr-Coulomb slope stability, and fluvial geomorphology.",
        "questions": CHAPTER_02_QUESTIONS
    },
    {
        "num": 3,
        "title": "Atmosphere and Climate",
        "file": "Social_Science_Exam_Papers/chapter_03_atmosphere_climate_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Stefan-Boltzmann radiation, Rossby waves, ENSO Walker circulation dynamics, and Rayleigh scattering.",
        "questions": CHAPTER_03_QUESTIONS
    },
    {
        "num": 4,
        "title": "Early Humans and Beginning of Civilisation",
        "file": "Social_Science_Exam_Papers/chapter_04_early_civilisation_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Bronze metallurgy, cire perdue, NBPW second urbanisation, Mehrgarh agrarian origins, and Harappan civic standardization.",
        "questions": CHAPTER_04_QUESTIONS
    },
    {
        "num": 5,
        "title": "State and Society up to 1000 CE",
        "file": "Social_Science_Exam_Papers/chapter_05_state_society_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Kautilya's Saptanga organic polity, Gupta administrative hierarchy, Uttaramerur Kudavolai lottery, and Chola revenue systems.",
        "questions": CHAPTER_05_QUESTIONS
    },
    {
        "num": 6,
        "title": "Democracy",
        "file": "Social_Science_Exam_Papers/chapter_06_democracy_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Montesquieu's Trias Politica, Kesavananda Bharati basic structure, procedural vs substantive democracy, and horizontal accountability.",
        "questions": CHAPTER_06_QUESTIONS
    },
    {
        "num": 7,
        "title": "Elections",
        "file": "Social_Science_Exam_Papers/chapter_07_elections_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Article 324 constitutional independence, FPTP vs Proportional Representation, RPA jurisprudence (Lily Thomas, ADR, PUCL), and delimitation freezes.",
        "questions": CHAPTER_07_QUESTIONS
    },
    {
        "num": 8,
        "title": "Building Blocks in Economics: The Problem of Choice",
        "file": "Social_Science_Exam_Papers/chapter_08_economics_choice_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Robbins scarcity postulates, PPF marginal opportunity cost concavity, human capital virtuous cycles, and factor market distribution.",
        "questions": CHAPTER_08_QUESTIONS
    },
    {
        "num": 9,
        "title": "The Price Puzzle: What Drives the Market",
        "file": "Social_Science_Exam_Papers/chapter_09_price_puzzle_set_g.html",
        "desc": "SET G (Final Mastery & Grand Challenge): Marshallian equilibrium scissors, Giffen/Veblen goods, deadweight loss under price ceilings, and price elasticity incidence.",
        "questions": CHAPTER_09_QUESTIONS
    }
]

HTML_TEMPLATE_SET_G = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 9 Social Science - Chapter {chapter_num}: {chapter_title} (SET G - Final Mastery & Grand Challenge)</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    .set-g-badge {{
      display: inline-block;
      background: linear-gradient(135deg, #b91c1c, #991b1b);
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 12px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .grand-banner {{
      background: #fef2f2;
      border: 1.5px solid #fecaca;
      border-left: 5px solid #b91c1c;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 16px;
      font-size: 12.5px;
      color: #7f1d1d;
      line-height: 1.5;
    }}
  </style>
</head>
<body>

<div class="exam-paper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="interactive-header no-print">
    <div class="timer-display">
      ⏱️ Grand Challenge Countdown: <span id="timerDisplay">60:00</span>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
      <button class="btn btn-primary" id="timerBtn" onclick="toggleTimer()">⏸️ Pause Timer</button>
      <button class="btn btn-secondary" onclick="checkAnswers()">🏆 Submit Grand Challenge</button>
      <button class="btn btn-primary" onclick="toggleAnswerKey()">🔑 View Detailed Solutions</button>
      <button class="btn btn-primary" onclick="window.print()">🖨️ Print Exam Paper</button>
    </div>
  </div>

  <!-- Standard CBSE School Exam Header -->
  <div class="exam-header">
    <div class="school-title">CENTRAL BOARD OF SECONDARY EDUCATION — PRACTICE EXAMINATION</div>
    <div class="exam-sub">CLASS IX • SOCIAL SCIENCE (SUBJECT CODE: 087) • ACADEMIC SESSION 2026-27</div>
    <div style="margin-top: 5px;">
      <span class="set-g-badge">SET G — FINAL MASTERY & GRAND CHALLENGE TEST (60 MINS)</span>
    </div>
    <div class="exam-chapter">CHAPTER {chapter_num_padded}: {chapter_title_upper}</div>
    <div class="meta-row">
      <span><b>TIME ALLOWED:</b> 60 MINUTES</span>
      <span><b>MAXIMUM MARKS:</b> 25 MARKS</span>
      <span><b>SERIES:</b> CBS-IX-SST-SET-G-{chapter_num_padded}</span>
    </div>
  </div>

  <!-- Student Info Box -->
  <div class="student-info-box">
    <div class="info-row">
      <div class="info-field"><b>Student's Name:</b> <span class="dotted-line" style="min-width: 250px;"></span></div>
      <div class="info-field" style="text-align: right;"><b>Roll No.:</b> <span class="dotted-line" style="min-width: 120px;"></span></div>
    </div>
    <div class="info-row" style="margin-top: 6px;">
      <div class="info-field"><b>Class & Section:</b> Class IX - <span class="dotted-line" style="min-width: 60px;"></span></div>
      <div class="info-field" style="text-align: center;"><b>Date of Exam:</b> <span class="dotted-line" style="min-width: 110px;"></span></div>
      <div class="info-field" style="text-align: right;"><b>Invigilator's Sign:</b> <span class="dotted-line" style="min-width: 120px;"></span></div>
    </div>
  </div>

  <!-- General Instructions -->
  <div class="instructions-box">
    <h4>General Instructions (SET G - Final Mastery & Grand Challenge Test):</h4>
    <ol>
      <li>The question paper comprises <b>25 Olympiad / NTSE / Advanced Analytical Multiple Choice Questions</b> of <b>1 mark each</b>.</li>
      <li>Designed for <b>Final Curricular Mastery & In-Depth Analytical Rigour</b>: Target time is <b>60 Minutes</b>.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding bubble on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <div class="grand-banner">
    🏆 <b>GRAND CHALLENGE SPECIAL:</b> This final assessment tests your multi-disciplinary analytical reasoning across historical source criticism, geomorphological dynamics, constitutional jurisprudence, and microeconomic market equilibria!
  </div>

  <!-- Questions Container -->
  <div class="questions-container">
{questions_html}
  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET G)</div>
    <div class="omr-grid">
{omr_grid_html}
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: 12px; font-size: 11.5px;">
      <div><b>Total Questions Attempted:</b> _____ / 25</div>
      <div><b>Marks Obtained:</b> _____ / 25</div>
      <div><b>Evaluator's Signature:</b> ___________________</div>
    </div>
  </div>

  <!-- Answer Key & Explanations (Separate Page in Print) -->
  <div class="answers-section" id="answerKeySection">
    <div class="answers-header">OFFICIAL ANSWER KEY & IN-DEPTH SCHOLARLY EXPLANATIONS (SET G)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Curricular Concept & Scholarly Analysis</th>
        </tr>
      </thead>
      <tbody>
{answer_table_rows}
      </tbody>
    </table>
  </div>

  <!-- Back to Dashboard Link (Hidden on Print) -->
  <div class="no-print" style="margin-top: 30px; text-align: center;">
    <a href="index.html" class="btn btn-secondary" style="font-size: 14px; padding: 10px 20px;">
      ⬅️ Return to Social Science Examination Dashboard
    </a>
  </div>

</div>

<script>
const correctAnswers = {answers_json};

let timeLeft = 60 * 60;
let timerRunning = true;
let timerInterval = setInterval(updateTimer, 1000);

function updateTimer() {{
  if (!timerRunning) return;
  if (timeLeft <= 0) {{
    clearInterval(timerInterval);
    document.getElementById("timerDisplay").innerText = "00:00 (Time Over)";
    alert("Grand Challenge time is up! Please submit and check your answers.");
    return;
  }}
  timeLeft--;
  let mins = Math.floor(timeLeft / 60);
  let secs = timeLeft % 60;
  document.getElementById("timerDisplay").innerText = 
    (mins < 10 ? "0" + mins : mins) + ":" + (secs < 10 ? "0" + secs : secs);
}}

function toggleTimer() {{
  timerRunning = !timerRunning;
  document.getElementById("timerBtn").innerText = timerRunning ? "⏸️ Pause Timer" : "▶️ Resume Timer";
}}

function checkAnswers() {{
  let score = 0;
  let total = Object.keys(correctAnswers).length;
  let unanswered = 0;

  for (let q in correctAnswers) {{
    let selected = document.querySelector(`input[name="${{q}}"]:checked`);
    let card = document.getElementById(`qcard_${{q}}`);
    let expBox = document.getElementById(`exp_${{q}}`);
    let qNum = q.replace("q", "");
    let omrRow = document.getElementById(`omr_row_${{qNum}}`);

    // Reset styles
    if (card) {{
      card.classList.remove("correct-card", "incorrect-card");
    }}
    if (omrRow) {{
      let bubbles = omrRow.querySelectorAll(".omr-bubble");
      bubbles.forEach(b => b.classList.remove("omr-filled", "omr-correct-bubble", "omr-wrong-bubble"));
    }}

    if (selected) {{
      let userAns = selected.value;
      if (omrRow) {{
        let chosenBubble = omrRow.querySelector(`.omr-bubble[data-opt="${{userAns}}"]`);
        if (chosenBubble) chosenBubble.classList.add("omr-filled");
      }}

      if (userAns === correctAnswers[q]) {{
        score++;
        if (card) card.classList.add("correct-card");
        if (omrRow) {{
          let correctB = omrRow.querySelector(`.omr-bubble[data-opt="${{userAns}}"]`);
          if (correctB) correctB.classList.add("omr-correct-bubble");
        }}
      }} else {{
        if (card) card.classList.add("incorrect-card");
        if (omrRow) {{
          let wrongB = omrRow.querySelector(`.omr-bubble[data-opt="${{userAns}}"]`);
          if (wrongB) wrongB.classList.add("omr-wrong-bubble");
          let rightB = omrRow.querySelector(`.omr-bubble[data-opt="${{correctAnswers[q]}}"]`);
          if (rightB) rightB.classList.add("omr-correct-bubble");
        }}
      }}
    }} else {{
      unanswered++;
      if (omrRow) {{
        let rightB = omrRow.querySelector(`.omr-bubble[data-opt="${{correctAnswers[q]}}"]`);
        if (rightB) rightB.classList.add("omr-correct-bubble");
      }}
    }}

    if (expBox) expBox.style.display = "block";
  }}

  // Show Answer key
  document.getElementById("answerKeySection").style.display = "block";

  // Score alert
  let perc = ((score / total) * 100).toFixed(1);
  alert(`Grand Challenge Completed!\\n\\nYour Score: ${{score}} / ${{total}} (${{perc}}%)\\nUnanswered: ${{unanswered}}\\n\\nReview the question cards and the official solution key below.`);
}}

function toggleAnswerKey() {{
  let sec = document.getElementById("answerKeySection");
  let isHidden = (sec.style.display === "none" || sec.style.display === "");
  sec.style.display = isHidden ? "block" : "none";
  
  // Also reveal individual explanations
  for (let q in correctAnswers) {{
    let expBox = document.getElementById(`exp_${{q}}`);
    if (expBox) expBox.style.display = isHidden ? "block" : "none";
  }}
}}
</script>

</body>
</html>
"""

def generate_questions_html(questions):
    html_parts = []
    opt_labels = ["A", "B", "C", "D"]
    
    for idx, q_data in enumerate(questions, start=1):
        q_id = f"q{idx}"
        q_text = q_data["q"]
        options = q_data["options"]
        ans = q_data["ans"]
        exp = q_data["exp"]
        
        opt_html_list = []
        for opt_idx, opt_text in enumerate(options):
            label = opt_labels[opt_idx]
            opt_html = f"""        <label class="option-label">
          <input type="radio" name="{q_id}" value="{label}" onchange="syncOmr('{idx}', '{label}')">
          <span class="opt-tag">{label}</span>
          <span>{opt_text}</span>
        </label>"""
            opt_html_list.append(opt_html)
            
        opt_container = "\n".join(opt_html_list)
        
        card_html = f"""    <!-- Question {idx} -->
    <div class="question-card" id="qcard_{q_id}">
      <div class="q-header">
        <span class="q-number">Q{idx}.</span>
        <span class="q-text">{q_text}</span>
      </div>
      <div class="options-group">
{opt_container}
      </div>
      <div class="exp-box" id="exp_{q_id}">
        <strong>Scholarly Concept & Analysis:</strong> {exp}
      </div>
    </div>"""
        html_parts.append(card_html)
        
    return "\n\n".join(html_parts)

def generate_omr_grid_html(num_questions):
    rows = []
    for i in range(1, num_questions + 1):
        row = f"""      <div class="omr-row" id="omr_row_{i}">
        <span class="omr-qnum">{i:02d}</span>
        <div class="omr-bubble" data-opt="A">A</div>
        <div class="omr-bubble" data-opt="B">B</div>
        <div class="omr-bubble" data-opt="C">C</div>
        <div class="omr-bubble" data-opt="D">D</div>
      </div>"""
        rows.append(row)
    return "\n".join(rows)

def generate_answer_table_rows(questions):
    rows = []
    for idx, q_data in enumerate(questions, start=1):
        ans = q_data["ans"]
        exp = q_data["exp"]
        row = f"""        <tr>
          <td style="text-align: center; font-weight: bold;">{idx}</td>
          <td style="text-align: center; font-weight: bold; color: #166534;">{ans}</td>
          <td>{exp}</td>
        </tr>"""
        rows.append(row)
    return "\n".join(rows)

def build_papers():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 70)
    print("BUILDING CBSE CLASS 9 SOCIAL SCIENCE - SET G (FINAL MASTERY)")
    print("=" * 70)
    
    for ch in CHAPTERS_DATA:
        ch_num = ch["num"]
        ch_num_padded = f"{ch_num:02d}"
        ch_title = ch["title"]
        ch_title_upper = ch_title.upper()
        out_rel_path = ch["file"]
        out_full_path = os.path.join(workspace_dir, out_rel_path)
        questions = ch["questions"]
        
        print(f"Generating Ch {ch_num:02d}: {ch_title} -> {out_rel_path} ({len(questions)} MCQs)...")
        
        # Build answer map
        answers_dict = {f"q{idx}": q["ans"] for idx, q in enumerate(questions, start=1)}
        answers_json = json.dumps(answers_dict)
        
        q_html = generate_questions_html(questions)
        omr_html = generate_omr_grid_html(len(questions))
        ans_rows = generate_answer_table_rows(questions)
        
        paper_html = HTML_TEMPLATE_SET_G.format(
            chapter_num=ch_num,
            chapter_num_padded=ch_num_padded,
            chapter_title=ch_title,
            chapter_title_upper=ch_title_upper,
            questions_html=q_html,
            omr_grid_html=omr_html,
            answer_table_rows=ans_rows,
            answers_json=answers_json
        )
        
        os.makedirs(os.path.dirname(out_full_path), exist_ok=True)
        with open(out_full_path, "w", encoding="utf-8") as f:
            f.write(paper_html)
            
    print("\nSUCCESS: All 9 Set G Social Science Exam Papers generated successfully!")
    print(f"Total MCQs generated: {len(CHAPTERS_DATA) * 25}")

if __name__ == "__main__":
    build_papers()
