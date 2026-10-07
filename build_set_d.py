"""
Build script for CBSE Class 9 Science - SET D (Assertion - Reasoning Special)
Generates 8 chapter-wise exam papers (25 Assertion-Reasoning questions each = 200 questions).
Strictly 100% CBSE English Medium.
"""

import json
import os
from data_set_d_part1 import (
    CHAPTER_01_QUESTIONS,
    CHAPTER_02_QUESTIONS,
    CHAPTER_03_QUESTIONS,
    CHAPTER_04_QUESTIONS,
)
from data_set_d_part2 import (
    CHAPTER_05_QUESTIONS,
    CHAPTER_06_QUESTIONS,
    CHAPTER_07_QUESTIONS,
    CHAPTER_08_QUESTIONS,
)

CHAPTERS_DATA = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "file": "Science_Exam_Papers/chapter_01_exploration_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Scientific measurement standards, dimensional consistency, pendulum mechanics, and experimental error control.",
        "questions": CHAPTER_01_QUESTIONS
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "file": "Science_Exam_Papers/chapter_02_cell_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Cytological mechanics, osmotic turgor, organelle endosymbiosis, lysosomal autolysis, and chromatin condensation.",
        "questions": CHAPTER_02_QUESTIONS
    },
    {
        "num": 3,
        "title": "Tissues: Plant & Animal Structures",
        "file": "Science_Exam_Papers/chapter_03_tissues_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Histological adaptations, meristematic division, vascular conductive mechanics, and muscular-epithelial specializations.",
        "questions": CHAPTER_03_QUESTIONS
    },
    {
        "num": 4,
        "title": "Describing Motion & Kinematics",
        "file": "Science_Exam_Papers/chapter_04_motion_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Vector kinematics, graphical derivatives, centripetal acceleration vectors, and non-uniform motion dynamics.",
        "questions": CHAPTER_04_QUESTIONS
    },
    {
        "num": 5,
        "title": "Exploring Mixtures: Solution, Colloid & Suspension",
        "file": "Science_Exam_Papers/chapter_05_mixtures_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Colloidal stability, Brownian motion kinetics, Tyndall scattering mechanisms, and phase separation thermodynamics.",
        "questions": CHAPTER_05_QUESTIONS
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion & Laws of Motion",
        "file": "Science_Exam_Papers/chapter_06_forces_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Newtonian inertial frames, momentum impulse rate of change, and simultaneous action-reaction non-cancellation.",
        "questions": CHAPTER_06_QUESTIONS
    },
    {
        "num": 7,
        "title": "Work, Energy & Simple Machines",
        "file": "Science_Exam_Papers/chapter_07_work_energy_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Orthogonal work nullification, mechanical energy conservation, power kinetics, and lever mechanical advantage.",
        "questions": CHAPTER_07_QUESTIONS
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom: Structure & Composition",
        "file": "Science_Exam_Papers/chapter_08_atom_set_d.html",
        "desc": "SET D (Assertion - Reasoning Special): Nuclear scattering kinematics, stationary quantum states, octet stability, isotopic mass calculations, and nuclear applications.",
        "questions": CHAPTER_08_QUESTIONS
    }
]

HTML_TEMPLATE_SET_D = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 9 Science - Chapter {chapter_num}: {chapter_title} (SET D - Assertion & Reasoning Special)</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    .set-d-badge {{
      display: inline-block;
      background: linear-gradient(135deg, #6d28d9, #4f46e5);
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-weight: 800;
      font-size: 12px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .ar-box {{
      background: #f8fafc;
      border-left: 4px solid #6d28d9;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin-top: 8px;
      margin-bottom: 12px;
      font-size: 13.5px;
      line-height: 1.6;
    }}
    .ar-box p {{
      margin: 4px 0;
    }}
    .ar-label {{
      font-weight: 800;
      color: #4c1d95;
    }}
    .ar-directions-banner {{
      background: #ede9fe;
      border: 1.5px solid #c4b5fd;
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 20px;
      font-size: 13px;
      line-height: 1.6;
      color: #312e81;
    }}
    .ar-directions-banner h5 {{
      margin: 0 0 6px 0;
      font-size: 13.5px;
      color: #4c1d95;
      font-weight: 800;
      text-transform: uppercase;
    }}
    .option-item {{
      font-size: 13px;
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
      <span class="set-d-badge">SET D — ASSERTION & REASONING SPECIAL</span>
    </div>
    <div class="exam-chapter">CHAPTER {chapter_num_padded}: {chapter_title_upper}</div>
    <div class="meta-row">
      <span><b>TIME ALLOWED:</b> 45 MINUTES</span>
      <span><b>MAXIMUM MARKS:</b> 25 MARKS</span>
      <span><b>SERIES:</b> CBS-IX-SCI-SET-D-{chapter_num_padded}</span>
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
    <h4>General Instructions (SET D - Assertion & Reasoning Special):</h4>
    <ol>
      <li>The question paper comprises <b>25 Assertion-Reasoning Questions</b> of <b>1 mark each</b>.</li>
      <li>Each question consists of two statements — <b>Assertion (A)</b> and <b>Reason (R)</b>.</li>
      <li>Select the correct option from the following 4 standardized choices:
        <ul style="margin: 4px 0 4px 20px; list-style-type: disc;">
          <li><b>(A)</b> Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).</li>
          <li><b>(B)</b> Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).</li>
          <li><b>(C)</b> Assertion (A) is true but Reason (R) is false.</li>
          <li><b>(D)</b> Assertion (A) is false but Reason (R) is true.</li>
        </ul>
      </li>
      <li><b>Section A (Q1 – Q10):</b> Core Theoretical Principles & Scientific Definitions.</li>
      <li><b>Section B (Q11 – Q18):</b> Experimental Observations & Phenomenological Inferences.</li>
      <li><b>Section C (Q19 – Q25):</b> Advanced Conceptual Nuances & Common Scientific Misconceptions.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding bubble on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <!-- Universal Directions Banner -->
  <div class="ar-directions-banner">
    <h5>Standard Directions for all 25 Assertion & Reasoning Questions:</h5>
    <div><b>(A)</b> Both (A) and (R) are true and (R) is the correct explanation of (A).</div>
    <div><b>(B)</b> Both (A) and (R) are true but (R) is NOT the correct explanation of (A).</div>
    <div><b>(C)</b> Assertion (A) is true but Reason (R) is false.</div>
    <div><b>(D)</b> Assertion (A) is false but Reason (R) is true.</div>
  </div>

  <!-- Questions Container -->
  <div class="questions-container">

    <div class="section-banner">
      <span>SECTION A: CORE THEORETICAL PRINCIPLES (Q.1 TO Q.10)</span>
      <span>[10 MARKS]</span>
    </div>

{section_a_html}

    <div class="section-banner">
      <span>SECTION B: EXPERIMENTAL OBSERVATIONS & INFERENCES (Q.11 TO Q.18)</span>
      <span>[8 MARKS]</span>
    </div>

{section_b_html}

    <div class="section-banner">
      <span>SECTION C: ADVANCED NUANCES & MISCONCEPTIONS (Q.19 TO Q.25)</span>
      <span>[7 MARKS]</span>
    </div>

{section_c_html}

  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET D)</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & SCIENTIFIC CAUSAL EXPLANATIONS (SET D)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Scientific Rationale & Causal Analysis</th>
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
  alert("SET D Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nReview the detailed scientific causal solutions below.");
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

def generate_set_d_papers():
    for ch in CHAPTERS_DATA:
        q_data = ch["questions"]
        answers_dict = {}
        
        sec_a_cards = []
        sec_b_cards = []
        sec_c_cards = []
        
        ar_options = [
            ("A", "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A)."),
            ("B", "Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A)."),
            ("C", "Assertion (A) is true but Reason (R) is false."),
            ("D", "Assertion (A) is false but Reason (R) is true.")
        ]
        
        for idx, item in enumerate(q_data):
            qnum = idx + 1
            answers_dict[qnum] = item["ans"]
            
            opts_html = []
            for letter, opt_text in ar_options:
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
                <div class="ar-box">
                  <p><span class="ar-label">Assertion (A):</span> {item["a"]}</p>
                  <p><span class="ar-label">Reason (R):</span> {item["r"]}</p>
                </div>
              </div>
              <div class="options-grid">
                {''.join(opts_html)}
              </div>
              <div class="feedback-msg" id="feedback_{qnum}"></div>
            </div>
            """
            
            if qnum <= 10:
                sec_a_cards.append(card_html)
            elif qnum <= 18:
                sec_b_cards.append(card_html)
            else:
                sec_c_cards.append(card_html)
                
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
            
        ans_rows = []
        for idx, item in enumerate(q_data):
            qnum = idx + 1
            ans_rows.append(f"""
            <tr>
              <td style="font-weight: bold; text-align: center;">Q.{qnum}</td>
              <td style="text-align: center;"><span class="ans-badge" style="background: #6d28d9;">({item['ans']})</span></td>
              <td>{item['exp']}</td>
            </tr>
            """)
            
        full_html = HTML_TEMPLATE_SET_D.format(
            chapter_num=ch["num"],
            chapter_num_padded=f"{ch['num']:02d}",
            chapter_title=ch["title"],
            chapter_title_upper=ch["title"].upper(),
            section_a_html=''.join(sec_a_cards),
            section_b_html=''.join(sec_b_cards),
            section_c_html=''.join(sec_c_cards),
            omr_grid_html=''.join(omr_rows),
            answer_table_rows=''.join(ans_rows),
            answers_json=json.dumps(answers_dict)
        )
        
        with open(ch["file"], "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[OK] Generated {ch['file']}")

if __name__ == "__main__":
    generate_set_d_papers()
    print("ALL SET D PAPERS GENERATED SUCCESSFULLY!")
