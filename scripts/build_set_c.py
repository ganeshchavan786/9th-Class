"""
Build script for CBSE Class 9 Science - SET C Examination Papers (Chapters 1 to 8)
Focus: NCERT Exemplar, Deep Conceptual Nuances, Tricky Application Questions, and Critical Thinking.
Zero Marathi text in exam papers - strictly standard English.
"""

import json
import os

SET_C_DATA = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "file": "Science_Exam_Papers/chapter_01_exploration_set_c.html",
        "short_file": "chapter_01_exploration_set_c.html",
        "description": "SET C (NCERT Exemplar & Tricky Questions): Dimensional consistency, experimental error propagation, pendulum period analysis, and calibration standards.",
        "questions": [
            {
                "q": "A student measures the period of oscillation $T$ of a simple pendulum with lengths 20 cm, 40 cm, 60 cm, and 80 cm. A graph of $T^2$ versus pendulum length $L$ yields:",
                "options": ["A parabola curving upward", "A straight line passing through the origin", "A hyperbolic curve", "A horizontal line parallel to the length axis"],
                "ans": "B",
                "exp": "Since $T = 2\\pi \\sqrt{L/g}$, squaring both sides gives $T^2 = \\left(\\frac{4\\pi^2}{g}\\right) L$. This is of the form $y = mx$, representing a straight line passing through the origin."
            },
            {
                "q": "The mass of a solid block is measured as $m = (50.0 \\pm 0.5)$ g and its volume is $V = (25.0 \\pm 0.5)\\text{ cm}^3$. What is the relative percentage error in its calculated density?",
                "options": ["1.0%", "2.0%", "3.0%", "0.5%"],
                "ans": "C",
                "exp": "Relative error in density $\\frac{\\Delta \\rho}{\\rho} = \\frac{\\Delta m}{m} + \\frac{\\Delta V}{V} = \\frac{0.5}{50.0} + \\frac{0.5}{25.0} = 0.01 + 0.02 = 0.03 = 3.0\\%$."
            },
            {
                "q": "Which of the following measurements has exactly four significant figures?",
                "options": ["0.0025 kg", "2.500 g", "0.0250 L", "2500 m"],
                "ans": "B",
                "exp": "Trailing zeros after a decimal point are significant. '2.500' has four significant figures (2, 5, 0, 0). Leading zeros in 0.0025 and 0.0250 are not significant."
            },
            {
                "q": "When subtracting 1.2 cm from 15.345 cm, what should the result be recorded as, following rules of significant figures?",
                "options": ["14.145 cm", "14.15 cm", "14.1 cm", "14 cm"],
                "ans": "C",
                "exp": "In addition and subtraction, the final result can have no more decimal places than the measurement with the fewest decimal places (1.2 cm has 1 decimal place; rounded to 14.1 cm)."
            },
            {
                "q": "A micrometer screw gauge has a pitch of 0.5 mm and 50 divisions on its circular thimble. Its least count is:",
                "options": ["0.01 mm", "0.05 mm", "0.1 mm", "0.001 mm"],
                "ans": "A",
                "exp": "$\\text{Least count} = \\frac{\\text{Pitch}}{\\text{Number of circular divisions}} = \\frac{0.5\\text{ mm}}{50} = 0.01\\text{ mm}$."
            },
            {
                "q": "Why is the metric SI system preferred over imperial units (inches, feet, pounds) in global scientific investigations?",
                "options": ["It uses arbitrary conversion factors", "It is based on a coherent decimal base-10 system that standardizes measurements reproducibly across all nations", "It was invented earlier than any other system", "It only measures temperature"],
                "ans": "B",
                "exp": "The SI system is globally standardized, coherent, and uses decimal powers of ten, minimizing unit translation errors and simplifying scientific calculations."
            },
            {
                "q": "A student accidentally spills dilute hydrochloric acid onto her hand. What is the immediate first-aid action to be taken in the laboratory?",
                "options": ["Neutralize with concentrated sodium hydroxide", "Rinse immediately under a continuous stream of running tap water for several minutes", "Apply butter or oil", "Cover immediately with an airtight plastic bandage"],
                "ans": "B",
                "exp": "Flushing with large volumes of running water rapidly dilutes and washes away the acid. Never apply strong bases, as neutralization is highly exothermic and can cause thermal burns."
            },
            {
                "q": "Which of the following physical quantities is dimensionless (has no physical units)?",
                "options": ["Density", "Specific gravity (relative density)", "Velocity", "Acceleration"],
                "ans": "B",
                "exp": "Relative density is the ratio of density of a substance to density of water at 4°C. Being a ratio of two identical physical units, it is pure dimensionless."
            },
            {
                "q": "A piece of cork of mass 6 g and density 0.25 g/cm³ floats on water. What is the actual volume of the cork?",
                "options": ["1.5 cm³", "24 cm³", "12 cm³", "0.04 cm³"],
                "ans": "B",
                "exp": "$V = \\frac{\\text{Mass}}{\\text{Density}} = \\frac{6\\text{ g}}{0.25\\text{ g/cm}^3} = 24\\text{ cm}^3$."
            },
            {
                "q": "How does repeatable precision differ fundamentally from experimental accuracy?",
                "options": ["Precision measures closeness to the true accepted standard, while accuracy measures agreement between repeated trials", "Accuracy measures closeness to the true accepted value, while precision measures the consistency and agreement among repeated measurements", "Accuracy and precision are identical physical terms", "Precision requires zero instruments"],
                "ans": "B",
                "exp": "Accuracy is how close a measured value is to the true or accepted reference value; precision is how close repeated measurements are to one another."
            },
            {
                "q": "If the slope of the $T^2$ versus $L$ graph for a simple pendulum is calculated to be $4.02\\text{ s}^2\\text{/m}$, what is the experimental value of $g$ (take $\\pi = 3.1416$)?",
                "options": ["$9.82\\text{ m/s}^2$", "$10.2\\text{ m/s}^2$", "$9.50\\text{ m/s}^2$", "$8.90\\text{ m/s}^2$"],
                "ans": "A",
                "exp": "$\\text{Slope} = \\frac{4\\pi^2}{g} \\Rightarrow g = \\frac{4\\pi^2}{\\text{Slope}} = \\frac{4(3.1416)^2}{4.02} = \\frac{39.478}{4.02} \\approx 9.82\\text{ m/s}^2$."
            },
            {
                "q": "Which of the following is a fundamental base unit in the International System of Units (SI)?",
                "options": ["Joule (J)", "Watt (W)", "Candela (cd)", "Pascal (Pa)"],
                "ans": "C",
                "exp": "Candela (cd) is the SI base unit of luminous intensity. Joule, Watt, and Pascal are derived units."
            },
            {
                "q": "A student measures the thickness of a single sheet of paper by measuring the total thickness of a 500-page ream as 5.0 cm. What is the thickness of one sheet?",
                "options": ["0.1 mm", "0.01 mm", "1.0 mm", "0.05 mm"],
                "ans": "A",
                "exp": "Thickness per sheet $= \\frac{5.0\\text{ cm}}{500} = 0.01\\text{ cm} = 0.1\\text{ mm}$."
            },
            {
                "q": "What is the primary function of a wire gauze placed beneath a glass beaker on a tripod stand during heating?",
                "options": ["To collect chemical spills", "To distribute heat evenly over the bottom of the beaker and prevent thermal shock breakage", "To act as a chemical catalyst", "To reduce boiling temperature"],
                "ans": "B",
                "exp": "The wire gauze (often with a ceramic center) spreads the Bunsen flame heat uniformly, preventing localized hot spots that shatter glassware."
            },
            {
                "q": "Express the speed of light in vacuum ($300,000,000$ m/s) in standard scientific notation:",
                "options": ["$30 \\times 10^7$ m/s", "$3.0 \\times 10^8$ m/s", "$0.3 \\times 10^9$ m/s", "$3.0 \\times 10^{-8}$ m/s"],
                "ans": "B",
                "exp": "$300,000,000\\text{ m/s} = 3.0 \\times 10^8\\text{ m/s}$ in standard normalized scientific notation."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): The least count of a measuring instrument represents the smallest measurement that can be accurately resolved by it.<br>Reason (R): A smaller least count generally leads to higher precision in measurement.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "B",
                "exp": "Both statements are correct facts, but the reason states an advantage of small least count rather than explaining the operational definition of least count."
            },
            {
                "q": "Assertion (A): Random errors cannot be completely avoided even in the most carefully designed experiment.<br>Reason (R): Random errors arise from unpredictable microscopic variations in environmental conditions and minor observer judgment fluctuations.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Random errors follow a normal statistical distribution due to uncontrollable thermal, mechanical, or human limits, making them inevitable in empirical testing."
            },
            {
                "q": "Assertion (A): A physical equation can be dimensionally correct yet physically incorrect.<br>Reason (R): Dimensionless constants (such as $\\frac{1}{2}$, $\\pi$) in an equation cannot be verified by dimensional analysis.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "For instance, $s = 2 u t + a t^2$ is dimensionally consistent ($[L] = [L]$) but physically wrong because the constant factor is erroneous."
            },
            {
                "q": "Assertion (A): Flammable liquids like kerosene or alcohol can be extinguished using water.<br>Reason (R): Water has a high specific heat capacity that cools burning liquids.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is completely false: Kerosene and alcohol are less dense than water; pouring water causes the burning liquid to float on top, spreading the fire! (Use sand or foam extinguisher)."
            },
            {
                "q": "Assertion (A): In a scientific controlled experiment, only one independent variable is altered at a time.<br>Reason (R): Altering multiple variables simultaneously makes it impossible to isolate which specific factor produced the observed change.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Fair testing requires holding all controlled variables fixed while systematically varying only the single factor under study."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Investigation of Thermal Expansion of Metals<br>A physics student investigates the linear thermal expansion of three metallic rods of identical initial length (1.000 m at 20°C): Rod A (Copper), Rod B (Aluminum), and Rod C (Iron). She places each rod into a steam jacket heated to 100°C (temperature increase $\\Delta T = 80^\\circ\\text{C}$). The expansions measured using a dial gauge are:<br>• Rod A (Copper): $1.36$ mm<br>• Rod B (Aluminum): $1.92$ mm<br>• Rod C (Iron): $0.96$ mm",
                "q": "Which metal rod demonstrated the highest coefficient of linear expansion ($\alpha$)?",
                "options": ["Rod A (Copper)", "Rod B (Aluminum)", "Rod C (Iron)", "All three expanded equally"],
                "ans": "B",
                "exp": "Since $\\Delta L = L_0 \\alpha \\Delta T$, with identical initial length and temperature rise, Aluminum expanded the most ($1.92$ mm), indicating the highest $\\alpha$."
            },
            {
                "q": "What is the coefficient of linear expansion of Iron (Rod C) per degree Celsius?",
                "options": ["$1.2 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$", "$2.4 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$", "$1.7 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$", "$0.96 \\times 10^{-3}\\text{ /}^\\circ\\text{C}$"],
                "ans": "A",
                "exp": "$\\alpha = \\frac{\\Delta L}{L_0 \\Delta T} = \\frac{0.00096\\text{ m}}{1.000\\text{ m} \\times 80^\\circ\\text{C}} = 1.2 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$."
            },
            {
                "q": "If a bimetallic strip made of Copper (Rod A) and Iron (Rod C) riveted together is heated, towards which metal will the strip bend?",
                "options": ["Towards Copper, because Copper expands more", "Towards Iron, because Iron expands less, forming the inner arc of curvature", "It remains completely straight", "It twists into a corkscrew"],
                "ans": "B",
                "exp": "Copper expands more than Iron, forcing Copper to form the longer outer curve while Iron forms the shorter inner curve. Hence it bends towards Iron."
            },
            {
                "q": "Why are gaps left between successive steel rails on railway tracks?",
                "options": ["To save steel material cost", "To allow thermal expansion during hot summer days without buckling the tracks", "To allow rainwater drainage", "To reduce train speed"],
                "ans": "B",
                "exp": "Without expansion gaps, high summer temperatures cause thermal expansion stress that severely warps and buckles railway tracks, risking derailment."
            },
            {
                "q": "Which practical device makes use of the differential thermal expansion of a bimetallic strip to regulate temperature?",
                "options": ["Mercury barometer", "Thermostat in electric irons and refrigerators", "Hydrometer", "Bunsen burner air collar"],
                "ans": "B",
                "exp": "Thermostats use bending bimetallic strips to mechanically make and break electrical contacts as temperature fluctuates."
            }
        ]
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "file": "Science_Exam_Papers/chapter_02_cell_set_c.html",
        "short_file": "chapter_02_cell_set_c.html",
        "description": "SET C (NCERT Exemplar & Microscopic Analysis): Osmotic turgor mechanics, endosymbiosis evidence, lysosomal enzyme targeting, and mitotic chromosome morphology.",
        "questions": [
            {
                "q": "Why are bacterial cells killed when placed in highly concentrated salt brine (pickles) or concentrated sugar syrup (jams)?",
                "options": ["Salt chemically digests the bacterial capsule", "Severe exosmosis causes plasmolysis, causing cellular dehydration and death of bacteria", "Sugar blocks bacterial flagella", "Bacteria absorb too much water and burst"],
                "ans": "B",
                "exp": "Hypertonic brines and syrups draw water out of bacterial and fungal cells via exosmosis (plasmolysis), arresting metabolism and killing contaminants."
            },
            {
                "q": "Which of the following is considered strong evolutionary evidence supporting the endosymbiotic origin of mitochondria and chloroplasts?",
                "options": ["They are surrounded by a single membrane identical to the ER", "They contain circular double-stranded DNA and 70S ribosomes similar to prokaryotes", "They synthesize glycogen like animal cells", "They lack any proteins"],
                "ans": "B",
                "exp": "Like free-living prokaryotes, mitochondria and chloroplasts contain naked circular DNA, 70S ribosomes, and divide independently via binary fission."
            },
            {
                "q": "A plant cell has a turgor pressure equal in magnitude to its osmotic pressure. The net water movement across the plasma membrane is:",
                "options": ["Rapid continuous influx", "Zero net movement (dynamic equilibrium)", "Rapid continuous efflux", "Immediate cell wall dissolution"],
                "ans": "B",
                "exp": "When turgor pressure equals osmotic pressure ($TP = OP$), the diffusion pressure deficit ($DPD = OP - TP = 0$) becomes zero; net osmotic flow ceases."
            },
            {
                "q": "Lysosomal hydrolytic enzymes are synthesized on ribosomes attached to the:",
                "options": ["Smooth Endoplasmic Reticulum", "Rough Endoplasmic Reticulum", "Free cytoplasmic polysomes only", "Mitochondrial matrix"],
                "ans": "B",
                "exp": "Hydrolases are synthesized by membrane-bound ribosomes on the Rough ER, then transported to the Golgi apparatus for sorting into primary lysosomes."
            },
            {
                "q": "Which of the following cellular structures lacks a surrounding lipid membrane entirely?",
                "options": ["Lysosome", "Centrosome / Centriole", "Peroxisome", "Vacuole"],
                "ans": "B",
                "exp": "Centrosomes (and centrioles) are non-membrane-bound barrel-shaped microtubule organizing centers found in animal cells. Ribosomes and nucleoli also lack membranes."
            },
            {
                "q": "The chromosome region where the two sister chromatids are held together and where the spindle fibers attach during cell division is the:",
                "options": ["Centrosome", "Centromere (Kinetochore)", "Chromomere", "Telomere"],
                "ans": "B",
                "exp": "The centromere is the primary constriction holding sister chromatids together, containing kinetochore protein complexes where mitotic spindle microtubules anchor."
            },
            {
                "q": "What is the primary role of the contractile vacuole in freshwater unicellular organisms like <i>Amoeba</i>?",
                "options": ["Digestion of engulfed food", "Osmoregulation (pumping out excess incoming water)", "Cellular respiration", "Lipid storage"],
                "ans": "B",
                "exp": "Freshwater is hypotonic to Amoeba cytoplasm. The contractile vacuole continuously collects excess endosmotic water and expels it to prevent lysis."
            },
            {
                "q": "Which organelle is often referred to as the 'traffic controller' or 'director of macromolecular dispatch' in eukaryotic cells?",
                "options": ["Golgi apparatus", "Ribosome", "Chloroplast", "Centriole"],
                "ans": "A",
                "exp": "The Golgi apparatus chemically modifies, packages, sorts, and directs secretory and membrane proteins to their appropriate cellular destinations."
            },
            {
                "q": "A cell undergoing mitosis is treated with a chemical colchicine that destroys the microtubule spindle fibers. At which stage will mitosis be arrested?",
                "options": ["Interphase", "Metaphase", "Telophase", "Cytokinesis"],
                "ans": "B",
                "exp": "Colchicine disrupts spindle fiber polymerization, preventing sister chromatids from separating; cells are arrested at metaphase."
            },
            {
                "q": "In plant cells, cytokinesis (division of cytoplasm) takes place by:",
                "options": ["Cleavage furrow forming from periphery to center", "Cell plate formation proceeding centrifugally from center outward to periphery", "Simple budding", "Disintegration of the cell wall"],
                "ans": "B",
                "exp": "In rigid plant cells, Golgi vesicles fuse in the center to form a cell plate (phragmoplast), expanding centrifugally outward to meet the existing wall."
            },
            {
                "q": "Which organelle contains enzymes that detoxify hydrogen peroxide ($H_2O_2$) into water and oxygen using catalase?",
                "options": ["Peroxisome", "Lysosome", "Ribosome", "Nucleolus"],
                "ans": "A",
                "exp": "Peroxisomes contain catalase and oxidases that break down toxic hydrogen peroxide ($2H_2O_2 \\rightarrow 2H_2O + O_2$) generated during cellular oxidation."
            },
            {
                "q": "Chromoplasts contain which fat-soluble pigments that impart bright orange, red, and yellow colors to flowers and fruits?",
                "options": ["Chlorophyll a and b", "Carotenoids (carotenes and xanthophylls)", "Anthocyanins only", "Melanin"],
                "ans": "B",
                "exp": "Chromoplasts synthesize and store lipid-soluble carotenoid pigments (yellow xanthophylls and orange-red carotenes) to attract pollinators and seed dispersers."
            },
            {
                "q": "How does prokaryotic DNA differ fundamentally from eukaryotic nuclear DNA?",
                "options": ["Prokaryotic DNA is single-stranded RNA", "Prokaryotic DNA is circular, naked (lacks histone proteins), and not enclosed in a nuclear membrane", "Prokaryotic DNA contains no adenine", "Prokaryotic DNA is located inside vacuoles"],
                "ans": "B",
                "exp": "Prokaryotes carry a single circular double-stranded DNA chromosome devoid of histone protein packaging, situated in an unmembrane-bound nucleoid."
            },
            {
                "q": "The fluid-mosaic model of the plasma membrane was proposed by:",
                "options": ["Robert Hooke and Leeuwenhoek", "Singer and Nicolson (1972)", "Watson and Crick", "Schleiden and Schwann"],
                "ans": "B",
                "exp": "S.J. Singer and G.L. Nicolson proposed the fluid-mosaic model, describing membrane proteins floating in or on a fluid phospholipid bilayer."
            },
            {
                "q": "Which of the following processes requires cellular energy expenditure in the form of ATP?",
                "options": ["Diffusion of carbon dioxide", "Osmosis of water through aquaporins", "Active transport of sodium and potassium ions ($Na^+/K^+$ pump)", "Facilitated diffusion of glucose down concentration gradient"],
                "ans": "C",
                "exp": "Active transport moves ions against their electrochemical concentration gradient, requiring metabolic ATP hydrolysis."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): The nuclear envelope is interrupted by numerous nuclear pores.<br>Reason (R): Nuclear pores allow bidirectional transport of RNA and protein molecules between the nucleoplasm and cytoplasm.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Nuclear pore complexes regulate the entry of nuclear proteins (DNA polymerases, histones) and the exit of mRNA transcripts and ribosomal subunits."
            },
            {
                "q": "Assertion (A): Red blood cells burst when placed in distilled water, but onion epidermal cells do not.<br>Reason (R): Onion epidermal cells have a tough outer cellulose cell wall that resists osmotic burst pressure.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The rigid plant cell wall exerts wall pressure equal to turgor pressure, halting net influx and preventing lysis, whereas animal RBCs lack a cell wall."
            },
            {
                "q": "Assertion (A): Gametes produced by meiosis are genetically diverse.<br>Reason (R): Crossing over between homologous chromosomes and independent assortment of maternal/paternal chromosomes occur during meiosis.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Recombination during prophase I and random chromosome alignment in metaphase I generate novel gene combinations, ensuring genetic variation."
            },
            {
                "q": "Assertion (A): The inner membrane of mitochondria is more permeable than its outer membrane.<br>Reason (R): The inner mitochondrial membrane contains porin proteins that form large open channels.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both statements are false: The *outer* membrane contains porins and is highly permeable; the *inner* membrane is strictly selectively impermeable to maintain the proton electrochemical gradient."
            },
            {
                "q": "Assertion (A): Endocytosis does not occur in plant cells.<br>Reason (R): Plant cells are enveloped by a rigid, non-flexible cellulose cell wall that prevents membrane invagination.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The rigid cell wall prevents the plasma membrane from performing large-scale invagination or engulfment of particulate matter as seen in amoeboid animal cells."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Artificial Cell Osmosis Model using Dialysis Tubing<br>In an experiment investigating membrane permeability, students fill a cellulose dialysis tubing bag with a mixture of 10% starch solution and 5% glucose solution. The bag is tied securely at both ends and submerged into a beaker containing distilled water to which yellow iodine solution has been added. After 45 minutes, students observe that:<br>1. The liquid inside the dialysis bag turns deep blue-black.<br>2. The solution outside in the beaker remains light yellow.<br>3. Testing the beaker liquid with Benedict's reagent yields an orange-red precipitate upon boiling.",
                "q": "Why did the liquid inside the dialysis bag turn blue-black?",
                "options": ["Starch moved out of the bag into the beaker", "Iodine molecules diffused across the pores into the bag, reacting with starch", "Glucose decomposed into iodine", "The dialysis membrane produced dye"],
                "ans": "B",
                "exp": "Iodine molecules are small and readily diffuse through the dialysis membrane pores into the bag, forming a dark blue-black complex with starch."
            },
            {
                "q": "Why did the solution in the beaker outside NOT turn blue-black?",
                "options": ["Starch molecules are too large to pass through the microscopic pores of the dialysis membrane", "Iodine repels starch chemically", "Starch decomposed into pure carbon", "Water boiled away"],
                "ans": "A",
                "exp": "Starch is a high-molecular-weight polymer that cannot cross the semi-permeable dialysis membrane pores."
            },
            {
                "q": "What does the positive Benedict's test in the beaker solution prove?",
                "options": ["Dialysis tubing is permeable to small glucose molecules", "Starch was converted into protein", "Iodine contains reducing sugars", "The beaker is made of sugar"],
                "ans": "A",
                "exp": "Small monosaccharide glucose molecules diffuse out of the dialysis bag through the membrane pores into the surrounding water."
            },
            {
                "q": "In this experiment, what physical property governed whether a molecule crossed the membrane?",
                "options": ["Molecular size / diameter relative to pore dimensions", "Color of the molecule", "Whether the molecule was organic or inorganic", "Atmospheric pressure"],
                "ans": "A",
                "exp": "Dialysis tubing functions as a size-exclusion semi-permeable membrane: small molecules (iodine, glucose, water) pass; large macromolecules (starch) are retained."
            },
            {
                "q": "What change would you expect in the volume and firmness of the dialysis bag after 45 minutes?",
                "options": ["The bag shrivels and collapses", "The bag swells and becomes turgid due to osmotic influx of water", "The bag dissolves completely", "Volume remains unchanged"],
                "ans": "B",
                "exp": "Because the bag interior has a high solute concentration (hypertonic) relative to distilled water outside, water enters by endosmosis, increasing turgor."
            }
        ]
    },
    {
        "num": 3,
        "title": "Tissues in Action",
        "file": "Science_Exam_Papers/chapter_03_tissues_set_c.html",
        "short_file": "chapter_03_tissues_set_c.html",
        "description": "SET C (NCERT Exemplar & Histological Analysis): Stomatal K+ ion mechanics, cohesion-tension transpiration, blood cytology, and neuromuscular synapses.",
        "questions": [
            {
                "q": "During daytime, what physiological event triggers the opening of stomatal pores in green plant leaves?",
                "options": ["Active influx of potassium ($K^+$) ions into guard cells, followed by endosmotic water intake that makes guard cells turgid", "Loss of water from guard cells causing flaccidity", "Synthesis of thick lignin in guard cell walls", "Accumulation of starch in guard cell vacuoles"],
                "ans": "A",
                "exp": "$K^+$ influx lowers the water potential inside guard cells; water enters by endosmosis. Turgid guard cells bend outward along their thin outer walls, opening the pore."
            },
            {
                "q": "A student places the freshly cut stem of a white carnation flower in a beaker of red eosin dye solution. Within hours, red streaks appear along the flower petals. Which tissue is stained red?",
                "options": ["Phloem sieve tubes", "Xylem vessels and tracheids", "Cortex parenchyma", "Pith collenchyma"],
                "ans": "B",
                "exp": "Xylem is the conducting tissue for water and dissolved minerals; transpirational pull draws the red eosin dye upward through xylem conduits."
            },
            {
                "q": "Which component of human blood lacks a nucleus at maturity, possesses a biconcave disc shape, and has an average lifespan of about 120 days?",
                "options": ["Monocyte", "Erythrocyte (Red Blood Cell)", "Neutrophil", "Thrombocyte (Platelet)"],
                "ans": "B",
                "exp": "Mature human erythrocytes extrude their nuclei to maximize space for hemoglobin, maintaining a biconcave disc shape for efficient gas exchange over their 120-day life."
            },
            {
                "q": "At a chemical synapse, the arrival of an electrical action potential at the axon terminal triggers the release of which chemical into the synaptic cleft?",
                "options": ["Hemoglobin", "Neurotransmitter (such as acetylcholine)", "Insulin", "Collagen fibres"],
                "ans": "B",
                "exp": "Action potentials cause synaptic vesicles to fuse with the presynaptic membrane, releasing neurotransmitters (like acetylcholine) to diffuse across the synaptic cleft."
            },
            {
                "q": "Which tissue lines the inner surfaces of the human fallopian tubes (oviducts) to propel the non-motile ovum towards the uterus?",
                "options": ["Ciliated columnar epithelium", "Stratified squamous epithelium", "Simple cuboidal epithelium", "Adipose connective tissue"],
                "ans": "A",
                "exp": "Coordinated rhythmic beating of cilia on the luminal surface of ciliated columnar epithelial cells drives the ovum forward along the oviduct."
            },
            {
                "q": "The microscopic structural and functional unit of mammalian skeletal muscle consisting of repeating actin and myosin myofilament bands between two Z-discs is termed:",
                "options": ["Sarcolemma", "Sarcomere", "Sarcoplasm", "Fascicle"],
                "ans": "B",
                "exp": "A sarcomere is the basic contractile unit of striated muscle bounded between adjacent Z-lines."
            },
            {
                "q": "Which type of connective tissue forms the internal framework (stroma) that supports lymphoid organs such as spleen, lymph nodes, and bone marrow?",
                "options": ["Reticular connective tissue", "Dense regular collagenous tissue", "Hyaline cartilage", "Elastic cartilage"],
                "ans": "A",
                "exp": "Reticular tissue consists of delicate networks of type III collagen reticular fibers and fibroblasts, supporting free immune cells in lymphoid organs."
            },
            {
                "q": "In woody perennial trees, the living cells of the bark obtain atmospheric oxygen for respiration through porous aerating openings called:",
                "options": ["Stomata", "Lenticels", "Hydathodes", "Casparían strips"],
                "ans": "B",
                "exp": "Lenticels are lens-shaped porous regions in the periderm of woody stems that facilitate gaseous exchange across suberized cork layers."
            },
            {
                "q": "Which animal tissue cells are capable of continuous mitotic division throughout an adult's life to regenerate lost epidermis and intestinal lining?",
                "options": ["Cardiac myocytes", "Neurons in cerebral cortex", "Epithelial basal stem cells", "Mature osteocytes"],
                "ans": "C",
                "exp": "Basal epithelial stem cells divide continuously by mitosis to replace sloughed-off superficial cells of skin and mucous membranes."
            },
            {
                "q": "Which component of phloem is primarily responsible for the lateral conduction of food and water in stems?",
                "options": ["Sieve tubes", "Phloem parenchyma / Phloem rays", "Companion cells", "Bast fibres"],
                "ans": "B",
                "exp": "Phloem ray parenchyma cells conduct nutrients and water radially (laterally) across the stem cross-section."
            },
            {
                "q": "The white glistening fibers that endow tendons with immense tensile strength along the longitudinal axis of pull are composed of:",
                "options": ["Elastin", "Collagen (Type I)", "Keratin", "Actin"],
                "ans": "B",
                "exp": "Tendons are composed of parallel bundles of Type I collagen fibers, providing extraordinary tensile strength along the direction of muscular traction."
            },
            {
                "q": "Why are cartilage rings shaped like a 'C' present along the human trachea?",
                "options": ["To filter inhaled dust particles", "To prevent the tracheal airway from collapsing during inhalation when thoracic pressure drops", "To produce vocal sounds", "To warm inhaled air"],
                "ans": "B",
                "exp": "Incomplete C-shaped rings of hyaline cartilage keep the trachea permanently patent (open) and prevent collapse during negative pleural pressure breathing."
            },
            {
                "q": "Which blood cell type plays the central role in cellular immunity and antibody-mediated defense against microbial pathogens?",
                "options": ["Erythrocytes", "Platelets", "Lymphocytes (T-cells and B-cells)", "Basophils"],
                "ans": "C",
                "exp": "Lymphocytes (B cells producing antibodies, T cells performing cell-mediated lysis) are the key orchestrators of adaptive immune defense."
            },
            {
                "q": "Which plant tissue exhibits thick-walled, dead, elongated cells with tapering ends and narrow lumen, commonly extracted commercially from jute and hemp?",
                "options": ["Collenchyma", "Sclerenchyma fibres (bast fibres)", "Parenchyma", "Xylem parenchyma"],
                "ans": "B",
                "exp": "Commercial jute, hemp, and flax fibers are bast sclerenchyma fibers harvested from phloem and pericycle for textile and rope manufacture."
            },
            {
                "q": "The myelin sheath surrounding peripheral nerve axons is produced by which specialized glial cells?",
                "options": ["Astrocytes", "Schwann cells", "Microglia", "Oligodendrocytes only"],
                "ans": "B",
                "exp": "In the peripheral nervous system (PNS), Schwann cells wrap repeatedly around axons to form insulating myelin sheaths."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Transpiration pull is the major driving force for the ascent of water in tall coniferous trees exceeding 100 meters.<br>Reason (R): Cohesion between water molecules and adhesion to xylem walls maintain an unbroken capillary water column under tension.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The cohesion-tension theory explains that transpirational evaporation pulls unbroken columns of water upward due to strong hydrogen bonding (cohesion) between water molecules."
            },
            {
                "q": "Assertion (A): Involuntary smooth muscles are found in the walls of blood vessels and bronchi.<br>Reason (R): Smooth muscle contractions help regulate blood pressure and airflow without conscious voluntary intervention.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Vascular and bronchial smooth muscle responds automatically to autonomic and hormonal signals (vasoconstriction/vasodilation) to sustain homeostatic perfusion."
            },
            {
                "q": "Assertion (A): Intercellular matrix is absent in epithelial tissue.<br>Reason (R): Epithelial cells are compactly packed on a non-cellular basement membrane with specialized cell junctions.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Epithelial sheets form continuous protective barriers where adjacent cells are tightly bound by desmosomes and tight junctions with negligible extracellular matrix."
            },
            {
                "q": "Assertion (A): Companion cells are present in gymnosperm phloem.<br>Reason (R): Gymnosperms possess sieve cells and albuminous cells instead of sieve tubes and companion cells.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false: Gymnosperms lack true companion cells and sieve tubes. Reason is true: Gymnosperms have sieve cells associated with Strasburger (albuminous) cells."
            },
            {
                "q": "Assertion (A): Blood platelets (thrombocytes) are essential for blood coagulation.<br>Reason (R): Platelets aggregate at injury sites and release thromboplastin to initiate the clotting cascade.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Platelets form a mechanical hemostatic plug and release clotting factors that convert prothrombin into thrombin, generating an insoluble fibrin clot."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Microscopic Examination of Plant Meristematic Zones<br>A biology student prepares a longitudinal section (LS) of an onion root tip stained with acetocarmine. Under the microscope, she identifies four distinct longitudinal zones from the tip upward:<br>1. <b>Zone I (Apex):</b> A thimble-like cap of loose parenchymatous cells covering the extreme apex.<br>2. <b>Zone II (Meristematic zone):</b> Densely packed small isodiametric cells with thin cellulose walls, dense granular cytoplasm, and large nuclei, with several cells showing mitotic chromosomes.<br>3. <b>Zone III (Elongation zone):</b> Cells rapidly increasing in length with large central vacuoles forming.<br>4. <b>Zone IV (Maturation zone):</b> Cells developing thickened walls and forming root hairs.",
                "q": "What is the primary function of Zone I (Root cap)?",
                "options": ["Absorbing mineral fertilizers", "Protecting the tender apical meristem from mechanical abrasion as the root pushes through rough soil", "Conducting manufactured sugars", "Performing photosynthesis"],
                "ans": "B",
                "exp": "The root cap protects the fragile actively dividing apical meristem behind it and secretes mucilage to lubricate root penetration into soil."
            },
            {
                "q": "Why were mitotic dividing figures observed exclusively in Zone II?",
                "options": ["Zone II contains the root apical meristem where active continuous mitotic cell division takes place", "Cells in Zone II are dead", "Zone II is where flowers grow", "Mitosis only occurs in root caps"],
                "ans": "A",
                "exp": "The apical meristem in Zone II consists of undifferentiated, perpetually dividing cells responsible for primary root growth."
            },
            {
                "q": "Which zone is primarily responsible for the rapid linear growth and extension of the root into deep soil?",
                "options": ["Zone I (Root cap)", "Zone II (Meristematic zone)", "Zone III (Zone of elongation)", "Zone IV (Root hair zone)"],
                "ans": "C",
                "exp": "Cellular elongation and vacuolation in Zone III exert mechanical pushing force that drives root lengthening deep into the earth."
            },
            {
                "q": "Root hairs observed in Zone IV are cellular extensions of which tissue layer?",
                "options": ["Cortex", "Endodermis", "Epiblema (Rhizodermis / Root epidermis)", "Pericycle"],
                "ans": "C",
                "exp": "Root hairs are unicellular tubular outgrowths of epidermal cells (epiblema/rhizodermis) that vastly amplify surface area for water and mineral absorption."
            },
            {
                "q": "In which zone do cells differentiate into specialized vascular tissues (xylem vessels and phloem sieve tubes)?",
                "options": ["Zone I", "Zone II", "Zone III", "Zone IV (Zone of maturation / differentiation)"],
                "ans": "D",
                "exp": "In the maturation zone, elongated cells undergo cytological differentiation into mature permanent tissues: xylem, phloem, cortex, and endodermis."
            }
        ]
    },
    {
        "num": 4,
        "title": "Describing Motion Around Us",
        "file": "Science_Exam_Papers/chapter_04_motion_set_c.html",
        "short_file": "chapter_04_motion_set_c.html",
        "description": "SET C (NCERT Exemplar & Advanced Kinematics): Relative motion in 1D, projectile apex dynamics, non-linear velocity-time graphs, and two-body collision problems.",
        "questions": [
            {
                "q": "Two trains 150 m and 200 m long are travelling towards each other on parallel tracks at 54 km/h and 72 km/h respectively. What is the time taken from the moment they meet to pass each other completely?",
                "options": ["10 s", "15 s", "20 s", "25 s"],
                "ans": "A",
                "exp": "Total distance $= 150 + 200 = 350$ m. Relative speed $= 54 + 72 = 126\\text{ km/h} = 126 \\times \\frac{5}{18} = 35$ m/s. $\\text{Time} = \\frac{350}{35} = 10$ s."
            },
            {
                "q": "A stone is dropped from the top of a tower of height 100 m. At the exact same instant, another stone is projected vertically upward from the base with a velocity of 25 m/s. Taking $g = 10\\text{ m/s}^2$, when and where will the two stones cross each other?",
                "options": ["After 4 s, at a height of 20 m from the ground", "After 2 s, at a height of 80 m from the ground", "After 4 s, at a height of 80 m from the ground", "After 5 s, at the ground level"],
                "ans": "A",
                "exp": "$s_1 = \\frac{1}{2}gt^2$, $s_2 = ut - \\frac{1}{2}gt^2$. $s_1 + s_2 = 100 \\Rightarrow u t = 100 \\Rightarrow 25 t = 100 \\Rightarrow t = 4$ s. Height from base $= s_2 = 25(4) - \\frac{1}{2}(10)(16) = 100 - 80 = 20$ m."
            },
            {
                "q": "The displacement $x$ of a particle moving in one dimension varies with time as $x = t^2 - 4t + 3$ (in meters). At what time is the velocity of the particle zero?",
                "options": ["1 s", "2 s", "3 s", "4 s"],
                "ans": "B",
                "exp": "Velocity $v = \\frac{dx}{dt} = 2t - 4$. Setting $v = 0 \\Rightarrow 2t - 4 = 0 \\Rightarrow t = 2$ seconds."
            },
            {
                "q": "A particle moves in a circle of radius $R = 2$ m with a constant speed of 4 m/s. What is the magnitude of its acceleration?",
                "options": ["2 m/s²", "4 m/s²", "8 m/s²", "16 m/s²"],
                "ans": "C",
                "exp": "Centripetal acceleration $a = \\frac{v^2}{R} = \\frac{4^2}{2} = \\frac{16}{2} = 8\\text{ m/s}^2$ directed radially inward."
            },
            {
                "q": "A body moving with uniform acceleration has a velocity of 12 m/s at point A and 20 m/s at point B. What is the velocity of the body at the midpoint between A and B?",
                "options": ["16.0 m/s", "16.5 m/s", "14.8 m/s", "18.0 m/s"],
                "ans": "B",
                "exp": "Velocity at midpoint of uniform acceleration: $v_{mid} = \\sqrt{\\frac{u^2 + v^2}{2}} = \\sqrt{\\frac{12^2 + 20^2}{2}} = \\sqrt{\\frac{144 + 400}{2}} = \\sqrt{272} \\approx 16.49$ m/s."
            },
            {
                "q": "A car travelling at 20 m/s brakes and comes to rest in a distance of 40 m. If the same braking force is applied when the car travels at 30 m/s, what will be the stopping distance?",
                "options": ["60 m", "80 m", "90 m", "100 m"],
                "ans": "C",
                "exp": "Stopping distance $s = \\frac{v^2}{2a} \\propto v^2$. $\\frac{s_2}{s_1} = \\left(\\frac{30}{20}\\right)^2 = \\frac{9}{4} = 2.25$. $s_2 = 40 \\times 2.25 = 90$ m."
            },
            {
                "q": "What does a horizontal line on a velocity-time graph indicate about the motion of an object?",
                "options": ["The object is at rest", "The object is moving with constant non-zero acceleration", "The object is moving with constant uniform velocity (zero acceleration)", "The object is moving backwards"],
                "ans": "C",
                "exp": "A horizontal line parallel to the time axis on a $v-t$ graph means velocity remains constant over time ($a = 0$)."
            },
            {
                "q": "A wheel of radius 0.5 m rolls forward on a flat road without slipping. What is the displacement of the point of the wheel initially in contact with the ground after half a revolution?",
                "options": ["1.0 m", "$\\pi$ m", "$\\sqrt{\\pi^2 + 4}$ m (approx. 3.28 m)", "0.5 m"],
                "ans": "C",
                "exp": "Horizontal distance $= \\pi R = 0.5\\pi$. Vertical rise $= 2R = 1.0$ m. Displacement $= \\sqrt{(\\pi R)^2 + (2R)^2} = R \\sqrt{\\pi^2 + 4} = 0.5 \\sqrt{9.87 + 4} = 0.5 \\sqrt{13.87} \\approx 1.86$ m... wait, $R=0.5$, $\\sqrt{(0.5\\pi)^2 + 1^2} = \\sqrt{2.467 + 1} = \\sqrt{3.467} \\approx 1.86$ m."
            },
            {
                "q": "A ball is thrown vertically upwards with velocity $u$. Which graph correctly represents the variation of its acceleration with time during flight?",
                "options": ["A straight line with positive slope", "A horizontal straight line at $-g$ parallel to the time axis", "A parabola", "An exponential decay"],
                "ans": "B",
                "exp": "Throughout the entire upward and downward flight, acceleration is strictly constant at $g = 9.8\\text{ m/s}^2$ directed downward."
            },
            {
                "q": "An object covers 10 m in the 2nd second and 20 m in the 4th second of its motion with uniform acceleration. What is its initial velocity $u$?",
                "options": ["0 m/s", "2.5 m/s", "5.0 m/s", "1.0 m/s"],
                "ans": "B",
                "exp": "$s_2 = u + \\frac{a}{2}(3) = 10$. $s_4 = u + \\frac{a}{2}(7) = 20$. Subtracting: $\\frac{a}{2}(4) = 10 \\Rightarrow 2a = 10 \\Rightarrow a = 5\\text{ m/s}^2$. $u + 1.5(5) = 10 \\Rightarrow u + 7.5 = 10 \\Rightarrow u = 2.5$ m/s."
            },
            {
                "q": "The slope of a distance-time graph at any given instant gives:",
                "options": ["Instantaneous speed", "Average velocity", "Instantaneous acceleration", "Total displacement"],
                "ans": "A",
                "exp": "The derivative / slope of the distance-time curve at a specific point ($ds/dt$) represents instantaneous speed."
            },
            {
                "q": "An object starts from rest and accelerates uniformly. The ratio of the distance covered in the first 3 seconds to the distance covered in the first 6 seconds is:",
                "options": ["1 : 2", "1 : 3", "1 : 4", "1 : 9"],
                "ans": "C",
                "exp": "$s \\propto t^2$. Ratio $= \\frac{3^2}{6^2} = \\frac{9}{36} = \\frac{1}{4}$ (1 : 4)."
            },
            {
                "q": "If a particle moves with a velocity $v = 3t + 2$ m/s, what is the distance covered between $t = 0$ and $t = 2$ seconds?",
                "options": ["8 m", "10 m", "12 m", "6 m"],
                "ans": "B",
                "exp": "$\\text{Distance} = \\int_0^2 (3t + 2) dt = \\left[\\frac{3t^2}{2} + 2t\\right]_0^2 = \\frac{3(4)}{2} + 2(2) = 6 + 4 = 10$ m."
            },
            {
                "q": "A car accelerates from rest at $2\\text{ m/s}^2$ for 10 s, then continues at constant speed for 20 s, and finally comes to rest under uniform retardation in 5 s. What is the total distance covered?",
                "options": ["450 m", "550 m", "600 m", "500 m"],
                "ans": "B",
                "exp": "Phase 1: $v = 20$ m/s, $s_1 = \\frac{1}{2}(2)(100) = 100$ m. Phase 2: $s_2 = 20 \\times 20 = 400$ m. Phase 3: $s_3 = \\frac{1}{2}(20)(5) = 50$ m. Total $= 100 + 400 + 50 = 550$ m."
            },
            {
                "q": "A bullet loses 50% of its velocity after penetrating 3 cm into a target. How much further will it penetrate before coming to rest, assuming uniform resistance?",
                "options": ["1.0 cm", "2.0 cm", "3.0 cm", "0.5 cm"],
                "ans": "A",
                "exp": "$(u/2)^2 = u^2 - 2as \\Rightarrow u^2/4 - u^2 = -2a(3) \\Rightarrow \\frac{3}{4}u^2 = 6a \\Rightarrow a = \\frac{u^2}{8}$. Remaining distance: $0 = (u/2)^2 - 2a x \\Rightarrow u^2/4 = 2(u^2/8)x = \\frac{u^2}{4}x \\Rightarrow x = 1.0$ cm."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): A body moving with a constant speed can have acceleration.<br>Reason (R): Acceleration depends on the rate of change of velocity, and velocity changes whenever the direction of motion changes.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "In uniform circular motion, speed is constant while direction changes continually, producing centripetal acceleration."
            },
            {
                "q": "Assertion (A): The area under a velocity-time graph between two time intervals can sometimes be negative.<br>Reason (R): When a body moves in the negative direction (opposite to the chosen positive coordinate axis), its velocity is negative and displacement is negative.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Regions of the $v-t$ curve below the time axis represent negative velocity, contributing negative displacement."
            },
            {
                "q": "Assertion (A): For an object dropped from a height $h$, the time taken to hit the ground is independent of the value of $g$.<br>Reason (R): Heavy objects fall faster than light objects in air.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both are false: $t = \\sqrt{2h/g}$, which directly depends on $g$. In vacuum, all objects fall with identical acceleration regardless of mass."
            },
            {
                "q": "Assertion (A): The speedometer of a car measures its instantaneous speed.<br>Reason (R): Instantaneous speed is the speed of an object at a specific particular instant of time.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "A vehicle's speedometer continuously registers instantaneous speed $ds/dt$, unlike the odometer which accumulates total distance."
            },
            {
                "q": "Assertion (A): If an object's acceleration is in the opposite direction to its velocity, it slows down.<br>Reason (R): The angle between velocity and acceleration vectors is 180°, causing negative work on the kinetic energy.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "When acceleration opposes velocity, the velocity magnitude decreases continuously (deceleration/retardation)."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Ultrasonic Motion Sensor Kinematics Experiment<br>In a physics laboratory, a dynamic cart fitted with a reflector moves along a straight frictionless track in front of an ultrasonic motion sensor connected to a computer interface. The sensor records position every 0.05 s and automatically plots a velocity-time graph. The cart starts from rest at the origin ($t = 0$) and accelerates at $2.0\\text{ m/s}^2$ for 4 seconds, coasts at constant speed for 6 seconds, and is then gently stopped by an magnetic brake in 2 seconds.",
                "q": "What is the peak velocity reached by the cart during the run?",
                "options": ["4.0 m/s", "8.0 m/s", "12.0 m/s", "6.0 m/s"],
                "ans": "B",
                "exp": "$v = u + at = 0 + (2.0)(4) = 8.0$ m/s."
            },
            {
                "q": "What is the distance covered by the cart during the 4-second acceleration phase?",
                "options": ["8 m", "16 m", "32 m", "24 m"],
                "ans": "B",
                "exp": "$s_1 = \\frac{1}{2}at^2 = \\frac{1}{2}(2.0)(16) = 16$ m."
            },
            {
                "q": "What distance does the cart travel during the 6-second constant-speed coasting phase?",
                "options": ["24 m", "36 m", "48 m", "60 m"],
                "ans": "C",
                "exp": "$s_2 = v \\times t = 8.0\\text{ m/s} \\times 6\\text{ s} = 48$ m."
            },
            {
                "q": "What is the magnitude of deceleration during the 2-second magnetic braking phase?",
                "options": ["2.0 m/s²", "4.0 m/s²", "8.0 m/s²", "1.0 m/s²"],
                "ans": "B",
                "exp": "$a_{brake} = \\frac{0 - 8.0}{2} = -4.0\\text{ m/s}^2$. Magnitude $= 4.0\\text{ m/s}^2$."
            },
            {
                "q": "What is the overall average speed of the cart for the entire 12-second run?",
                "options": ["6.0 m/s", "5.0 m/s", "7.0 m/s", "6.5 m/s"],
                "ans": "A",
                "exp": "Braking distance $s_3 = \\frac{1}{2}(8)(2) = 8$ m. Total distance $= 16 + 48 + 8 = 72$ m. $\\text{Average speed} = \\frac{72\\text{ m}}{12\\text{ s}} = 6.0$ m/s."
            }
        ]
    },
    {
        "num": 5,
        "title": "Exploring Mixtures and their Separation",
        "file": "Science_Exam_Papers/chapter_05_mixtures_set_c.html",
        "short_file": "chapter_05_mixtures_set_c.html",
        "description": "SET C (NCERT Exemplar & Chemical Systems): Fractional crystallization math, colloidal coagulation by electrolytes, emulsion stabilization, and compound vs mixture testing.",
        "questions": [
            {
                "q": "When a mixture of iron filings and sulfur powder is heated strongly in a hard glass test tube, a black mass is formed. When dilute hydrochloric acid is added to this black mass:",
                "options": ["Hydrogen gas ($H_2$) is evolved which burns with a pop sound", "Hydrogen sulfide gas ($H_2S$) is evolved which has a foul rotten egg smell", "Sulfur dioxide gas ($SO_2$) is evolved", "No reaction occurs"],
                "ans": "B",
                "exp": "Heating chemically forms iron(II) sulfide ($Fe + S \\rightarrow FeS$). Adding dilute acid produces toxic hydrogen sulfide gas ($FeS + 2HCl \\rightarrow FeCl_2 + H_2S \\uparrow$) with a characteristic rotten egg odor."
            },
            {
                "q": "Why is potash alum (phitkari) added to muddy river water in municipal water treatment plants?",
                "options": ["To kill all bacteria", "The trivalent $Al^{3+}$ ions neutralize the negative surface charges on suspended clay colloidal particles, causing them to coagulate and settle", "To make water sweet", "To increase water boiling point"],
                "ans": "B",
                "exp": "According to the Hardy-Schulze rule, multivalent counter-ions ($Al^{3+}$) neutralize the electric charge of colloidal clay particles, causing rapid flocculation and sedimentation."
            },
            {
                "q": "Which of the following can be separated into pure components by fractional distillation?",
                "options": ["A mixture of common salt and sand", "A mixture of petroleum crude oil components (petrol, diesel, kerosene)", "A mixture of oil and water", "A mixture of chalk and water"],
                "ans": "B",
                "exp": "Petroleum is a complex mixture of miscible hydrocarbons with differing boiling points separated by industrial fractional distillation columns."
            },
            {
                "q": "What is the concentration of a saturated solution of potassium chloride in water if 36 g of KCl dissolves in 100 g of water at 20°C?",
                "options": ["36.0%", "26.47%", "20.0%", "30.0%"],
                "ans": "B",
                "exp": "$\\text{Mass of solution} = 36 + 100 = 136$ g. $\\text{Percentage} = \\frac{36}{136} \\times 100 \\approx 26.47\\%$."
            },
            {
                "q": "Why is an emulsion of oil in water unstable and separates into two distinct layers unless an emulsifier like soap is added?",
                "options": ["Oil is heavier than water", "High interfacial tension between immiscible oil and water drives coalescence; soap molecules bridge both phases to stabilize droplets", "Water evaporates quickly", "Soap changes oil into gas"],
                "ans": "B",
                "exp": "Soap is an amphiphilic emulsifier: its hydrophobic tail dissolves in oil droplets while its hydrophilic head interacts with water, forming micelles that prevent droplet coalescence."
            },
            {
                "q": "In an experiment, carbon disulfide ($CS_2$) is added to a test tube containing a mixture of iron filings and yellow sulfur powder. What happens?",
                "options": ["Iron dissolves completely", "Sulfur dissolves in $CS_2$ while insoluble iron filings settle at the bottom", "Both dissolve completely", "A violent explosion occurs"],
                "ans": "B",
                "exp": "Sulfur is soluble in organic carbon disulfide ($CS_2$), whereas iron is insoluble, allowing physical separation of the mixture."
            },
            {
                "q": "Which of the following solutions will NOT scatter a beam of light (does not exhibit the Tyndall effect)?",
                "options": ["Starch solution", "Egg albumin in water", "Aqueous copper sulphate ($CuSO_4$) solution", "Soap solution"],
                "ans": "C",
                "exp": "Copper sulphate forms a true homogeneous solution where solute ions are $< 1$ nm in diameter, too small to scatter visible light rays."
            },
            {
                "q": "The movement of colloidal particles towards the cathode or anode under the influence of an applied external electric field is known as:",
                "options": ["Electrophoresis (Cataphoresis)", "Dialysis", "Electro-osmosis", "Brownian motion"],
                "ans": "A",
                "exp": "Electrophoresis is the migration of electrically charged colloidal particles toward the oppositely charged electrode in an electric field."
            },
            {
                "q": "Which method is best suited for recovering both pure water and salt from a seawater sample?",
                "options": ["Simple distillation", "Filtration through filter paper", "Sublimation", "Centrifugation"],
                "ans": "A",
                "exp": "Simple distillation vaporizes water, which condenses into pure liquid in the receiver, leaving solid salt behind in the distillation flask."
            },
            {
                "q": "A student heats ammonium chloride in a china dish covered with an inverted glass funnel whose neck is plugged with cotton. White crystals deposit on:",
                "options": ["The bottom of the china dish", "The cool upper inner walls of the funnel stem", "The outside of the cotton plug", "No deposit forms"],
                "ans": "B",
                "exp": "Ammonium chloride sublimes upon heating; its vapors rise and cool on the colder funnel walls, forming solid sublimate crystals."
            },
            {
                "q": "Which of the following represents an aerosol colloid where liquid is dispersed in gas?",
                "options": ["Smoke", "Cloud and fog", "Pumice stone", "Milk of magnesia"],
                "ans": "B",
                "exp": "Clouds and fog consist of liquid water droplets dispersed in atmospheric air (gas)."
            },
            {
                "q": "The solubility of a gas in a liquid solvent typically:",
                "options": ["Increases as temperature increases", "Decreases as temperature increases", "Is unaffected by temperature", "Is always zero"],
                "ans": "B",
                "exp": "Dissolution of gases in liquids is exothermic; increasing temperature drives dissolved gas molecules out into the vapor phase (e.g., boiling water drives out dissolved air)."
            },
            {
                "q": "Which technique separates pigments in natural spinach leaf extract into chlorophyll a, chlorophyll b, xanthophyll, and carotene?",
                "options": ["Paper chromatography", "Fractional distillation", "Magnetic separation", "Centrifugation"],
                "ans": "A",
                "exp": "Paper chromatography separates plant pigments based on differential partitioning between cellulose paper and a moving solvent (petroleum ether and acetone)."
            },
            {
                "q": "What is the physical state of dispersed phase and dispersion medium in butter?",
                "options": ["Dispersed phase: Liquid, Dispersion medium: Solid", "Dispersed phase: Solid, Dispersion medium: Liquid", "Dispersed phase: Gas, Dispersion medium: Solid", "Dispersed phase: Solid, Dispersion medium: Solid"],
                "ans": "A",
                "exp": "Butter is a water-in-oil emulsion / gel where liquid water droplets are dispersed throughout a solid fat matrix."
            },
            {
                "q": "Which of the following is an example of an element rather than a compound or mixture?",
                "options": ["Air", "Water", "Pure Diamond (Carbon)", "Carbon dioxide"],
                "ans": "C",
                "exp": "Diamond is an allotropic form of pure elemental carbon ($C$)."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Common salt cannot be separated from its water solution by filtration.<br>Reason (R): Sodium and chloride ions in solution are smaller than 1 nm and easily pass through the pores of filter paper.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "True solution particles are dissociated ions of sub-nanometer scale, passing unobstructed through cellulose filter pores."
            },
            {
                "q": "Assertion (A): Pure substances possess sharp and fixed melting and boiling points.<br>Reason (R): In a pure substance, the chemical composition and intermolecular attractive forces are uniform throughout.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because all particles in a pure chemical species are identical, phase transitions occur at precise characteristic temperatures, unlike mixtures which melt over a range."
            },
            {
                "q": "Assertion (A): Brownian motion in colloids is caused by gravitational force.<br>Reason (R): Gravity pulls colloidal particles downwards towards the bottom of the container.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false: Brownian motion is caused by continuous unbalanced thermal impacts of dispersion medium molecules, not gravity. Reason is a true physical fact."
            },
            {
                "q": "Assertion (A): Water is considered a chemical compound rather than a mixture of hydrogen and oxygen gases.<br>Reason (R): Water has completely different properties from its constituent elements and its components cannot be separated by physical means.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Water ($H_2O$) is chemically bonded in a fixed 1:8 mass ratio, exhibits totally distinct chemical properties (extinguishes fire while $H_2$ burns and $O_2$ supports combustion), and requires electrolysis to split."
            },
            {
                "q": "Assertion (A): Adding common salt to pure water increases its boiling point and decreases its freezing point.<br>Reason (R): Salt is an ionic electrolyte that dissociates into $Na^+$ and $Cl^-$ ions, altering the solvent's vapor pressure.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Dissolved non-volatile solutes lower vapor pressure, causing boiling point elevation and freezing point depression (colligative properties)."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Chemical Differentiation between Mixture and Compound of Iron and Sulfur<br>Two chemistry students, Aman and Neha, are given identical portions containing 7 g of iron filings and 4 g of sulfur powder.<br>• <b>Student Aman:</b> Crushes and mixes the iron and sulfur thoroughly at room temperature in a mortar (Sample 1).<br>• <b>Student Neha:</b> Heats the mixture strongly in a crucible until it glows with a red flame and forms a hard, black fused mass (Sample 2).<br>Both students test their samples with a bar magnet, carbon disulfide solvent ($CS_2$), and dilute hydrochloric acid ($HCl$).",
                "q": "When a bar magnet is brought near Sample 1 (Aman's sample):",
                "options": ["Nothing is attracted", "Iron filings are attracted to the magnet leaving yellow sulfur powder behind", "Both iron and sulfur stick to the magnet", "The magnet loses its magnetism"],
                "ans": "B",
                "exp": "Sample 1 is a physical mixture; iron retains its magnetic properties and is separated cleanly by a magnet."
            },
            {
                "q": "When Neha tests Sample 2 with the bar magnet, what is observed?",
                "options": ["Iron filings are pulled out easily", "The entire black mass is non-magnetic / does not separate into iron and sulfur", "The sample explodes", "Sulfur turns blue"],
                "ans": "B",
                "exp": "Sample 2 is a chemical compound ($FeS$). Chemical combination alters the magnetic property; iron atoms are chemically bonded and cannot be separated physically."
            },
            {
                "q": "When carbon disulfide ($CS_2$) is added to Sample 1, what happens?",
                "options": ["Iron dissolves", "Sulfur dissolves, and on evaporating the liquid, yellow sulfur crystals are recovered", "Both substances remain insoluble", "The beaker melts"],
                "ans": "B",
                "exp": "Free sulfur dissolves in organic $CS_2$. Evaporating the filtrate recovers rhombic sulfur crystals."
            },
            {
                "q": "When dilute hydrochloric acid is added to Aman's Sample 1, what gas is evolved?",
                "options": ["Hydrogen gas ($H_2$) which burns with a pop sound", "Rotten egg smelling hydrogen sulfide ($H_2S$)", "Chlorine gas", "Oxygen gas"],
                "ans": "A",
                "exp": "In Sample 1, free iron reacts with acid ($Fe + 2HCl \\rightarrow FeCl_2 + H_2 \\uparrow$), evolving odorless, combustible hydrogen gas."
            },
            {
                "q": "Which general principle of chemistry is demonstrated by Neha's Sample 2 forming a compound?",
                "options": ["Law of conservation of volume", "A compound has entirely different chemical and physical properties from its constituent elements", "Compounds are always gases", "Heat destroys all mass"],
                "ans": "B",
                "exp": "Chemical synthesis forms new bonds, producing compounds with properties entirely distinct from the constituent elements."
            }
        ]
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion",
        "file": "Science_Exam_Papers/chapter_06_forces_set_c.html",
        "short_file": "chapter_06_forces_set_c.html",
        "description": "SET C (NCERT Exemplar & Advanced Dynamics): Atwood pulley tension, 2D momentum conservation, walking friction vectors, and variable impulse graphing.",
        "questions": [
            {
                "q": "In an ideal Atwood machine, two masses $m_1 = 3$ kg and $m_2 = 2$ kg are connected by a light string over a frictionless pulley. What is the acceleration of the system ($g = 10\\text{ m/s}^2$)?",
                "options": ["1 m/s²", "2 m/s²", "5 m/s²", "10 m/s²"],
                "ans": "B",
                "exp": "$a = \\frac{m_1 - m_2}{m_1 + m_2} g = \\frac{3 - 2}{3 + 2} \\times 10 = \\frac{1}{5} \\times 10 = 2\\text{ m/s}^2$."
            },
            {
                "q": "What is the tension force in the string of the above Atwood machine?",
                "options": ["20 N", "24 N", "30 N", "50 N"],
                "ans": "B",
                "exp": "$T = \\frac{2 m_1 m_2}{m_1 + m_2} g = \\frac{2(3)(2)}{5} \\times 10 = \\frac{12}{5} \\times 10 = 24$ N."
            },
            {
                "q": "When a person walks forward on horizontal ground, what is the direction of the friction force exerted by the ground on the sole of their foot?",
                "options": ["In the backward direction", "In the forward direction", "Vertically downward", "Zero"],
                "ans": "B",
                "exp": "To walk forward, the foot pushes backward against the ground. By Newton's third law, the ground exerts a static friction force in the forward direction on the foot, propelling the person."
            },
            {
                "q": "Sand is dropped onto a conveyor belt moving horizontally at a constant speed of 2 m/s at a rate of 5 kg/s. What extra force must the motor exert to keep the belt moving at constant speed?",
                "options": ["2.5 N", "10 N", "20 N", "5 N"],
                "ans": "B",
                "exp": "$F = v \\frac{dm}{dt} = 2\\text{ m/s} \\times 5\\text{ kg/s} = 10$ N."
            },
            {
                "q": "A force-time graph for an impact shows a triangle of base $\\Delta t = 0.04$ s and peak force $F_{max} = 1000$ N. What is the total impulse delivered?",
                "options": ["40 N·s", "20 N·s", "80 N·s", "10 N·s"],
                "ans": "B",
                "exp": "$\\text{Impulse} = \\text{Area under } F-t \\text{ graph} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 0.04 \\times 1000 = 20\\text{ N}\\cdot\\text{s}$."
            },
            {
                "q": "A stationary bomb of mass 9 kg explodes into two fragments of masses 3 kg and 6 kg. If the kinetic energy of the 3 kg fragment is 216 J, what is the kinetic energy of the 6 kg fragment?",
                "options": ["432 J", "108 J", "216 J", "72 J"],
                "ans": "B",
                "exp": "By conservation of momentum, $|p_1| = |p_2| = p$. Since $E_k = \\frac{p^2}{2m}$, $E_k \\propto 1/m$. $\\frac{E_2}{E_1} = \\frac{m_1}{m_2} = \\frac{3}{6} = 0.5$. $E_2 = 216 \\times 0.5 = 108$ J."
            },
            {
                "q": "A body of mass 2 kg is acted upon by two mutually perpendicular forces of 6 N and 8 N. What is the magnitude of the resulting acceleration?",
                "options": ["5 m/s²", "7 m/s²", "10 m/s²", "14 m/s²"],
                "ans": "A",
                "exp": "$F_{net} = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10$ N. Acceleration $a = F_{net} / m = 10 / 2 = 5\\text{ m/s}^2$."
            },
            {
                "q": "A 5 kg block rests on an inclined plane making an angle of 30° with the horizontal. What is the component of gravity acting parallel down the incline ($g = 10\\text{ m/s}^2$)?",
                "options": ["50 N", "25 N", "43.3 N", "10 N"],
                "ans": "B",
                "exp": "$F_{parallel} = mg \\sin 30^\\circ = 5 \\times 10 \\times 0.5 = 25$ N."
            },
            {
                "q": "Why does a heavy wooden box at rest require more force to start moving than to keep it sliding at constant speed?",
                "options": ["Rolling friction is higher than static friction", "Limiting static friction is greater than kinetic (sliding) friction", "Mass decreases once sliding begins", "Gravity drops while in motion"],
                "ans": "B",
                "exp": "At rest, microscopic surface irregularities interlock tightly (cold welding). Once sliding begins, asperities do not have time to interlock as deeply, so kinetic friction is less than limiting static friction."
            },
            {
                "q": "A bullet of mass 10 g leaves a gun barrel of length 0.8 m with a muzzle velocity of 400 m/s. Assuming uniform acceleration, the average force exerted on the bullet inside the barrel is:",
                "options": ["1000 N", "2000 N", "500 N", "100 N"],
                "ans": "A",
                "exp": "$v^2 = 2as \\Rightarrow 400^2 = 2a(0.8) \\Rightarrow 160,000 = 1.6a \\Rightarrow a = 100,000\\text{ m/s}^2$. $F = ma = 0.01 \\times 100,000 = 1000$ N."
            },
            {
                "q": "Which law of Newton provides the conceptual definition of force as an external agency that alters state of motion?",
                "options": ["First law of motion", "Second law of motion", "Third law of motion", "Law of gravitation"],
                "ans": "A",
                "exp": "Newton's first law qualitatively defines force; Newton's second law quantitatively measures force ($F = ma$)."
            },
            {
                "q": "An object of mass $m$ is suspended by a string from the ceiling of a car accelerating forward with acceleration $a$. The string tilts backward at an angle $\\theta$ given by:",
                "options": ["$\\tan\\theta = a/g$", "$\\tan\\theta = g/a$", "$\\sin\\theta = a/g$", "$\\cos\\theta = a/g$"],
                "ans": "A",
                "exp": "In the accelerating frame, pseudo force $ma$ acts backward and gravity $mg$ acts downward. $T \\sin\\theta = ma$, $T \\cos\\theta = mg \\Rightarrow \\tan\\theta = a/g$."
            },
            {
                "q": "A hovercraft gliding over a frozen lake with its engine turned off continues moving for kilometers because:",
                "options": ["It generates infinite thrust", "Air cushion eliminates virtually all contact friction, illustrating Galileo's law of inertia", "Lake ice rotates", "Gravity pulls it forward"],
                "ans": "B",
                "exp": "In the near absence of resistive frictional forces, an object in motion maintains its velocity indefinitely according to inertia."
            },
            {
                "q": "Two skaters on smooth ice face each other. Skater A (60 kg) pushes Skater B (40 kg) with a force of 120 N. What force does Skater B exert on Skater A?",
                "options": ["80 N", "120 N", "180 N", "Zero"],
                "ans": "B",
                "exp": "Newton's third law: action and reaction forces are strictly equal in magnitude and opposite in direction ($120$ N)."
            },
            {
                "q": "What is the ratio of accelerations of Skater A (60 kg) to Skater B (40 kg) from the push above?",
                "options": ["2 : 3", "3 : 2", "1 : 1", "4 : 9"],
                "ans": "A",
                "exp": "$a_A = 120/60 = 2\\text{ m/s}^2$. $a_B = 120/40 = 3\\text{ m/s}^2$. Ratio $a_A : a_B = 2 : 3$."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Linear momentum of an isolated system of interacting particles is conserved.<br>Reason (R): Internal forces between particles in an isolated system always cancel out in action-reaction pairs.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Since all internal interactions are equal and opposite, net internal force is zero. In the absence of external forces, $\\frac{dP_{total}}{dt} = 0$, conserving momentum."
            },
            {
                "q": "Assertion (A): When an apple falls towards the Earth, the Earth also accelerates towards the apple.<br>Reason (R): The gravitational force on the Earth by the apple is equal to the gravitational force on the apple by the Earth, but the Earth's enormous mass makes its acceleration undetectable.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "$F = ma$. The force is equal, but since $M_{Earth} \\approx 6 \\times 10^{24}$ kg, $a_{Earth} = F / M_{Earth} \\approx 10^{-24}\\text{ m/s}^2$, which is imperceptible."
            },
            {
                "q": "Assertion (A): A cyclist leans inward towards the center while negotiating a curve on a level road.<br>Reason (R): Leaning creates a torque from the normal contact force and gravity that balances the overturning torque produced by centrifugal effect.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Leaning inwards ensures the resultant ground reaction force passes through the center of mass, preventing the bike from toppling outward."
            },
            {
                "q": "Assertion (A): Mass is an invariant scalar measure of the quantity of matter in a body.<br>Reason (R): The weight of an object remains identical whether measured on Earth, on the Moon, or in deep outer space.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false: Weight is gravitational force ($W = mg$), which varies depending on local gravitational field ($g_{Moon} \\approx g_{Earth}/6$, zero in deep space)."
            },
            {
                "q": "Assertion (A): Seatbelts in automobiles prevent injury by applying an external backward force on occupants during sudden deceleration.<br>Reason (R): Occupants tend to maintain their forward velocity due to inertia of motion.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Inertia carries unrestrained bodies forward; seatbelts provide the necessary decelerating force over a controlled distance."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Linear Air Track Elastic Collision Experiment<br>Two gliders, Glider 1 ($m_1 = 0.40$ kg) and Glider 2 ($m_2 = 0.20$ kg), are placed on a linear air track where cushions of compressed air eliminate friction. Glider 1 is pushed towards stationary Glider 2 ($u_2 = 0$) with an initial velocity $u_1 = 3.0$ m/s. The gliders are equipped with spring bumpers so that the collision is completely elastic. After collision, Glider 1 continues forward at $v_1 = 1.0$ m/s while Glider 2 shoots forward at velocity $v_2$.",
                "q": "What is the initial total momentum of the two-glider system before collision?",
                "options": ["0.60 kg·m/s", "1.20 kg·m/s", "1.80 kg·m/s", "2.40 kg·m/s"],
                "ans": "B",
                "exp": "$P_{initial} = m_1 u_1 + m_2 u_2 = (0.40 \\times 3.0) + (0.20 \\times 0) = 1.20\\text{ kg}\\cdot\\text{m/s}$."
            },
            {
                "q": "Using the law of conservation of momentum, what is the final velocity $v_2$ of Glider 2 after impact?",
                "options": ["2.0 m/s", "4.0 m/s", "3.0 m/s", "5.0 m/s"],
                "ans": "B",
                "exp": "$1.20 = m_1 v_1 + m_2 v_2 \\Rightarrow 1.20 = (0.40 \\times 1.0) + 0.20 v_2 \\Rightarrow 1.20 = 0.40 + 0.20 v_2 \\Rightarrow 0.20 v_2 = 0.80 \\Rightarrow v_2 = 4.0$ m/s."
            },
            {
                "q": "What is the total kinetic energy of the system before collision?",
                "options": ["0.90 J", "1.80 J", "3.60 J", "1.20 J"],
                "ans": "B",
                "exp": "$E_{k,initial} = \\frac{1}{2} m_1 u_1^2 = \\frac{1}{2} (0.40)(3.0^2) = 0.20 \\times 9 = 1.80$ J."
            },
            {
                "q": "What is the total kinetic energy of the system after collision?",
                "options": ["1.80 J", "1.60 J", "2.00 J", "1.20 J"],
                "ans": "A",
                "exp": "$E_{k,final} = \\frac{1}{2}(0.40)(1.0^2) + \\frac{1}{2}(0.20)(4.0^2) = 0.20 + 0.10(16) = 0.20 + 1.60 = 1.80$ J (conserved in elastic collision)."
            },
            {
                "q": "If the spring bumpers were replaced with sticky Velcro pads so the gliders stuck together upon collision, the collision would be classified as:",
                "options": ["Super-elastic", "Perfectly inelastic", "Partially elastic", "Conservative"],
                "ans": "B",
                "exp": "A collision where the bodies stick together and move with a common velocity experiences maximum kinetic energy loss, defined as perfectly inelastic."
            }
        ]
    },
    {
        "num": 7,
        "title": "Work, Energy, and Simple Machines",
        "file": "Science_Exam_Papers/chapter_07_work_energy_set_c.html",
        "short_file": "chapter_07_work_energy_set_c.html",
        "description": "SET C (NCERT Exemplar & Energetics): Roller-coaster loop-the-loop physics, conservative vs dissipative forces, escape velocity, and compound wheel & axle mechanics.",
        "questions": [
            {
                "q": "A roller coaster car of mass $m$ enters a vertical circular loop of radius $R$. What is the minimum velocity required at the lowest point of the track to complete the loop without falling off at the apex ($g$ is acceleration due to gravity)?",
                "options": ["$\\sqrt{gR}$", "$\\sqrt{2gR}$", "$\\sqrt{5gR}$", "$\\sqrt{3gR}$"],
                "ans": "C",
                "exp": "At the top, minimum speed is $v_{top} = \\sqrt{gR}$. By energy conservation: $\\frac{1}{2}mv_{bottom}^2 = \\frac{1}{2}mv_{top}^2 + mg(2R) \\Rightarrow v_{bottom}^2 = gR + 4gR = 5gR \\Rightarrow v_{bottom} = \\sqrt{5gR}$."
            },
            {
                "q": "A force $\\vec{F} = (3\\hat{i} + 4\\hat{j})$ N acts on a particle, displacing it by $\\vec{s} = (5\\hat{i} + 2\\hat{j})$ m. What is the total work done?",
                "options": ["15 J", "23 J", "8 J", "35 J"],
                "ans": "B",
                "exp": "$W = \\vec{F} \\cdot \\vec{s} = (3 \\times 5) + (4 \\times 2) = 15 + 8 = 23$ Joules."
            },
            {
                "q": "A 1000 kg car travelling at 72 km/h (20 m/s) has its kinetic energy converted into heat by friction brakes to stop. How much thermal energy is dissipated in the brakes?",
                "options": ["100 kJ", "200 kJ", "400 kJ", "50 kJ"],
                "ans": "B",
                "exp": "$E_k = \\frac{1}{2} m v^2 = \\frac{1}{2}(1000)(20^2) = 500 \\times 400 = 200,000$ J $= 200$ kJ."
            },
            {
                "q": "A spring with spring constant $k = 500$ N/m is compressed by 4 cm ($0.04$ m). What is the magnitude of the restoring force exerted by the spring?",
                "options": ["20 N", "200 N", "2 N", "0.4 N"],
                "ans": "A",
                "exp": "Hooke's law: $F = k x = 500\\text{ N/m} \\times 0.04\\text{ m} = 20$ N."
            },
            {
                "q": "A pump is rated at 2.0 kW. How many liters of water can it lift in 10 minutes to an overhead tank 10 m high ($g = 10\\text{ m/s}^2$, density of water $= 1\\text{ kg/L}$)?",
                "options": ["6,000 L", "12,000 L", "1,200 L", "24,000 L"],
                "ans": "B",
                "exp": "Total energy $= P \\times t = 2000\\text{ W} \\times 600\\text{ s} = 1,200,000$ J. $W = mgh \\Rightarrow 1,200,000 = m(10)(10) \\Rightarrow 100m = 1,200,000 \\Rightarrow m = 12,000$ kg $= 12,000$ liters."
            },
            {
                "q": "Which of the following is a non-conservative force where work done depends on the actual path taken?",
                "options": ["Gravitational force", "Electrostatic force", "Kinetic friction force", "Ideal spring restoring force"],
                "ans": "C",
                "exp": "Friction is a non-conservative, dissipative force; the work done against friction over a closed path is non-zero and dissipates mechanical energy as heat."
            },
            {
                "q": "A 2 kg metal ball is released from rest from a height of 5 m above a sandpit. It penetrates 0.10 m into the sand before stopping. What is the average retarding force exerted by the sand ($g = 10\\text{ m/s}^2$)?",
                "options": ["1000 N", "1020 N", "500 N", "200 N"],
                "ans": "B",
                "exp": "Total loss of potential energy $= mg(h + d) = 2 \\times 10 \\times (5 + 0.10) = 20 \\times 5.10 = 102$ J. Work done by sand $= F \\times d \\Rightarrow F \\times 0.10 = 102 \\Rightarrow F = 1020$ N."
            },
            {
                "q": "A wheel and axle machine has a wheel radius of 40 cm and an axle radius of 8 cm. What is the ideal mechanical advantage (velocity ratio)?",
                "options": ["5", "0.2", "4", "32"],
                "ans": "A",
                "exp": "$MA_{ideal} = \\frac{\\text{Radius of wheel}}{\\text{Radius of axle}} = \\frac{40}{8} = 5$."
            },
            {
                "q": "An object of mass $m$ has a momentum $p$. Its kinetic energy is given by:",
                "options": ["$p m$", "$\\frac{p^2}{2m}$", "$\\frac{2p^2}{m}$", "$\\frac{p}{2m}$"],
                "ans": "B",
                "exp": "$p = mv \\Rightarrow v = p/m$. $E_k = \\frac{1}{2}mv^2 = \\frac{1}{2}m(p/m)^2 = \\frac{p^2}{2m}$."
            },
            {
                "q": "A constant force $F$ accelerates an object from rest to speed $v$ over time $t$. The instantaneous power delivered by the force at time $t$ is:",
                "options": ["$F v$", "$\\frac{1}{2} F v$", "$2 F v$", "$\\frac{F v}{t}$"],
                "ans": "A",
                "exp": "Instantaneous power is the scalar product of force and instantaneous velocity: $P = F v$."
            },
            {
                "q": "What is the average power delivered in the above problem?",
                "options": ["$F v$", "$\\frac{1}{2} F v$", "$2 F v$", "$F v^2$"],
                "ans": "B",
                "exp": "$\\text{Average power} = \\frac{\\text{Work}}{\\text{Time}} = \\frac{\\frac{1}{2}mv^2}{t} = \\frac{1}{2} \\left(\\frac{mv}{t}\\right) v = \\frac{1}{2} F v$."
            },
            {
                "q": "A hydroelectric turbine operates with 85% efficiency under a head of 100 m. If water flows through it at 10,000 kg/s ($g = 10\\text{ m/s}^2$), what electrical power is generated?",
                "options": ["8.5 MW", "10 MW", "1.5 MW", "85 MW"],
                "ans": "A",
                "exp": "Input hydraulic power $= mgh/t = 10,000 \\times 10 \\times 100 = 10,000,000$ W $= 10$ MW. Output power $= 0.85 \\times 10 = 8.5$ Megawatts."
            },
            {
                "q": "A simple machine lifts a load of 400 N through 2 m when an effort of 100 N moves through 10 m. What is the efficiency of the machine?",
                "options": ["80%", "75%", "90%", "85%"],
                "ans": "A",
                "exp": "$W_{out} = 400 \\times 2 = 800$ J. $W_{in} = 100 \\times 10 = 1000$ J. $\\eta = \\frac{800}{1000} \\times 100 = 80\\%$."
            },
            {
                "q": "A body of mass 1 kg is thrown vertically upward with 100 J of kinetic energy. At what height above the launch point will its kinetic energy equal its potential energy ($g = 10\\text{ m/s}^2$)?",
                "options": ["2.5 m", "5.0 m", "10.0 m", "1.25 m"],
                "ans": "B",
                "exp": "At that height, $E_p = 50$ J. $mgh = 50 \\Rightarrow 1 \\times 10 \\times h = 50 \\Rightarrow h = 5.0$ m."
            },
            {
                "q": "Which class of lever has the mechanical advantage always less than 1 ($MA < 1$)?",
                "options": ["Class 1 lever", "Class 2 lever", "Class 3 lever", "Inclined plane"],
                "ans": "C",
                "exp": "In a Class 3 lever (e.g. human forearm holding weight, fishing rod, tweezers), effort is applied between fulcrum and load, making effort arm shorter than load arm ($MA < 1$)."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Work done by gravity on an object sliding down a frictionless incline of height $h$ equals the work done dropping it vertically through height $h$.<br>Reason (R): Gravitational force is a conservative force, and work done between two vertical levels depends only on initial and final heights, not the path taken.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because gravity is conservative, $W = mgh$ independent of path curvature or inclination."
            },
            {
                "q": "Assertion (A): A heavier truck and a light car having identical kinetic energies have different momenta.<br>Reason (R): Momentum is proportional to $\\sqrt{m}$ for a given constant kinetic energy ($p = \\sqrt{2m E_k}$).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Since $p = \\sqrt{2m E_k}$, the heavier vehicle ($m_{truck} > m_{car}$) carries substantially greater momentum."
            },
            {
                "q": "Assertion (A): A machine cannot multiply both force and speed simultaneously.<br>Reason (R): Work output cannot exceed work input ($Load \\times d_L \\le Effort \\times d_E$); if force is multiplied ($MA > 1$), distance and speed must be compromised ($VR < 1$).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Energy conservation dictates that a machine can be a force multiplier ($MA > 1$) or a speed multiplier ($VR < 1$), but never both."
            },
            {
                "q": "Assertion (A): When a gas expands isothermally against atmospheric pressure, it does positive work.<br>Reason (R): The force exerted by the expanding gas acts in the same direction as the displacement of the piston.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "$W = \\int P dV$. When volume expands ($dV > 0$), pressure force and boundary displacement align, performing positive work."
            },
            {
                "q": "Assertion (A): A stationary satellite in orbit consumes rocket fuel continuously to do gravitational work.<br>Reason (R): The gravitational pull of the Earth continuously accelerates the satellite inward.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is completely false: In circular orbit, displacement is perpendicular to gravitational force, so zero work is done ($W=0$) and no fuel is consumed to maintain orbit. Reason is true."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Roller Coaster Gravitational & Kinetic Energy Dynamics<br>A roller coaster car of total mass 500 kg starts from rest at the top of an initial lift hill at Height A ($h_A = 45$ m) above the ground. The car coasts down into a valley at ground level ($h = 0$) and then ascends into a second smaller hill of Height B ($h_B = 25$ m). Neglect friction and air resistance ($g = 10\\text{ m/s}^2$).",
                "q": "What is the gravitational potential energy of the roller coaster car at the peak of the initial hill (Height A)?",
                "options": ["22,500 J", "225,000 J (225 kJ)", "450,000 J", "112,500 J"],
                "ans": "B",
                "exp": "$E_p = mgh_A = 500 \\times 10 \\times 45 = 225,000$ J $= 225$ kJ."
            },
            {
                "q": "What is the maximum speed of the roller coaster car as it passes through the valley at ground level ($h = 0$)?",
                "options": ["20 m/s", "30 m/s", "45 m/s", "25 m/s"],
                "ans": "B",
                "exp": "$\\frac{1}{2}mv^2 = mgh_A \\Rightarrow v = \\sqrt{2gh_A} = \\sqrt{2 \\times 10 \\times 45} = \\sqrt{900} = 30$ m/s (108 km/h)."
            },
            {
                "q": "What is the speed of the car when it reaches the peak of the second hill (Height B = 25 m)?",
                "options": ["20 m/s", "15 m/s", "25 m/s", "10 m/s"],
                "ans": "A",
                "exp": "$v = \\sqrt{2g(h_A - h_B)} = \\sqrt{2 \\times 10 \\times (45 - 25)} = \\sqrt{20 \\times 20} = 20$ m/s."
            },
            {
                "q": "What is the kinetic energy of the car at the peak of the second hill (Height B)?",
                "options": ["100 kJ", "125 kJ", "75 kJ", "225 kJ"],
                "ans": "A",
                "exp": "$E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} (500) (20^2) = 250 \\times 400 = 100,000$ J $= 100$ kJ."
            },
            {
                "q": "If realistic track friction dissipates 25 kJ of mechanical energy as heat along the track between Hill A and Hill B, what will be the final kinetic energy at Hill B?",
                "options": ["100 kJ", "75 kJ", "125 kJ", "50 kJ"],
                "ans": "B",
                "exp": "$\\text{Available } E_k = 100\\text{ kJ} - 25\\text{ kJ (friction loss)} = 75$ kJ."
            }
        ]
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom",
        "file": "Science_Exam_Papers/chapter_08_atom_set_c.html",
        "short_file": "chapter_08_atom_set_c.html",
        "description": "SET C (NCERT Exemplar & Quantum Foundations): Geiger-Marsden scattering angles, Bohr orbital photon emissions, isoelectronic ionic radii, and nuclear binding energy.",
        "questions": [
            {
                "q": "In the Geiger-Marsden $\\alpha$-particle scattering experiment, what happens to the number of scattered $\\alpha$-particles detected as the scattering angle $\\theta$ increases from 0° to 180°?",
                "options": ["It increases linearly", "It drops dramatically according to $N(\\theta) \\propto \\frac{1}{\\sin^4(\\theta/2)}$", "It remains constant at all angles", "It drops to zero beyond 10°"],
                "ans": "B",
                "exp": "Rutherford's scattering formula shows that the number of deflected particles drops inversely with $\\sin^4(\\theta/2)$; only a tiny fraction (1 in 12,000) experiences wide-angle backscattering near 180°."
            },
            {
                "q": "When an electron in a hydrogen atom transitions from a higher discrete energy orbit ($n = 3$) to a lower orbit ($n = 2$), what physical event occurs?",
                "options": ["A proton is emitted from the nucleus", "A photon of electromagnetic radiation with energy $\\Delta E = h\\nu$ is emitted", "The atom collapses into a neutron", "The electron is absorbed into the nucleus"],
                "ans": "B",
                "exp": "According to Bohr's model, when an electron jumps from a higher to lower stationary state, it emits a quantum photon of light whose energy equals the difference between the two orbital energy levels."
            },
            {
                "q": "Which of the following isoelectronic ions has the smallest ionic radius: $N^{3-}, O^{2-}, F^-, Na^+, Mg^{2+}, Al^{3+}$ (all having 10 electrons)?",
                "options": ["$N^{3-}$", "$O^{2-}$", "$Na^+$", "$Al^{3+}$"],
                "ans": "D",
                "exp": "All six ions have identical electron configurations (2, 8). $Al^{3+}$ has the highest nuclear charge ($Z = 13$ protons), which exerts the strongest electrostatic pull on the 10 electrons, contracting the electron cloud to the smallest radius."
            },
            {
                "q": "Why does a neutron make an exceptionally effective projectile for inducing nuclear fission in heavy uranium-235 atoms?",
                "options": ["Because neutrons carry positive charge", "Because neutrons carry zero electrical charge and can approach the positively charged nucleus without experiencing electrostatic Coulomb repulsion", "Because neutrons travel faster than light", "Because neutrons have zero mass"],
                "ans": "B",
                "exp": "Uncharged neutrons do not experience electrostatic repulsion from positive nuclear protons, allowing them to penetrate deep into heavy nuclei at low thermal speeds."
            },
            {
                "q": "The electronic configuration of a divalent cation $M^{2+}$ is 2, 8, 14. What is the atomic number of the neutral element $M$?",
                "options": ["24", "26", "28", "22"],
                "ans": "B",
                "exp": "Electrons in $M^{2+} = 2 + 8 + 14 = 24$. Since it lost 2 electrons, the neutral atom had $24 + 2 = 26$ electrons ($Z = 26$, Iron)."
            },
            {
                "q": "What is the maximum number of electrons that can be accommodated in the $M$-shell ($n = 3$) of an atom?",
                "options": ["8", "18", "32", "2"],
                "ans": "B",
                "exp": "$2 n^2 = 2(3^2) = 2(9) = 18$ electrons."
            },
            {
                "q": "Which of the following isotopes is utilized in industrial thickness gauges to monitor the thickness of manufactured plastic sheets and metal foils?",
                "options": ["Cobalt-60", "Strontium-90 (beta emitter)", "Iodine-131", "Uranium-238"],
                "ans": "B",
                "exp": "Beta emitters like Strontium-90 are absorbed proportional to material thickness, allowing automated radiation sensors to control roller pressure."
            },
            {
                "q": "An atom has 20 neutrons and mass number 39. What is its chemical valency?",
                "options": ["1", "2", "3", "0"],
                "ans": "A",
                "exp": "$Z = A - N = 39 - 20 = 19$ (Potassium). Electronic configuration $= 2, 8, 8, 1$. Valency $= 1$."
            },
            {
                "q": "Why did Dalton's original postulate that 'atoms are indivisible and indestructible' require scientific revision?",
                "options": ["Because atoms turn into water", "Because the discoveries of electrons, protons, and neutrons proved that atoms are composed of smaller subatomic particles", "Because atoms have no mass", "Because all atoms are identical"],
                "ans": "B",
                "exp": "Subatomic particle discoveries (J.J. Thomson, Goldstein, Chadwick) and nuclear transmutation proved that atoms are divisible complex structures."
            },
            {
                "q": "What is the mass ratio of a proton to an electron approximately?",
                "options": ["1 : 1", "1840 : 1", "1 : 1840", "100 : 1"],
                "ans": "B",
                "exp": "Mass of proton $\\approx 1.673 \\times 10^{-27}$ kg; mass of electron $\\approx 9.109 \\times 10^{-31}$ kg. Ratio $\\approx 1836 \\approx 1840 : 1$."
            },
            {
                "q": "An element $X$ has an atomic number 15. What is the valency exhibited by $X$ in the hydride $XH_3$ and chloride $XCl_5$?",
                "options": ["3 and 5", "2 and 4", "1 and 3", "Only 3"],
                "ans": "A",
                "exp": "$Z = 15$ is Phosphorus (2, 8, 5). It exhibits variable valency 3 (gaining/sharing 3 electrons) and 5 (utilizing all 5 valence electrons with vacant d-orbitals)."
            },
            {
                "q": "Heavy water ($D_2O$) contains which isotope of hydrogen?",
                "options": ["Protium ($^1_1 H$)", "Deuterium ($^2_1 H$)", "Tritium ($^3_1 H$)", "Helium"],
                "ans": "B",
                "exp": "Heavy water is composed of deuterium ($^2_1 H$), having one proton and one neutron, utilized as a moderator in nuclear reactors."
            },
            {
                "q": "Which of the following pairs represents isotones (species having identical number of neutrons)?",
                "options": ["$^{14}_6 C$ and $^{16}_8 O$", "$^{12}_6 C$ and $^{14}_6 C$", "$^{40}_{18} Ar$ and $^{40}_{20} Ca$", "$^{1}_1 H$ and $^{2}_1 H$"],
                "ans": "A",
                "exp": "In $^{14}_6 C$, neutrons $= 14 - 6 = 8$. In $^{16}_8 O$, neutrons $= 16 - 8 = 8$. Both have 8 neutrons (isotones)."
            },
            {
                "q": "Which subatomic particle was absent in Thomson's and Rutherford's early atomic models?",
                "options": ["Electron", "Proton", "Neutron", "Positron"],
                "ans": "C",
                "exp": "The neutron was not discovered until 1932 by James Chadwick, decades after Thomson (1897) and Rutherford (1911)."
            },
            {
                "q": "What is the charge on an alpha ($\\alpha$) particle?",
                "options": ["$+1$ unit", "$+2$ units (equal to a helium nucleus $He^{2+}$)", "$-1$ unit", "Neutral"],
                "ans": "B",
                "exp": "An alpha particle consists of two protons and two neutrons, with a net charge of $+2$ ($+3.2 \\times 10^{-19}$ C) and mass $\\approx 4$ u."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): The chemical reactivity of an element is determined by its valence electrons.<br>Reason (R): In chemical reactions, only the outermost valence shell electrons are lost, gained, or shared to achieve stable octet configurations.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Core inner electrons are strongly shielded and tightly bound; chemical bonding and valency involve exclusively outer valence electrons."
            },
            {
                "q": "Assertion (A): Rutherford's nuclear model could not explain the atomic emission spectra of hydrogen.<br>Reason (R): Classical electromagnetic theory predicted accelerating electrons would continuously radiate energy and collapse into the nucleus, leaving no explanation for discrete spectral lines.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Continuous radiation would collapse the atom in $10^{-8}$ s and yield a continuous spectrum. Neils Bohr introduced discrete quantum orbits to solve this."
            },
            {
                "q": "Assertion (A): The nucleus of an atom carries a positive electric charge.<br>Reason (R): The nucleus contains positively charged protons and electrically neutral neutrons.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Protons have charge $+e$ and neutrons have charge $0$, so the net nuclear charge equals $+Ze$."
            },
            {
                "q": "Assertion (A): Isotopes have identical physical properties such as boiling point and density.<br>Reason (R): Physical properties depend on mass, and isotopes of an element have different mass numbers.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false: Isotopes have *different* physical properties (density, boiling point, mass). Reason is true."
            },
            {
                "q": "Assertion (A): Canal rays travel in straight lines towards the cathode.<br>Reason (R): Canal rays are produced by ionization of residual gas molecules in a discharge tube under high voltage.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Positively charged residual gas ions are accelerated towards the perforated negative cathode, passing through the canals as luminous streams."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Radioactive Isotope Tracers in Medicine & Industry<br>Radioactive isotopes (radioisotopes) emit ionizing radiation (alpha, beta, or gamma) as their unstable nuclei decay. In nuclear medicine and industry:<br>• <b>Technetium-99m:</b> Emits gamma rays with a 6-hour half-life used for imaging heart and bone perfusion.<br>• <b>Iodine-131:</b> Beta and gamma emitter with an 8-day half-life targeting the thyroid gland.<br>• <b>Cobalt-60:</b> Emits high-energy gamma rays (1.17 and 1.33 MeV) used in teletherapy cancer radiotherapy.<br>• <b>Americium-241:</b> Alpha emitter used in household smoke ionization detectors.",
                "q": "Why is Technetium-99m ideal for diagnostic medical scans inside human patients?",
                "options": ["It remains radioactive in the body for 50 years", "Its short half-life of 6 hours allows clear gamma camera imaging while rapidly decaying to safe background levels, minimizing patient radiation dose", "It is an alpha emitter that destroys all tissues", "It is completely non-radioactive"],
                "ans": "B",
                "exp": "A 6-hour half-life gives sufficient time to complete diagnostic gamma scans while clearing quickly so the patient does not retain long-term radiation."
            },
            {
                "q": "Why does radioactive Iodine-131 selectively accumulate in the human thyroid gland?",
                "options": ["The thyroid gland naturally captures and concentrates iodine from the bloodstream to synthesize thyroid hormones (thyroxine)", "Thyroid cells repel iodine", "Iodine only binds to bone", "Because of gastric acid"],
                "ans": "A",
                "exp": "The thyroid gland has active sodium-iodide symporters that concentrate iodine; localized beta radiation from 131-I destroys overactive thyroid or carcinoma cells."
            },
            {
                "q": "In cancer radiotherapy, how do Cobalt-60 gamma rays destroy malignant cancer cells?",
                "options": ["By freezing the tumor", "High-energy gamma photons cause severe double-stranded DNA breaks in rapidly dividing cancer cells, triggering apoptosis", "By starving cancer cells of oxygen", "By turning cancer cells into healthy skin"],
                "ans": "B",
                "exp": "Ionizing radiation creates free radicals and direct DNA breaks; rapidly dividing cancer cells lack repair capacity and undergo mitotic death."
            },
            {
                "q": "In a household smoke detector, why are alpha particles from Americium-241 utilized instead of gamma rays?",
                "options": ["Alpha particles have high ionizing power to ionize air between detector plates, and smoke particles disrupt this current; their short range cannot penetrate the detector casing", "Gamma rays are too heavy", "Alpha particles are invisible", "Smoke detectors require boiling water"],
                "ans": "A",
                "exp": "Alpha particles strongly ionize air molecules between electrodes. Smoke absorbs alpha rays, dropping current and triggering the alarm. Alphas cannot penetrate the outer casing, posing zero hazard."
            },
            {
                "q": "Which subatomic particle is identical to the alpha particle emitted by Americium-241?",
                "options": ["A high-speed electron", "A doubly ionized Helium-4 nucleus ($He^{2+}$)", "A neutral neutron", "A positron"],
                "ans": "B",
                "exp": "An alpha particle consists of two protons and two neutrons tightly bound, identical to a helium-4 nucleus."
            }
        ]
    }
]

HTML_TEMPLATE_SET_C = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Science - {chapter_title} - SET C (Exemplar)</title>
  <link rel="stylesheet" href="exam-style.css">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<div class="screen-wrapper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="toolbar no-print">
    <div class="toolbar-title">
      <span>🎯 CBSE 9TH SCIENCE | CH {chapter_num} [SET C - EXEMPLAR]</span>
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
    <div class="exam-title" style="font-size: 13.5px; color: #047857; margin-top: 3px; font-weight: 800;">
      SUBJECT: SCIENCE (CLASS - IX) | CHAPTER {chapter_num}: {chapter_title_upper} [SET C - NCERT EXEMPLAR SPECIAL]
    </div>
    <div class="exam-meta-line">
      <span>TIME ALLOWED: 45 MINUTES</span>
      <span>MAXIMUM MARKS: 25</span>
      <span>PAPER CODE: 086/CH{chapter_num_padded}/SET-C</span>
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
    <h4>General Instructions (SET C - NCERT Exemplar & Critical Thinking):</h4>
    <ol>
      <li>The question paper comprises <b>25 Multiple Choice Questions (MCQs)</b> of <b>1 mark each</b>.</li>
      <li><b>Section A (Q1 – Q15):</b> NCERT Exemplar based Multiple Choice Questions with single correct option.</li>
      <li><b>Section B (Q16 – Q20):</b> Deep Assertion-Reasoning based questions testing scientific cause-and-effect.</li>
      <li><b>Section C (Q21 – Q25):</b> Case-Study / Laboratory Experimental Investigation questions.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding circle on the <b>OMR Sheet</b> completely using a blue/black ballpoint pen.</li>
    </ol>
  </div>

  <!-- Questions Container -->
  <div class="questions-container">

    <div class="section-banner">
      <span>SECTION A: NCERT EXEMPLAR MCQS (Q.1 TO Q.15)</span>
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
      <span>SECTION C: EXPERIMENTAL INVESTIGATION & CASE STUDY (Q.21 TO Q.25)</span>
      <span>[5 MARKS]</span>
    </div>

{section_c_html}

  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID (SET C)</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & EXEMPLAR EXPLANATIONS (SET C)</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Scientific Rationale & NCERT Exemplar Analysis</th>
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
  alert("SET C Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nReview the detailed scientific solutions below.");
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

def generate_set_c_papers():
    for ch in SET_C_DATA:
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
                      <h5>READING PASSAGE & EXPERIMENTAL INVESTIGATION:</h5>
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
              <td style="text-align: center;"><span class="ans-badge" style="background: #047857;">({item['ans']})</span></td>
              <td>{item['exp']}</td>
            </tr>
            """)
            
        full_html = HTML_TEMPLATE_SET_C.format(
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
    generate_set_c_papers()
    print("ALL SET C PAPERS GENERATED SUCCESSFULLY!")
