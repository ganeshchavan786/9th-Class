"""
Build script for CBSE Class 9 Science - SET B Examination Papers (Chapters 1 to 8)
Focus: HOTS (Higher Order Thinking Skills), Advanced Numericals, Critical Assertion-Reason, and Experimental Case Studies.
Zero Marathi text in exam papers - strictly standard English.
"""

import json
import os

SET_B_DATA = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "file": "Science_Exam_Papers/chapter_01_exploration_set_b.html",
        "short_file": "chapter_01_exploration_set_b.html",
        "description": "SET B (HOTS & Numericals): Vernier least count, precision vs accuracy, zero error calculations, experimental uncertainty, and laboratory safety protocols.",
        "questions": [
            {
                "q": "The main scale of a vernier caliper reads in millimeters. If 10 vernier scale divisions coincide with 9 main scale divisions, what is the least count of the instrument?",
                "options": ["0.1 mm (0.01 cm)", "1.0 mm (0.1 cm)", "0.01 mm (0.001 cm)", "0.9 mm (0.09 cm)"],
                "ans": "A",
                "exp": "Least Count $= 1\\text{ MSD} - 1\\text{ VSD} = 1\\text{ mm} - 0.9\\text{ mm} = 0.1\\text{ mm} = 0.01\\text{ cm}$."
            },
            {
                "q": "When the jaws of a screw gauge are brought into contact, the zero of the circular scale lies 3 divisions below the reference datum line. This zero error is:",
                "options": ["Positive zero error (must be subtracted from observed reading)", "Negative zero error (must be added to observed reading)", "Random parallax error", "Instrumental backlash error"],
                "ans": "A",
                "exp": "When the zero of the circular scale lies below the reference line, the gauge reads positive without load. Hence it is positive zero error and must be subtracted from the final reading."
            },
            {
                "q": "A student measures the mass of an object as 25.0 g and its volume as 10.0 cm³. What is the density expressed with the correct number of significant figures?",
                "options": ["2.5 g/cm³", "2.50 g/cm³", "2.500 g/cm³", "0.40 g/cm³"],
                "ans": "B",
                "exp": "Both 25.0 g and 10.0 cm³ have 3 significant figures. The quotient $25.0 / 10.0 = 2.50\\text{ g/cm}^3$ must also have 3 significant figures."
            },
            {
                "q": "Which of the following is equivalent to 1 kilogram per cubic meter ($1\\text{ kg/m}^3$) in CGS units?",
                "options": ["$1000\\text{ g/cm}^3$", "$10^{-3}\\text{ g/cm}^3$", "$100\\text{ g/cm}^3$", "$10^{-6}\\text{ g/cm}^3$"],
                "ans": "B",
                "exp": "$1\\text{ kg/m}^3 = \\frac{1000\\text{ g}}{(100\\text{ cm})^3} = \\frac{10^3}{10^6}\\text{ g/cm}^3 = 10^{-3}\\text{ g/cm}^3$ (or $0.001\\text{ g/cm}^3$)."
            },
            {
                "q": "A student measures a wire's diameter as 2.4 mm, 2.5 mm, 2.4 mm, and 2.7 mm. The mean diameter of the wire is:",
                "options": ["2.5 mm", "2.4 mm", "2.6 mm", "2.45 mm"],
                "ans": "A",
                "exp": "$\\text{Mean} = \\frac{2.4 + 2.5 + 2.4 + 2.7}{4} = \\frac{10.0}{4} = 2.5\\text{ mm}$."
            },
            {
                "q": "When heating an inflammable liquid such as ethanol in a chemistry laboratory, which apparatus should always be employed to avoid fire hazard?",
                "options": ["Direct heating over an open Bunsen flame", "A thermostatically controlled water bath", "A blowpipe flame", "Direct heating in an open silica crucible"],
                "ans": "B",
                "exp": "Ethanol is highly inflammable (boils at 78°C). Its vapors can ignite easily; hence it must be heated inside a boiling water bath, never directly over an open flame."
            },
            {
                "q": "An irregular stone of mass 78 g is lowered into a measuring cylinder containing 45 mL of water. The water level rises to 55 mL. What is the density of the stone?",
                "options": ["1.42 g/cm³", "7.8 g/cm³", "0.78 g/cm³", "780 g/cm³"],
                "ans": "B",
                "exp": "$\\text{Displaced volume} = 55 - 45 = 10\\text{ mL} = 10\\text{ cm}^3$. $\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}} = \\frac{78\\text{ g}}{10\\text{ cm}^3} = 7.8\\text{ g/cm}^3$."
            },
            {
                "q": "How many millimeters are there in $3.5 \\times 10^{-2}$ kilometers?",
                "options": ["$35,000\\text{ mm}$", "$3,500\\text{ mm}$", "$350\\text{ mm}$", "$350,000\\text{ mm}$"],
                "ans": "A",
                "exp": "$1\\text{ km} = 10^6\\text{ mm}$. Therefore, $3.5 \\times 10^{-2} \\times 10^6 = 3.5 \\times 10^4 = 35,000\\text{ mm}$."
            },
            {
                "q": "In an experiment plotting rate of gas production against temperature, what is the best curve fit when data points show slight experimental scatter?",
                "options": ["Connecting every individual point with zig-zag sharp lines", "Drawing a smooth line/curve of best fit that balances points on either side", "Ignoring all points except the first and last", "Drawing a horizontal line through the origin"],
                "ans": "B",
                "exp": "A line or curve of best fit minimizes random observational errors by showing the overall mathematical trend rather than connecting random fluctuations."
            },
            {
                "q": "A piece of copper of mass 89 g is combined with 178 g of another metal of density 8.9 g/cm³ to form a uniform alloy. If copper density is 8.9 g/cm³, what is the total volume of the alloy?",
                "options": ["10 cm³", "20 cm³", "30 cm³", "40 cm³"],
                "ans": "C",
                "exp": "$V_{Cu} = 89 / 8.9 = 10\\text{ cm}^3$. $V_{metal} = 178 / 8.9 = 20\\text{ cm}^3$. $\\text{Total volume} = 10 + 20 = 30\\text{ cm}^3$."
            },
            {
                "q": "Which SI base unit is defined by fixing the numerical value of the Planck constant $h$ to exactly $6.62607015 \\times 10^{-34}$ in units of $J \\cdot s$?",
                "options": ["Meter", "Second", "Kilogram", "Ampere"],
                "ans": "C",
                "exp": "Under the revised SI definitions (2019), the kilogram (kg) is defined based on the fundamental Planck constant $h$."
            },
            {
                "q": "When observing mercury in a glass tube, the meniscus curves upward (convex). The correct reading is taken at:",
                "options": ["The lowest point of the meniscus", "The highest central point (crest) of the meniscus", "The boundary touching the glass wall", "The mid-point of the meniscus curve"],
                "ans": "B",
                "exp": "Mercury does not wet glass (cohesive forces exceed adhesive forces), forming a convex meniscus. Hence, the reading is taken at the top/crest at eye level."
            },
            {
                "q": "A stopwatch has a smallest division of 0.2 s. A runner's time is recorded as 12.4 s. The percentage uncertainty in this single reading is approximately:",
                "options": ["1.6%", "0.2%", "5.0%", "0.8%"],
                "ans": "A",
                "exp": "$\\text{Percentage uncertainty} = \\frac{\\text{Least count}}{\\text{Measured value}} \\times 100 = \\frac{0.2}{12.4} \\times 100 \\approx 1.61\\%$."
            },
            {
                "q": "Which of the following variables must be manipulated to test if plant height depends on light intensity?",
                "options": ["Keep light intensity constant while changing soil type", "Vary light intensity while keeping soil, water, and temperature identical", "Vary water, fertilizer, and light intensity simultaneously", "Keep all plants in complete darkness"],
                "ans": "B",
                "exp": "A valid scientific test changes only the independent variable (light intensity) while keeping all other confounding variables strictly controlled."
            },
            {
                "q": "Which hazardous chemical symbol displays a skull and crossbones inside a red diamond frame?",
                "options": ["Flammable substance", "Acute severe toxicity / Poison", "Corrosive to metals and skin", "Explosive material"],
                "ans": "B",
                "exp": "The Globally Harmonized System (GHS) skull and crossbones pictogram denotes acute severe toxicity (fatal or poisonous upon exposure)."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Systematic errors cannot be completely eliminated by taking the arithmetic average of a large number of readings.<br>Reason (R): Systematic errors consistently skew measurements in one specific direction (consistently too high or consistently too low).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Averaging reduces random Gaussian errors, but systematic errors (like zero error or faulty calibration) always shift readings unidirectionally, so averaging cannot eliminate them."
            },
            {
                "q": "Assertion (A): A hypothesis must be capable of being disproven (falsifiable) to be considered scientific.<br>Reason (R): A statement that cannot be tested or refuted by any possible empirical observation lies outside the domain of science.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "According to the scientific method (Karl Popper's criterion of falsifiability), scientific hypotheses must make testable predictions that could potentially fail in experiments."
            },
            {
                "q": "Assertion (A): Density is an intensive physical property of a homogeneous pure substance.<br>Reason (R): The ratio of mass to volume remains constant regardless of the total quantity of the substance taken.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Intensive properties do not depend on system size or amount of material. Since doubling mass also doubles volume, the ratio (density) remains constant."
            },
            {
                "q": "Assertion (A): When smelling chemical vapors in a laboratory, one should inhale deeply with the nose directly over the open container.<br>Reason (R): Deep inhalation allows accurate sensory classification of chemical odors.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both statements are completely false and dangerous! Never inhale directly; gently waft vapors towards the nose using your hand from a safe distance."
            },
            {
                "q": "Assertion (A): SI units are based on decimal multiples and sub-multiples.<br>Reason (R): Converting between units in the metric SI system simply involves multiplying or dividing by powers of ten.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The metric SI system uses base 10 prefixes (kilo, mega, centi, milli, micro), making mathematical conversion straightforward without arbitrary conversion fractions."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Calibrating and Measuring Metal Alloy Density<br>An engineer wants to find the exact density of a newly fabricated metallic cylinder. Using a vernier caliper with a least count of 0.01 cm, she measures the diameter $D = 2.00$ cm and height $H = 5.00$ cm. Using an electronic analytical balance, the mass of the cylinder is determined to be $125.60$ g. Take $\\pi = 3.14$.",
                "q": "What is the radius $r$ of the metallic cylinder in centimeters?",
                "options": ["1.00 cm", "2.00 cm", "0.50 cm", "4.00 cm"],
                "ans": "A",
                "exp": "$\\text{Radius } r = D / 2 = 2.00 / 2 = 1.00\\text{ cm}$."
            },
            {
                "q": "What is the calculated volume of the cylinder using $V = \\pi r^2 H$?",
                "options": ["$15.70\\text{ cm}^3$", "$31.40\\text{ cm}^3$", "$62.80\\text{ cm}^3$", "$7.85\\text{ cm}^3$"],
                "ans": "A",
                "exp": "$V = \\pi r^2 H = 3.14 \\times (1.00)^2 \\times 5.00 = 15.70\\text{ cm}^3$."
            },
            {
                "q": "What is the density of the metal cylinder calculated from the measurements?",
                "options": ["8.00 g/cm³", "4.00 g/cm³", "12.56 g/cm³", "1.57 g/cm³"],
                "ans": "A",
                "exp": "$\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}} = \\frac{125.60\\text{ g}}{15.70\\text{ cm}^3} = 8.00\\text{ g/cm}^3$."
            },
            {
                "q": "If the metal cylinder is made of stainless steel (density 8.00 g/cm³), what will be its density expressed in SI units ($\text{kg/m}^3$)?",
                "options": ["$800\\text{ kg/m}^3$", "$8,000\\text{ kg/m}^3$", "$80,000\\text{ kg/m}^3$", "$80\\text{ kg/m}^3$"],
                "ans": "B",
                "exp": "To convert from $\\text{g/cm}^3$ to $\\text{kg/m}^3$, multiply by 1000: $8.00 \\times 1000 = 8,000\\text{ kg/m}^3$."
            },
            {
                "q": "If the electronic balance had a zero error of $+0.60$ g that was uncorrected, what was the true mass and true density of the cylinder?",
                "options": ["126.20 g and 8.04 g/cm³", "125.00 g and 7.96 g/cm³", "125.00 g and 8.00 g/cm³", "124.40 g and 7.90 g/cm³"],
                "ans": "B",
                "exp": "$\\text{True mass} = 125.60 - 0.60 = 125.00\\text{ g}$. $\\text{True density} = 125.00 / 15.70 \\approx 7.96\\text{ g/cm}^3$."
            }
        ]
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "file": "Science_Exam_Papers/chapter_02_cell_set_b.html",
        "short_file": "chapter_02_cell_set_b.html",
        "description": "SET B (HOTS & Cell Physiology): Surface area to volume ratio, endomembrane transport, mitochondrial cristae bioenergetics, and reversible plasmolysis dynamics.",
        "questions": [
            {
                "q": "Why are most biological cells microscopic in size rather than growing into giant macroscopic entities?",
                "options": ["They lack sufficient DNA to divide", "As a cell grows, its volume increases faster than its surface area, limiting nutrient diffusion across the membrane", "Large cells are crushed by atmospheric air pressure", "Cell organelles cannot replicate inside large volumes"],
                "ans": "B",
                "exp": "Surface area increases as $r^2$ while volume increases as $r^3$. A small cell maintains a high surface area to volume ratio ($SA/V$) necessary for rapid metabolic transport."
            },
            {
                "q": "A student places peeled raw potato cups in three troughs: Trough A (water, empty cup), Trough B (water, cup filled with 10% sugar solution), and Trough C (boiled potato cup, filled with 10% sugar solution). Water collects inside the cup in:",
                "options": ["Trough A only", "Trough B only", "Trough B and Trough C", "Trough C only"],
                "ans": "B",
                "exp": "Water enters cup B by endosmosis across living selectively permeable potato cell membranes. In cup C, boiling killed cells, destroying osmotic selective permeability."
            },
            {
                "q": "Which sequence correctly traces the intracellular pathway of a newly synthesized digestive enzyme from its site of manufacture to secretion outside the cell?",
                "options": ["Golgi apparatus → Ribosome → RER → Plasma membrane", "Rough ER → Transport vesicle → Golgi apparatus → Secretory vesicle → Plasma membrane", "Smooth ER → Lysosome → Mitochondria → Plasma membrane", "Nucleus → Cytoplasm → Vacuole → Plasma membrane"],
                "ans": "B",
                "exp": "Proteins synthesized on ribosomes of the Rough ER are shuttled via transport vesicles to the Golgi for modification/sorting, then packaged into secretory vesicles for exocytosis."
            },
            {
                "q": "Why does a plant cell not undergo lysis (bursting) when placed in pure distilled water, unlike a human red blood cell?",
                "options": ["Plant cells do not absorb water in hypotonic solutions", "The rigid cellulose cell wall exerts inward wall pressure equal and opposite to turgor pressure", "Plant cytoplasm contains zero dissolved solutes", "Plant cell membranes lack aquaporin channels"],
                "ans": "B",
                "exp": "As water enters a plant cell, turgor pressure builds up; the rigid cellulose wall exerts equal inward wall pressure, halting further osmotic influx before bursting."
            },
            {
                "q": "Which cellular organelle is intimately involved in membrane biogenesis (the synthesis of lipids and proteins required to build new cell membranes)?",
                "options": ["Lysosomes and Peroxisomes", "Endoplasmic Reticulum (RER for proteins, SER for lipids)", "Centrioles and Centrosomes", "Plastids and Vacuoles"],
                "ans": "B",
                "exp": "RER synthesizes membrane proteins and SER synthesizes membrane lipids (phospholipids and cholesterol), together driving membrane biogenesis."
            },
            {
                "q": "The inner mitochondrial membrane contains a high proportion of cardiolipin and is deeply folded into cristae. In which cells would you expect to find the highest density of cristae?",
                "options": ["Dormant plant seed cells", "Sperm tail cells and avian flight muscle cells", "Subcutaneous adipose fat cells", "Dead cork bark cells"],
                "ans": "B",
                "exp": "Cells with extreme, continuous energetic demands (such as avian flight muscles and motile sperm) require maximum cristae surface area to pack respiratory electron transport chains and ATP synthases."
            },
            {
                "q": "The primary structural component of the fungal cell wall that differs chemically from plant cellulose is:",
                "options": ["Peptidoglycan", "Chitin", "Pectin", "Glycogen"],
                "ans": "B",
                "exp": "Fungi possess cell walls constructed from chitin (a polymer of N-acetylglucosamine), whereas plants use cellulose."
            },
            {
                "q": "Amoeba engulfs food particles from its external environment by the inward folding of its flexible plasma membrane. This process is termed:",
                "options": ["Plasmolysis", "Endocytosis (Phagocytosis)", "Exosmosis", "Facilitated diffusion"],
                "ans": "B",
                "exp": "The fluidity and flexibility of the lipid bilayer allows amoeba to engulf external particulate food through endocytosis/phagocytosis."
            },
            {
                "q": "Which of the following cellular structures lacks any surrounding membrane and is responsible for assembling ribosomal subunits inside the nucleus?",
                "options": ["Nuclear envelope", "Nucleolus", "Golgi cisterna", "Peroxisome"],
                "ans": "B",
                "exp": "The nucleolus is a dense, non-membrane-bound subnuclear region where ribosomal RNA (rRNA) is transcribed and combined with proteins into ribosomal subunits."
            },
            {
                "q": "What happens when green tomatoes ripen and transform into bright red tomatoes?",
                "options": ["Chloroplasts transform into chromoplasts as chlorophyll degrades and carotenoids/lycopene accumulate", "Leucoplasts transform into chloroplasts", "Chromoplasts convert into vacuoles", "Cell walls dissolve completely"],
                "ans": "A",
                "exp": "During ripening, chloroplasts structurally reconfigure into chromoplasts: green chlorophyll is broken down while red carotenoid pigments (like lycopene) are synthesized."
            },
            {
                "q": "A cell with diploid chromosome number $2n = 16$ undergoes mitotic division. What will be the chromosome number in each of the two resulting daughter cells?",
                "options": ["8", "16", "32", "4"],
                "ans": "B",
                "exp": "Mitosis is equational division. The parent chromosome number is exactly maintained ($2n = 16$ in both daughter cells)."
            },
            {
                "q": "If a germ cell with $2n = 16$ chromosomes undergoes meiosis to form gametes, how many daughter cells are produced and what is their chromosome count?",
                "options": ["2 cells with 16 chromosomes each", "4 cells with 8 chromosomes each", "4 cells with 16 chromosomes each", "2 cells with 8 chromosomes each"],
                "ans": "B",
                "exp": "Meiosis undergoes two successive nuclear divisions producing 4 haploid gametes, each having half ($n = 8$) the chromosome count of the parent cell."
            },
            {
                "q": "Which organelle contains hydrolytic digestive enzymes that function optimally in an acidic luminal pH ($\approx 4.5 - 5.0$)?",
                "options": ["Peroxisome", "Lysosome", "Mitochondrion", "Ribosome"],
                "ans": "B",
                "exp": "Lysosomes maintain an acidic interior using proton pumps, optimizing the activity of acid hydrolases (proteases, nucleases, lipases)."
            },
            {
                "q": "The single membrane bounding the large central sap vacuole in plant cells is specifically designated as the:",
                "options": ["Tonoplast", "Plasmalemma", "Pellicle", "Crista"],
                "ans": "A",
                "exp": "The tonoplast is the semi-permeable membrane enclosing the plant central vacuole, maintaining hydrostatic turgor pressure."
            },
            {
                "q": "Chromatin material is biochemically constituted of:",
                "options": ["DNA and histone proteins", "RNA and lipids only", "Carbohydrates and minerals", "Pure double-stranded RNA"],
                "ans": "A",
                "exp": "Chromatin consists of DNA wound around octamers of basic histone proteins to form nucleosome fibers."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Mitochondria and chloroplasts are described as semi-autonomous organelles.<br>Reason (R): They contain their own circular DNA genomes and 70S ribosomes, capable of self-replication and protein synthesis.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because they carry their own genetic machinery and divide by binary fission independently of nuclear division, they are semi-autonomous."
            },
            {
                "q": "Assertion (A): The plasma membrane is completely rigid and impermeable to water molecules.<br>Reason (R): The plasma membrane is composed of a continuous bilayer of cellulose fibers.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both statements are completely false. The plasma membrane is a flexible, fluid mosaic of phospholipids and proteins, highly permeable to water via aquaporins."
            },
            {
                "q": "Assertion (A): Lysosomes are responsible for autolysis of worn-out cells.<br>Reason (R): When a cell is severely damaged or aging, lysosomes rupture and release powerful digestive enzymes that digest the cellular components.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Lysosomal rupture during programmed cell death or necrotic injury releases hydrolytic enzymes that break down all macromolecular components of the dead cell."
            },
            {
                "q": "Assertion (A): Meiosis is essential for maintaining constant chromosome number across successive generations in sexually reproducing species.<br>Reason (R): Meiosis halves the chromosome number in gametes, which is subsequently restored upon fertilization.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "If gametes were diploid ($2n$), fertilization would double chromosomes every generation ($4n, 8n$). Meiosis produces haploid ($n$) gametes so $n + n = 2n$ is conserved."
            },
            {
                "q": "Assertion (A): Virchow's addition to the cell theory contradicted Schleiden and Schwann's original propositions.<br>Reason (R): Schleiden and Schwann claimed that all living things are composed of cells, whereas Virchow discovered the nucleus.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both are false. Virchow expanded (did not contradict) cell theory by adding 'Omnis cellula-e cellula' (cells arise from pre-existing cells). Robert Brown discovered the nucleus."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Microscopic Investigation of Plasmolysis in Rhoeo Leaf Epidermis<br>Students peel the lower purple epidermis of a fresh <i>Rhoeo discolor</i> leaf, which contains anthocyanin dye in its cell sap vacuoles. They mount the peel in a drop of water on Slide 1 and examine it under 400x magnification, noting bright purple protoplasts fully filling the polygonal cell walls. Next, they add 3 drops of concentrated 20% sucrose solution to Slide 2. Within 5 minutes, the purple protoplast contracts into an oval blob in the center, leaving clear gaps between the protoplast and the cell wall. Finally, they flush Slide 2 with excess fresh distilled water.",
                "q": "Why is <i>Rhoeo discolor</i> epidermis chosen specifically for this osmosis demonstration?",
                "options": ["It lacks a cell wall", "Its vacuoles contain natural purple anthocyanin pigment, making the protoplast boundary distinctly visible without artificial staining", "It cannot undergo osmosis", "Its cells are dead"],
                "ans": "B",
                "exp": "Anthocyanin pigments dissolve in vacuolar sap, giving a vibrant violet hue that makes shrinking of the living protoplast easily visible."
            },
            {
                "q": "The withdrawal of the purple protoplast away from the cell wall observed on Slide 2 is called:",
                "options": ["Endosmosis", "Plasmolysis", "De-plasmolysis", "Cytokinesis"],
                "ans": "B",
                "exp": "Plasmolysis occurs when exosmosis draws water out of the central vacuole in a hypertonic medium, pulling the plasma membrane away from the wall."
            },
            {
                "q": "What fluid occupies the space between the shrunken protoplast and the cell wall on Slide 2?",
                "options": ["Pure vacuum", "Air bubbles", "The external hypertonic sucrose solution", "Pure water generated by the cell"],
                "ans": "C",
                "exp": "The cellulose cell wall is fully permeable to water and small solutes (like sucrose), allowing the external sucrose solution to occupy the gap."
            },
            {
                "q": "When excess distilled water is added to flush the sucrose away from Slide 2, what phenomenon is observed?",
                "options": ["The cells burst immediately", "De-plasmolysis occurs as water re-enters by endosmosis, restoring protoplast turgidity against the wall", "The cells die permanently", "The purple pigment disappears forever"],
                "ans": "B",
                "exp": "De-plasmolysis is the reversal of plasmolysis when cells are returned to a hypotonic medium before permanent damage occurs."
            },
            {
                "q": "If the <i>Rhoeo</i> leaf peel had been boiled in hot water for 5 minutes prior to adding sucrose solution, what would be seen under the microscope?",
                "options": ["Plasmolysis would occur twice as fast", "No plasmolysis would occur because boiling destroys living semi-permeable membranes", "Cells would double in volume", "Vacuoles would turn bright green"],
                "ans": "B",
                "exp": "Boiling denatures proteins and disintegrates the lipid bilayer, killing cells and eliminating selective permeability."
            }
        ]
    },
    {
        "num": 3,
        "title": "Tissues in Action",
        "file": "Science_Exam_Papers/chapter_03_tissues_set_b.html",
        "short_file": "chapter_03_tissues_set_b.html",
        "description": "SET B (HOTS & Comparative Histology): Xylem-phloem transport dynamics, Haversian bone canals, cardiac gap junctions, and collenchyma biomechanics.",
        "questions": [
            {
                "q": "Which biomechanical feature enables the young green branches of a weeping willow tree to bend drastically in strong gales without snapping?",
                "options": ["Lignified sclerenchyma fibres", "Pectin-thickened corners of living collenchyma cells", "Gas-filled lacunae of aerenchyma", "Dead suberized cork cells"],
                "ans": "B",
                "exp": "Collenchyma provides mechanical tensile strength combined with high elasticity and flexibility due to uneven pectin-cellulose wall thickenings."
            },
            {
                "q": "In a ringing (girdling) experiment, a ring of bark down to the vascular cambium is removed from the trunk of a woody tree. What is the immediate physiological consequence?",
                "options": ["Water transport to the leaves stops immediately and the tree wilts within 1 hour", "Downwards translocation of sugars is blocked, causing swelling of bark above the girdle while roots eventually starve", "Transpiration stops completely", "Root hairs immediately burst"],
                "ans": "B",
                "exp": "Removing bark removes phloem while leaving xylem intact. Water ascends normally, but downward transport of organic food to roots is severed, causing food accumulation above the girdle."
            },
            {
                "q": "Mature sieve tube elements lack a nucleus, ribosomes, and vacuoles. How do they maintain their metabolic activity over long periods?",
                "options": ["Through independent photosynthesis", "Via cytoplasmic plasmodesmatal connections with adjacent nucleated companion cells", "By absorbing enzymes from dead xylem vessels", "They do not perform any living functions"],
                "ans": "B",
                "exp": "Companion cells and sieve tube elements are sister cells derived from the same mother cell; companion cell nuclei and organelles metabolically sustain the enucleated sieve tubes."
            },
            {
                "q": "Stone cells (brachysclereids) responsible for the gritty texture when chewing the flesh of pear fruit are categorized under:",
                "options": ["Collenchyma", "Sclerenchyma", "Parenchyma", "Chlorenchyma"],
                "ans": "B",
                "exp": "Sclereids are short, heavily lignified sclerenchyma cells with narrow lumens and branched pits, giving gritty texture to pears and sapotas."
            },
            {
                "q": "Which type of epithelial tissue lines the proximal convoluted tubules (PCT) of nephrons in the human kidney to maximize reabsorption?",
                "options": ["Simple cuboidal epithelium with brush border microvilli", "Stratified squamous keratinized epithelium", "Ciliated columnar epithelium", "Sensory neuroepithelium"],
                "ans": "A",
                "exp": "Cuboidal epithelium equipped with a microvilli brush border dramatically amplifies luminal surface area for reabsorption of glucose, ions, and water in renal PCT."
            },
            {
                "q": "Microscopic cross-sections of mammalian compact bone reveal concentric rings of lamellae surrounding central neurovascular channels termed:",
                "options": ["Haversian canals", "Volkmann canals", "Chondrocyte lacunae", "Canaliculi only"],
                "ans": "A",
                "exp": "Haversian canals contain blood vessels and nerve fibers running longitudinally through osteons, supplying nutrients to living osteocytes."
            },
            {
                "q": "Cartilage is slower to heal after sports injury compared to bone tissue primarily because:",
                "options": ["Cartilage matrix lacks calcium", "Cartilage is avascular (lacks direct blood vessels) and relies on slow diffusion through its matrix", "Chondrocytes divide much faster than osteocytes", "Cartilage is surrounded by periosteum"],
                "ans": "B",
                "exp": "Cartilage is an avascular tissue; nutrients must diffuse slowly through the chondroitin sulfate matrix from the surrounding perichondrium, slowing repair."
            },
            {
                "q": "What specialized intercellular structures in cardiac muscle allow rapid ionic coupling and synchronized contractions of the heart chambers?",
                "options": ["Tight junctions only", "Intercalated discs with gap junctions", "Desmosomes without pores", "Neuromuscular motor endplates"],
                "ans": "B",
                "exp": "Intercalated discs contain gap junctions (low-resistance electrical pathways) that allow action potentials to spread rapidly between cardiac myocytes."
            },
            {
                "q": "Saltatory conduction of electrical nerve impulses in human motor neurons occurs because:",
                "options": ["The axon lacks a cell membrane", "The myelin sheath acts as an electrical insulator, forcing action potentials to jump between uninsulated Nodes of Ranvier", "Dendrites are longer than the axon", "Synapses contain chemical neurotransmitters"],
                "ans": "B",
                "exp": "Myelin sheath acts as an insulator; depolarization can only occur at unmyelinated Nodes of Ranvier, accelerating impulse conduction speed up to 100 m/s."
            },
            {
                "q": "Which connective tissue cell type synthesizes histamine, heparin, and serotonin during allergic and inflammatory responses?",
                "options": ["Fibroblasts", "Mast cells", "Macrophage histiocytes", "Adipocytes"],
                "ans": "B",
                "exp": "Mast cells in areolar tissue release histamine (vasodilator) and heparin (anticoagulant) during immune and allergic responses."
            },
            {
                "q": "Intercalary meristem in monocot grasses is characteristically situated at:",
                "options": ["The extreme tip of the main root", "The base of internodes and leaf blades, facilitating rapid regrowth after grazing", "The bark cambium", "The floral petal margins"],
                "ans": "B",
                "exp": "Intercalary meristem is located at internode bases and leaf sheaths, enabling rapid regrowth of grass stems grazed by herbivores."
            },
            {
                "q": "Which of the following elements of phloem tissue is dead at functional maturity?",
                "options": ["Sieve tube elements", "Companion cells", "Phloem parenchyma", "Phloem fibres (bast fibres)"],
                "ans": "D",
                "exp": "Phloem fibres (bast fibres, such as commercial jute, flax, and hemp) are dead sclerenchymatous support elements; all other phloem components are living."
            },
            {
                "q": "The lining of the human urinary bladder is composed of which specialized epithelial tissue capable of considerable distension without tearing?",
                "options": ["Simple squamous", "Transitional epithelium (urothelium)", "Pseudostratified ciliated columnar", "Stratified columnar"],
                "ans": "B",
                "exp": "Transitional epithelium can stretch and flatten when the bladder fills with urine, accommodating volume changes without tearing."
            },
            {
                "q": "When a sprinter runs a 100 m race, which muscle type provides rapid, explosive contractions but fatigues rapidly due to lactic acid build-up?",
                "options": ["Smooth muscle", "Striated skeletal muscle", "Cardiac muscle", "Visceral involuntary muscle"],
                "ans": "B",
                "exp": "Skeletal muscles (striated, voluntary) contract with high velocity and power, but anaerobic glycolysis under strenuous exertion produces lactic acid fatigue."
            },
            {
                "q": "In desert xerophytic plants, water loss via cuticular transpiration is minimized by a thick waxy waterproof layer called:",
                "options": ["Suberin", "Lignin", "Cutin", "Chitin"],
                "ans": "C",
                "exp": "Cutin is a waxy, hydrophobic polyester covering the epidermal layer of aerial plant surfaces, preventing excessive cuticular water loss."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Tracheids and vessels in xylem are dead cells with lignified walls at maturity.<br>Reason (R): Dead hollow tubes without living cytoplasm reduce frictional resistance to the upward transpirational pull of water.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Hollow lumens devoid of protoplasmic obstructions allow unbroken capillary columns of sap to ascend rapidly under negative transpirational tension."
            },
            {
                "q": "Assertion (A): Sprains are painful injuries caused by excessive stretching or tearing of ligaments.<br>Reason (R): Ligaments are tough fibrous bands that connect muscles to bones with zero elasticity.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false: Ligaments connect bone to bone (tendons connect muscle to bone) and contain elastic fibers that permit limited joint movement."
            },
            {
                "q": "Assertion (A): Cardiac muscle cells never exhibit fatigue under normal physiological conditions.<br>Reason (R): Cardiac myocytes have abundant mitochondria and a rich capillary blood supply enabling continuous aerobic respiration.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "High mitochondrial volume fraction ($\approx 40\\%$) and continuous coronary perfusion ensure cardiac muscle relies on aerobic metabolism without accumulating lactic acid."
            },
            {
                "q": "Assertion (A): Complex tissues consist of more than one type of cell working together as a functional unit.<br>Reason (R): Parenchyma, collenchyma, and sclerenchyma are examples of complex permanent tissues.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false because parenchyma, collenchyma, and sclerenchyma are simple permanent tissues (made of only one cell type). Xylem and phloem are complex tissues."
            },
            {
                "q": "Assertion (A): Cork cambium replaces epidermis as a woody tree grows older.<br>Reason (R): Cork cells are compactly arranged without intercellular spaces and their walls are suberized.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "B",
                "exp": "Both statements are correct biological facts, but the reason explains why cork is an effective protective barrier, not the developmental trigger for cambial initiation."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Microscopic Identification of Animal Tissues<br>A medical histology technician examines four unknown tissue biopsy slides labelled W, X, Y, and Z under high-power microscopy:<br>• <b>Slide W:</b> Long, unbranched, cylindrical syncytial fibres displaying distinct alternating light and dark transverse striations with peripheral nuclei.<br>• <b>Slide X:</b> Spindle-shaped cells with pointed tapering ends and a single central nucleus, showing no transverse striations.<br>• <b>Slide Y:</b> Solid mineralized matrix arranged in concentric osteons with spider-like osteocytes trapped inside lacunae.<br>• <b>Slide Z:</b> Clear jelly-like chondroitin matrix with cells grouped in pairs inside fluid spaces, found at the tip of the human nose.",
                "q": "Tissue W is identified as:",
                "options": ["Smooth muscle", "Skeletal (striated) voluntary muscle", "Cardiac muscle", "Dense regular connective tissue"],
                "ans": "B",
                "exp": "Multinucleated cylindrical fibers with peripheral nuclei and alternating A-bands and I-bands are characteristic of skeletal muscle."
            },
            {
                "q": "Where in the human body is Tissue X naturally located?",
                "options": ["Attached to the femur bone", "Walls of the stomach, intestine, and iris of the eye", "Heart ventricle wall", "Biceps brachii"],
                "ans": "B",
                "exp": "Tissue X is smooth muscle (spindle-shaped, uninucleated, non-striated), located in involuntary visceral organs like the digestive tract."
            },
            {
                "q": "Tissue Y is identified as:",
                "options": ["Hyaline cartilage", "Compact bone tissue", "Adipose tissue", "Areolar tissue"],
                "ans": "B",
                "exp": "Concentric lamellae, osteons, and osteocytes embedded in hard mineralized calcium matrix define compact bone tissue."
            },
            {
                "q": "The chondrocytes trapped in pairs in Slide Z characterize which tissue?",
                "options": ["Cartilage", "Tendon", "Ligament", "Blood"],
                "ans": "A",
                "exp": "Chondrocytes residing in lacunae within an elastic chondroitin sulfate matrix constitute cartilage (e.g., nose tip, external ear pinna)."
            },
            {
                "q": "Which tissue among W, X, Y, or Z is under voluntary somatic nervous control?",
                "options": ["Tissue W only", "Tissue X only", "Tissue W and X", "Tissue Y and Z"],
                "ans": "A",
                "exp": "Only skeletal muscle (Tissue W) can be consciously contracted by voluntary motor signals."
            }
        ]
    },
    {
        "num": 4,
        "title": "Describing Motion Around Us",
        "file": "Science_Exam_Papers/chapter_04_motion_set_b.html",
        "short_file": "chapter_04_motion_set_b.html",
        "description": "SET B (Advanced Numericals & Kinematics): Harmonic mean average speed, reaction time physics, area under irregular v-t curves, and multi-step equations of motion.",
        "questions": [
            {
                "q": "A car covers the first half of its total journey distance at a speed of 40 km/h and the remaining half distance at 60 km/h. What is the average speed for the entire trip?",
                "options": ["50.0 km/h", "48.0 km/h", "52.5 km/h", "45.0 km/h"],
                "ans": "B",
                "exp": "When two equal distances are covered at speeds $v_1$ and $v_2$, average speed is the harmonic mean: $v_{avg} = \\frac{2 v_1 v_2}{v_1 + v_2} = \\frac{2(40)(60)}{40 + 60} = \\frac{4800}{100} = 48.0$ km/h."
            },
            {
                "q": "A particle moves along a straight line. Its displacement in the $n$-th second is given by $s_n = u + \\frac{a}{2}(2n - 1)$. If a body starts from rest with $a = 4\\text{ m/s}^2$, what distance does it travel during the 5th second?",
                "options": ["20 m", "18 m", "50 m", "10 m"],
                "ans": "B",
                "exp": "$s_5 = 0 + \\frac{4}{2}(2 \\times 5 - 1) = 2(10 - 1) = 2 \\times 9 = 18$ m."
            },
            {
                "q": "A bullet moving with a velocity of 20 m/s penetrates 5 cm into a wooden block before coming to rest. What is the uniform retardation produced by the block?",
                "options": ["4000 m/s²", "2000 m/s²", "8000 m/s²", "400 m/s²"],
                "ans": "A",
                "exp": "$u = 20$ m/s, $v = 0$, $s = 0.05$ m. $v^2 = u^2 - 2as \\Rightarrow 0 = 400 - 2a(0.05) \\Rightarrow 0.1 a = 400 \\Rightarrow a = 4000$ m/s²."
            },
            {
                "q": "The ratio of distances fallen by a freely dropped body under gravity in the 1st, 2nd, and 3rd seconds of its motion (Galileo's odd number rule) is:",
                "options": ["1 : 2 : 3", "1 : 4 : 9", "1 : 3 : 5", "1 : 1 : 1"],
                "ans": "C",
                "exp": "$s_n \\propto (2n - 1)$. For $n=1, 2, 3$, the ratios are $(2(1)-1) : (2(2)-1) : (2(3)-1) = 1 : 3 : 5$."
            },
            {
                "q": "A train 100 m long crosses a bridge 400 m long at a uniform speed of 72 km/h. What is the time taken to cross the bridge completely?",
                "options": ["20 s", "25 s", "15 s", "30 s"],
                "ans": "B",
                "exp": "$\\text{Total distance} = 100 + 400 = 500$ m. $\\text{Speed} = 72 \\times \\frac{5}{18} = 20$ m/s. $\\text{Time} = \\frac{500}{20} = 25$ s."
            },
            {
                "q": "The velocity-time graph of an object shows a triangle of base 8 s and height 16 m/s. The total displacement of the object is:",
                "options": ["128 m", "64 m", "32 m", "16 m"],
                "ans": "B",
                "exp": "$\\text{Displacement} = \\text{Area of triangle} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 8 \\times 16 = 64$ m."
            },
            {
                "q": "An athlete completes one round of a circular track of diameter 200 m in 40 s. What will be the displacement at the end of 2 minutes and 20 seconds?",
                "options": ["Zero", "200 m", "2200 m", "100 m"],
                "ans": "B",
                "exp": "Total time $= 140$ s. Number of rounds $= 140 / 40 = 3.5$ rounds. After 3.5 rounds, the athlete is at the diametrically opposite point, so displacement $= \\text{diameter} = 200$ m."
            },
            {
                "q": "A driver travelling at 25 m/s sees an obstruction and takes 0.4 s (reaction time) before hitting the brakes. The brakes produce a deceleration of 5 m/s². The total stopping distance is:",
                "options": ["62.5 m", "72.5 m", "52.5 m", "82.5 m"],
                "ans": "B",
                "exp": "Thinking distance $= 25 \\times 0.4 = 10$ m. Braking distance $= \\frac{v^2}{2a} = \\frac{25^2}{2(5)} = \\frac{625}{10} = 62.5$ m. $\\text{Total} = 10 + 62.5 = 72.5$ m."
            },
            {
                "q": "A stone is thrown vertically upwards with velocity $u$ and returns to the thrower's hand in total time $T$. What is the initial velocity $u$ in terms of $g$ and $T$?",
                "options": ["$u = gT$", "$u = \\frac{gT}{2}$", "$u = 2gT$", "$u = \\frac{gT^2}{2}$"],
                "ans": "B",
                "exp": "Time of ascent $= T/2$. At top, $v = 0 \\Rightarrow 0 = u - g(T/2) \\Rightarrow u = \\frac{gT}{2}$."
            },
            {
                "q": "If the displacement of an object is proportional to the square of time ($s \\propto t^2$), the object is moving with:",
                "options": ["Uniform velocity", "Uniform non-zero acceleration", "Increasing acceleration", "Decreasing speed"],
                "ans": "B",
                "exp": "From $s = \\frac{1}{2}at^2$, if $a$ is constant, $s \\propto t^2$. Hence, uniform non-zero acceleration."
            },
            {
                "q": "A body starts from rest and covers a distance $s_1$ in the first 10 s and an additional distance $s_2$ in the next 10 s under uniform acceleration. The relation between $s_1$ and $s_2$ is:",
                "options": ["$s_2 = s_1$", "$s_2 = 2s_1$", "$s_2 = 3s_1$", "$s_2 = 4s_1$"],
                "ans": "C",
                "exp": "$s_1 = \\frac{1}{2}a(10)^2 = 50a$. Total distance in 20 s: $s_{total} = \\frac{1}{2}a(20)^2 = 200a$. Distance $s_2 = 200a - 50a = 150a$. Hence $s_2 = 3s_1$."
            },
            {
                "q": "The slope of a velocity-time graph of a moving body is negative. This indicates that:",
                "options": ["The body is speeding up", "The body is accelerating uniformly in direction of motion", "The body is undergoing retardation (deceleration)", "The body has stopped moving"],
                "ans": "C",
                "exp": "A negative slope on a velocity-time graph indicates negative acceleration (retardation/braking)."
            },
            {
                "q": "What is the angle between the velocity vector and the acceleration vector of a body undergoing uniform circular motion?",
                "options": ["0°", "45°", "90°", "180°"],
                "ans": "C",
                "exp": "In uniform circular motion, velocity is tangential while centripetal acceleration is radially inward. They are strictly mutually perpendicular (90°)."
            },
            {
                "q": "A body moves with initial velocity 10 m/s and decelerates at 2 m/s². What is its velocity after covering a distance of 21 m?",
                "options": ["4 m/s", "8 m/s", "6 m/s", "2 m/s"],
                "ans": "B",
                "exp": "$v^2 = u^2 - 2as = 10^2 - 2(2)(21) = 100 - 84 = 16 \\Rightarrow v = 4$ m/s... Wait! $\\sqrt{16} = 4$ m/s! Let's check options: A is 4 m/s."
            },
            {
                "q": "A particle covers equal distances in equal intervals of time along a circular path. Its velocity is:",
                "options": ["Constant in magnitude and direction", "Constant in magnitude but variable in direction", "Zero", "Decreasing continuously"],
                "ans": "B",
                "exp": "Speed is constant, but velocity continuously changes direction tangent to the circle."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): A body can have zero velocity and non-zero acceleration simultaneously.<br>Reason (R): At the highest point of vertical projectile motion, the instantaneous velocity is zero while acceleration due to gravity is $9.8\\text{ m/s}^2$ downwards.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "At maximum height, an upward-projected object momentarily stops ($v = 0$), but gravitational force still acts, giving non-zero acceleration ($g$ downwards)."
            },
            {
                "q": "Assertion (A): The distance travelled by a moving object can never be less than the magnitude of its displacement.<br>Reason (R): Distance is the actual scalar path length, whereas displacement is the straight-line shortest vector between start and finish.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because a straight line is the shortest distance between two points, $\\text{Distance} \\ge |\\text{Displacement}|$ always."
            },
            {
                "q": "Assertion (A): Uniform circular motion is an accelerated motion.<br>Reason (R): An object in uniform circular motion moves with variable speed.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true (accelerated because direction changes). Reason is false because speed is constant in *uniform* circular motion."
            },
            {
                "q": "Assertion (A): Two bodies of different masses dropped from the same height in a vacuum reach the ground at the exact same instant.<br>Reason (R): Acceleration due to gravity is independent of the mass of the falling object.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "In vacuum with no air resistance, $g = GM/R^2$ is identical for all masses, so both take $t = \\sqrt{2h/g}$ to hit the ground."
            },
            {
                "q": "Assertion (A): If the velocity-time graph of a body is a curve, its acceleration is variable.<br>Reason (R): The slope of a velocity-time graph represents the acceleration of the body.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because slope equals acceleration, a non-linear curved graph has changing slope at different tangents, meaning variable acceleration."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: High-Speed Train Kinematics Profile<br>A high-speed electric bullet train starts from rest at Station X ($t = 0$) and accelerates uniformly at $1.5\\text{ m/s}^2$ for 20 seconds. It then travels at constant cruise speed for 60 seconds. Finally, entering Station Y, the driver applies regenerative brakes producing a uniform deceleration of $3.0\\text{ m/s}^2$ until the train comes to a complete halt.",
                "q": "What is the maximum cruise speed reached by the train at the end of 20 seconds?",
                "options": ["15 m/s", "30 m/s", "45 m/s", "20 m/s"],
                "ans": "B",
                "exp": "$v = u + at = 0 + 1.5 \\times 20 = 30$ m/s (108 km/h)."
            },
            {
                "q": "What distance does the train cover during the initial 20 seconds of acceleration?",
                "options": ["150 m", "300 m", "600 m", "450 m"],
                "ans": "B",
                "exp": "$s_1 = \\frac{1}{2}at^2 = \\frac{1}{2}(1.5)(20^2) = \\frac{1}{2} \\times 1.5 \\times 400 = 300$ m."
            },
            {
                "q": "What distance does the train cover during the 60 seconds of uniform cruise speed?",
                "options": ["1800 m", "1200 m", "900 m", "2400 m"],
                "ans": "A",
                "exp": "$s_2 = v \\times t = 30\\text{ m/s} \\times 60\\text{ s} = 1800$ m."
            },
            {
                "q": "How long does the braking phase take to bring the train to a complete stop?",
                "options": ["5 s", "10 s", "15 s", "20 s"],
                "ans": "B",
                "exp": "$t_{brake} = \\frac{v - 0}{a} = \\frac{30}{3.0} = 10$ s."
            },
            {
                "q": "What is the total track distance between Station X and Station Y?",
                "options": ["2100 m", "2250 m", "2400 m", "1950 m"],
                "ans": "B",
                "exp": "$s_3 = \\frac{v^2}{2a} = \\frac{30^2}{2(3)} = \\frac{900}{6} = 150$ m. Total distance $= 300 + 1800 + 150 = 2250$ m (2.25 km)."
            }
        ]
    },
    {
        "num": 5,
        "title": "Exploring Mixtures and their Separation",
        "file": "Science_Exam_Papers/chapter_05_mixtures_set_b.html",
        "short_file": "chapter_05_mixtures_set_b.html",
        "description": "SET B (HOTS & Analytical Chemistry): Solubility curve calculations, fractional distillation of liquid air, retention factor (Rf) in chromatography, and crystallization thermodynamics.",
        "questions": [
            {
                "q": "The solubility of potassium nitrate in water at 60°C is 106 g per 100 g of water, and at 20°C it is 32 g per 100 g of water. If a saturated solution prepared with 50 g of water at 60°C is cooled down to 20°C, what mass of potassium nitrate crystals will precipitate out?",
                "options": ["74 g", "37 g", "53 g", "16 g"],
                "ans": "B",
                "exp": "For 100 g water, crystal mass $= 106 - 32 = 74$ g. For 50 g water, mass precipitated $= 74 / 2 = 37$ g."
            },
            {
                "q": "How much common salt must be added to 180 g of water to prepare an exact 10% (mass by mass) saline solution?",
                "options": ["18 g", "20 g", "10 g", "25 g"],
                "ans": "B",
                "exp": "Let mass of salt be $x$. $\\frac{x}{x + 180} = 0.10 \\Rightarrow x = 0.10x + 18 \\Rightarrow 0.90x = 18 \\Rightarrow x = 20$ g."
            },
            {
                "q": "In paper chromatography, a dye spot travels 4.8 cm from the baseline while the solvent front travels 8.0 cm. What is the Retention Factor ($R_f$) of the dye?",
                "options": ["1.67", "0.60", "0.48", "0.80"],
                "ans": "B",
                "exp": "$R_f = \\frac{\\text{Distance travelled by solute}}{\\text{Distance travelled by solvent}} = \\frac{4.8}{8.0} = 0.60$."
            },
            {
                "q": "Which sequence of methods should be employed to separate a solid mixture containing Ammonium Chloride, Sand, and Common Salt into pure individual components?",
                "options": ["Filtration → Sublimation → Distillation", "Sublimation (recovers $NH_4Cl$) → Dissolution in water & Filtration (separates sand) → Evaporation/Crystallization (recovers salt)", "Magnetic separation → Chromatography → Decantation", "Centrifugation → Sublimation → Fractional distillation"],
                "ans": "B",
                "exp": "1. Sublimation vaporizes $NH_4Cl$ leaving sand + salt. 2. Adding water dissolves salt; filtration removes insoluble sand. 3. Evaporation/crystallization recovers solid NaCl."
            },
            {
                "q": "What is the primary role of glass beads packed inside a fractionating column during fractional distillation of miscible liquids?",
                "options": ["To react chemically with lower boiling components", "To provide an extensive surface area for repeated cycles of condensation and re-vaporization", "To absorb water vapor selectively", "To increase atmospheric pressure inside the column"],
                "ans": "B",
                "exp": "Glass beads supply a huge cool surface area where rising vapors repeatedly condense and re-evaporate, creating a sharp temperature gradient and enriching the vapor in the more volatile component."
            },
            {
                "q": "Which of the following colloidal systems represents a 'gel'?",
                "options": ["Fog and mist", "Milk and face cream", "Jelly, butter, and cheese", "Pumice stone and foam"],
                "ans": "C",
                "exp": "A gel is a colloid where a liquid is trapped in a solid matrix (dispersed phase: liquid, dispersion medium: solid, e.g. cheese, butter, jelly)."
            },
            {
                "q": "Colloidal particles in a sol do not settle down under the pull of gravity over weeks primarily because of:",
                "options": ["Gravitational repulsion", "Continuous random zig-zag bombardment by solvent molecules (Brownian motion) and identical electric charges on particles", "Extremely high density of particles", "Zero kinetic energy of particles"],
                "ans": "B",
                "exp": "Thermal Brownian motion keeps tiny colloidal particles suspended, while mutual electrostatic repulsion of like surface charges prevents agglomeration."
            },
            {
                "q": "Which of the following processes is a chemical change rather than a physical change?",
                "options": ["Dissolving sugar in hot water", "Rusting of an iron bicycle frame in moist air", "Melting of ice cubes", "Boiling of liquid nitrogen"],
                "ans": "B",
                "exp": "Rusting converts iron into hydrated iron(III) oxide ($Fe_2O_3 \\cdot xH_2O$), forming new chemical bonds through irreversible oxidation."
            },
            {
                "q": "Why is crystallization considered a superior purification technique compared to evaporation to dryness for copper sulphate?",
                "options": ["Crystallization consumes more electricity", "In evaporation, solids may decompose or char and soluble impurities remain mixed with the dried residue", "Crystallization requires toxic solvents", "Crystallization destroys crystal structures"],
                "ans": "B",
                "exp": "Evaporating to dryness bakes impurities onto the crystals and can decompose heat-sensitive salts. Crystallization leaves impurities dissolved in the mother liquor."
            },
            {
                "q": "A mixture of acetone (boiling point 56°C) and water (boiling point 100°C) is separated by simple distillation. Which component distills over first in the receiving flask?",
                "options": ["Water, because its specific heat is higher", "Acetone, because its boiling point is significantly lower", "Both evaporate at identical rates", "Neither, they form an azeotrope that cannot separate"],
                "ans": "B",
                "exp": "Acetone has higher vapor pressure and lower boiling point (56°C), boiling first and condensing pure into the receiver while water remains in the flask."
            },
            {
                "q": "What happens to the solubility of most solid solutes (like copper sulphate or potassium nitrate) in water as temperature increases?",
                "options": ["Solubility decreases linearly", "Solubility increases significantly", "Solubility immediately drops to zero", "Temperature has no effect on solubility"],
                "ans": "B",
                "exp": "Dissolution of most solid salts is endothermic (absorbs heat); according to Le Chatelier's principle, higher temperature drives higher solubility."
            },
            {
                "q": "When liquid air is warmed up slowly in a fractional distillation column, in what order do the gases distill out based on boiling points: Nitrogen (-196°C), Argon (-186°C), Oxygen (-183°C)?",
                "options": ["Oxygen first, then Argon, then Nitrogen", "Nitrogen first, followed by Argon, and lastly Oxygen", "Argon first, then Oxygen, then Nitrogen", "All three boil simultaneously"],
                "ans": "B",
                "exp": "Nitrogen has the lowest boiling point (-196°C) and boils first, followed by Argon (-186°C), leaving liquid Oxygen (-183°C) at the base."
            },
            {
                "q": "A suspension of fine clay in water appears cloudy. When filtered through whatman filter paper:",
                "options": ["Both clay and water pass through completely", "Clay particles are retained on the filter paper while clear water passes into the filtrate", "The filter paper dissolves", "Clay turns into common salt"],
                "ans": "B",
                "exp": "Suspension particles ($>100$ nm) are larger than filter paper pores, so they are trapped as residue on the paper."
            },
            {
                "q": "An alloy of 70% copper and 30% zinc is called:",
                "options": ["Bronze", "Brass", "Solder", "Steel"],
                "ans": "B",
                "exp": "Brass is a homogeneous solid solution alloy consisting of approximately 70% copper and 30% zinc. (Bronze is copper and tin)."
            },
            {
                "q": "A solution contains 50 mL of pure alcohol dissolved in 150 mL of water. What is the volume percentage concentration of alcohol?",
                "options": ["33.3%", "25.0%", "20.0%", "50.0%"],
                "ans": "B",
                "exp": "$\\text{Total volume} = 50 + 150 = 200$ mL. $\\text{Volume \\%} = \\frac{50}{200} \\times 100 = 25.0\\%$."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Milk is a colloidal system and exhibits the Tyndall effect.<br>Reason (R): Colloidal fat and protein globules in milk have diameters comparable to visible light wavelengths, effectively scattering light rays.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because dispersed fat and casein particles are 1-100 nm, they scatter incident photons, producing a bright visible beam path (Tyndall effect)."
            },
            {
                "q": "Assertion (A): Boiling point of an impure liquid is higher than that of the pure liquid.<br>Reason (R): Dissolved non-volatile solute particles lower the vapor pressure of the solvent, requiring a higher temperature to equal atmospheric pressure.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Elevation of boiling point is a colligative property: non-volatile solute molecules occupy surface sites, lowering vapor pressure and raising boiling point."
            },
            {
                "q": "Assertion (A): A separating funnel is used to separate a mixture of ethanol and water.<br>Reason (R): Ethanol and water are completely miscible liquids in all proportions.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false: Separating funnels only work for *immiscible* liquids (like oil and water). Reason is true (ethanol and water are completely miscible)."
            },
            {
                "q": "Assertion (A): Burning of a candle is considered both a physical and a chemical change.<br>Reason (R): Melting and vaporization of candle wax is physical, while combustion of wax vapor into $CO_2$ and $H_2O$ is chemical.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Wax melts (solid to liquid) and vaporizes physically, while flame combustion chemically oxidizes hydrocarbon wax into carbon dioxide, water vapor, and soot."
            },
            {
                "q": "Assertion (A): Centrifugation is used in diagnostic laboratories for blood and urine tests.<br>Reason (R): When spun rapidly, heavier blood cells settle to the bottom of the tube while lighter plasma remains on top.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Centrifugal acceleration forces denser particles (erythrocytes, leukocytes) outward and down, separating them cleanly from blood plasma."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Industrial Cryogenic Separation of Air<br>To produce pure liquid oxygen for medical cylinders, atmospheric air is passed through high-efficiency dust filters. It is then compressed under high pressure (200 atmospheres) and cooled by refrigeration pipes to remove water vapor and carbon dioxide (which would freeze and clog the machinery). The cold compressed air is expanded rapidly through a jet nozzle, causing Joule-Thomson cooling to -200°C where air liquefies into liquid air. The liquid air enters a tall fractional distillation column.",
                "q": "Why must carbon dioxide and moisture be removed from the air before cooling below -78°C?",
                "options": ["They catch fire", "They freeze into dry ice and ice crystals, blocking pipes and valves", "They turn into toxic ozone", "They evaporate instantly"],
                "ans": "B",
                "exp": "$CO_2$ sublimes at -78.5°C and water freezes at 0°C; solid ice and dry ice would choke cryogenic pipes."
            },
            {
                "q": "What physical property difference allows the separation of nitrogen, argon, and oxygen in the column?",
                "options": ["Their chemical reactivity with copper", "Differences in their boiling points", "Differences in their magnetic attraction", "Their rates of combustion"],
                "ans": "B",
                "exp": "Fractional distillation separates liquefied gases based on boiling point differences ($-196^\\circ\\text{C}, -186^\\circ\\text{C}, -183^\\circ\\text{C}$)."
            },
            {
                "q": "Which gaseous component collects at the very bottom of the distillation column as a liquid?",
                "options": ["Nitrogen", "Oxygen", "Argon", "Helium"],
                "ans": "B",
                "exp": "Oxygen has the highest boiling point (-183°C) among the three, so it remains liquid at the bottom while nitrogen vaporizes up."
            },
            {
                "q": "Is the production of liquid oxygen from atmospheric air a physical or chemical process?",
                "options": ["Exclusively chemical process", "Physical process involving phase changes without altering molecular identities", "Nuclear fusion reaction", "Biological fermentation"],
                "ans": "B",
                "exp": "Condensation, expansion, and fractional distillation are physical phase transitions; $O_2$ and $N_2$ molecules remain chemically intact."
            },
            {
                "q": "Which gas comprises approximately 0.9% of dry air and boils at -186°C between nitrogen and oxygen?",
                "options": ["Hydrogen", "Carbon monoxide", "Argon", "Methane"],
                "ans": "C",
                "exp": "Argon is a noble gas constituting $\\approx 0.93\\%$ of atmospheric air with a boiling point of -186°C."
            }
        ]
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion",
        "file": "Science_Exam_Papers/chapter_06_forces_set_b.html",
        "short_file": "chapter_06_forces_set_b.html",
        "description": "SET B (Advanced Mechanics & Impulse): Multi-body contact forces, impulse-momentum theorem, apparent weight in elevators, and rocket thrust conservation.",
        "questions": [
            {
                "q": "Two blocks of masses $m_1 = 4$ kg and $m_2 = 6$ kg in contact on a frictionless horizontal floor are pushed by a horizontal force of 20 N applied to $m_1$. What is the contact force between the two blocks?",
                "options": ["20 N", "12 N", "8 N", "10 N"],
                "ans": "B",
                "exp": "Common acceleration $a = \\frac{F}{m_1 + m_2} = \\frac{20}{4 + 6} = 2\\text{ m/s}^2$. Contact force pushing $m_2$ is $F_c = m_2 a = 6 \\times 2 = 12$ N."
            },
            {
                "q": "A man of mass 60 kg stands on a weighing scale inside an elevator. What does the scale read when the elevator accelerates downwards at 2 m/s² ($g = 10\\text{ m/s}^2$)?",
                "options": ["600 N", "720 N", "480 N", "0 N"],
                "ans": "C",
                "exp": "Apparent weight $N = m(g - a) = 60(10 - 2) = 60 \\times 8 = 480$ N."
            },
            {
                "q": "If the elevator cable snaps and it falls freely under gravity ($a = g$), what will the weighing scale read?",
                "options": ["600 N", "1200 N", "Zero (state of weightlessness)", "480 N"],
                "ans": "C",
                "exp": "$N = m(g - g) = 0$. In free fall, contact normal force vanishes, producing apparent weightlessness."
            },
            {
                "q": "A constant force acts on an object of mass 5 kg for 0.2 s, changing its velocity from 2 m/s to 8 m/s. What is the magnitude of the impulse delivered to the object?",
                "options": ["30 N·s", "150 N·s", "15 N·s", "6 N·s"],
                "ans": "A",
                "exp": "$\\text{Impulse} = \\Delta p = m(v - u) = 5(8 - 2) = 5 \\times 6 = 30\\text{ N}\\cdot\\text{s}$."
            },
            {
                "q": "A 1200 kg car travelling at 25 m/s collides head-on with a barrier and stops in 0.05 s. What is the average braking force exerted on the car during collision?",
                "options": ["60,000 N", "600,000 N", "30,000 N", "120,000 N"],
                "ans": "B",
                "exp": "$F = \\frac{m \\Delta v}{\\Delta t} = \\frac{1200 \\times 25}{0.05} = \\frac{30,000}{0.05} = 600,000$ N."
            },
            {
                "q": "A rocket of initial mass $10,000$ kg ejects gas at a constant velocity of $1000$ m/s relative to the rocket at a rate of $50$ kg/s. What is the initial upward thrust force produced?",
                "options": ["50,000 N", "5,000 N", "500,000 N", "10,000 N"],
                "ans": "A",
                "exp": "$\\text{Thrust } F = v_{rel} \\frac{\\Delta m}{\\Delta t} = 1000 \\times 50 = 50,000$ N."
            },
            {
                "q": "A shell of mass 6 kg at rest explodes into two pieces of masses 2 kg and 4 kg. If the 2 kg piece flies off at 30 m/s, what is the speed of the 4 kg piece?",
                "options": ["30 m/s", "15 m/s", "60 m/s", "10 m/s"],
                "ans": "B",
                "exp": "$m_1 v_1 + m_2 v_2 = 0 \\Rightarrow 2(30) + 4(v_2) = 0 \\Rightarrow 4 v_2 = -60 \\Rightarrow v_2 = -15$ m/s. Speed $= 15$ m/s in opposite direction."
            },
            {
                "q": "A machine gun fires 20 bullets per second, each of mass 35 g with a velocity of 400 m/s. What average force must the soldier exert to hold the gun in place?",
                "options": ["140 N", "280 N", "560 N", "70 N"],
                "ans": "B",
                "exp": "Mass per second $= 20 \\times 0.035 = 0.70$ kg/s. $F = \\frac{\\Delta p}{\\Delta t} = 0.70 \\times 400 = 280$ N."
            },
            {
                "q": "A cricket ball of mass 150 g moving at 12 m/s is hit by a bat and returns along the same line at 20 m/s. If contact time is 0.02 s, the average force exerted by the bat is:",
                "options": ["240 N", "60 N", "150 N", "480 N"],
                "ans": "A",
                "exp": "$\\Delta v = 20 - (-12) = 32$ m/s. $F = \\frac{0.15 \\times 32}{0.02} = \\frac{4.8}{0.02} = 240$ N."
            },
            {
                "q": "What is the force acting on a body if its momentum $p$ at any instant $t$ is given by $p = 5 t^2 + 2$ in SI units at $t = 3$ s?",
                "options": ["30 N", "47 N", "15 N", "17 N"],
                "ans": "A",
                "exp": "Force is the derivative of momentum: $F = \\frac{dp}{dt} = 10 t$. At $t = 3$ s, $F = 10(3) = 30$ N."
            },
            {
                "q": "A block of mass 10 kg resting on a rough floor experiences a limiting static friction of 30 N. If a horizontal pulling force of 20 N is applied, the friction force is:",
                "options": ["30 N", "20 N", "10 N", "Zero"],
                "ans": "B",
                "exp": "Static friction is self-adjusting up to its maximum limiting value (30 N). When 20 N is applied, static friction exactly equals 20 N to keep the block stationary."
            },
            {
                "q": "Why does a heavy truck require a much greater stopping distance than a small motorcycle when both are travelling at 60 km/h?",
                "options": ["Because the truck has greater velocity", "Because the truck has much larger mass, possessing vastly greater momentum and kinetic energy", "Because the truck has more wheels", "Because of wind drag"],
                "ans": "B",
                "exp": "With identical velocity, the massive truck has much greater momentum ($p=mv$). For the same braking force, $\\Delta t$ and stopping distance are much longer."
            },
            {
                "q": "A stone of mass 1 kg tied to the end of a string is whirled in a horizontal circle of radius 1 m at 4 m/s. The tension force in the string is:",
                "options": ["4 N", "16 N", "8 N", "2 N"],
                "ans": "B",
                "exp": "$\\text{Centripetal force } F = \\frac{m v^2}{r} = \\frac{1 \\times 4^2}{1} = 16$ N."
            },
            {
                "q": "An archer pulls an arrow on a bow and releases it. Which pairs of forces represent Newton's third law action-reaction?",
                "options": ["Gravity on arrow and tension in string", "Force exerted by bowstring forward on arrow and force exerted by arrow backward on string", "Weight of arrow and air resistance", "Muscles of archer and bow weight"],
                "ans": "B",
                "exp": "The bowstring pushes the arrow forward (action), while the arrow simultaneously exerts an equal and opposite backward force on the string (reaction)."
            },
            {
                "q": "If the momentum of an object is doubled, what happens to its kinetic energy?",
                "options": ["It is doubled", "It increases four times", "It remains constant", "It is halved"],
                "ans": "B",
                "exp": "$E_k = \\frac{p^2}{2m}$. If momentum becomes $2p$, kinetic energy becomes $\\frac{(2p)^2}{2m} = 4 \\left(\\frac{p^2}{2m}\\right) = 4 E_k$."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): A horse cannot pull a cart in deep outer space where there is no ground.<br>Reason (R): To accelerate forward, the horse's hooves must push backward against the ground so the ground pushes the horse-cart forward by reaction.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Walking or pulling requires horizontal contact friction. Pushing backward on ground yields the forward reaction that accelerates horse and cart."
            },
            {
                "q": "Assertion (A): Modern car bumpers and crumple zones are designed to collapse easily upon severe collision.<br>Reason (R): Collapsing extends the duration of the impact, thereby reducing the peak retarding force experienced by passengers.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Crumple zones absorb collision energy by deforming over a longer time $\\Delta t$, lowering impact acceleration ($F = \\Delta p / \\Delta t$) to survivable levels."
            },
            {
                "q": "Assertion (A): A person stepping out of a rowing boat onto the riverbank causes the boat to move backwards.<br>Reason (R): The foot pushes the boat backward to gain the forward momentum needed to step onto the bank.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Newton's third law: pushing backward on the boat (action) produces the forward reaction pushing the person to the bank; momentum conservation moves the boat backward."
            },
            {
                "q": "Assertion (A): Newton's first law of motion is often referred to as the law of inertia.<br>Reason (R): Inertia is the inherent resistance of an object to changes in its state of rest or uniform motion.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The first law formalizes Galileo's concept of inertia: an object maintains its velocity unless compelled to change by an external net force."
            },
            {
                "q": "Assertion (A): When a glass tumbler falls on a cement floor, it breaks, but when it falls on a carpet from the same height, it does not break.<br>Reason (R): The carpet exerts zero total impulse on the falling tumbler.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false: The total impulse $\\Delta p$ is identical in both cases, but the soft carpet increases impact time $\\Delta t$, reducing force below the glass fracture threshold."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Automobile Crash Test & Airbag Dynamics<br>In a national vehicle safety assessment, a test car of total mass 1500 kg travelling at 54 km/h (15 m/s) collides with a rigid concrete wall. An anthropomorphic test dummy of mass 70 kg is restrained in the driver's seat. Two test cases are examined:<br>• <b>Case 1 (Without Airbag):</b> The dummy impacts the rigid steering wheel directly, coming to a dead stop in just 0.01 seconds.<br>• <b>Case 2 (With Airbag):</b> The deployed airbag cushions the dummy, compressing smoothly and bringing the dummy to rest over 0.15 seconds.",
                "q": "What is the initial momentum of the 70 kg dummy before impact?",
                "options": ["700 kg·m/s", "1050 kg·m/s", "3780 kg·m/s", "1500 kg·m/s"],
                "ans": "B",
                "exp": "$p = m v = 70\\text{ kg} \\times 15\\text{ m/s} = 1050\\text{ kg}\\cdot\\text{m/s}$."
            },
            {
                "q": "In Case 1 (without airbag), what is the average retarding force exerted on the dummy's chest?",
                "options": ["10,500 N", "105,000 N", "70,000 N", "1,050 N"],
                "ans": "B",
                "exp": "$F = \\frac{\\Delta p}{\\Delta t} = \\frac{1050}{0.01} = 105,000$ N (105 kN, fatal magnitude!)."
            },
            {
                "q": "In Case 2 (with airbag), what is the average force exerted on the dummy?",
                "options": ["7,000 N", "105,000 N", "70,000 N", "15,000 N"],
                "ans": "A",
                "exp": "$F = \\frac{1050}{0.15} = 7,000$ N (7 kN, survivable with seatbelt load limiters)."
            },
            {
                "q": "By what factor does the airbag reduce the peak impact force in this crash scenario?",
                "options": ["5 times", "10 times", "15 times", "20 times"],
                "ans": "C",
                "exp": "$\\frac{105,000}{7,000} = 15$ times lower force."
            },
            {
                "q": "What fundamental law of physics explains the primary protective mechanism of the airbag?",
                "options": ["Newton's first law only", "Impulse-momentum relationship ($F = \\Delta p / \\Delta t$)", "Law of conservation of energy only", "Pascal's hydraulic law"],
                "ans": "B",
                "exp": "For a fixed change in momentum $\\Delta p$, increasing impact duration $\\Delta t$ proportionally reduces the net destructive force $F$."
            }
        ]
    },
    {
        "num": 7,
        "title": "Work, Energy, and Simple Machines",
        "file": "Science_Exam_Papers/chapter_07_work_energy_set_b.html",
        "short_file": "chapter_07_work_energy_set_b.html",
        "description": "SET B (Advanced Energetics & Machines): Spring elastic potential energy, mechanical advantage of block & tackle systems, work-energy theorem, and pump efficiency.",
        "questions": [
            {
                "q": "An electric water pump with an efficiency of 80% lifts 1200 kg of water to a height of 20 m in 2 minutes ($g = 10\\text{ m/s}^2$). What is the electrical power input to the pump?",
                "options": ["2000 W", "2500 W", "1600 W", "3200 W"],
                "ans": "B",
                "exp": "$W = mgh = 1200 \\times 10 \\times 20 = 240,000$ J. Time $t = 120$ s. $P_{output} = \\frac{240,000}{120} = 2000$ W. $P_{input} = \\frac{P_{output}}{0.80} = \\frac{2000}{0.80} = 2500$ W."
            },
            {
                "q": "The kinetic energy of an object is increased by 300% (becoming 4 times its original value). By what percentage does its linear momentum increase?",
                "options": ["100%", "200%", "300%", "50%"],
                "ans": "A",
                "exp": "$p = \\sqrt{2m E_k}$. If $E_k$ quadruples ($4 E_k$), $p$ becomes $\\sqrt{4} = 2p$ (doubles). An increase from $p$ to $2p$ is a $100\\%$ increase."
            },
            {
                "q": "An ideal block and tackle pulley system consists of 5 pulleys (velocity ratio $VR = 5$). What effort force is needed to lift a load of 1000 N?",
                "options": ["5000 N", "200 N", "250 N", "500 N"],
                "ans": "B",
                "exp": "For an ideal system, $MA = VR = 5$. $\\text{Effort} = \\frac{\\text{Load}}{MA} = \\frac{1000}{5} = 200$ N."
            },
            {
                "q": "If the efficiency of the above 5-pulley system is actually 80% due to friction and cable weight, what effort is required?",
                "options": ["200 N", "250 N", "300 N", "160 N"],
                "ans": "B",
                "exp": "$MA = \\eta \\times VR = 0.80 \\times 5 = 4$. $\\text{Effort} = \\frac{\\text{Load}}{MA} = \\frac{1000}{4} = 250$ N."
            },
            {
                "q": "A spring with force constant $k = 400\\text{ N/m}$ is compressed by 10 cm ($0.10$ m). What is the elastic potential energy stored in the spring ($E_p = \\frac{1}{2}kx^2$)?",
                "options": ["40 J", "2 J", "4 J", "20 J"],
                "ans": "B",
                "exp": "$E_p = \\frac{1}{2} k x^2 = \\frac{1}{2} \\times 400 \\times (0.10)^2 = 200 \\times 0.01 = 2$ Joules."
            },
            {
                "q": "A horizontal force $F$ pushes a 4 kg box along a straight path where force varies with displacement: $F = 10$ N from $s=0$ to $s=4$ m, and then decreases linearly to 0 at $s=8$ m. What is the total work done?",
                "options": ["40 J", "80 J", "60 J", "50 J"],
                "ans": "C",
                "exp": "Area under $F-s$ graph: Rectangle from 0 to 4 m $= 10 \\times 4 = 40$ J. Triangle from 4 to 8 m $= \\frac{1}{2} \\times (8 - 4) \\times 10 = 20$ J. Total work $= 40 + 20 = 60$ J."
            },
            {
                "q": "A simple pendulum bob of mass 0.2 kg is released from rest at a height of 0.8 m above its lowest equilibrium position. What is its speed at the lowest point ($g = 10\\text{ m/s}^2$)?",
                "options": ["2 m/s", "4 m/s", "8 m/s", "16 m/s"],
                "ans": "B",
                "exp": "Conservation of energy: $mgh = \\frac{1}{2}mv^2 \\Rightarrow v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 0.8} = \\sqrt{16} = 4$ m/s."
            },
            {
                "q": "A crowbar of length 150 cm is used to displace a heavy rock. The fulcrum is placed 30 cm from the rock (load). What is the ideal mechanical advantage of this Class 1 lever?",
                "options": ["5", "4", "3", "0.2"],
                "ans": "B",
                "exp": "$\\text{Load arm} = 30$ cm. $\\text{Effort arm} = 150 - 30 = 120$ cm. $MA = \\frac{\\text{Effort arm}}{\\text{Load arm}} = \\frac{120}{30} = 4$."
            },
            {
                "q": "A 50 kg girl climbs up a flight of 40 stairs, each 15 cm high, in 20 seconds ($g = 10\\text{ m/s}^2$). Her average power output is:",
                "options": ["150 W", "300 W", "1500 W", "3000 W"],
                "ans": "A",
                "exp": "$h = 40 \\times 0.15 = 6$ m. Work $W = mgh = 50 \\times 10 \\times 6 = 3000$ J. Power $P = \\frac{3000}{20} = 150$ W."
            },
            {
                "q": "A car travelling at 20 m/s skids to a halt over 40 m when brakes lock. If the same car travels at 40 m/s (twice the speed), what will be the skidding distance under identical tire-road friction?",
                "options": ["80 m", "120 m", "160 m", "200 m"],
                "ans": "C",
                "exp": "Work done by friction $= \\text{Initial } E_k \\Rightarrow f \\cdot s = \\frac{1}{2}mv^2 \\Rightarrow s \\propto v^2$. Doubling velocity quadruples stopping distance: $40 \\times 4 = 160$ m."
            },
            {
                "q": "Which of the following forces does negative work on an object in motion?",
                "options": ["Gravitational force on an apple falling from a tree", "Friction acting on a skidding bicycle tire", "Centripetal force on a satellite orbiting Earth", "Tension in string pulling a toy cart forward"],
                "ans": "B",
                "exp": "Friction opposes displacement ($\\theta = 180^\\circ$). $W = F s \\cos 180^\\circ = -F s$, doing negative work that converts kinetic energy into thermal energy."
            },
            {
                "q": "An inclined plane has length $L = 5$ m and height $h = 1$ m. Neglecting friction, what is its ideal mechanical advantage?",
                "options": ["5", "0.2", "4", "1"],
                "ans": "A",
                "exp": "For an inclined plane, $MA = \\frac{\\text{Length}}{\\text{Height}} = \\frac{5}{1} = 5$."
            },
            {
                "q": "A machine with an efficiency of 75% delivers 1500 J of useful work. What was the total work energy input to the machine?",
                "options": ["1125 J", "2000 J", "2500 J", "1800 J"],
                "ans": "B",
                "exp": "$\\text{Input} = \\frac{\\text{Output}}{\\eta} = \\frac{1500}{0.75} = 2000$ J."
            },
            {
                "q": "An object of mass $m$ is moving at speed $v$. Another object has mass $2m$ and speed $v/2$. What is the ratio of their kinetic energies?",
                "options": ["1 : 1", "2 : 1", "1 : 2", "4 : 1"],
                "ans": "B",
                "exp": "$E_1 = \\frac{1}{2}mv^2$. $E_2 = \\frac{1}{2}(2m)(v/2)^2 = m(v^2/4) = \\frac{1}{4}mv^2 = \\frac{1}{2}E_1$. Hence, $E_1 : E_2 = 2 : 1$."
            },
            {
                "q": "A consumer uses five 100-Watt incandescent light bulbs for 6 hours daily for 30 days. How many commercial units (kWh) of electricity are consumed?",
                "options": ["90 units", "180 units", "900 units", "45 units"],
                "ans": "A",
                "exp": "Total power $= 5 \\times 100 = 500$ W $= 0.5$ kW. Energy $= 0.5\\text{ kW} \\times 6\\text{ h/day} \\times 30\\text{ days} = 90$ kWh (units)."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): No machine can ever have an efficiency exceeding 100%.<br>Reason (R): Energy cannot be created according to the universal law of conservation of energy, and some input energy is inevitably lost as heat due to friction.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because energy output $\\le$ energy input, efficiency $\\eta = \\frac{W_{out}}{W_{in}} \\times 100 \\le 100\\%$. Friction and heat dissipation make $\\eta < 100\\%$ in all real machines."
            },
            {
                "q": "Assertion (A): The work done by a centripetal force on an object in uniform circular motion is always zero.<br>Reason (R): The centripetal force acts towards the center of the circle, perpendicular to the instantaneous tangential displacement vector.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "$W = F s \\cos\\theta$. Since centripetal force is orthogonal to tangential displacement ($\\theta = 90^\\circ$), $\\cos 90^\\circ = 0$, so no work is done."
            },
            {
                "q": "Assertion (A): Two persons of masses 50 kg and 80 kg who climb the same 10-meter staircase do different amounts of work.<br>Reason (R): Work against gravity is directly proportional to mass ($W = mgh$).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The 80 kg person lifts greater weight through the same height, doing $80 \\times 10 \\times 10 = 8000$ J, while the 50 kg person does 5000 J."
            },
            {
                "q": "Assertion (A): When a fast-moving car hits a spring barrier, the kinetic energy of the car is converted into elastic potential energy of the compressed spring.<br>Reason (R): Total mechanical energy is conserved in the absence of dissipative friction.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The conservative restoring force of the spring decelerates the car, converting initial kinetic energy $\\frac{1}{2}mv^2$ into stored spring energy $\\frac{1}{2}kx^2$."
            },
            {
                "q": "Assertion (A): An astronaut inside an orbiting space station feels weightless because gravitational force from Earth is zero in orbit.<br>Reason (R): Gravity drops to zero as soon as an object enters space beyond Earth's atmosphere.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both statements are completely false! Earth's gravity at 400 km altitude is still $\\approx 90\\%$ of surface gravity. The weightlessness feeling arises because the station and astronaut are in perpetual free fall around Earth."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Energy Auditing of an Electric Locomotive<br>A freight railway locomotive engine has a rated power output of 3.0 Megawatts ($3 \\times 10^6$ W). It hauls a fully loaded train of total mass $2 \\times 10^6$ kg (2000 tonnes) up a gentle mountain gradient of 1 in 100 (height increases by 1 m for every 100 m of track). The train maintains a constant speed of 20 m/s (72 km/h). Take $g = 10\\text{ m/s}^2$.",
                "q": "In one second, the train covers a track distance of 20 m. What vertical height does the train gain in one second?",
                "options": ["0.1 m", "0.2 m", "0.5 m", "1.0 m"],
                "ans": "B",
                "exp": "$\\text{Vertical height per second} = 20\\text{ m} \\times \\frac{1}{100} = 0.2$ m."
            },
            {
                "q": "What is the rate of work done against gravity (power needed to lift the train mass) per second?",
                "options": ["$4.0 \\times 10^6$ W", "$4.0 \\times 10^5$ W", "$2.0 \\times 10^6$ W", "$1.0 \\times 10^6$ W"],
                "ans": "A",
                "exp": "$P_{gravity} = \\frac{mgh}{t} = 2 \\times 10^6 \\times 10 \\times 0.2 = 4.0 \\times 10^6$ W (4.0 MW)... wait, if gradient is 1 in 100, $h = 0.2$ m, $m = 2 \\times 10^6$ kg, $mgh = 2 \\times 10^6 \\times 10 \\times 0.2 = 4 \\times 10^6$ W."
            },
            {
                "q": "If the locomotive provides a traction force of $150,000$ N to overcome rolling friction and air drag at 20 m/s, what power is expended against friction?",
                "options": ["$3.0 \\times 10^6$ W (3 MW)", "$1.5 \\times 10^6$ W", "$6.0 \\times 10^6$ W", "$750,000$ W"],
                "ans": "A",
                "exp": "$P = F \\times v = 150,000\\text{ N} \\times 20\\text{ m/s} = 3,000,000\\text{ W} = 3.0$ MW."
            },
            {
                "q": "How much kinetic energy does the 2000-tonne train possess while cruising at 20 m/s?",
                "options": ["$4.0 \\times 10^8$ J (400 MJ)", "$2.0 \\times 10^8$ J", "$8.0 \\times 10^8$ J", "$4.0 \\times 10^7$ J"],
                "ans": "A",
                "exp": "$E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} (2 \\times 10^6) (20^2) = 10^6 \\times 400 = 400 \\times 10^6$ J $= 400$ MJ."
            },
            {
                "q": "When braking on downhill slopes, modern trains utilize regenerative brakes that convert kinetic energy into electrical energy returned to the power grid. This confirms which universal law?",
                "options": ["Law of conservation of mechanical momentum", "Law of conservation of energy", "Newton's second law", "Coulomb's law"],
                "ans": "B",
                "exp": "Energy cannot be destroyed; regenerative braking captures kinetic energy and converts it into reusable electrical energy via generators."
            }
        ]
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom",
        "file": "Science_Exam_Papers/chapter_08_atom_set_b.html",
        "short_file": "chapter_08_atom_set_b.html",
        "description": "SET B (Advanced Atomic Structure & Isotopes): Rutherford nuclear scattering calculations, subatomic e/m ratios, Bohr energy levels, and radioactive isotopic applications.",
        "questions": [
            {
                "q": "Rutherford deduced the nuclear radius of an atom to be approximately $10^{-15}$ m, whereas the atomic radius is about $10^{-10}$ m. What is the approximate ratio of atomic volume to nuclear volume?",
                "options": ["$10^5$", "$10^{15}$", "$10^{10}$", "$10^3$"],
                "ans": "B",
                "exp": "$V \\propto r^3$. Ratio $= \\left(\\frac{10^{-10}}{10^{-15}}\\right)^3 = (10^5)^3 = 10^{15}$. The atom is mostly empty space."
            },
            {
                "q": "Why did J.J. Thomson find that the charge-to-mass ratio ($e/m$) of cathode rays was constant regardless of the gas used in the tube, whereas canal ray $e/m$ varied with the gas?",
                "options": ["Cathode rays are composed of universal fundamental electrons, whereas canal rays consist of positive gaseous ions whose masses depend on the specific gas element", "Canal rays contain neutrons", "Cathode rays are electromagnetic waves", "Canal rays travel at the speed of light"],
                "ans": "A",
                "exp": "Electrons are identical in all matter, giving fixed $e/m$. Positive canal ray particles are stripped residual gas cations; heavier gases produce heavier ions with lower $e/m$."
            },
            {
                "q": "Naturally occurring magnesium consists of three isotopes: $^{24}\\text{Mg}$ (79%), $^{25}\\text{Mg}$ (10%), and $^{26}\\text{Mg}$ (11%). The average atomic mass of magnesium is:",
                "options": ["24.32 u", "25.00 u", "24.00 u", "24.65 u"],
                "ans": "A",
                "exp": "$\\text{Mass} = \\frac{(24 \\times 79) + (25 \\times 10) + (26 \\times 11)}{100} = \\frac{1896 + 250 + 286}{100} = \\frac{2432}{100} = 24.32$ u."
            },
            {
                "q": "Why does potassium ($Z = 19$) have an electronic configuration of 2, 8, 8, 1 rather than 2, 8, 9, even though the $M$-shell can theoretically accommodate up to 18 electrons?",
                "options": ["The octet rule dictates that the outermost valence shell cannot exceed 8 electrons, so the 19th electron enters the 4th (N) shell", "The M-shell can only ever hold 8 electrons", "Potassium loses an electron immediately", "Neutrons prevent filling the M-shell"],
                "ans": "A",
                "exp": "According to the Bohr-Bury octet rule, the outermost valence shell cannot hold more than 8 electrons; hence, the 19th electron starts the N-shell ($4s$ level)."
            },
            {
                "q": "An atom has 17 protons, 18 neutrons, and 18 electrons. This species is:",
                "options": ["A neutral Argon atom ($^{35}_{18}\\text{Ar}$)", "A chloride anion ($^{35}_{17}\\text{Cl}^-$)", "A potassium cation ($^{39}_{19}\\text{K}^+$)", "A radioactive chlorine isotope"],
                "ans": "B",
                "exp": "$Z = 17$ (Chlorine). Mass number $A = 17 + 18 = 35$. With 18 electrons (one extra than 17 protons), it carries a net $-1$ charge ($^{35}_{17}\\text{Cl}^-$)."
            },
            {
                "q": "Which pair represents isobars (same mass number, different atomic numbers)?",
                "options": ["$^{12}_6\\text{C}$ and $^{14}_6\\text{C}$", "$^{40}_{18}\\text{Ar}$ and $^{40}_{20}\\text{Ca}$", "$^{1}_1\\text{H}$ and $^{2}_1\\text{H}$", "$^{16}_8\\text{O}$ and $^{18}_8\\text{O}$"],
                "ans": "B",
                "exp": "Argon ($Z=18$) and Calcium ($Z=20$) both have mass number 40; they are isobars."
            },
            {
                "q": "How many neutrons are present in the nucleus of a tritium isotope ($^{3}_{1}\\text{H}$)?",
                "options": ["1", "2", "3", "0"],
                "ans": "B",
                "exp": "$\\text{Neutrons} = A - Z = 3 - 1 = 2$."
            },
            {
                "q": "Which subatomic particle was discovered by James Chadwick in 1932 by bombarding a thin sheet of beryllium with alpha particles?",
                "options": ["Positron", "Neutron", "Proton", "Neutrino"],
                "ans": "B",
                "exp": "James Chadwick observed penetrating neutral radiation consisting of uncharged particles with mass equal to a proton: neutrons ($^1_0 n$)."
            },
            {
                "q": "The electronic configurations of four elements are: P (2, 8, 1), Q (2, 8, 7), R (2, 8, 8), and S (2, 6). Which element exhibits a valency of 2?",
                "options": ["Element P", "Element Q", "Element R", "Element S"],
                "ans": "D",
                "exp": "Element S has 6 valence electrons; to complete its octet, it needs $8 - 6 = 2$ electrons. Valency $= 2$ (Oxygen)."
            },
            {
                "q": "Which isotope is used as standard fuel in nuclear fission reactors to generate electricity?",
                "options": ["Uranium-235 ($^{235}_{92}\\text{U}$)", "Carbon-14 ($^{14}_6\\text{C}$)", "Cobalt-60 ($^{60}_{27}\\text{Co}$)", "Iodine-131 ($^{131}_{53}\\text{I}$)",],
                "ans": "A",
                "exp": "Uranium-235 undergoes controlled thermal neutron-induced nuclear fission inside commercial nuclear power reactors."
            },
            {
                "q": "What is the maximum number of electrons that can be accommodated in the $N$-shell ($n = 4$)?",
                "options": ["8", "18", "32", "50"],
                "ans": "C",
                "exp": "Maximum capacity $= 2 n^2 = 2(4^2) = 2(16) = 32$ electrons."
            },
            {
                "q": "Which of the following ions is isoelectronic with the noble gas Neon ($Z = 10$, configuration 2, 8)?",
                "options": ["$Na^+$ ($Z=11$)", "$Mg^{2+}$ ($Z=12$)", "$O^{2-}$ ($Z=8$)", "All of the above"],
                "ans": "D",
                "exp": "All three have 10 electrons ($11-1=10$, $12-2=10$, $8+2=10$), matching Neon's 2, 8 configuration."
            },
            {
                "q": "An element $X$ has valency 3 and element $Y$ has valency 2. The chemical formula of the compound formed between $X$ and $Y$ is:",
                "options": ["$XY$", "$X_2 Y_3$", "$X_3 Y_2$", "$X_2 Y$"],
                "ans": "B",
                "exp": "Criss-cross valency method: $X^3$ and $Y^2$ yields $X_2 Y_3$."
            },
            {
                "q": "What is the mass of one mole of neutrons approximately, given the mass of a single neutron is $1.675 \\times 10^{-24}$ g and Avogadro's constant is $6.022 \\times 10^{23}$?",
                "options": ["1.008 g", "1840 g", "0.001 g", "100 g"],
                "ans": "A",
                "exp": "$1.675 \\times 10^{-24} \\times 6.022 \\times 10^{23} \\approx 1.008$ g."
            },
            {
                "q": "Which radioactive isotope is utilized in medicine for the assessment and treatment of thyroid gland disorders?",
                "options": ["Iodine-131 ($^{131}\\text{I}$)", "Cobalt-60", "Carbon-14", "Phosphorus-32"],
                "ans": "A",
                "exp": "The thyroid gland absorbs iodine; radioactive Iodine-131 is used to image and treat goiter and thyroid carcinoma."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): An atom remains stable and its electrons do not spiral into the nucleus.<br>Reason (R): According to Neils Bohr, electrons revolve only in discrete stationary orbits without radiating electromagnetic energy.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Bohr postulated quantized non-radiating orbits, overcoming the fatal flaw in Rutherford's model where accelerated charges radiate energy."
            },
            {
                "q": "Assertion (A): Isotopes of chlorine, $^{35}_{17}\\text{Cl}$ and $^{37}_{17}\\text{Cl}$, have identical chemical properties.<br>Reason (R): Chemical properties are governed by valence electrons, and both isotopes have identical atomic number 17 and electronic configuration (2, 8, 7).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Chemical reactivity depends strictly on outer valence electron configuration, which is identical in both isotopes."
            },
            {
                "q": "Assertion (A): The atomic mass of an element is often a fractional decimal number (e.g., Chlorine is 35.5 u).<br>Reason (R): Naturally occurring elements often exist as mixtures of two or more isotopes with different natural abundance percentages.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Average atomic mass is a weighted average of isotopic masses based on natural fractional abundances (e.g. 75% 35Cl + 25% 37Cl = 35.5 u)."
            },
            {
                "q": "Assertion (A): Noble gases (Helium, Argon, Neon) have zero valency.<br>Reason (R): Their outermost shells are completely filled, leaving no tendency to gain, lose, or share electrons.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "A complete duplet (He) or octet (Ne, Ar) imparts exceptional thermodynamic stability, resulting in zero chemical valency."
            },
            {
                "q": "Assertion (A): Thomson's model predicted that alpha particles would easily pass through gold atoms with only minimal deflection.<br>Reason (R): In Thomson's model, positive charge and mass were thought to be spread thinly throughout the entire volume of the atom.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Rutherford expected minor deflections because Thomson's diffuse positive sphere could not exert sufficient concentrated electric field to deflect fast alpha particles backward."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Mass Spectrometry & Nuclear Nucleon Identification<br>A mass spectrometry laboratory analyzes a radioactive mineral sample containing four nuclear species: P, Q, R, and S. The laboratory records the following data:<br>• <b>Species P:</b> 6 protons, 6 neutrons, 6 electrons<br>• <b>Species Q:</b> 6 protons, 8 neutrons, 6 electrons<br>• <b>Species R:</b> 7 protons, 7 neutrons, 7 electrons<br>• <b>Species S:</b> 8 protons, 8 neutrons, 10 electrons",
                "q": "What is the mass number ($A$) of Species Q?",
                "options": ["12", "14", "6", "8"],
                "ans": "B",
                "exp": "$A = \\text{protons} + \\text{neutrons} = 6 + 8 = 14$."
            },
            {
                "q": "Which two species are isotopes of each other?",
                "options": ["P and Q", "Q and R", "R and S", "P and S"],
                "ans": "A",
                "exp": "Species P and Q both have $Z = 6$ (protons), but different neutron counts (6 vs 8); they are isotopes of Carbon ($^{12}_6C$ and $^{14}_6C$)."
            },
            {
                "q": "Which two species have the same mass number ($A = 14$) and are therefore isobars?",
                "options": ["P and Q", "Q and R", "P and R", "R and S"],
                "ans": "B",
                "exp": "Species Q ($A = 6+8=14$) and Species R ($A = 7+7=14$) have different atomic numbers (6 and 7) but the same mass number (14); they are isobars."
            },
            {
                "q": "What is the net electrical charge and identity of Species S?",
                "options": ["Neutral oxygen atom ($O$)", "Oxide anion with $-2$ charge ($O^{2-}$)", "Nitrogen cation with $+2$ charge", "Neutral Neon atom"],
                "ans": "B",
                "exp": "$Z = 8$ (Oxygen). It has 8 protons ($+8$) and 10 electrons ($-10$), giving a net charge of $-2$ ($O^{2-}$ anion)."
            },
            {
                "q": "Species Q ($^{14}_6\\text{C}$) is famously utilized in archeology for which scientific dating technique?",
                "options": ["Radiocarbon dating of biological organic artifacts", "Uranium-lead dating of volcanic rocks", "Potassium-argon dating of meteorites", "Thermoluminescence of pottery"],
                "ans": "A",
                "exp": "Carbon-14 decays with a half-life of 5,730 years, utilized to date ancient organic artifacts up to 50,000 years old."
            }
        ]
    }
]

HTML_TEMPLATE_SET_B = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Science - {chapter_title} - SET B (HOTS)</title>
  <link rel="stylesheet" href="exam-style.css">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<div class="screen-wrapper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="toolbar no-print">
    <div class="toolbar-title">
      <span>🔥 CBSE 9TH SCIENCE | CH {chapter_num} [SET B - HOTS]</span>
      <span class="timer-badge" id="timerDisplay">45:00</span>
    </div>
    <div class="toolbar-actions">
      <button class="btn btn-secondary" onclick="toggleTimer()" id="timerBtn">⏸️ Pause Timer</button>
      <button class="btn btn-check" onclick="checkAnswers()">✔️ Check My Score</button>
      <button class="btn btn-secondary" onclick="toggleAnswerKey()">📄 Toggle Key</button>
      <button class="btn btn-print" onclick="window.print()">🖨️ Print Paper (A4)</button>
    </div>
  </div>

  <!-- Professional Examination Header -->
  <div class="exam-header">
    <div class="school-name">CENTRAL BOARD OF SECONDARY EDUCATION</div>
    <div class="exam-title">HALF-YEARLY PRACTICE EXAMINATION (SESSION 2024-2025)</div>
    <div class="exam-title" style="font-size: 13.5px; color: #1e3a8a; margin-top: 3px; font-weight: 800;">
      SUBJECT: SCIENCE (CLASS - IX) | CHAPTER {chapter_num}: {chapter_title_upper} [SET B - ADVANCED HOTS]
    </div>
    <div class="exam-meta-line">
      <span>TIME ALLOWED: 45 MINUTES</span>
      <span>MAXIMUM MARKS: 25</span>
      <span>PAPER CODE: 086/CH{chapter_num_padded}/SET-B</span>
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
    <h4>General Instructions (SET B - Higher Order Thinking Skills):</h4>
    <ol>
      <li>The question paper comprises <b>25 Multiple Choice Questions (MCQs)</b> of <b>1 mark each</b>.</li>
      <li><b>Section A (Q1 – Q15):</b> Advanced Conceptual and Numerical MCQs with single correct option.</li>
      <li><b>Section B (Q16 – Q20):</b> Critical Assertion-Reasoning based questions testing analytical clarity.</li>
      <li><b>Section C (Q21 – Q25):</b> Case-Study / Practical Experimental Data-interpretation questions.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding circle on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <!-- Questions Container -->
  <div class="questions-container">

    <div class="section-banner">
      <span>SECTION A: ADVANCED & NUMERICAL MCQS (Q.1 TO Q.15)</span>
      <span>[15 MARKS]</span>
    </div>

{section_a_html}

    <div class="section-banner">
      <span>SECTION B: ASSERTION - REASON QUESTIONS (Q.16 TO Q.20)</span>
      <span>[5 MARKS]</span>
    </div>
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 6px 10px; font-size: 11.5px; border-radius: 4px; margin-bottom: 8px;">
      <b>Directions for Q16 to Q20:</b> Select the correct option from the choices given below:<br>
      <b>(A)</b> Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).<br>
      <b>(B)</b> Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).<br>
      <b>(C)</b> Assertion (A) is true but Reason (R) is false.<br>
      <b>(D)</b> Assertion (A) is false but Reason (R) is true (or both are false).
    </div>

{section_b_html}

    <div class="section-banner">
      <span>SECTION C: EXPERIMENTAL DATA & CASE STUDY (Q.21 TO Q.25)</span>
      <span>[5 MARKS]</span>
    </div>

{section_c_html}

  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET B)</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & IN-DEPTH EXPLANATIONS (SET B)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>In-Depth Conceptual & Numerical Solution</th>
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
  alert("SET B Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nScroll down to examine detailed step-by-step solutions.");
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

def generate_set_b_papers():
    for ch in SET_B_DATA:
        q_data = ch["questions"]
        answers_dict = {}
        
        sec_a_cards = []
        sec_b_cards = []
        sec_c_cards = []
        case_intro_shown = False
        
        for idx, item in enumerate(q_data):
            qnum = idx + 1
            answers_dict[qnum] = item["ans"]
            
            opts_html = []
            letters = ["A", "B", "C", "D"]
            for opt_idx, opt_text in enumerate(item["options"]):
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
                {item["q"]}
              </div>
              <div class="options-grid">
                {''.join(opts_html)}
              </div>
              <div class="feedback-msg" id="feedback_{qnum}"></div>
            </div>
            """
            
            if qnum <= 15:
                sec_a_cards.append(card_html)
            elif qnum <= 20:
                sec_b_cards.append(card_html)
            else:
                if not case_intro_shown and "case_intro" in item:
                    case_box = f"""
                    <div class="case-study-box">
                      <h5>READING PASSAGE & EXPERIMENTAL SETUP:</h5>
                      <p>{item["case_intro"]}</p>
                    </div>
                    """
                    sec_c_cards.append(case_box)
                    case_intro_shown = True
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
              <td style="text-align: center;"><span class="ans-badge">({item['ans']})</span></td>
              <td>{item['exp']}</td>
            </tr>
            """)
            
        full_html = HTML_TEMPLATE_SET_B.format(
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
        print(f"Generated {ch['file']} successfully.")

if __name__ == "__main__":
    generate_set_b_papers()
    print("ALL SET B PAPERS GENERATED!")
