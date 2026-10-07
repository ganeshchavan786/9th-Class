"""
Build script for CBSE Class 9 Science Chapter-wise Examination Papers (Chapters 1 to 8)
Generates standalone, print-ready HTML examination papers with CSS and interactive features.
Zero Marathi text in exam papers - strictly standard English.
"""

import json
import os

CHAPTERS_DATA = [
    {
        "num": 1,
        "title": "Exploration: Entering the World of Secondary Science",
        "file": "chapter_01_exploration.html",
        "description": "Scientific inquiry, SI units, variables, laboratory apparatus, measurement, and experimental accuracy.",
        "questions": [
            {
                "q": "Which of the following is considered the fundamental base unit for temperature in the International System of Units (SI)?",
                "options": ["Degree Celsius (°C)", "Kelvin (K)", "Fahrenheit (°F)", "Calorie (cal)"],
                "ans": "B",
                "exp": "Kelvin (K) is the SI base unit of thermodynamic temperature. Degree Celsius and Fahrenheit are derived or conventional scales."
            },
            {
                "q": "While measuring the volume of water in a graduated cylinder, a student notices a curved surface of the liquid. For water, the reading should be taken at:",
                "options": ["The upper meniscus at eye level", "The lower meniscus at eye level", "The midpoint between upper and lower levels", "The upper meniscus from an angle above"],
                "ans": "B",
                "exp": "For liquids that wet glass like water (concave meniscus), the correct volume measurement is read at the bottom/lower meniscus at eye level to prevent parallax error."
            },
            {
                "q": "In a scientific experiment designed to test how temperature affects the rate of sugar dissolving in water, which parameter is the independent variable?",
                "options": ["The time taken for sugar to dissolve", "The temperature of water", "The amount of water used", "The stirring speed"],
                "ans": "B",
                "exp": "The independent variable is the factor deliberately altered by the experimenter (here, water temperature) to observe its effect on the dependent variable (dissolution rate)."
            },
            {
                "q": "Which laboratory burner flame is non-luminous, produces the highest temperature, and is used for heating without leaving soot?",
                "options": ["A yellow flame with closed air hole", "A blue flame with fully opened air hole", "An orange smoky flame", "A red flickering flame"],
                "ans": "B",
                "exp": "When the air hole of a Bunsen burner is open, complete combustion of gas occurs, producing a hot, blue, non-luminous flame without soot deposit."
            },
            {
                "q": "A student measures the length of an object four times and gets 12.1 cm, 12.1 cm, 12.0 cm, and 12.1 cm. The actual true length is 15.0 cm. The measurements are:",
                "options": ["Both accurate and precise", "Accurate but not precise", "Precise but not accurate", "Neither accurate nor precise"],
                "ans": "C",
                "exp": "Precision refers to the closeness of repeated measurements to each other (12.0-12.1 cm), while accuracy refers to closeness to the true value (15.0 cm). Hence, precise but not accurate."
            },
            {
                "q": "Which of the following prefixes represents $10^{-6}$ in the metric measurement system?",
                "options": ["Milli (m)", "Micro (µ)", "Nano (n)", "Pico (p)"],
                "ans": "B",
                "exp": "Micro represents $10^{-6}$, whereas milli is $10^{-3}$, nano is $10^{-9}$, and pico is $10^{-12}$."
            },
            {
                "q": "What is the primary purpose of having a 'control group' in a scientific controlled experiment?",
                "options": ["To test multiple hypotheses simultaneously", "To provide a baseline for comparison against the experimental group", "To ensure all variables change at once", "To speed up the completion of the experiment"],
                "ans": "B",
                "exp": "A control group does not receive the experimental treatment and serves as a standard baseline to verify whether changes are due to the independent variable."
            },
            {
                "q": "Which piece of laboratory glassware is designed specifically for preparing solutions of exact and precise known volumes?",
                "options": ["Beaker", "Volumetric flask", "Conical flask", "Graduated test tube"],
                "ans": "B",
                "exp": "A volumetric flask is calibrated to contain a precise volume of liquid at a specific temperature, ideal for standard solutions."
            },
            {
                "q": "If a balance consistently reads 0.25 g even when nothing is placed on the pan, this error is categorized as:",
                "options": ["Random error", "Systematic zero error", "Human observational error", "Parallax error"],
                "ans": "B",
                "exp": "A non-zero reading with zero load is a systematic zero error that shifts all measurements by a fixed amount."
            },
            {
                "q": "What safety equipment should be immediately used if a chemical splashes into a student's eyes during a science laboratory experiment?",
                "options": ["Safety shower", "Eyewash station for at least 15 minutes", "Fire blanket", "Fume hood"],
                "ans": "B",
                "exp": "In case of chemical contact with eyes, flush immediately at an eyewash station with clean water continuously for at least 15 minutes."
            },
            {
                "q": "Which of the following is a derived SI unit rather than a base unit?",
                "options": ["Second (s)", "Kilogram (kg)", "Newton (N)", "Mole (mol)"],
                "ans": "C",
                "exp": "Newton ($N = kg \\cdot m/s^2$) is a derived unit of force, whereas second, kilogram, and mole are fundamental base SI units."
            },
            {
                "q": "A hypothesis in secondary science is best described as:",
                "options": ["A proven scientific law that never changes", "A testable and falsifiable proposed explanation for an observation", "An unquestionable fact accepted by scientists", "A random guess made without background reasoning"],
                "ans": "B",
                "exp": "A scientific hypothesis must be testable through experiment and capable of being proven false (falsifiable)."
            },
            {
                "q": "When heating a test tube containing a chemical liquid over a flame, the mouth of the test tube should be directed:",
                "options": ["Towards oneself to monitor the bubbling", "Towards the teacher only", "Away from oneself and all fellow classmates", "Directly downward towards the lab bench"],
                "ans": "C",
                "exp": "To prevent accidental injury from sudden boiling or chemical spurting, always point the open mouth of a heating test tube away from yourself and others."
            },
            {
                "q": "The density of an aluminum block with mass 54 g and volume 20 cm³ is:",
                "options": ["2.7 g/cm³", "0.37 g/cm³", "1080 g/cm³", "74 g/cm³"],
                "ans": "A",
                "exp": "$\\text{Density} = \\frac{\\text{Mass}}{\\text{Volume}} = \\frac{54\\text{ g}}{20\\text{ cm}^3} = 2.7\\text{ g/cm}^3$."
            },
            {
                "q": "In scientific notation, the diameter of a typical animal cell measuring 0.000025 m is written as:",
                "options": ["$25 \\times 10^{-4}$ m", "$2.5 \\times 10^{-5}$ m", "$0.25 \\times 10^{-6}$ m", "$2.5 \\times 10^{-6}$ m"],
                "ans": "B",
                "exp": "Shifting the decimal point 5 places to the right gives $2.5 \\times 10^{-5}$ m."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): SI units are accepted universally by scientists worldwide.<br>Reason (R): Standardized units ensure consistency, accuracy, and clear communication in scientific findings across all nations.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The SI system was adopted globally so that scientific measurements are mutually understood and reproducible worldwide without unit confusion."
            },
            {
                "q": "Assertion (A): Parallax error occurs when the observer's eye is placed obliquely to the measurement scale.<br>Reason (R): Parallax error is a type of systematic instrumental fault caused by poor calibration.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true (oblique viewing angle causes apparent shift). However, Reason is false because parallax error is an observational human error, not an instrumental fault."
            },
            {
                "q": "Assertion (A): In any controlled science experiment, all variables except the one being tested must be kept constant.<br>Reason (R): If multiple variables change at once, it is impossible to determine which factor caused the observed result.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Controlled variables ensure a fair test by isolating the effect of the single independent variable under investigation."
            },
            {
                "q": "Assertion (A): Water should never be poured directly into concentrated sulfuric acid when diluting it in a laboratory.<br>Reason (R): The dissolution of sulfuric acid in water is highly exothermic, and pouring water can cause boiling acid to violently splash out.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Always add acid slowly to water with constant stirring ('Acid to Water, like A to W') because water has high specific heat capacity to absorb the released heat."
            },
            {
                "q": "Assertion (A): A scientific theory can never be challenged or modified once established.<br>Reason (R): Science progresses as new evidence, higher precision tools, and fresh observations emerge.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false because science is dynamic and theories can be revised when new empirical evidence arises. Reason is true."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Investigation on Rate of Evaporation<br>A group of Class 9 students conducted an inquiry to investigate how surface area affects the rate of evaporation of water. They took three containers: Container X (a narrow test tube, diameter 1.5 cm), Container Y (a beaker, diameter 6 cm), and Container Z (a wide petri dish, diameter 12 cm). Each container was filled with exactly 50 mL of distilled water. All three containers were placed side by side on the same laboratory table at 25°C with no wind for 24 hours. After 24 hours, the remaining water volume was measured.",
                "q": "In this experiment, what is the independent variable being tested by the students?",
                "options": ["The volume of remaining water", "The surface area exposed to the air", "The ambient room temperature", "The duration of 24 hours"],
                "ans": "B",
                "exp": "The independent variable is the surface area of the water, varied by using containers of different diameters."
            },
            {
                "q": "Which of the following serves as the dependent variable in this inquiry?",
                "options": ["Diameter of the container", "Rate of evaporation / Volume of water evaporated", "Room temperature", "Type of liquid used"],
                "ans": "B",
                "exp": "The dependent variable is the volume of water evaporated, which is measured in response to changes in surface area."
            },
            {
                "q": "Which container will show the greatest loss of water due to evaporation after 24 hours?",
                "options": ["Container X (narrow test tube)", "Container Y (beaker)", "Container Z (wide petri dish)", "All three will lose identical amounts"],
                "ans": "C",
                "exp": "Evaporation is a surface phenomenon. Larger surface area allows more water molecules to escape into vapor phase per unit time."
            },
            {
                "q": "Why were all three containers kept in the exact same room at the same temperature and humidity?",
                "options": ["To make the test unfair", "To act as controlled variables and ensure fair comparison", "To increase random errors", "Because the lab had no other rooms available"],
                "ans": "B",
                "exp": "Keeping environmental factors like temperature, humidity, and airflow constant ensures they do not confound the effect of surface area."
            },
            {
                "q": "If the students want to increase the evaporation rate in all three containers simultaneously, which modification should they make?",
                "options": ["Increase room humidity", "Place an electric fan nearby to increase air velocity", "Lower the room temperature", "Cover the containers with glass lids"],
                "ans": "B",
                "exp": "Increasing wind speed/air velocity moves vapor particles away quickly, maintaining a steep concentration gradient and accelerating evaporation."
            }
        ]
    },
    {
        "num": 2,
        "title": "Cell: The Building Block of Life",
        "file": "chapter_02_cell.html",
        "description": "Cell discovery, plasma membrane, osmosis, cell organelles (mitochondria, plastids, ER, Golgi, lysosomes), and cell division.",
        "questions": [
            {
                "q": "Who first observed living, free-moving microscopic cells in pond water using an improved microscope in 1674?",
                "options": ["Robert Hooke", "Anton van Leeuwenhoek", "Robert Brown", "Rudolf Virchow"],
                "ans": "B",
                "exp": "Anton van Leeuwenhoek (1674) observed living cells in pond water. Robert Hooke (1665) had observed dead cork cells."
            },
            {
                "q": "Which scientist expanded the Cell Theory by stating 'Omnis cellula-e cellula' (all cells arise from pre-existing cells)?",
                "options": ["Matthias Schleiden", "Theodor Schwann", "Rudolf Virchow", "Purkinje"],
                "ans": "C",
                "exp": "Rudolf Virchow (1855) added the crucial tenet that all cells arise from pre-existing living cells by division."
            },
            {
                "q": "The plasma membrane is described as selectively permeable primarily because it:",
                "options": ["Allows all substances to enter freely", "Permits only specific molecules to pass through while preventing others", "Is made entirely of impermeable lignin", "Does not allow water molecules to cross"],
                "ans": "B",
                "exp": "The cell membrane regulates transport, allowing essential nutrients and water to enter while blocking harmful or unwanted substances."
            },
            {
                "q": "If red blood cells are placed in a hypotonic salt solution, what physical change will occur?",
                "options": ["They will shrink due to exosmosis", "They will swell and may burst due to endosmosis", "They will remain unchanged in size", "Their cell walls will become turgid"],
                "ans": "B",
                "exp": "In a hypotonic solution (lower solute concentration outside), water enters the cell via endosmosis. Lacking a rigid cell wall, animal cells swell and can burst (lysis)."
            },
            {
                "q": "The shrinkage of plant cytoplasm away from the cell wall when placed in a concentrated hypertonic sugar solution is called:",
                "options": ["Endosmosis", "Plasmolysis", "De-plasmolysis", "Imbibition"],
                "ans": "B",
                "exp": "Plasmolysis is the withdrawal of protoplasm from the cell wall when a plant cell loses water in a hypertonic medium."
            },
            {
                "q": "Which cell organelle is responsible for synthesizing lipids and detoxifying poisons and drugs in vertebrate liver cells?",
                "options": ["Rough Endoplasmic Reticulum (RER)", "Smooth Endoplasmic Reticulum (SER)", "Golgi apparatus", "Ribosome"],
                "ans": "B",
                "exp": "Smooth ER synthesizes lipids and steroids, and plays a major detoxifying role in liver cells. Rough ER synthesizes proteins."
            },
            {
                "q": "Which organelle consists of a stack of membrane-bound cisternae involved in packaging and dispatching proteins?",
                "options": ["Mitochondria", "Golgi apparatus", "Vacuole", "Centrosome"],
                "ans": "B",
                "exp": "Camillo Golgi described the Golgi apparatus, which modifies, packages, and routes proteins and complex biochemicals."
            },
            {
                "q": "Why are lysosomes known as the 'suicidal bags' of a cell?",
                "options": ["They produce poisonous toxins", "When a cell is damaged, they burst and their powerful digestive enzymes digest the cell itself", "They starve the cell of ATP", "They absorb harmful UV radiation"],
                "ans": "B",
                "exp": "Lysosomes contain strong hydrolytic digestive enzymes. If the cell undergoes severe damage, lysosomes rupture, causing autolysis (self-digestion)."
            },
            {
                "q": "Which two organelles possess their own DNA and 70S ribosomes, enabling them to make some of their own proteins?",
                "options": ["Mitochondria and Chloroplasts", "Lysosomes and Ribosomes", "Golgi apparatus and Endoplasmic Reticulum", "Nucleus and Vacuole"],
                "ans": "A",
                "exp": "Mitochondria and plastids (chloroplasts) are semi-autonomous organelles with their own circular DNA and ribosomes."
            },
            {
                "q": "The inner membrane of a mitochondrion is deeply folded into cristae. What is the functional advantage of these folds?",
                "options": ["To store extra water", "To vastly increase surface area for ATP-generating chemical reactions", "To protect the mitochondrial DNA from radiation", "To give structural rigidity to the organelle"],
                "ans": "B",
                "exp": "Folds (cristae) provide a huge surface area for enzymes associated with the electron transport chain and ATP synthesis."
            },
            {
                "q": "A colourless plastid responsible for storing starch, oils, or protein granules in plant cells is termed:",
                "options": ["Chromoplast", "Chloroplast", "Leucoplast", "Amyloplast only"],
                "ans": "C",
                "exp": "Leucoplasts are non-pigmented plastids whose primary function is nutrient storage (starch in amyloplasts, oils in elaioplasts)."
            },
            {
                "q": "The cell wall of plants is primarily composed of which complex carbohydrate that provides structural strength?",
                "options": ["Glycogen", "Cellulose", "Chitin", "Starch"],
                "ans": "B",
                "exp": "Cellulose provides mechanical tensile strength and structural support to plant cell walls. (Chitin is found in fungal cell walls)."
            },
            {
                "q": "In a mature plant cell, turgidity and rigidity are maintained mainly by:",
                "options": ["Centrioles", "A large central sap vacuole filled with cell sap", "Lysosomal hydrolytic enzymes", "Chromatin fibres"],
                "ans": "B",
                "exp": "The central vacuole occupies 50-90% of the volume of mature plant cells, exerting turgor pressure against the cell wall."
            },
            {
                "q": "Which type of cell division leads to the formation of two genetically identical diploid daughter cells for body growth and tissue repair?",
                "options": ["Meiosis I", "Mitosis", "Reduction division", "Binary fission only"],
                "ans": "B",
                "exp": "Mitosis is equational division where chromosome number is conserved, resulting in two identical daughter cells for somatic growth and repair."
            },
            {
                "q": "How many haploid daughter cells are produced at the completion of meiosis, and what is their chromosome count relative to the parent cell?",
                "options": ["Two cells with identical chromosome count", "Four cells with half the chromosome count", "Four cells with double the chromosome count", "Two cells with half the chromosome count"],
                "ans": "B",
                "exp": "Meiosis produces 4 gamete cells, each carrying half ($n$) the original chromosome number of the diploid ($2n$) parent cell."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Plant cells can withstand much greater osmotic changes in surrounding hypotonic solutions than animal cells.<br>Reason (R): Plant cells possess a rigid cellulose cell wall that exerts inward pressure against the swollen cytoplasm.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The strong cell wall exerts wall pressure equal and opposite to turgor pressure, preventing plant cells from bursting in hypotonic media."
            },
            {
                "q": "Assertion (A): Mitochondria are termed the powerhouses of the cell.<br>Reason (R): Mitochondria produce cellular energy in the form of Adenosine Triphosphate (ATP) molecules.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Mitochondria carry out cellular respiration, synthesizing ATP which fuels virtually all endergonic biochemical processes."
            },
            {
                "q": "Assertion (A): Ribosomes are known as protein factories of the cell.<br>Reason (R): Ribosomes are surrounded by a double-layered lipid membrane to safeguard newly formed enzymes.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true (ribosomes translate mRNA into proteins). Reason is false because ribosomes are non-membrane-bound ribonucleoprotein complexes."
            },
            {
                "q": "Assertion (A): Chromosomes are visible as distinct rod-shaped structures only when a cell is actively dividing.<br>Reason (R): In a non-dividing cell, DNA remains entangled as a thread-like mass called chromatin.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Chromatin condenses into tightly coiled discrete chromosomes only during prophase of cell division."
            },
            {
                "q": "Assertion (A): A prokaryotic cell has a well-defined membrane-bound nucleus containing multiple linear chromosomes.<br>Reason (R): Bacteria and blue-green algae are prokaryotic organisms.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false because prokaryotes lack a nuclear membrane and contain an undefined nucleoid. Reason is true."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Osmosis Experiment with Dried Raisins and Peeled Potato<br>In a laboratory practical, Aryan placed 10 g of dried, shriveled raisins into a beaker of pure distilled water (Setup 1). At the same time, his classmate Priya placed swollen raisins into a concentrated 20% sodium chloride (salt) solution (Setup 2). After 4 hours, Aryan observed that his raisins had swollen significantly and became firm, while Priya observed that her raisins shrank and lost volume.",
                "q": "The swelling of raisins in pure distilled water observed by Aryan is due to:",
                "options": ["Exosmosis", "Endosmosis", "Plasmolysis", "Active transport"],
                "ans": "B",
                "exp": "Distilled water is hypotonic relative to raisin interior; water molecules enter raisins by endosmosis."
            },
            {
                "q": "In Setup 2, why did the raisins shrink when placed in the 20% salt solution?",
                "options": ["Salt moved into the raisins by diffusion", "Water moved out of the raisins because the outer medium was hypertonic", "The raisin skins dissolved in salt", "No water movement took place"],
                "ans": "B",
                "exp": "The concentrated salt solution has lower water chemical potential (hypertonic), causing water to flow out (exosmosis)."
            },
            {
                "q": "Which natural barrier in the raisin cells acted as the semi-permeable membrane during this experiment?",
                "options": ["The cell wall only", "The plasma membrane / cell membrane", "The nuclear envelope", "The vacuolar tonoplast exclusively"],
                "ans": "B",
                "exp": "The selectively permeable plasma membrane regulates water movement via osmosis."
            },
            {
                "q": "If boiled raisins were used in Setup 1 instead of raw raisins, what would happen?",
                "options": ["They would swell twice as much", "They would not show osmosis because boiling destroys the living cell membranes", "They would turn into gas", "They would divide rapidly"],
                "ans": "B",
                "exp": "Boiling denatures proteins and destroys membrane integrity, rendering the cell non-living and unable to exhibit selective osmosis."
            },
            {
                "q": "What would happen if the swollen raisins from Setup 1 were transferred into a solution with identical water concentration (isotonic)?",
                "options": ["They would burst instantaneously", "There would be no net movement of water, and raisin size would remain constant", "They would double in size", "They would immediately dissolve"],
                "ans": "B",
                "exp": "In an isotonic medium, the rate of water entering equals the rate of water leaving; net osmotic change is zero."
            }
        ]
    },
    {
        "num": 3,
        "title": "Tissues in Action",
        "file": "chapter_03_tissues.html",
        "description": "Plant tissues (meristematic, parenchyma, collenchyma, sclerenchyma, xylem, phloem) and Animal tissues (epithelial, connective, muscular, nervous).",
        "questions": [
            {
                "q": "Which meristematic tissue is situated at the growing tips of stems and roots and causes an increase in their length?",
                "options": ["Lateral meristem", "Apical meristem", "Intercalary meristem", "Vascular cambium"],
                "ans": "B",
                "exp": "Apical meristem is present at growing root and shoot apices and brings about primary elongation growth."
            },
            {
                "q": "The increase in the girth (diameter/thickness) of a tree trunk is brought about by the activity of:",
                "options": ["Apical meristem", "Lateral meristem (cambium)", "Intercalary meristem", "Parenchyma cells"],
                "ans": "B",
                "exp": "Lateral meristems, including vascular cambium and cork cambium, produce secondary growth, increasing plant girth."
            },
            {
                "q": "Which simple permanent plant tissue provides both mechanical support and flexibility, allowing stems and tendrils to bend without breaking?",
                "options": ["Parenchyma", "Collenchyma", "Sclerenchyma", "Xylem vessels"],
                "ans": "B",
                "exp": "Collenchyma has localized pectin thickening at cell corners, giving tensile strength and flexibility without brittleness."
            },
            {
                "q": "The husk of a coconut is composed of which dead, heavily lignified plant tissue?",
                "options": ["Aerenchyma", "Collenchyma", "Sclerenchyma fibres", "Chlorenchyma"],
                "ans": "C",
                "exp": "Sclerenchyma consists of long, narrow, dead cells with thick lignified walls that give hardness and rigidity to coconut husk."
            },
            {
                "q": "Which of the following complex tissue elements in xylem is living and functions to store food materials?",
                "options": ["Tracheids", "Xylem vessels", "Xylem parenchyma", "Xylem fibres"],
                "ans": "C",
                "exp": "In xylem, tracheids, vessels, and xylem fibres are dead; only xylem parenchyma consists of living cells."
            },
            {
                "q": "Which phloem component lacks a nucleus at maturity yet remains living and functions in close association with companion cells?",
                "options": ["Phloem parenchyma", "Sieve tube elements", "Bast fibres", "Xylem tracheids"],
                "ans": "B",
                "exp": "Mature sieve tube elements lack a nucleus to facilitate sap transport; their metabolic functions are governed by adjacent nucleated companion cells."
            },
            {
                "q": "The chemical substance deposited in the cell walls of cork (bark) that makes them impervious to gases and water is:",
                "options": ["Lignin", "Suberin", "Pectin", "Cutin"],
                "ans": "B",
                "exp": "Suberin is a waxy, waterproof lipid deposited in walls of cork cells, making bark impervious to moisture and pathogens."
            },
            {
                "q": "Which epithelial tissue lines the alveoli of lungs and blood capillaries to facilitate rapid diffusion of gases and liquids?",
                "options": ["Stratified keratinized epithelium", "Simple squamous epithelium", "Ciliated columnar epithelium", "Cuboidal epithelium"],
                "ans": "B",
                "exp": "Simple squamous epithelium consists of extremely thin, flat, tile-like cells ideal for rapid diffusion across barriers."
            },
            {
                "q": "Ciliated columnar epithelium is characteristically found lining which part of the human body?",
                "options": ["Skin surface", "Respiratory tract (trachea and bronchi)", "Urinary bladder", "Stomach lining"],
                "ans": "B",
                "exp": "Cilia on columnar cells beat rhythmically in the respiratory tract to propel mucus and trapped dust particles upward."
            },
            {
                "q": "Which connective tissue connects a muscle to a bone and exhibits great fibrous strength with limited flexibility?",
                "options": ["Ligament", "Tendon", "Cartilage", "Areolar tissue"],
                "ans": "B",
                "exp": "Tendons connect skeletal muscle to bone and are tough collagenous cords. (Ligaments connect bone to bone)."
            },
            {
                "q": "The matrix of bone tissue is dense and hard primarily due to deposits of compounds of:",
                "options": ["Sodium and Potassium", "Calcium and Phosphorus", "Iron and Magnesium", "Sulphur and Silicon"],
                "ans": "B",
                "exp": "Bone matrix is composed of collagen fibers impregnated with hydroxyapatite crystals (calcium and phosphorus salts)."
            },
            {
                "q": "Which specialized connective tissue acts as a thermal insulator and is located beneath the skin and around vital organs like kidneys?",
                "options": ["Adipose tissue", "Areolar tissue", "Hyaline cartilage", "Dense fibrous tissue"],
                "ans": "A",
                "exp": "Adipose tissue stores fat droplets in adipocytes, providing cushioning and thermal insulation against cold."
            },
            {
                "q": "Smooth muscle fibres (unstriated muscles) are structurally:",
                "options": ["Cylindrical, syncytial, voluntary", "Spindle-shaped, uninucleated, involuntary", "Branched, uninucleated, striated", "Multinucleated, branched, voluntary"],
                "ans": "B",
                "exp": "Smooth muscles are unbranched, spindle-shaped (fusiform), with a single central nucleus, working involuntarily (e.g., alimentary canal)."
            },
            {
                "q": "Cardiac muscle tissue is characterized by which unique combination of features?",
                "options": ["Voluntary, unbranched, non-striated", "Involuntary, branched, uninucleated, with intercalated discs", "Voluntary, multinucleated, cylindrical", "Involuntary, unbranched, multinucleated"],
                "ans": "B",
                "exp": "Cardiac muscles are cylindrical, branched, uninucleated, striated, and involuntary, beating rhythmically throughout life without fatigue."
            },
            {
                "q": "The long, slender cylindrical projection that conducts electrical impulses away from the cell body (cyton) of a neuron is the:",
                "options": ["Dendrite", "Axon", "Synapse", "Myelin node"],
                "ans": "B",
                "exp": "Dendrites receive incoming signals and transmit them to the cyton; the axon carries the action potential away toward the synaptic terminal."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Meristematic cells have dense cytoplasm, prominent nuclei, and thin walls, but lack vacuoles.<br>Reason (R): Meristematic cells are actively dividing and do not need to store food or maintain large hydrostatic turgor pressure.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because meristematic cells divide continuously, storing nutrients or maintaining large central sap vacuoles would hinder rapid mitotic spindle formation."
            },
            {
                "q": "Assertion (A): Blood is classified as a fluid connective tissue.<br>Reason (R): Blood has a liquid extracellular matrix called plasma in which RBCs, WBCs, and platelets are suspended.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Connective tissues are characterized by cells distributed within an extracellular matrix. In blood, the fluid matrix is plasma."
            },
            {
                "q": "Assertion (A): Skeletal muscles are called voluntary muscles.<br>Reason (R): Their contractions can be consciously initiated and controlled at will by our nervous system.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Skeletal muscles are attached to the skeleton and are under voluntary somatic nervous control."
            },
            {
                "q": "Assertion (A): Xylem transports food manufactured in leaves to all other plant parts.<br>Reason (R): Phloem transports water and mineral salts absorbed by roots upward to the leaves.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Both statements are reversed: Xylem transports water and minerals unidirectionally; Phloem translocates photosynthesized sugars bidirectionally."
            },
            {
                "q": "Assertion (A): Ligaments connect two bones together at a joint.<br>Reason (R): Ligaments contain very little matrix and are composed of highly flexible elastic fibres.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Ligaments are strong, elastic connective tissues binding bone to bone to stabilize joints while permitting motion."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Microscopic Examination of Plant Stems<br>During a laboratory session, a student took a thin transverse section (TS) of a herbaceous dicot stem, stained it with safranin and fast green, and mounted it on a glass slide. Under the compound microscope, she noticed: (i) an outer protective epidermis with stomata, (ii) a cortex region beneath containing loosely packed cells with thin cellulose walls and large intercellular spaces, (iii) patches of cells at the corners with uneven pectin thickening, and (iv) vascular bundles containing thick-walled tube-like vessels arranged in rings.",
                "q": "The loosely packed cells in the cortex with thin cellulose walls and large intercellular spaces belong to:",
                "options": ["Sclerenchyma", "Parenchyma", "Collenchyma", "Cork"],
                "ans": "B",
                "exp": "Parenchyma is the ground tissue made of living cells with thin cellulose walls and prominent intercellular spaces."
            },
            {
                "q": "If the parenchyma cells in a green stem develop chlorophyll and carry out photosynthesis, they are specifically termed:",
                "options": ["Aerenchyma", "Chlorenchyma", "Collenchyma", "Sclerenchyma"],
                "ans": "B",
                "exp": "Parenchyma containing chloroplasts capable of photosynthesis is called chlorenchyma."
            },
            {
                "q": "The patches of cells showing uneven thickening at corners with no intercellular spaces are identified as:",
                "options": ["Collenchyma", "Xylem vessels", "Sclerenchyma fibres", "Glandular tissue"],
                "ans": "A",
                "exp": "Localized cellulose and pectin deposition at corner junctions without intercellular spaces is the hallmark of collenchyma."
            },
            {
                "q": "Why were the xylem vessel walls strongly stained red with safranin?",
                "options": ["Because they contain starch", "Because safranin selectively stains lignified dead secondary cell walls", "Because xylem contains hemoglobin", "Because xylem vessels are living cells"],
                "ans": "B",
                "exp": "Safranin binds to lignin, staining the lignified walls of xylem vessels and sclerenchyma bright red."
            },
            {
                "q": "Which specialized epidermal structures observed by the student regulate transpiration and gaseous exchange in the stem?",
                "options": ["Trichomes", "Stomata with kidney-shaped guard cells", "Lenticels only", "Cuticle layer without pores"],
                "ans": "B",
                "exp": "Stomata, regulated by two guard cells, open and close to mediate water vapor transpiration and gas exchange ($O_2 / CO_2$)."
            }
        ]
    },
    {
        "num": 4,
        "title": "Describing Motion Around Us",
        "file": "chapter_04_motion.html",
        "description": "Distance, displacement, speed, velocity, acceleration, distance-time & velocity-time graphs, equations of motion, and circular motion.",
        "questions": [
            {
                "q": "A runner completes one full round of a circular track of radius 7 m. What is the ratio of the total distance covered to the magnitude of displacement?",
                "options": ["0", "44 : 0 (Displacement is zero, distance is 44 m)", "1 : 1", "22 : 7"],
                "ans": "B",
                "exp": "Distance $= 2\\pi r = 2 \\times \\frac{22}{7} \\times 7 = 44$ m. Returning to the starting point gives displacement $= 0$ m."
            },
            {
                "q": "Under which of the following conditions is the magnitude of average velocity equal to the average speed of an object?",
                "options": ["When the object moves in a circular path", "When the object moves along a straight line in a single unchanging direction", "When the object travels back and forth", "Average velocity can never equal average speed"],
                "ans": "B",
                "exp": "Along a straight line without reversing direction, distance equals displacement magnitude, so average speed equals average velocity."
            },
            {
                "q": "A car accelerates uniformly from rest to a velocity of 72 km/h in 10 seconds. What is the acceleration of the car?",
                "options": ["7.2 m/s²", "2.0 m/s²", "4.0 m/s²", "20 m/s²"],
                "ans": "B",
                "exp": "$u = 0$, $v = 72 \\times \\frac{5}{18} = 20$ m/s, $t = 10$ s. $a = \\frac{v - u}{t} = \\frac{20 - 0}{10} = 2.0$ m/s²."
            },
            {
                "q": "What does the slope of a distance-time graph represent?",
                "options": ["Acceleration", "Speed", "Displacement", "Force"],
                "ans": "B",
                "exp": "Slope of distance-time graph $= \\frac{\\Delta \\text{distance}}{\\Delta \\text{time}} = \\text{Speed}$."
            },
            {
                "q": "What physical quantity does the area under a velocity-time graph represent?",
                "options": ["Acceleration", "Distance or Displacement", "Speed", "Rate of change of velocity"],
                "ans": "B",
                "exp": "Area under a velocity-time graph $= \\text{velocity} \\times \\text{time} = \\text{displacement}$ (or distance for uni-directional motion)."
            },
            {
                "q": "A body starts from rest and moves with uniform acceleration of 3 m/s². What distance does it cover during the first 4 seconds?",
                "options": ["12 m", "24 m", "48 m", "6 m"],
                "ans": "B",
                "exp": "$s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2}(3)(4^2) = \\frac{1}{2} \\times 3 \\times 16 = 24$ m."
            },
            {
                "q": "Which equation of motion gives the relation between velocity and displacement without involving time explicitly?",
                "options": ["$v = u + at$", "$s = ut + \\frac{1}{2}at^2$", "$v^2 = u^2 + 2as$", "$s = \\frac{u + v}{2} t$"],
                "ans": "C",
                "exp": "$v^2 - u^2 = 2as$ relates final velocity ($v$), initial velocity ($u$), acceleration ($a$), and displacement ($s$)."
            },
            {
                "q": "An object moves in a circular path of radius $R$ with a constant speed $v$. Its acceleration is:",
                "options": ["Zero because speed is constant", "Non-zero and directed towards the centre of the circle", "Directed tangent to the circle", "Constant in direction"],
                "ans": "B",
                "exp": "In uniform circular motion, direction changes continuously; the resulting centripetal acceleration is directed radially inward."
            },
            {
                "q": "A train travelling at 20 m/s is brought to rest by applying brakes that produce a uniform retardation of 2 m/s². The time taken to stop is:",
                "options": ["5 s", "10 s", "20 s", "40 s"],
                "ans": "B",
                "exp": "$u = 20$ m/s, $v = 0$, $a = -2$ m/s². $v = u + at \\Rightarrow 0 = 20 - 2t \\Rightarrow 2t = 20 \\Rightarrow t = 10$ s."
            },
            {
                "q": "The odometer of an automobile records:",
                "options": ["Instantaneous speed", "Average velocity", "Total distance travelled", "Uniform acceleration"],
                "ans": "C",
                "exp": "An odometer measures total distance covered in kilometers, whereas a speedometer measures instantaneous speed."
            },
            {
                "q": "A ball is thrown vertically upward with an initial velocity of 20 m/s. Taking $g = 10$ m/s², what is the maximum height reached?",
                "options": ["10 m", "20 m", "40 m", "200 m"],
                "ans": "B",
                "exp": "At max height $v = 0$. $v^2 = u^2 - 2gh \\Rightarrow 0 = 20^2 - 2(10)h \\Rightarrow 20h = 400 \\Rightarrow h = 20$ m."
            },
            {
                "q": "If the displacement-time graph of a moving object is a straight line parallel to the time axis, the object is:",
                "options": ["Moving with uniform speed", "Moving with uniform acceleration", "At rest", "Moving with non-uniform velocity"],
                "ans": "C",
                "exp": "A horizontal line on a displacement-time graph means displacement does not change as time advances, so the object is stationary."
            },
            {
                "q": "A particle moves with uniform acceleration. If its velocity changes from 10 m/s to 30 m/s while covering a distance of 80 m, the acceleration is:",
                "options": ["2.5 m/s²", "5.0 m/s²", "1.25 m/s²", "10 m/s²"],
                "ans": "B",
                "exp": "$v^2 = u^2 + 2as \\Rightarrow 30^2 = 10^2 + 2a(80) \\Rightarrow 900 - 100 = 160a \\Rightarrow 800 = 160a \\Rightarrow a = 5$ m/s²."
            },
            {
                "q": "Which of the following is a vector quantity?",
                "options": ["Distance", "Speed", "Displacement", "Time"],
                "ans": "C",
                "exp": "Displacement has both magnitude and direction, making it a vector quantity."
            },
            {
                "q": "A cyclist goes around a circular path of circumference 220 m in 44 seconds. What is the speed of the cyclist?",
                "options": ["5 m/s", "10 m/s", "0.2 m/s", "50 m/s"],
                "ans": "A",
                "exp": "$\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}} = \\frac{220\\text{ m}}{44\\text{ s}} = 5$ m/s."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): The displacement of a moving body can be zero even if the distance travelled is non-zero.<br>Reason (R): Displacement is the vector representing the shortest path from initial to final position.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "If an object returns to its starting point, initial and final coordinates coincide, making displacement zero while distance is $>0$."
            },
            {
                "q": "Assertion (A): Motion in a circular track with constant speed is an accelerated motion.<br>Reason (R): Velocity is a vector, and in circular motion, the direction of motion changes continuously at every instant.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Even though magnitude of velocity (speed) is fixed, change in direction means velocity changes, causing continuous centripetal acceleration."
            },
            {
                "q": "Assertion (A): The slope of a velocity-time graph gives the acceleration of the body.<br>Reason (R): Acceleration is defined as the time rate of change of displacement.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false because acceleration is the rate of change of *velocity*, not displacement (rate of change of displacement is velocity)."
            },
            {
                "q": "Assertion (A): An object can have constant speed and varying velocity.<br>Reason (R): Speed is a scalar quantity while velocity depends on both magnitude and direction.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "In uniform circular motion, speed is constant while direction changes, resulting in varying velocity."
            },
            {
                "q": "Assertion (A): When a body moves with uniform velocity, its acceleration is non-zero.<br>Reason (R): Uniform velocity means velocity is changing at a uniform rate.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "Both (A) and (R) are false."
                ],
                "ans": "D",
                "exp": "Both statements are false. Uniform velocity means velocity remains constant ($v - u = 0$), so acceleration is strictly zero."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Velocity-Time Graph Analysis of an Electric Metro Train<br>An electric metro train starts from Station A and travels to Station B along a straight track. The velocity-time profile is recorded: During the first 10 seconds, it accelerates uniformly from 0 to 20 m/s. For the next 30 seconds, it maintains a constant cruise velocity of 20 m/s. Finally, brakes are applied and it decelerates uniformly to a complete stop in 10 seconds at Station B.",
                "q": "What is the acceleration of the metro train during the first 10 seconds?",
                "options": ["1 m/s²", "2 m/s²", "4 m/s²", "0.5 m/s²"],
                "ans": "B",
                "exp": "$a = \\frac{20 - 0}{10} = 2$ m/s²."
            },
            {
                "q": "What is the distance travelled by the train during the 30-second period of uniform velocity?",
                "options": ["300 m", "600 m", "450 m", "200 m"],
                "ans": "B",
                "exp": "$\\text{Distance} = v \\times t = 20\\text{ m/s} \\times 30\\text{ s} = 600$ m."
            },
            {
                "q": "What is the magnitude of retardation (deceleration) during the braking phase in the last 10 seconds?",
                "options": ["-2 m/s²", "2 m/s²", "1 m/s²", "0.5 m/s²"],
                "ans": "B",
                "exp": "Retardation is the magnitude of negative acceleration: $a = \\frac{0 - 20}{10} = -2$ m/s², so retardation $= 2$ m/s²."
            },
            {
                "q": "What is the total distance between Station A and Station B?",
                "options": ["600 m", "700 m", "800 m", "1000 m"],
                "ans": "C",
                "exp": "Total distance is the area of trapezoid: $\\text{Area} = \\frac{1}{2} \\times (\\text{sum of parallel sides}) \\times \\text{height} = \\frac{1}{2} \\times (50 + 30) \\times 20 = 40 \\times 20 = 800$ m."
            },
            {
                "q": "What was the average speed of the train for the entire journey from Station A to Station B?",
                "options": ["16 m/s", "20 m/s", "12 m/s", "10 m/s"],
                "ans": "A",
                "exp": "$\\text{Average speed} = \\frac{\\text{Total distance}}{\\text{Total time}} = \\frac{800\\text{ m}}{50\\text{ s}} = 16$ m/s."
            }
        ]
    },
    {
        "num": 5,
        "title": "Exploring Mixtures and their Separation",
        "file": "chapter_05_mixtures.html",
        "description": "Homogeneous & heterogeneous mixtures, true solutions, suspensions, colloids, Tyndall effect, and separation methods.",
        "questions": [
            {
                "q": "Which of the following is a homogeneous mixture?",
                "options": ["Chalk powder in water", "A brass alloy of copper and zinc", "Muddy pond water", "Oil and water mixture"],
                "ans": "B",
                "exp": "Brass is a solid solution (alloy) having uniform composition and properties throughout, making it a homogeneous mixture."
            },
            {
                "q": "What is the mass by mass percentage concentration of a solution prepared by dissolving 40 g of common salt in 360 g of water?",
                "options": ["11.1%", "10.0%", "9.0%", "12.5%"],
                "ans": "B",
                "exp": "$\\text{Mass of solution} = 40 + 360 = 400$ g. $\\text{Percentage} = \\frac{40}{400} \\times 100 = 10.0\\%$."
            },
            {
                "q": "Which property correctly characterizes a true solution?",
                "options": ["Particle size is greater than 100 nm", "Solute particles settle down on standing", "Particles pass completely through standard filter paper", "It clearly scatters a light beam (Tyndall effect)"],
                "ans": "C",
                "exp": "In a true solution, solute particles are $< 1$ nm, pass through filter pores, do not scatter light, and never settle under gravity."
            },
            {
                "q": "The scattering of a visible beam of light when passed through a colloidal solution is known as:",
                "options": ["Raman effect", "Tyndall effect", "Doppler effect", "Photoelectric effect"],
                "ans": "B",
                "exp": "Colloidal particles are large enough (1-100 nm) to scatter visible light rays, illuminating the path of the beam (Tyndall effect)."
            },
            {
                "q": "Which of the following mixtures will show a noticeable Tyndall effect?",
                "options": ["Salt solution", "Copper sulphate solution", "Milk", "Sugar solution"],
                "ans": "C",
                "exp": "Milk is a colloidal emulsion of fat and protein droplets in water, which scatters light and shows Tyndall effect."
            },
            {
                "q": "In a colloidal aerosol like fog, clouds, and mist, what are the dispersed phase and dispersion medium?",
                "options": ["Dispersed phase: Liquid, Dispersion medium: Gas", "Dispersed phase: Gas, Dispersion medium: Liquid", "Dispersed phase: Solid, Dispersion medium: Liquid", "Dispersed phase: Gas, Dispersion medium: Gas"],
                "ans": "A",
                "exp": "In fog and mist, tiny liquid water droplets (dispersed phase) are dispersed in air/gas (dispersion medium)."
            },
            {
                "q": "Which separation technique is based on difference in density where heavier particles are forced to the bottom by rapid spinning?",
                "options": ["Fractional distillation", "Centrifugation", "Sublimation", "Chromatography"],
                "ans": "B",
                "exp": "Centrifugation spins mixtures at high speed, forcing denser particles to the bottom (used for separating cream from milk and blood diagnostics)."
            },
            {
                "q": "Two miscible liquids having boiling points of 65°C and 78°C (difference of 13°C) can be best separated using:",
                "options": ["Simple distillation", "Fractional distillation", "Separating funnel", "Filtration"],
                "ans": "B",
                "exp": "When boiling point difference is less than 25 K (or 25°C), fractional distillation with a fractionating column is required."
            },
            {
                "q": "Which mixture can be separated by the method of sublimation?",
                "options": ["Sodium chloride and water", "Ammonium chloride and sodium chloride", "Iron filings and sand", "Water and kerosene oil"],
                "ans": "B",
                "exp": "Ammonium chloride sublimes directly into vapor upon heating, leaving non-sublimable sodium chloride behind."
            },
            {
                "q": "The technique of paper chromatography separates solutes present in a mixture based on differences in their:",
                "options": ["Densities", "Boiling points", "Solubility in the mobile solvent phase", "Magnetic properties"],
                "ans": "C",
                "exp": "Solutes with higher solubility travel faster with the solvent front up the chromatography paper, separating into distinct bands."
            },
            {
                "q": "Crystallization is preferred over simple evaporation to dryness for purifying salts like copper sulphate because:",
                "options": ["It requires less time", "Some solids decompose or get charred upon heating to complete dryness", "Evaporation removes all impurities completely", "Crystallization requires toxic solvents"],
                "ans": "B",
                "exp": "Evaporating to dryness can decompose salts (charring) and leaves soluble impurities behind, whereas crystallization produces pure crystals."
            },
            {
                "q": "A mixture of kerosene oil and water is heterogeneous and can be separated using:",
                "options": ["Fractionating column", "A separating funnel", "Sublimation apparatus", "Chromatography paper"],
                "ans": "B",
                "exp": "Immiscible liquids form distinct layers based on density and are separated using a separating funnel with a stopcock."
            },
            {
                "q": "What type of colloid is shaving cream, where gas is dispersed in a liquid?",
                "options": ["Sol", "Gel", "Foam", "Emulsion"],
                "ans": "C",
                "exp": "A colloid with gas dispersed in a liquid medium is termed a foam."
            },
            {
                "q": "When a beam of sunlight enters a dusty, dimly lit room through a small window hole, the path of light becomes visible because:",
                "options": ["Light is absorbed by dust", "Air dust and smoke particles scatter light (Tyndall effect)", "Sunlight consists of ultraviolet rays", "Light slows down to zero speed"],
                "ans": "B",
                "exp": "Suspended dust and smoke particles in air act as colloidal scattering centers, making the light beam visible."
            },
            {
                "q": "A solution that contains the maximum amount of solute dissolved at a given specific temperature is termed a:",
                "options": ["Unsaturated solution", "Saturated solution", "Supersaturated suspension", "Colloid"],
                "ans": "B",
                "exp": "A saturated solution can dissolve no more solute at that specified temperature."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): Air is considered a homogeneous mixture of gases.<br>Reason (R): The gaseous components of air are uniformly mixed and cannot be distinguished by physical boundaries.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Air has a uniform chemical composition of nitrogen, oxygen, argon, etc., without visible phase boundaries."
            },
            {
                "q": "Assertion (A): A suspension is a heterogeneous mixture and its particles settle down under gravity when left undisturbed.<br>Reason (R): The solute particles in a suspension are larger than 100 nm and are visible to the naked eye.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because suspension particles are heavy ($>100$ nm), thermal molecular motion cannot overcome gravity, causing sedimentation."
            },
            {
                "q": "Assertion (A): Sugar dissolved in water can be separated by filtration using filter paper.<br>Reason (R): Sugar solution is a true solution whose particle size is less than 1 nm.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Assertion is false (sugar particles pass through filter pores easily). Reason is true (true solution particle size $<1$ nm)."
            },
            {
                "q": "Assertion (A): Fractional distillation is used to separate different gases from liquid air.<br>Reason (R): Different gases in air have different boiling points with differences greater than 100°C.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false: The boiling points of nitrogen (-196°C), argon (-186°C), and oxygen (-183°C) differ by only 3°C to 13°C (much less than 100°C)."
            },
            {
                "q": "Assertion (A): Tincture of iodine is a solution of solid iodine dissolved in liquid alcohol.<br>Reason (R): In tincture of iodine, alcohol acts as the solute and iodine acts as the solvent.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false because iodine is the dissolved solid (solute) and alcohol is the dissolving liquid (solvent)."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Forensic Ink Analysis by Chromatography<br>A forensic examiner is investigating a suspicious cheque where the written payment amount seems to have been altered with a second black ink pen. The examiner places a drop of the cheque's ink alongside standard ink samples from Pen X and Pen Y onto a strip of chromatography filter paper. The paper is suspended in a beaker containing a solvent of water and ethanol. As the solvent rises, the cheque ink splits into three distinct colored dye spots (blue, yellow, pink) that match exactly with the spot heights of Pen Y, while Pen X yields only blue and purple spots.",
                "q": "What is the physical principle underlying the separation in paper chromatography?",
                "options": ["Differential boiling points of dyes", "Differential solubility and adsorption rates of pigments in the mobile solvent", "Difference in magnetic attraction", "Sublimation temperatures of ink"],
                "ans": "B",
                "exp": "Chromatography separates mixtures based on relative affinity for the stationary phase (paper) versus mobile phase (solvent)."
            },
            {
                "q": "Based on the examiner's observation, which pen was used to write or alter the cheque?",
                "options": ["Pen X", "Pen Y", "Neither Pen X nor Pen Y", "Both pens simultaneously"],
                "ans": "B",
                "exp": "The dye components and spot positions of the cheque ink matched Pen Y identically."
            },
            {
                "q": "Which component in paper chromatography acts as the stationary phase?",
                "options": ["The rising water-ethanol solvent", "The strip of chromatography paper", "The ink solvent vapor", "The beaker glass wall"],
                "ans": "B",
                "exp": "The porous paper matrix through which the solvent migrates is the stationary phase."
            },
            {
                "q": "The dye component that travels the fastest and reaches highest on the paper strip is the one that:",
                "options": ["Has the greatest mass", "Is most soluble in the moving solvent", "Has the highest boiling point", "Is least soluble in water"],
                "ans": "B",
                "exp": "Components with higher solubility in the solvent move faster and travel further along the paper."
            },
            {
                "q": "Which of the following is another practical real-world application of chromatography?",
                "options": ["Purifying drinking water from muddy lakes", "Separating drugs from blood samples in pathology", "Extracting common salt from seawater", "Separating iron scrap from garbage"],
                "ans": "B",
                "exp": "Medical and forensic laboratories use chromatography to isolate and identify pharmaceutical compounds and toxins from blood."
            }
        ]
    },
    {
        "num": 6,
        "title": "How Forces Affect Motion",
        "file": "chapter_06_forces.html",
        "description": "Balanced & unbalanced forces, inertia, Newton's first, second, and third laws of motion, and conservation of momentum.",
        "questions": [
            {
                "q": "Which of the following is an effect that a balanced force system CAN produce on an object?",
                "options": ["Change in the speed of the object", "Change in the direction of moving object", "Change in the shape and size of the object", "Causing acceleration from rest"],
                "ans": "C",
                "exp": "Balanced forces have zero net force, so they cannot accelerate an object, but equal opposite forces can compress or distort its shape (e.g., squeezing a rubber ball)."
            },
            {
                "q": "The inertia of an object depends fundamentally and directly on its:",
                "options": ["Velocity", "Mass", "Volume", "Acceleration"],
                "ans": "B",
                "exp": "Mass is the quantitative measure of inertia. A heavier body has greater resistance to changes in its state of motion."
            },
            {
                "q": "When a moving passenger bus suddenly takes a sharp turn to the right, the passengers lean towards the left due to:",
                "options": ["Inertia of rest", "Inertia of motion", "Inertia of direction", "Gravitational pull"],
                "ans": "C",
                "exp": "Due to inertia of direction, passenger bodies tend to maintain their original straight-line path when the bus turns right."
            },
            {
                "q": "What is the momentum of an object of mass $m$ moving with a velocity $v$?",
                "options": ["$(mv)^2$", "$m v^2$", "$\\frac{1}{2} m v^2$", "$m v$"],
                "ans": "D",
                "exp": "Linear momentum is defined as the product of mass and velocity ($p = mv$), with SI unit $kg \\cdot m/s$."
            },
            {
                "q": "What constant force is required to accelerate a 5 kg block from 4 m/s to 10 m/s in 3 seconds?",
                "options": ["10 N", "15 N", "20 N", "30 N"],
                "ans": "A",
                "exp": "$a = \\frac{10 - 4}{3} = 2$ m/s². $F = ma = 5 \\times 2 = 10$ N."
            },
            {
                "q": "A cricket fielder pulls his hands backwards while catching a fast-moving ball. This action protects the fielder by:",
                "options": ["Decreasing the time of impact to maximize force", "Increasing the time of impact, thereby reducing the rate of change of momentum and impact force", "Increasing the momentum of the ball", "Decreasing the mass of the ball"],
                "ans": "B",
                "exp": "From $F = \\frac{\\Delta p}{\\Delta t}$, increasing duration $\\Delta t$ drastically reduces the impact force $F$ felt by the palms."
            },
            {
                "q": "According to Newton's Third Law of Motion, action and reaction forces:",
                "options": ["Act on the same body in the same direction", "Act on two different bodies in opposite directions simultaneously", "Act on the same body in opposite directions", "Cancel each other out completely so no motion occurs"],
                "ans": "B",
                "exp": "Action and reaction forces always act on two different interacting objects simultaneously with equal magnitude and opposite direction."
            },
            {
                "q": "A gun of mass 4 kg fires a bullet of mass 0.02 kg with a muzzle velocity of 400 m/s. What is the recoil velocity of the gun?",
                "options": ["-2 m/s", "-4 m/s", "-1 m/s", "-8 m/s"],
                "ans": "A",
                "exp": "$m_1 v_1 + m_2 v_2 = 0 \\Rightarrow 4 \\times v_{gun} + 0.02 \\times 400 = 0 \\Rightarrow 4 v_{gun} = -8 \\Rightarrow v_{gun} = -2$ m/s."
            },
            {
                "q": "A 1000 kg car travelling at 20 m/s collides with a wall and comes to rest in 0.1 s. The average force exerted on the car during impact is:",
                "options": ["20,000 N", "200,000 N", "2,000 N", "2,000,000 N"],
                "ans": "B",
                "exp": "$F = \\frac{m(v - u)}{t} = \\frac{1000(0 - 20)}{0.1} = -200,000$ N."
            },
            {
                "q": "Why does a swimmer push water backwards with hands and feet to propel himself forward in a pool?",
                "options": ["Because water is denser than air", "According to Newton's third law, the water exerts an equal and opposite forward reaction force on the swimmer", "To increase his body weight", "To reduce water friction"],
                "ans": "B",
                "exp": "Pushing water backwards (action) produces an equal and opposite forward push (reaction) from the water on the swimmer."
            },
            {
                "q": "Which famous Italian scientist first deduced that an object moving on a frictionless horizontal plane would continue to move with constant velocity indefinitely?",
                "options": ["Isaac Newton", "Galileo Galilei", "Archimedes", "Johannes Kepler"],
                "ans": "B",
                "exp": "Galileo studied motion on double inclined planes and concluded that an object in motion continues moving unless resisted by friction."
            },
            {
                "q": "If the net external unbalanced force acting on an object is zero, the acceleration of the object is:",
                "options": ["Continuously increasing", "Zero", "9.8 m/s²", "Dependent on shape"],
                "ans": "B",
                "exp": "By $F = ma$, if $F_{net} = 0$, then $a = 0$. The object maintains constant velocity or remains at rest."
            },
            {
                "q": "When a carpet is beaten with a stick, dust particles fall out. This phenomenon is explained by:",
                "options": ["Inertia of rest of dust particles", "Inertia of motion of the carpet", "Newton's third law only", "Electrostatic attraction"],
                "ans": "A",
                "exp": "The carpet moves forward when struck, but dust particles tend to remain in their state of rest due to inertia and fall away."
            },
            {
                "q": "A force of 5 N acts on a mass $m_1$ giving it an acceleration of 10 m/s², and on mass $m_2$ giving it an acceleration of 20 m/s². What acceleration would it give if both masses are tied together?",
                "options": ["6.67 m/s²", "15 m/s²", "5.0 m/s²", "30 m/s²"],
                "ans": "A",
                "exp": "$m_1 = 5/10 = 0.5$ kg, $m_2 = 5/20 = 0.25$ kg. Combined mass $M = 0.75$ kg. $a = F/M = 5/0.75 = 6.67$ m/s²."
            },
            {
                "q": "The principle of rocket propulsion is primarily based on:",
                "options": ["Conservation of energy", "Newton's third law and conservation of linear momentum", "Newton's first law only", "Pascal's principle"],
                "ans": "B",
                "exp": "Expulsion of exhaust gases at high speed downward imparts an equal upward thrust (momentum conservation / action-reaction)."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): A heavy iron ball has greater inertia than a football of identical size.<br>Reason (R): The inertia of an object is directly proportional to its mass.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Mass determines inertia. Because iron is much denser and more massive than a football, it offers greater resistance to acceleration."
            },
            {
                "q": "Assertion (A): Action and reaction forces never cancel each other out.<br>Reason (R): Action and reaction act on two completely different bodies.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Forces cancel only when acting on the same single body. Action and reaction act on different interacting bodies."
            },
            {
                "q": "Assertion (A): Newton's second law gives a quantitative measurement of force.<br>Reason (R): Force is directly proportional to the rate of change of momentum.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "The formula $F = ma$ derived from Newton's second law provides the mathematical definition and metric value of force."
            },
            {
                "q": "Assertion (A): Passengers in a car must wear safety seatbelts.<br>Reason (R): In a sudden collision, seatbelts provide an external force to restrain the passengers' bodies which tend to continue forward due to inertia of motion.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "When a car stops abruptly, inertia carries unbelted occupants forward into windshield or steering wheel; seatbelts supply the decelerating force."
            },
            {
                "q": "Assertion (A): When a bullet is fired from a rifle, the rifle recoils with the same acceleration as the bullet.<br>Reason (R): The force exerted on the rifle is equal and opposite to the force on the bullet.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "D",
                "exp": "Reason is true (forces are equal and opposite). But Assertion is false because $a = F/m$; since the rifle is much more massive, its acceleration is far smaller than the bullet's."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: High Jump Safety and Collision Mechanics<br>In a school athletics track and field championship, athletes competing in the high jump event were instructed to land on a 50 cm thick foam cushion mattress. In previous decades, high jumpers landed on packed sand or hard ground. Physical training instructors demonstrated that landing on the thick foam cushion prevents severe spinal and limb injuries because the foam compresses gradually upon impact.",
                "q": "What physical quantity remains the same when an athlete lands on hard ground versus on a foam mattress from a given height?",
                "options": ["Impact force", "Duration of collision", "Total change in momentum of the athlete", "Maximum compression distance"],
                "ans": "C",
                "exp": "The athlete has the same mass and reaches the ground with the same impact velocity, so the change in momentum $\\Delta p = 0 - mv$ is identical in both cases."
            },
            {
                "q": "How does the soft foam mattress reduce the impact force felt by the athlete?",
                "options": ["By reducing the athlete's mass", "By increasing the time duration taken for the athlete's momentum to become zero", "By increasing gravity", "By completely eliminating energy transformation"],
                "ans": "B",
                "exp": "Foam compresses over time $\\Delta t$. Because $F = \\frac{\\Delta p}{\\Delta t}$, increasing impact time substantially lowers impact force."
            },
            {
                "q": "If an athlete of mass 60 kg hits the cushion with a downward velocity of 6 m/s and comes to rest in 0.3 s, the average retarding force exerted by the cushion is:",
                "options": ["120 N", "1200 N", "3600 N", "600 N"],
                "ans": "B",
                "exp": "$F = \\frac{m \\Delta v}{\\Delta t} = \\frac{60 \\times 6}{0.3} = 1200$ N."
            },
            {
                "q": "If the same athlete had landed on hard concrete stopping in just 0.01 s, the impact force would have been:",
                "options": ["1,200 N", "12,000 N", "36,000 N", "360 N"],
                "ans": "C",
                "exp": "$F = \\frac{60 \\times 6}{0.01} = 36,000$ N (30 times higher, enough to fracture bones!)."
            },
            {
                "q": "Which similar practical safety mechanism utilizes this same impulse-momentum principle?",
                "options": ["Automobile air bags", "Packing fragile glass items in bubble wrap", "Shock absorbers in motorcycles", "All of the above"],
                "ans": "D",
                "exp": "Airbags, bubble wrap, and shock absorbers all increase collision contact duration to minimize peak impact force."
            }
        ]
    },
    {
        "num": 7,
        "title": "Work, Energy, and Simple Machines",
        "file": "chapter_07_work_energy.html",
        "description": "Work done by constant force, kinetic & potential energy, work-energy theorem, power, and simple machines (levers, pulleys).",
        "questions": [
            {
                "q": "A porter lifts a luggage luggage of 15 kg from the ground and puts it on his head 1.5 m above the ground. Taking $g = 10$ m/s², the work done by him against gravity is:",
                "options": ["150 J", "225 J", "22.5 J", "15 J"],
                "ans": "B",
                "exp": "$W = mgh = 15 \\times 10 \\times 1.5 = 225$ J."
            },
            {
                "q": "A satellite revolves around the Earth in a circular orbit under the gravitational pull of the Earth. What is the work done by gravity on the satellite in one complete revolution?",
                "options": ["Positive and equal to kinetic energy", "Zero", "Negative", "Infinite"],
                "ans": "B",
                "exp": "Gravitational force is directed towards the Earth's center (perpendicular to tangential displacement, $\\theta = 90^\\circ$). Since $W = F s \\cos 90^\\circ = 0$, work done is zero."
            },
            {
                "q": "What happens to the kinetic energy of a moving object if its speed is doubled?",
                "options": ["It is doubled", "It becomes four times its initial value", "It is halved", "It remains unchanged"],
                "ans": "B",
                "exp": "$E_k = \\frac{1}{2}mv^2$. Since $E_k \\propto v^2$, doubling speed ($2v$) makes kinetic energy $(2)^2 = 4$ times."
            },
            {
                "q": "The work done by friction on an object sliding across a rough floor is always:",
                "options": ["Positive", "Negative", "Zero", "Imaginary"],
                "ans": "B",
                "exp": "Friction acts in the direction opposite to displacement ($\\theta = 180^\\circ$). Therefore, $W = F s \\cos 180^\\circ = -F s$ (negative work)."
            },
            {
                "q": "An electric bulb consumes 1000 J of electrical energy in 10 seconds. The power of the bulb is:",
                "options": ["100 W", "10,000 W", "10 W", "0.1 W"],
                "ans": "A",
                "exp": "$\\text{Power} = \\frac{\\text{Energy}}{\\text{Time}} = \\frac{1000\\text{ J}}{10\\text{ s}} = 100$ Watts."
            },
            {
                "q": "One commercial unit of electrical energy (1 kilowatt-hour or 1 kWh) is equal to how many Joules?",
                "options": ["$3.6 \\times 10^5$ J", "$3.6 \\times 10^6$ J", "$3.6 \\times 10^4$ J", "$1.0 \\times 10^3$ J"],
                "ans": "B",
                "exp": "$1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6$ J."
            },
            {
                "q": "A body of mass 2 kg is dropped freely from a height of 20 m. Its kinetic energy just before striking the ground is ($g = 10$ m/s²):",
                "options": ["200 J", "400 J", "40 J", "800 J"],
                "ans": "B",
                "exp": "By conservation of mechanical energy, final $E_k = \\text{initial } E_p = mgh = 2 \\times 10 \\times 20 = 400$ J."
            },
            {
                "q": "The mechanical advantage (MA) of a simple machine is defined as the ratio of:",
                "options": ["Effort to Load", "Load to Effort", "Work output to Work input", "Distance moved by effort to distance moved by load"],
                "ans": "B",
                "exp": "Mechanical Advantage $= \\frac{\\text{Load}}{\\text{Effort}}$. A machine with $MA > 1$ acts as a force multiplier."
            },
            {
                "q": "In a Class 1 lever, which component is located in the middle between Load and Effort?",
                "options": ["Fulcrum", "Load", "Effort", "Resistance"],
                "ans": "A",
                "exp": "Class 1 lever has the Fulcrum in the middle (e.g., seesaw, crowbar, scissors). Class 2 has Load in the middle; Class 3 has Effort in the middle."
            },
            {
                "q": "A wheelbarrow and a nutcracker are classic examples of which class of lever?",
                "options": ["Class 1 lever", "Class 2 lever", "Class 3 lever", "Compound pulley"],
                "ans": "B",
                "exp": "In a wheelbarrow and nutcracker, the Load is positioned between the Fulcrum and the Effort (Class 2 lever, $MA > 1$)."
            },
            {
                "q": "An electric motor takes 2 minutes to lift a 200 kg mass through a vertical height of 30 m. The power of the motor is ($g = 10$ m/s²):",
                "options": ["500 W", "60,000 W", "250 W", "1000 W"],
                "ans": "A",
                "exp": "$W = mgh = 200 \\times 10 \\times 30 = 60,000$ J. Time $t = 2 \\times 60 = 120$ s. $P = \\frac{60000}{120} = 500$ W."
            },
            {
                "q": "A compressed spring possesses which form of potential energy?",
                "options": ["Gravitational potential energy", "Elastic potential energy", "Chemical energy", "Thermal energy"],
                "ans": "B",
                "exp": "Work done against restoring spring force is stored as elastic potential energy due to configuration change."
            },
            {
                "q": "A force of 10 N displaces an object by 5 m at an angle of 60° to the direction of the force. The work done is ($\\cos 60° = 0.5$):",
                "options": ["50 J", "25 J", "0 J", "100 J"],
                "ans": "B",
                "exp": "$W = F s \\cos 60^\\circ = 10 \\times 5 \\times 0.5 = 25$ J."
            },
            {
                "q": "Which of the following devices transforms chemical energy directly into electrical energy?",
                "options": ["Electric generator", "Dry cell / Electric battery", "Solar cell", "Electric toaster"],
                "ans": "B",
                "exp": "A chemical battery/cell converts stored chemical energy into electrical energy through redox reactions."
            },
            {
                "q": "An ideal single fixed pulley has a mechanical advantage of:",
                "options": ["1", "2", "4", "0.5"],
                "ans": "A",
                "exp": "A single fixed pulley does not multiply force ($MA = 1$); it simply changes the direction of the applied effort to make lifting convenient."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): When a student holds a heavy 20 kg school bag motionless on his shoulder for 30 minutes, no scientific work is done.<br>Reason (R): Work is done only when a force produces a non-zero displacement in the object.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because displacement $s = 0$, scientific work $W = F \\times s = 0$, despite physiological muscular fatigue."
            },
            {
                "q": "Assertion (A): The total mechanical energy of a freely falling body under gravity remains constant at every point in its fall.<br>Reason (R): As the body falls, its potential energy decreases by the exact amount by which its kinetic energy increases.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "In the absence of air resistance, mechanical energy $E_k + E_p$ is conserved; gravitational potential energy converts completely into kinetic energy."
            },
            {
                "q": "Assertion (A): A pair of tweezers or sugar tongs is a Class 3 lever with mechanical advantage less than 1.<br>Reason (R): In a Class 3 lever, the Effort is applied between the Fulcrum and the Load, acting as a speed/distance multiplier rather than a force multiplier.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "In Class 3 levers, effort arm is shorter than load arm ($MA < 1$), requiring more effort force but providing precision and amplified displacement."
            },
            {
                "q": "Assertion (A): Power is the scalar product of force and velocity.<br>Reason (R): Power measures the rate at which energy is consumed or work is executed.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "B",
                "exp": "Both are true ($P = W/t = F \\cdot v$), but the second statement is the definition rather than the derived proof of $F \\cdot v$."
            },
            {
                "q": "Assertion (A): A fast-moving bullet possesses high kinetic energy.<br>Reason (R): Kinetic energy of an object depends inversely on its velocity.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false because kinetic energy is directly proportional to the square of velocity ($E_k = \\frac{1}{2}mv^2$)."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Hydroelectric Power Station Energy Transformations<br>At a hydroelectric dam, water stored in a huge high-altitude reservoir at a height of 50 m falls through massive pipes (penstocks) onto turbine blades located at the base of the dam. The gushing water spins the turbines at high speed. The spinning turbine drives an electric generator that produces electricity, which is then transmitted via high-voltage transmission lines to illuminate homes and power industries.",
                "q": "What form of energy is stored in the reservoir water high above the dam?",
                "options": ["Kinetic energy", "Gravitational potential energy", "Chemical energy", "Thermal energy"],
                "ans": "B",
                "exp": "Water elevated to height $h$ possesses gravitational potential energy given by $mgh$."
            },
            {
                "q": "As water rushes down the penstock pipe towards the turbine, the energy transformation occurring is:",
                "options": ["Kinetic energy into chemical energy", "Potential energy into kinetic energy", "Electrical energy into potential energy", "Nuclear energy into thermal energy"],
                "ans": "B",
                "exp": "As water loses height, its potential energy is converted into kinetic energy of flowing water."
            },
            {
                "q": "If 2000 kg of water falls onto the turbine blades every second from a height of 50 m ($g = 10$ m/s²), the potential energy converted per second (power) is:",
                "options": ["100 kW", "500 kW", "1000 kW (1 MW)", "2000 kW"],
                "ans": "C",
                "exp": "$\\text{Energy per second} = mgh = 2000 \\times 10 \\times 50 = 1,000,000$ J/s $= 1000$ kW $= 1$ Megawatt."
            },
            {
                "q": "What device converts the kinetic energy of the rotating turbine shaft into electrical energy?",
                "options": ["Electric motor", "Electric generator / Alternator", "Step-down transformer", "Electric battery"],
                "ans": "B",
                "exp": "A generator uses electromagnetic induction to convert rotational kinetic energy into electricity."
            },
            {
                "q": "Which fundamental universal law confirms that no new energy is created, only transformed from one form to another during this process?",
                "options": ["Newton's first law of motion", "Law of conservation of energy", "Kepler's third law", "Hooke's law of elasticity"],
                "ans": "B",
                "exp": "The law of conservation of energy states that energy cannot be created or destroyed, only transformed."
            }
        ]
    },
    {
        "num": 8,
        "title": "Journey Inside the Atom",
        "file": "chapter_08_atom.html",
        "description": "Subatomic particles (electrons, protons, neutrons), Thomson & Rutherford models, Bohr's atomic model, Bohr-Bury scheme, valency, isotopes & isobars.",
        "questions": [
            {
                "q": "Who discovered the cathode rays (negatively charged subatomic electrons) in 1897?",
                "options": ["John Dalton", "J.J. Thomson", "Ernest Rutherford", "James Chadwick"],
                "ans": "B",
                "exp": "J.J. Thomson discovered the electron through cathode ray tube experiments, demonstrating that atoms are divisible."
            },
            {
                "q": "Canal rays discovered by E. Goldstein in 1886 led to the identification of which positively charged subatomic particle?",
                "options": ["Electron", "Proton", "Neutron", "Positron"],
                "ans": "B",
                "exp": "E. Goldstein observed positively charged radiation passing through perforations in cathode rays (canal rays), identifying protons."
            },
            {
                "q": "In Rutherford's famous alpha-particle scattering experiment, what metal foil was used because of its exceptional malleability?",
                "options": ["Aluminum foil", "Gold foil", "Silver foil", "Platinum foil"],
                "ans": "B",
                "exp": "Rutherford used gold foil because it could be hammered extremely thin (about 1000 atoms thick)."
            },
            {
                "q": "What surprising observation in Rutherford's alpha scattering experiment led to the discovery of the atomic nucleus?",
                "options": ["All alpha particles were absorbed", "Most particles were deflected by 90°", "Nearly 1 in 12,000 alpha particles rebounded backwards at nearly 180°", "Alpha particles turned into beta particles"],
                "ans": "C",
                "exp": "Alpha particles rebounding straight back showed that positive charge and almost all mass are concentrated in a tiny dense core (nucleus)."
            },
            {
                "q": "What major drawback of Rutherford's nuclear model was successfully resolved by Neils Bohr's atomic model?",
                "options": ["Failure to explain mass of neutron", "The orbital instability of accelerating electrons radiating energy and collapsing into the nucleus", "Inability to predict chemical bonds", "Inability to explain atomic weight of chlorine"],
                "ans": "B",
                "exp": "Classical physics stated accelerating charges radiate energy. Bohr proposed discrete non-radiating stationary energy orbits."
            },
            {
                "q": "According to the Bohr-Bury scheme, what is the maximum number of electrons that can be accommodated in the $M$-shell ($n = 3$)?",
                "options": ["8", "18", "32", "2"],
                "ans": "B",
                "exp": "Maximum electrons $= 2n^2$. For M-shell ($n=3$): $2(3^2) = 2 \\times 9 = 18$."
            },
            {
                "q": "An atom has atomic number $Z = 16$. What is the electron distribution in its $K, L,$ and $M$ shells?",
                "options": ["2, 8, 6", "2, 6, 8", "8, 6, 2", "2, 14"],
                "ans": "A",
                "exp": "Sulfur ($Z=16$): K-shell holds 2, L-shell holds 8, remaining 6 enter M-shell (2, 8, 6)."
            },
            {
                "q": "What is the valency of a chlorine atom having atomic number 17 and electronic configuration 2, 8, 7?",
                "options": ["7", "1", "8", "3"],
                "ans": "B",
                "exp": "Chlorine needs 1 electron to complete its valence octet. Valency $= 8 - 7 = 1$."
            },
            {
                "q": "Who discovered the neutral subatomic particle 'neutron' in 1932?",
                "options": ["Ernest Rutherford", "James Chadwick", "Niels Bohr", "Henry Moseley"],
                "ans": "B",
                "exp": "James Chadwick discovered neutrons by bombarding beryllium with alpha particles, observing neutral radiation of mass $\\approx 1$ u."
            },
            {
                "q": "An atom of an element has 11 protons, 12 neutrons, and 11 electrons. What are its atomic number ($Z$) and mass number ($A$)?",
                "options": ["$Z = 11, A = 12$", "$Z = 11, A = 23$", "$Z = 12, A = 23$", "$Z = 23, A = 11$"],
                "ans": "B",
                "exp": "$Z = \\text{protons} = 11$. $A = \\text{protons} + \\text{neutrons} = 11 + 12 = 23$ (Sodium)."
            },
            {
                "q": "Atoms of the same element having the same atomic number but different mass numbers are termed:",
                "options": ["Isobars", "Isotopes", "Isotones", "Isomers"],
                "ans": "B",
                "exp": "Isotopes have identical atomic numbers (same chemical properties) but different neutron counts (different mass numbers)."
            },
            {
                "q": "Which radioactive isotope is widely utilized in medical therapy for the treatment of cancer?",
                "options": ["Carbon-14", "Cobalt-60", "Iodine-131", "Uranium-235"],
                "ans": "B",
                "exp": "Cobalt-60 emits penetrating gamma rays utilized in targeted radiation therapy for cancer."
            },
            {
                "q": "Naturally occurring chlorine exists as two isotopes: $^{35}_{17}\\text{Cl}$ (75%) and $^{37}_{17}\\text{Cl}$ (25%). The average atomic mass of chlorine is:",
                "options": ["35.0 u", "36.0 u", "35.5 u", "37.0 u"],
                "ans": "C",
                "exp": "$\\text{Average mass} = \\left(35 \\times \\frac{75}{100}\\right) + \\left(37 \\times \\frac{25}{100}\\right) = 26.25 + 9.25 = 35.5$ u."
            },
            {
                "q": "Calcium ($^{40}_{20}\\text{Ca}$) and Argon ($^{40}_{18}\\text{Ar}$) have different atomic numbers but the same mass number (40). They are termed:",
                "options": ["Isotopes", "Isobars", "Allotropes", "Homologues"],
                "ans": "B",
                "exp": "Isobars are atoms of different elements having different atomic numbers but identical mass numbers."
            },
            {
                "q": "What is the maximum number of electrons that can be accommodated in the outermost valence shell of any stable atom?",
                "options": ["2", "8", "18", "32"],
                "ans": "B",
                "exp": "According to the octet rule of the Bohr-Bury scheme, the outermost valence shell cannot accommodate more than 8 electrons."
            },
            # Assertion-Reason (Q16-Q20)
            {
                "q": "Assertion (A): An atom as a whole is electrically neutral.<br>Reason (R): The number of positively charged protons in the nucleus equals the number of negatively charged electrons revolving around it.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Because proton charge ($+1$) balances electron charge ($-1$) and their numbers are equal, the net atomic charge is zero."
            },
            {
                "q": "Assertion (A): Isotopes of an element have identical chemical properties.<br>Reason (R): Chemical properties depend on the number and arrangement of valence electrons, which is identical in all isotopes of an element.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Chemical bonding involves valence electrons. Since isotopes have identical electron configurations, their chemical behavior is identical."
            },
            {
                "q": "Assertion (A): The mass of an atom is almost entirely concentrated inside its central nucleus.<br>Reason (R): Protons and neutrons (nucleons) reside in the nucleus, and the mass of electrons is negligibly small ($1/1840$ of a proton).",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "Each proton and neutron has a mass of $\\approx 1$ u, while an electron has negligible mass ($0.00054$ u)."
            },
            {
                "q": "Assertion (A): Noble gases like Helium, Neon, and Argon exhibit zero valency.<br>Reason (R): Their outermost shells have completely filled octets (or duplet in Helium), rendering them chemically unreactive.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "A",
                "exp": "With complete valence shells, noble gases do not gain, lose, or share electrons, hence valency $= 0$."
            },
            {
                "q": "Assertion (A): Thomson's atomic model is known as the plum pudding model.<br>Reason (R): Thomson proved that all the positive charge is concentrated in a tiny central nucleus.",
                "options": [
                    "Both (A) and (R) are true and (R) is the correct explanation of (A).",
                    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A).",
                    "(A) is true but (R) is false.",
                    "(A) is false but (R) is true."
                ],
                "ans": "C",
                "exp": "Assertion is true. Reason is false: Thomson proposed positive charge is distributed uniformly throughout a sphere; the tiny nucleus was discovered by Rutherford."
            },
            # Case-Based Questions (Q21-Q25)
            {
                "case_intro": "Case Study: Atomic Structure of Elements X, Y, and Z<br>Study the table below representing three neutral elements and answer questions 21 to 25:<br><br><table style='border-collapse:collapse;width:100%;margin:8px 0;font-size:12px;'><thead><tr style='background:#e2e8f0;'><th style='border:1px solid #cbd5e1;padding:4px 8px;'>Element</th><th style='border:1px solid #cbd5e1;padding:4px 8px;'>Atomic Number (Z)</th><th style='border:1px solid #cbd5e1;padding:4px 8px;'>Mass Number (A)</th><th style='border:1px solid #cbd5e1;padding:4px 8px;'>Neutrons</th></tr></thead><tbody><tr><td style='border:1px solid #cbd5e1;padding:4px 8px;'><b>Element X</b></td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>6</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>12</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>6</td></tr><tr><td style='border:1px solid #cbd5e1;padding:4px 8px;'><b>Element Y</b></td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>6</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>14</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>8</td></tr><tr><td style='border:1px solid #cbd5e1;padding:4px 8px;'><b>Element Z</b></td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>7</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>14</td><td style='border:1px solid #cbd5e1;padding:4px 8px;'>7</td></tr></tbody></table>",
                "q": "What is the relationship between Element X and Element Y?",
                "options": ["They are isobars", "They are isotopes of carbon", "They are allotropes of nitrogen", "They have different numbers of electrons"],
                "ans": "B",
                "exp": "Both have $Z = 6$ (carbon) but different mass numbers (12 and 14); hence, they are isotopes."
            },
            {
                "q": "What is the relationship between Element Y and Element Z?",
                "options": ["They are isotopes", "They are isobars", "They belong to the same group", "They have identical chemical properties"],
                "ans": "B",
                "exp": "Element Y ($^{14}_6\\text{C}$) and Element Z ($^{14}_7\\text{N}$) have different atomic numbers (6 and 7) but the same mass number (14); they are isobars."
            },
            {
                "q": "What is the electronic configuration of Element X?",
                "options": ["2, 4", "2, 8, 2", "6, 0", "2, 2, 2"],
                "ans": "A",
                "exp": "For $Z = 6$, electrons $= 6$. Distribution is K-shell = 2, L-shell = 4 (2, 4)."
            },
            {
                "q": "What is the valency of Element Z (atomic number 7)?",
                "options": ["5", "3", "7", "1"],
                "ans": "B",
                "exp": "For $Z = 7$, configuration is 2, 5. To complete its octet, it requires 3 electrons. Valency $= 8 - 5 = 3$."
            },
            {
                "q": "Which radioactive isotope among X, Y, or Z is used in archaeological radiocarbon dating to determine the age of ancient fossils?",
                "options": ["Element X (Carbon-12)", "Element Y (Carbon-14)", "Element Z (Nitrogen-14)", "None of these"],
                "ans": "B",
                "exp": "Carbon-14 (Element Y) is a beta-emitting radioactive isotope with a half-life of 5,730 years used in radiocarbon dating."
            }
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Science - {chapter_title} - Question Paper</title>
  <link rel="stylesheet" href="exam-style.css">
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<div class="screen-wrapper">

  <!-- Interactive Control Bar (Hidden on Print) -->
  <div class="toolbar no-print">
    <div class="toolbar-title">
      <span>📚 CBSE CLASS 9 SCIENCE | CHAPTER {chapter_num}</span>
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
    <div class="exam-title" style="font-size: 13.5px; color: #334155; margin-top: 3px;">
      SUBJECT: SCIENCE (CLASS - IX) | CHAPTER {chapter_num}: {chapter_title_upper}
    </div>
    <div class="exam-meta-line">
      <span>TIME ALLOWED: 45 MINUTES</span>
      <span>MAXIMUM MARKS: 25</span>
      <span>PAPER CODE: 086/CH{chapter_num_padded}</span>
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
    <h4>General Instructions:</h4>
    <ol>
      <li>The question paper comprises <b>25 Multiple Choice Questions (MCQs)</b> of <b>1 mark each</b>.</li>
      <li><b>Section A (Q1 – Q15):</b> Standard Multiple Choice Questions with one correct option.</li>
      <li><b>Section B (Q16 – Q20):</b> Assertion-Reasoning based questions. Read both statements carefully before marking.</li>
      <li><b>Section C (Q21 – Q25):</b> Case-Study / Practical Data based questions.</li>
      <li>All questions are compulsory. There is no negative marking.</li>
      <li>Darken the corresponding circle on the <b>OMR Sheet</b> using a blue or black ballpoint pen.</li>
    </ol>
  </div>

  <!-- Questions Container -->
  <div class="questions-container">

    <div class="section-banner">
      <span>SECTION A: MULTIPLE CHOICE QUESTIONS (Q.1 TO Q.15)</span>
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
      <b>(D)</b> Assertion (A) is false but Reason (R) is true.
    </div>

{section_b_html}

    <div class="section-banner">
      <span>SECTION C: CASE-BASED / EXPERIMENTAL QUESTIONS (Q.21 TO Q.25)</span>
      <span>[5 MARKS]</span>
    </div>

{section_c_html}

  </div>

  <!-- Printable OMR Sheet Grid -->
  <div class="omr-section">
    <div class="omr-title">CBSE CANDIDATE OMR ANSWER RESPONSE GRID</div>
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
    <div class="answers-header">OFFICIAL ANSWER KEY & DETAILED EXPLANATIONS</div>
    <table class="answer-table">
      <thead>
        <tr>
          <th style="width: 50px;">Q. No.</th>
          <th style="width: 70px;">Correct</th>
          <th>Conceptual Explanation & Syllabus Rationale</th>
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
      ⬅️ Return to All Chapters Dashboard
    </a>
  </div>

</div>

<script>
// Answer key verification data
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
  alert("Test Evaluated!\\nYour Score: " + score + " / " + total + " (" + Math.round((score/total)*100) + "%)\\nScroll down to review correct answers and explanations.");
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

def generate_html_paper(ch):
    q_data = ch["questions"]
    answers_dict = {}
    
    sec_a_cards = []
    sec_b_cards = []
    sec_c_cards = []
    
    case_intro_shown = False
    
    for idx, item in enumerate(q_data):
        qnum = idx + 1
        answers_dict[qnum] = item["ans"]
        
        # Build options HTML
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
            
    # OMR grid HTML
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
        
    # Answer table rows
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
        
    full_html = HTML_TEMPLATE.format(
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

def generate_index_dashboard():
    cards_html = []
    for ch in CHAPTERS_DATA:
        card = f"""
        <div class="chapter-card">
          <div class="chapter-badge">CHAPTER {ch['num']}</div>
          <div class="chapter-title">{ch['title']}</div>
          <p class="chapter-desc">{ch['description']}</p>
          <div class="chapter-meta">
            <span>📝 25 MCQs (1 Mark each)</span>
            <span>⏱️ 45 Mins</span>
            <span>🎯 A4 Print Ready</span>
          </div>
          <div class="card-actions">
            <a href="{ch['file']}" class="btn-portal btn-primary">📖 Open & Practice Test</a>
            <a href="{ch['file']}?print=1" onclick="openAndPrint('{ch['file']}'); return false;" class="btn-portal btn-outline">🖨️ Direct Print (PDF)</a>
          </div>
        </div>
        """
        cards_html.append(card)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 9 Science - Half-Yearly Exam Preparation Portal</title>
  <link rel="stylesheet" href="exam-style.css">
  <style>
    body {{
      background: #f1f5f9;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .dashboard-container {{
      max-width: 1050px;
      margin: 30px auto;
      padding: 0 20px;
    }}
    .hero-banner {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
      color: #ffffff;
      padding: 35px 40px;
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.25);
      margin-bottom: 30px;
    }}
    .hero-banner h1 {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .hero-banner p {{
      font-size: 14.5px;
      color: #cbd5e1;
      line-height: 1.6;
    }}
    .badge-grid {{
      display: flex;
      gap: 12px;
      margin-top: 15px;
      flex-wrap: wrap;
    }}
    .badge-item {{
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(5px);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}
    .chapters-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(470px, 1fr));
      gap: 20px;
    }}
    .chapter-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 22px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .chapter-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
      border-color: #93c5fd;
    }}
    .chapter-badge {{
      display: inline-block;
      background: #e0e7ff;
      color: #3730a3;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
      align-self: flex-start;
    }}
    .chapter-title {{
      font-size: 16.5px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
    }}
    .chapter-desc {{
      font-size: 13px;
      color: #475569;
      line-height: 1.5;
      margin-bottom: 14px;
      flex-grow: 1;
    }}
    .chapter-meta {{
      display: flex;
      gap: 12px;
      font-size: 11.5px;
      color: #64748b;
      font-weight: 600;
      padding-top: 10px;
      border-top: 1px solid #f1f5f9;
      margin-bottom: 15px;
    }}
    .card-actions {{
      display: flex;
      gap: 10px;
    }}
    .btn-portal {{
      flex: 1;
      padding: 9px 12px;
      text-align: center;
      border-radius: 6px;
      font-weight: 600;
      font-size: 13px;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
    }}
    .btn-primary {{
      background: #1e40af;
      color: #ffffff;
      border: 1px solid #1e40af;
    }}
    .btn-primary:hover {{
      background: #1e3a8a;
    }}
    .btn-outline {{
      background: #ffffff;
      color: #1e293b;
      border: 1.5px solid #cbd5e1;
    }}
    .btn-outline:hover {{
      background: #f8fafc;
      border-color: #94a3b8;
    }}
    .guide-box {{
      margin-top: 35px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 24px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }}
    .guide-box h3 {{
      font-size: 16px;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    .guide-box ul {{
      padding-left: 20px;
      font-size: 13px;
      color: #334155;
      line-height: 1.7;
    }}
  </style>
</head>
<body>

<div class="dashboard-container">
  <div class="hero-banner">
    <h1>CBSE CLASS IX SCIENCE - HALF-YEARLY EXAMINATION PORTAL</h1>
    <p>Comprehensive Chapter-Wise Practice Question Papers based on the latest 2024-2025 NCERT Science Curriculum (Chapters 1 to 8). Specially designed with professional school examination layout, printable OMR answer sheets, and interactive evaluation mode.</p>
    <div class="badge-grid">
      <div class="badge-item">🎯 Total 200 Unique MCQs</div>
      <div class="badge-item">📄 Standard A4 Printable Layout</div>
      <div class="badge-item">⭕ Realistic OMR Bubble Sheets</div>
      <div class="badge-item">💡 Complete Step-by-Step Solutions</div>
      <div class="badge-item">🌐 100% CBSE English Medium</div>
    </div>
  </div>

  <div class="chapters-grid">
    {''.join(cards_html)}
  </div>

  <div class="guide-box">
    <h3>💡 How to Use These Examination Papers for Maximum Practice:</h3>
    <ul>
      <li><b>Option 1: Real Exam Simulation on Paper (Recommended):</b> Click <b>"🖨️ Direct Print (PDF)"</b> on any chapter. Press <code>Ctrl + P</code> in your browser, select <b>"Save as PDF"</b> or choose your printer with A4 paper format. Give the printed question paper and OMR sheet to the student with a 45-minute timer.</li>
      <li><b>Option 2: Interactive Practice in Web Browser:</b> Open <b>"📖 Open & Practice Test"</b> on a computer, tablet, or mobile phone. The child can select options online with an active 45-minute countdown clock, and click <b>"Check My Score"</b> for immediate automated marking and instant feedback.</li>
      <li><b>Separate Answer Key:</b> The Answer Key & Explanations sheet has an automatic page-break (`page-break-before: always`), so you can easily separate the answers before handing the test to the student.</li>
    </ul>
  </div>
</div>

<script>
function openAndPrint(url) {{
  let w = window.open(url, '_blank');
  w.onload = function() {{
    setTimeout(function() {{
      w.print();
    }}, 600);
  }};
}}
</script>

</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Generated index.html successfully.")

if __name__ == "__main__":
    for ch in CHAPTERS_DATA:
        generate_html_paper(ch)
    generate_index_dashboard()
    print("ALL PAPERS GENERATED SUCCESSFULLY!")
