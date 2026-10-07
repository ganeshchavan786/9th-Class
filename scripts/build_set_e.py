"""
Build script for CBSE Class 9 Science - SET E (Case Study & Practical Experiments)
Generates 8 chapter-wise exam papers (5 Case Studies / 25 questions each = 200 questions).
Strictly 100% CBSE English Medium.
"""

import json
import os
import sys

# Ensure scripts folder is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_set_e_part1 import (
    CHAPTER_01_CASES,
    CHAPTER_02_CASES,
    CHAPTER_03_CASES,
    CHAPTER_04_CASES,
)
from data_set_e_part2 import (
    CHAPTER_05_CASES,
    CHAPTER_06_CASES,
    CHAPTER_07_CASES,
    CHAPTER_08_CASES,
)

CHAPTERS_DATA = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "file": "Science_Exam_Papers/chapter_01_exploration_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Simple pendulum period calculation, vernier and screw gauge metrology, density by liquid displacement, thermal expansion, and laboratory spill safety.",
        "cases": CHAPTER_01_CASES
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "file": "Science_Exam_Papers/chapter_02_cell_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Onion epidermal mount preparation, Rhoeo leaf plasmolysis, RBC osmotic fragility, cell fractionation bioenergetics, and endomembrane autoradiography.",
        "cases": CHAPTER_02_CASES
    },
    {
        "num": 3,
        "title": "Tissues: Plant & Animal Structures",
        "file": "Science_Exam_Papers/chapter_03_tissues_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Dicot stem T.S. histology, stomatal density and cobalt chloride transpiration, eosin xylem dye tracing, muscular slide comparisons, and blood smear hematology.",
        "cases": CHAPTER_03_CASES
    },
    {
        "num": 4,
        "title": "Describing Motion & Kinematics",
        "file": "Science_Exam_Papers/chapter_04_motion_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Ticker-timer acceleration down a ramp, automotive thinking and braking distances, automated photogate free-fall determination of g, multi-stage v-t graphs, and centripetal apparatus.",
        "cases": CHAPTER_04_CASES
    },
    {
        "num": 5,
        "title": "Exploring Mixtures: Solution, Colloid & Suspension",
        "file": "Science_Exam_Papers/chapter_05_mixtures_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Optical Tyndall scattering and filter tests, copper sulfate crystallization curves, ink paper chromatography, separating funnel extraction of kerosene-water, and heating iron-sulfur.",
        "cases": CHAPTER_05_CASES
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion & Laws of Motion",
        "file": "Science_Exam_Papers/chapter_06_forces_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Verifying Newton's second law on friction-compensated track, automotive crash dummy impulse forces, air track glider momentum conservation, spring balance action-reaction pairs, and ramp friction.",
        "cases": CHAPTER_06_CASES
    },
    {
        "num": 7,
        "title": "Work, Energy & Simple Machines",
        "file": "Science_Exam_Papers/chapter_07_work_energy_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Roller coaster mechanical energy conservation, lifting vs ramp work against friction, electric pump efficiency and kWh billing, lever principle of moments, and 4-pulley tackle systems.",
        "cases": CHAPTER_07_CASES
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom: Structure & Composition",
        "file": "Science_Exam_Papers/chapter_08_atom_set_e.html",
        "desc": "SET E (Case Study & Practical Experiments): Geiger-Marsden alpha scattering data, cathode and canal ray discharge tubes, Bohr-Bury quantum shells, valency dynamics, and chlorine fractional isotope mass calculations.",
        "cases": CHAPTER_08_CASES
    }
]

HTML_TEMPLATE_SET_E = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 9 Science - Chapter {chapter_num}: {chapter_title} (SET E - Case Study & Practical Experiments)</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    .set-e-badge {{
      display: inline-block;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 12px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .case-banner {{
      background: #f0f9ff;
      border: 1.5px solid #bae6fd;
      border-left: 5px solid #0284c7;
      border-radius: 6px;
      padding: 14px 18px;
      margin-top: 20px;
      margin-bottom: 15px;
    }}
    .case-banner h4 {{
      margin: 0 0 8px 0;
      color: #0369a1;
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .case-passage {{
      font-size: 13px;
      line-height: 1.65;
      color: #0f172a;
    }}
  </style>
</head>
<body>

<div class="exam-paper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="interactive-header no-print">
    <div class="timer-display">
      ⏱️ Time Remaining: <span id="timerDisplay">45:00</span>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
      <button class="btn btn-primary" id="timerBtn" onclick="toggleTimer()">⏸️ Pause Timer</button>
      <button class="btn btn-secondary" onclick="checkAnswers()">✅ Submit & Check</button>
      <button class="btn btn-primary" onclick="toggleAnswerKey()">🔑 View Solutions</button>
      <button class="btn btn-primary" onclick="window.print()">🖨️ Print Exam Paper</button>
    </div>
  </div>

  <!-- Standard CBSE School Exam Header -->
  <div class="exam-header">
    <div class="school-title">CENTRAL BOARD OF SECONDARY EDUCATION — PRACTICE EXAMINATION</div>
    <div class="exam-sub">CLASS IX • SCIENCE (SUBJECT CODE: 086) • ACADEMIC SESSION 2026-27</div>
    <div style="margin-top: 5px;">
      <span class="set-e-badge">SET E — CASE STUDY & PRACTICAL EXPERIMENTS</span>
    </div>
    <div class="exam-chapter">CHAPTER {chapter_num_padded}: {chapter_title_upper}</div>
    <div class="meta-row">
      <span><b>TIME ALLOWED:</b> 45 MINUTES</span>
      <span><b>MAXIMUM MARKS:</b> 25 MARKS</span>
      <span><b>SERIES:</b> CBS-IX-SCI-SET-E-{chapter_num_padded}</span>
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
    <h4>General Instructions (SET E - Case Study & Practical Experiments):</h4>
    <ol>
      <li>The question paper comprises <b>5 In-Depth Practical Case Studies</b> with <b>5 MCQs each (Total: 25 Questions, 1 Mark each)</b>.</li>
      <li>Read each laboratory experiment, data table, and passage carefully before answering the corresponding questions.</li>
      <li>Each question has 4 options with a single correct answer.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding bubble on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <!-- Questions Container -->
  <div class="questions-container">
{cases_html}
  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET E)</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & PRACTICAL INVESTIGATION EXPLANATIONS (SET E)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Scientific Rationale & Experimental Data Analysis</th>
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
      ⬅️ Return to Science Examination Dashboard
    </a>
  </div>

</div>

<script>
const correctAnswers = {answers_json};

let timeLeft = 45 * 60;
let timerRunning = true;
let timerInterval = setInterval(updateTimer, 1000);

function updateTimer() {{
  if (!timerRunning) return;
  if (timeLeft <= 0) {{
    clearInterval(timerInterval);
    document.getElementById("timerDisplay").innerText = "00:00 (Time Over)";
    alert("Time is up! Please submit and check your answers.");
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
  alert("SET E Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nReview the detailed experimental solutions below.");
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

def generate_set_e_papers():
    for ch in CHAPTERS_DATA:
        cases = ch["cases"]
        answers_dict = {}
        all_cases_html = []
        ans_rows = []
        global_qnum = 1
        
        for case in cases:
            case_html_parts = []
            case_html_parts.append(f"""
            <div class="case-banner">
              <h4>{case["title"]}</h4>
              <div class="case-passage">{case["passage"]}</div>
            </div>
            """)
            
            for q in case["questions"]:
                qnum = global_qnum
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
                case_html_parts.append(card_html)
                
                ans_rows.append(f"""
                <tr>
                  <td style="font-weight: bold; text-align: center;">Q.{qnum}</td>
                  <td style="text-align: center;"><span class="ans-badge" style="background: #0284c7;">({q['ans']})</span></td>
                  <td>{q['exp']}</td>
                </tr>
                """)
                
                global_qnum += 1
                
            all_cases_html.append(''.join(case_html_parts))
            
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
            
        full_html = HTML_TEMPLATE_SET_E.format(
            chapter_num=ch["num"],
            chapter_num_padded=f"{ch['num']:02d}",
            chapter_title=ch["title"],
            chapter_title_upper=ch["title"].upper(),
            cases_html=''.join(all_cases_html),
            omr_grid_html=''.join(omr_rows),
            answer_table_rows=''.join(ans_rows),
            answers_json=json.dumps(answers_dict)
        )
        
        with open(ch["file"], "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[OK] Generated {ch['file']}")

if __name__ == "__main__":
    generate_set_e_papers()
    print("ALL SET E PAPERS GENERATED SUCCESSFULLY!")
