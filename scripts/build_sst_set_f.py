"""
Build script for CBSE Class 9 Social Science - SET F (Rapid Fire Speed Test)
Generates 9 chapter-wise exam papers (25 Rapid Fire MCQs each = 225 questions).
Curriculum: NCERT Class 9 Social Science (Latest Edition)
Strictly 100% CBSE English Medium.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_sst_set_f_part1 import (
    CHAPTER_01_QUESTIONS,
    CHAPTER_02_QUESTIONS,
    CHAPTER_03_QUESTIONS,
    CHAPTER_04_QUESTIONS,
)
from data_sst_set_f_part2 import (
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
        "file": "Social_Science_Exam_Papers/chapter_01_understanding_sst_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Epigraphy, numismatics, James Prinsep, Wheeler stratigraphy, C-14 half-life, and Popper's falsifiability.",
        "questions": CHAPTER_01_QUESTIONS
    },
    {
        "num": 2,
        "title": "Shaping of the Earth's Surface",
        "file": "Social_Science_Exam_Papers/chapter_02_shaping_earth_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Endogenic vs exogenic forces, P and S seismic waves, plate boundaries, meanders, cirques, and barchan dunes.",
        "questions": CHAPTER_02_QUESTIONS
    },
    {
        "num": 3,
        "title": "Atmosphere and Climate",
        "file": "Social_Science_Exam_Papers/chapter_03_atmosphere_climate_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Tropospheric lapse rate, stratospheric ozone, Coriolis Ferrel's Law, Southwest monsoon, and Montreal Protocol.",
        "questions": CHAPTER_03_QUESTIONS
    },
    {
        "num": 4,
        "title": "Early Humans and Beginning of Civilisation",
        "file": "Social_Science_Exam_Papers/chapter_04_early_civilisation_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Mesolithic microliths, Bhimbetka art, Mehrgarh farming, 1:2:4 bricks, Great Bath, and Lothal dockyard.",
        "questions": CHAPTER_04_QUESTIONS
    },
    {
        "num": 5,
        "title": "State and Society up to 1000 CE",
        "file": "Social_Science_Exam_Papers/chapter_05_state_society_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Kautilya's Saptanga, Samaharta, Ashoka's Major Rock Edicts, Prayag Prashasti, Aryabhatiya, and Uttaramerur Kudavolai.",
        "questions": CHAPTER_05_QUESTIONS
    },
    {
        "num": 6,
        "title": "Democracy",
        "file": "Social_Science_Exam_Papers/chapter_06_democracy_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Lincoln's definition, Mexico's PRI, Musharraf's LFO, 'one person one vote one value', and Sen's famine thesis.",
        "questions": CHAPTER_06_QUESTIONS
    },
    {
        "num": 7,
        "title": "Elections",
        "file": "Social_Science_Exam_Papers/chapter_07_elections_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): 543 Lok Sabha seats, 84 SC / 47 ST reserved, 61st Amendment 18 years, Article 324 ECI, and standalone EVM/VVPAT.",
        "questions": CHAPTER_07_QUESTIONS
    },
    {
        "num": 8,
        "title": "Building Blocks in Economics: The Problem of Choice",
        "file": "Social_Science_Exam_Papers/chapter_08_economics_choice_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Scarcity postulates, opportunity cost, 4 factors of production, PPF downward slope and concavity, and structural transformation.",
        "questions": CHAPTER_08_QUESTIONS
    },
    {
        "num": 9,
        "title": "The Price Puzzle: What Drives the Market",
        "file": "Social_Science_Exam_Papers/chapter_09_price_puzzle_set_f.html",
        "desc": "SET F (Rapid Fire Speed Test): Law of Demand and Supply, market-clearing equilibrium, substitutes vs complements, price ceilings, and MSP buffer stocks.",
        "questions": CHAPTER_09_QUESTIONS
    }
]

HTML_TEMPLATE_SET_F = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 9 Social Science - Chapter {chapter_num}: {chapter_title} (SET F - Rapid Fire Speed Test)</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    .set-f-badge {{
      display: inline-block;
      background: linear-gradient(135deg, #ea580c, #c2410c);
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 12px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .rapid-banner {{
      background: #fff7ed;
      border: 1.5px solid #fed7aa;
      border-left: 5px solid #ea580c;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 16px;
      font-size: 12.5px;
      color: #9a3412;
      line-height: 1.5;
    }}
  </style>
</head>
<body>

<div class="exam-paper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="interactive-header no-print">
    <div class="timer-display">
      ⏱️ Speed Countdown: <span id="timerDisplay">30:00</span>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
      <button class="btn btn-primary" id="timerBtn" onclick="toggleTimer()">⏸️ Pause Timer</button>
      <button class="btn btn-secondary" onclick="checkAnswers()">⚡ Submit Speed Test</button>
      <button class="btn btn-primary" onclick="toggleAnswerKey()">🔑 View Solutions</button>
      <button class="btn btn-primary" onclick="window.print()">🖨️ Print Exam Paper</button>
    </div>
  </div>

  <!-- Standard CBSE School Exam Header -->
  <div class="exam-header">
    <div class="school-title">CENTRAL BOARD OF SECONDARY EDUCATION — PRACTICE EXAMINATION</div>
    <div class="exam-sub">CLASS IX • SOCIAL SCIENCE (SUBJECT CODE: 087) • ACADEMIC SESSION 2026-27</div>
    <div style="margin-top: 5px;">
      <span class="set-f-badge">SET F — RAPID FIRE SPEED TEST (30 MINS)</span>
    </div>
    <div class="exam-chapter">CHAPTER {chapter_num_padded}: {chapter_title_upper}</div>
    <div class="meta-row">
      <span><b>TIME ALLOWED:</b> 30 MINUTES</span>
      <span><b>MAXIMUM MARKS:</b> 25 MARKS</span>
      <span><b>SERIES:</b> CBS-IX-SST-SET-F-{chapter_num_padded}</span>
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
    <h4>General Instructions (SET F - Rapid Fire Speed Test):</h4>
    <ol>
      <li>The question paper comprises <b>25 Rapid Fire Multiple Choice Questions</b> of <b>1 mark each</b>.</li>
      <li>Designed for <b>Rapid Recall & High-Speed Accuracy</b>: Recommended target time is <b>30 Minutes</b>.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding bubble on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <div class="rapid-banner">
    ⚡ <b>SPEED CHALLENGE INSTRUCTIONS:</b> Answer promptly without looking at notes. Test your instant recall of historical milestones, geographic terms, constitutional provisions, and core economic laws!
  </div>

  <!-- Questions Container -->
  <div class="questions-container">
{questions_html}
  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET F)</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & RAPID RECALL EXPLANATIONS (SET F)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Curricular Concept & Rapid Recall Analysis</th>
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

let timeLeft = 30 * 60;
let timerRunning = true;
let timerInterval = setInterval(updateTimer, 1000);

function updateTimer() {{
  if (!timerRunning) return;
  if (timeLeft <= 0) {{
    clearInterval(timerInterval);
    document.getElementById("timerDisplay").innerText = "00:00 (Time Over)";
    alert("Speed Test time is up! Please submit and check your answers.");
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
  let total = 25;
  for (let i = 1; i <= total; i++) {{
    let radios = document.getElementsByName("q" + i);
    let selected = null;
    for (let r of radios) {{
      if (r.checked) selected = r.value;
    }}
    let card = document.getElementById("qcard_" + i);
    let feedback = document.getElementById("feedback_" + i);
    if (!feedback) continue;
    
    if (selected === correctAnswers[i]) {{
      score++;
      feedback.className = "feedback-msg feedback-correct";
      feedback.style.display = "block";
      feedback.innerHTML = "✅ Correct! (" + correctAnswers[i] + ")";
      if (card) card.style.borderColor = "#86efac";
    }} else if (selected === null) {{
      feedback.className = "feedback-msg feedback-wrong";
      feedback.style.display = "block";
      feedback.innerHTML = "⚠️ Unattempted. Correct option is <b>(" + correctAnswers[i] + ")</b>";
      if (card) card.style.borderColor = "#fca5a5";
    }} else {{
      feedback.className = "feedback-msg feedback-wrong";
      feedback.style.display = "block";
      feedback.innerHTML = "❌ Your answer: (" + selected + ") | Correct: <b>(" + correctAnswers[i] + ")</b>";
      if (card) card.style.borderColor = "#fca5a5";
    }}
  }}
  alert("SET F Speed Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nReview the detailed solutions below.");
}}

function toggleAnswerKey() {{
  let sec = document.getElementById("answerKeySection");
  if (sec.style.display === "none") {{
    sec.style.display = "block";
  }} else {{
    sec.style.display = "none";
  }}
}}
</script>

</body>
</html>
"""

def generate_set_f_papers():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for ch in CHAPTERS_DATA:
        questions = ch["questions"]
        answers_dict = {}
        all_q_html = []
        ans_rows = []
        
        for idx, q in enumerate(questions):
            qnum = idx + 1
            answers_dict[qnum] = q["ans"]
            
            opts_html = []
            letters = ["A", "B", "C", "D"]
            for opt_idx, opt_text in enumerate(q["options"]):
                letter = letters[opt_idx]
                opts_html.append(f"""
                <label class="option-item">
                  <input type="radio" name="q{qnum}" value="{letter}">
                  <span class="option-letter">({letter})</span>
                  <span>{opt_text}</span>
                </label>
                """)
                
            card_html = f"""
            <div class="question-card" id="qcard_{qnum}">
              <div class="question-text">
                <span class="question-number">Q.{qnum}</span>
                {q["q"]}
              </div>
              <div class="options-grid">
                {''.join(opts_html)}
              </div>
              <div class="feedback-msg" id="feedback_{qnum}"></div>
            </div>
            """
            all_q_html.append(card_html)
            
            ans_rows.append(f"""
            <tr>
              <td style="font-weight: bold; text-align: center;">Q.{qnum}</td>
              <td style="text-align: center;"><span class="ans-badge" style="background: #ea580c;">({q['ans']})</span></td>
              <td>{q['exp']}</td>
            </tr>
            """)
            
        omr_rows = []
        for qnum in range(1, 26):
            omr_rows.append(f"""
            <div class="omr-row">
              <span class="omr-qnum">{qnum:02d}</span>
              <div class="omr-bubbles">
                <div class="bubble">A</div>
                <div class="bubble">B</div>
                <div class="bubble">C</div>
                <div class="bubble">D</div>
              </div>
            </div>
            """)
            
        full_html = HTML_TEMPLATE_SET_F.format(
            chapter_num=ch["num"],
            chapter_num_padded=f"{ch['num']:02d}",
            chapter_title=ch["title"],
            chapter_title_upper=ch["title"].upper(),
            questions_html=''.join(all_q_html),
            omr_grid_html=''.join(omr_rows),
            answer_table_rows=''.join(ans_rows),
            answers_json=json.dumps(answers_dict)
        )
        
        target_path = os.path.join(root_dir, ch["file"])
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[OK] Generated {ch['file']}")

if __name__ == "__main__":
    generate_set_f_papers()
    print("ALL 9 SOCIAL SCIENCE SET F PAPERS GENERATED SUCCESSFULLY!")
