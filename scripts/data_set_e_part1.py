"""
Data module for CBSE Class 9 Science - SET E (Case Study & Practical Experiments)
Part 1: Chapters 1 to 4 (5 Case Studies per Chapter = 25 questions each, 100 MCQs total)
Strictly 100% CBSE English Medium.
"""

CHAPTER_01_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Simple Pendulum Oscillation & Determination of Acceleration due to Gravity ($g$)",
        "passage": "A group of Class 9 students set up a simple pendulum in the physics laboratory to study the variation of its time period ($T$) with its effective length ($L$). They used a light, inextensible thread tied to a spherical brass bob of mass 50 g. The effective length was measured from the point of suspension to the center of gravity of the bob. Keeping the angular displacement small (< 10°), they timed 20 complete oscillations using a digital stopwatch for different lengths and recorded the data below:<br><br>"
                   "<b>Table 1: Pendulum Experimental Observations</b><br>"
                   "• Length $L_1 = 0.40\\text{ m} \\rightarrow$ Time for 20 oscillations = $25.4\\text{ s} \\rightarrow T = 1.27\\text{ s} \\rightarrow T^2 = 1.61\\text{ s}^2$<br>"
                   "• Length $L_2 = 0.60\\text{ m} \\rightarrow$ Time for 20 oscillations = $31.1\\text{ s} \\rightarrow T = 1.55\\text{ s} \\rightarrow T^2 = 2.40\\text{ s}^2$<br>"
                   "• Length $L_3 = 0.80\\text{ m} \\rightarrow$ Time for 20 oscillations = $35.9\\text{ s} \\rightarrow T = 1.80\\text{ s} \\rightarrow T^2 = 3.24\\text{ s}^2$<br>"
                   "• Length $L_4 = 1.00\\text{ m} \\rightarrow$ Time for 20 oscillations = $40.1\\text{ s} \\rightarrow T = 2.01\\text{ s} \\rightarrow T^2 = 4.04\\text{ s}^2$<br>"
                   "The students then plotted a graph of $T^2$ versus $L$ to calculate $g$ using the relation $T = 2\\pi \\sqrt{L/g}$.",
        "questions": [
            {
                "q": "What is the expected nature and mathematical shape of the graph plotted between $T^2$ (on y-axis) and length $L$ (on x-axis)?",
                "options": [
                    "A parabola curving towards the length axis",
                    "A straight line passing through the origin",
                    "A hyperbola curving asymptotically",
                    "A horizontal line parallel to the length axis"
                ],
                "ans": "B",
                "exp": "Squaring $T = 2\\pi \\sqrt{L/g}$ gives $T^2 = \\left(\\frac{4\\pi^2}{g}\\right) L$. Since $\\frac{4\\pi^2}{g}$ is a constant slope ($m$), the equation fits $y = mx$, which is a straight line passing through the origin."
            },
            {
                "q": "Based on the experimental data for $L = 1.00$ m ($T^2 = 4.04\\text{ s}^2$), what is the calculated experimental value of $g$ (take $\\pi = 3.1416$)?",
                "options": [
                    "$9.77\\text{ m/s}^2$",
                    "$9.80\\text{ m/s}^2$",
                    "$10.2\\text{ m/s}^2$",
                    "$9.50\\text{ m/s}^2$"
                ],
                "ans": "A",
                "exp": "$g = \\frac{4\\pi^2 L}{T^2} = \\frac{4 \\times (3.1416)^2 \\times 1.00}{4.04} = \\frac{39.478}{4.04} \\approx 9.77\\text{ m/s}^2$."
            },
            {
                "q": "Why were the students instructed to record the time for 20 full oscillations rather than timing a single oscillation?",
                "options": [
                    "Because a pendulum bob stops after 20 oscillations",
                    "To substantially reduce human reaction time error in stopwatch operation by distributing it over 20 cycles",
                    "Because the formula is valid only for 20 oscillations",
                    "To increase the amplitude of the pendulum"
                ],
                "ans": "B",
                "exp": "Human reaction time error in pressing start/stop is typically $\\pm 0.2$ s. Timing 20 oscillations divides this error by 20, improving experimental accuracy."
            },
            {
                "q": "If the 50 g brass bob is replaced by a 150 g lead bob while keeping the length strictly at 1.00 m, what will happen to the time period?",
                "options": [
                    "It will triple to 6.03 s",
                    "It will decrease to 1.16 s",
                    "It will remain unchanged at 2.01 s",
                    "It will increase by $\\sqrt{3}$ times"
                ],
                "ans": "C",
                "exp": "The time period of a simple pendulum is strictly independent of the mass and material of the bob ($T = 2\\pi \\sqrt{L/g}$ contains no mass term)."
            },
            {
                "q": "Why is it essential to maintain small angular amplitude (< 10°) during simple pendulum experiments in school laboratories?",
                "options": [
                    "To prevent air resistance from breaking the string",
                    "Because simple harmonic motion is strictly valid under the small angle approximation $\\sin\\theta \\approx \\theta$",
                    "To allow the bob to accelerate past the speed of sound",
                    "To increase the value of gravitational acceleration"
                ],
                "ans": "B",
                "exp": "The formula $T = 2\\pi \\sqrt{L/g}$ is derived assuming simple harmonic motion, which requires $\\sin\\theta \\approx \\theta$ in radians (valid only when $\\theta < 10^\\circ$)."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Precision Metrology with Vernier Calipers and Screw Gauge",
        "passage": "In a physics metrology practical, students measured the dimensions of a solid metallic cylinder and a thin copper wire using precision laboratory instruments.<br>"
                   "• <b>Instrument 1 (Vernier Calipers):</b> Used to measure the length and external diameter of the cylinder. The main scale is graduated in millimeters (1 MSD = 1 mm). 10 vernier scale divisions (VSD) coincide exactly with 9 main scale divisions.<br>"
                   "• <b>Instrument 2 (Micrometer Screw Gauge):</b> Used to measure the diameter of the thin copper wire. The pitch of the screw is 0.5 mm, and the circular thimble has 50 equal divisions.<br>"
                   "Before taking readings, the students inspected both instruments for zero error. The screw gauge showed that when the studs were brought into contact, the zero mark of the circular scale was 3 divisions below the reference line.",
        "questions": [
            {
                "q": "What is the least count of the Vernier Calipers used by the students?",
                "options": ["0.1 cm", "0.01 cm (0.1 mm)", "0.001 cm", "0.05 mm"],
                "ans": "B",
                "exp": "$\\text{Least count} = 1\\text{ MSD} - 1\\text{ VSD} = 1\\text{ mm} - 0.9\\text{ mm} = 0.1\\text{ mm} = 0.01\\text{ cm}$."
            },
            {
                "q": "What is the least count of the Micrometer Screw Gauge?",
                "options": ["0.01 mm", "0.001 mm", "0.05 mm", "0.1 mm"],
                "ans": "A",
                "exp": "$\\text{Least count} = \\frac{\\text{Pitch}}{\\text{Number of circular divisions}} = \\frac{0.5\\text{ mm}}{50} = 0.01\\text{ mm}$."
            },
            {
                "q": "What type of zero error is present in the screw gauge when its circular zero lies 3 divisions below the reference line?",
                "options": [
                    "Positive zero error of $+0.03$ mm",
                    "Negative zero error of $-0.03$ mm",
                    "Positive zero error of $+0.15$ mm",
                    "Zero error is absent"
                ],
                "ans": "A",
                "exp": "When the zero mark of the circular scale is below the reference datum line, the zero error is positive ($+3 \\times 0.01\\text{ mm} = +0.03\\text{ mm}$). It must be subtracted from the observed reading."
            },
            {
                "q": "While measuring the diameter of the wire, the main scale reads 1.5 mm and the 38th circular division aligns with the reference line. What is the true corrected diameter of the wire?",
                "options": ["1.88 mm", "1.85 mm", "1.91 mm", "1.53 mm"],
                "ans": "B",
                "exp": "Observed reading $= 1.5\\text{ mm} + (38 \\times 0.01\\text{ mm}) = 1.88\\text{ mm}$. True reading $= \\text{Observed} - (\\text{Zero Error}) = 1.88 - (+0.03) = 1.85\\text{ mm}$."
            },
            {
                "q": "Why is a ratchet provided at the back of a micrometer screw gauge?",
                "options": [
                    "To quickly spin the screw without measuring",
                    "To prevent overtightening and ensure uniform contact pressure on the object during all measurements",
                    "To lock the main scale firmly in place",
                    "To calibrate the pitch of the screw"
                ],
                "ans": "B",
                "exp": "The ratchet slips and produces a clicking sound once optimum contact pressure is reached, preventing mechanical deformation of the object or stripping of the fine threads."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Density Determination & Archimedes' Liquid Displacement",
        "passage": "A student was provided with an irregular piece of solid stone of mass 54.0 g. To determine its density experimentally, she used a spring balance, a graduated measuring cylinder of capacity 100 mL, and water of density $1.00\\text{ g/cm}^3$.<br>"
                   "• The spring balance had a least count of 1.0 g.<br>"
                   "• The initial water volume in the graduated cylinder was recorded as $V_1 = 50.0\\text{ mL}$.<br>"
                   "• The stone was tied to a fine thread and gently lowered completely into the water without touching the walls or bottom of the cylinder.<br>"
                   "• The new water level rose to $V_2 = 70.0\\text{ mL}$.<br>"
                   "The student then repeated the immersion using a saturated salt brine solution of density $1.20\\text{ g/cm}^3$.",
        "questions": [
            {
                "q": "What is the volume of the irregular stone piece?",
                "options": ["50.0 cm³", "70.0 cm³", "20.0 cm³", "120.0 cm³"],
                "ans": "C",
                "exp": "Volume of stone $= V_2 - V_1 = 70.0\\text{ mL} - 50.0\\text{ mL} = 20.0\\text{ mL} = 20.0\\text{ cm}^3$."
            },
            {
                "q": "What is the calculated density of the stone in SI units (kg/m³)?",
                "options": ["$2.70\\text{ kg/m}^3$", "$2700\\text{ kg/m}^3$", "$270\\text{ kg/m}^3$", "$0.27\\text{ kg/m}^3$"],
                "ans": "B",
                "exp": "Density $\\rho = \\frac{\\text{Mass}}{\\text{Volume}} = \\frac{54.0\\text{ g}}{20.0\\text{ cm}^3} = 2.70\\text{ g/cm}^3$. In SI units: $2.70 \\times 1000 = 2700\\text{ kg/m}^3$."
            },
            {
                "q": "What is the magnitude of the buoyant force exerted by pure water on the completely submerged stone ($g = 9.8\\text{ m/s}^2$)?",
                "options": ["0.540 N", "0.196 N", "0.200 N", "1.96 N"],
                "ans": "B",
                "exp": "Buoyant force $F_b = V \\rho_{water} g = (20 \\times 10^{-6}\\text{ m}^3) \\times 1000\\text{ kg/m}^3 \\times 9.8\\text{ m/s}^2 = 0.196\\text{ N}$."
            },
            {
                "q": "When the same stone is immersed in the salt brine (density $1.20\\text{ g/cm}^3$), what is the new buoyant force exerted on it?",
                "options": ["0.196 N", "0.235 N", "0.163 N", "0.270 N"],
                "ans": "B",
                "exp": "$F_b = V \\rho_{brine} g = (20 \\times 10^{-6}) \\times 1200 \\times 9.8 = 0.2352\\text{ N} \\approx 0.235\\text{ N}$."
            },
            {
                "q": "Which precautionary technique ensures accurate volume reading of the water meniscus in a glass graduated cylinder?",
                "options": [
                    "Reading the highest edge of the convex liquid curve",
                    "Viewing the cylinder from an oblique angle above the scale",
                    "Placing the eye level exactly horizontal to the lowest point of the concave meniscus",
                    "Adding oil to flatten the meniscus curve"
                ],
                "ans": "C",
                "exp": "Water forms a concave meniscus in glass due to adhesive forces. To avoid parallax error, the observer's line of sight must align horizontally with the bottom of the meniscus."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Thermal Expansion of Metals & Bimetallic Mechanics",
        "passage": "In an experiment investigating the thermal expansion of solids, a student heated three metallic strips of equal initial length (100.0 cm) and cross-section from 25°C to 125°C (temperature increase $\\Delta T = 100^\\circ\\text{C}$). The expansions recorded were:<br>"
                   "• Strip A (Copper): $\\Delta L = 1.70\\text{ mm}$<br>"
                   "• Strip B (Iron): $\\Delta L = 1.20\\text{ mm}$<br>"
                   "• Strip C (Aluminum): $\\Delta L = 2.40\\text{ mm}$<br>"
                   "The teacher then presented a bimetallic strip made by welding Strip A (Copper) and Strip B (Iron) together and heated it over a Bunsen burner flame.",
        "questions": [
            {
                "q": "Which of the three metals exhibits the lowest coefficient of linear expansion ($\alpha$)?",
                "options": ["Strip A (Copper)", "Strip B (Iron)", "Strip C (Aluminum)", "All three have identical coefficients"],
                "ans": "B",
                "exp": "Since $\\Delta L = L_0 \\alpha \\Delta T$, for identical initial length and temperature change, Iron expanded the least (1.20 mm), meaning it has the smallest $\\alpha$."
            },
            {
                "q": "What is the coefficient of linear expansion of Copper (Strip A) per degree Celsius?",
                "options": [
                    "$1.7 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$",
                    "$2.4 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$",
                    "$1.2 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$",
                    "$1.7 \\times 10^{-3}\\text{ /}^\\circ\\text{C}$"
                ],
                "ans": "A",
                "exp": "$\\alpha = \\frac{\\Delta L}{L_0 \\Delta T} = \\frac{0.00170\\text{ m}}{1.00\\text{ m} \\times 100^\\circ\\text{C}} = 1.7 \\times 10^{-5}\\text{ /}^\\circ\\text{C}$."
            },
            {
                "q": "When the Copper-Iron bimetallic strip is heated strongly, in which direction does it bend?",
                "options": [
                    "Towards the Copper side",
                    "Towards the Iron side",
                    "It twists into a coil but remains straight",
                    "It expands symmetrically without any curvature"
                ],
                "ans": "B",
                "exp": "Copper expands more than Iron ($1.7 > 1.2$). To accommodate the greater length, Copper forms the outer curve, forcing the strip to bend towards the less-expanded Iron side."
            },
            {
                "q": "If the same Copper-Iron bimetallic strip is subsequently cooled below room temperature in dry ice, what will occur?",
                "options": [
                    "It bends towards the Iron side even more",
                    "It bends towards the Copper side",
                    "It fractures immediately into two pieces",
                    "It stays completely straight"
                ],
                "ans": "B",
                "exp": "Upon cooling, Copper contracts more than Iron, forming the shorter inner curve. Hence, the strip reverses its bend and curves towards the Copper side."
            },
            {
                "q": "Which common home electrical appliance uses the bending of a bimetallic strip to automatically regulate temperature?",
                "options": ["Electric kettle thermostat", "Incandescent filament bulb", "Electric immersion rod without controller", "Step-down voltage stabilizer"],
                "ans": "A",
                "exp": "Thermostats in electric irons, refrigerators, and automatic kettles use bimetallic strips that bend upon heating to break the electrical circuit, regulating temperature."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Chemical Safety & Hazardous Spill Management",
        "passage": "During a chemistry laboratory orientation session, the lab instructor conducted a safety drill on handling hazardous chemicals, heating glassware, and responding to accidental chemical spills.<br>"
                   "• <b>Scenario A:</b> A student accidentally spills concentrated sulfuric acid ($H_2SO_4$) onto the laboratory workbench and his forearm.<br>"
                   "• <b>Scenario B:</b> Another student needs to prepare 250 mL of dilute sulfuric acid from concentrated acid.<br>"
                   "• <b>Scenario C:</b> A liquid in an open glass beaker is being heated over a Bunsen burner.",
        "questions": [
            {
                "q": "What is the correct and immediate first-aid response when concentrated acid spills onto a student's skin?",
                "options": [
                    "Apply strong sodium hydroxide solution immediately to neutralize it",
                    "Wash immediately under a continuous stream of copious running tap water for at least 15 minutes",
                    "Smear the skin thickly with petroleum jelly or cooking oil",
                    "Wrap the skin tightly with dry cotton bandage"
                ],
                "ans": "B",
                "exp": "Flushing with large volumes of running water rapidly cools and washes away the acid. Never apply strong alkalis, as exothermic neutralization causes severe thermal burns."
            },
            {
                "q": "What is the strictly mandated procedure for safely diluting concentrated sulfuric acid with water?",
                "options": [
                    "Pour water rapidly into concentrated acid while stirring",
                    "Add concentrated acid slowly and dropwise to water along the sides of the container with continuous stirring",
                    "Mix equal volumes of water and acid together in a sealed bottle and shake vigorously",
                    "Boil the acid first before mixing with cold water"
                ],
                "ans": "B",
                "exp": "Dilution of acid is highly exothermic. Adding acid slowly to a large volume of water allows the water to absorb the heat, preventing dangerous acid splattering."
            },
            {
                "q": "Why is a wire gauze placed on the tripod stand beneath a glass beaker during heating over a Bunsen burner?",
                "options": [
                    "To prevent chemical vapors from escaping into the room",
                    "To distribute flame heat evenly across the bottom of the beaker and prevent thermal shock breakage",
                    "To act as a chemical catalyst for the boiling reaction",
                    "To absorb smoke produced by the Bunsen flame"
                ],
                "ans": "B",
                "exp": "The wire gauze (often ceramic-centered) diffuses heat uniformly across the glass surface, preventing localized hot spots that shatter laboratory glassware."
            },
            {
                "q": "Which region of a Bunsen burner flame is the hottest and recommended for efficient heating?",
                "options": [
                    "The inner dark cone of unburnt gas",
                    "The outer non-luminous pale blue zone of complete combustion",
                    "The luminous yellow zone of incomplete combustion",
                    "The base of the burner collar"
                ],
                "ans": "B",
                "exp": "The non-luminous outer blue cone receives maximum oxygen, ensuring complete combustion and reaching temperatures up to 1500°C without leaving soot."
            },
            {
                "q": "Which of the following personal protective equipment (PPE) is mandatory whenever heating chemicals or working with acids in the lab?",
                "options": [
                    "Safety goggles and cotton lab coat",
                    "Woolen gloves and dark sunglasses",
                    "Synthetic nylon jacket and flip-flops",
                    "Leather welding helmet"
                ],
                "ans": "A",
                "exp": "Chemical splash goggles protect eyes from unexpected eruptions/splatters, while cotton lab coats protect skin and clothing from corrosive chemical damage."
            }
        ]
    }
]

CHAPTER_02_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Temporary Mount of Onion Peel & Microscopic Cytology",
        "passage": "Students prepared a temporary mount of an onion bulb leaf peel to examine plant cell architecture under a compound microscope.<br>"
                   "1. They peeled a thin translucent layer from the concave inner surface of an onion scale leaf.<br>"
                   "2. The peel was transferred to a watch glass containing water to prevent desiccation.<br>"
                   "3. It was stained with a dilute solution of Safranin for 2 minutes and washed.<br>"
                   "4. The stained peel was mounted on a clean glass slide in a drop of glycerin and covered with a glass coverslip, gently lowering it with a needle to avoid trapping air bubbles.<br>"
                   "Under 100x and 400x magnification, they observed contiguous rectangular cells with distinct boundaries.",
        "questions": [
            {
                "q": "Why is glycerin used as a mounting medium instead of plain water?",
                "options": [
                    "Glycerin dissolves the cell wall to reveal organelles",
                    "Glycerin prevents the biological specimen from drying out during extended microscopic observation",
                    "Glycerin stains the chromosomes bright purple",
                    "Glycerin acts as an adhesive to permanently glue the coverslip"
                ],
                "ans": "B",
                "exp": "Glycerin is hygroscopic and has high optical clarity; it prevents dehydration and shrinkage of the specimen under the warm microscope lamp."
            },
            {
                "q": "What is the primary biological purpose of staining the onion peel with Safranin?",
                "options": [
                    "To kill bacteria on the slide",
                    "To impart contrast by staining cell walls and nuclei, making cellular structures clearly visible",
                    "To induce active mitosis in the cells",
                    "To make the cell membrane permeable to glucose"
                ],
                "ans": "B",
                "exp": "Unstained living plant cells are mostly transparent. Safranin stains lignified and cellulosic cell walls and chromatin pink/red, providing visual contrast."
            },
            {
                "q": "Which organelle is prominently observed as a dense, darkly stained spherical body located towards the periphery of each onion cell?",
                "options": ["Mitochondrion", "Chloroplast", "Nucleus", "Centriole"],
                "ans": "C",
                "exp": "The nucleus stains darkly with Safranin and is pushed towards the peripheral cytoplasm due to the presence of a large central vacuole."
            },
            {
                "q": "Why are chloroplasts absent in the cells of an onion scale leaf peel?",
                "options": [
                    "Onion is an animal organism",
                    "Onion scale leaves are underground storage organs and are not exposed to sunlight for photosynthesis",
                    "The cells were killed by Safranin staining",
                    "Chloroplasts were filtered out during peeling"
                ],
                "ans": "B",
                "exp": "Onion bulbs grow underground to store food. In the absence of sunlight, plastids differentiate into colorless leucoplasts rather than green chloroplasts."
            },
            {
                "q": "What visual artifact indicates that the coverslip was dropped improperly onto the mount?",
                "options": [
                    "Circular dark-bordered rings that move when the slide is pressed (air bubbles)",
                    "Elongated rectangular cell walls",
                    "Bright red nuclei",
                    "Clear transparent cytoplasm"
                ],
                "ans": "A",
                "exp": "Air bubbles trapped under the coverslip appear as spherical or oval structures with thick, dark, refractive boundaries that interfere with observation."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Plasmolysis & Osmotic Mechanics in *Rhoeo Discolor* Leaf",
        "passage": "A biology teacher instructed students to investigate osmosis and plasmolysis using the colored lower epidermal peel of *Rhoeo discolor* leaf.<br>"
                   "• The lower epidermis of *Rhoeo* contains anthocyanin pigment dissolved in its vacuolar sap, giving cells a striking purple color.<br>"
                   "• <b>Slide 1:</b> A fresh peel mounted in pure water.<br>"
                   "• <b>Slide 2:</b> A fresh peel mounted in concentrated (20%) sucrose solution and observed after 5 minutes.<br>"
                   "• <b>Slide 3:</b> A leaf peel boiled in water for 5 minutes, then mounted in concentrated (20%) sucrose solution.",
        "questions": [
            {
                "q": "What morphological change is observed in the epidermal cells of Slide 2 (mounted in 20% sucrose)?",
                "options": [
                    "The cells swell up and burst",
                    "The purple protoplast shrinks away from the cell wall (plasmolysis) as water exits the vacuole via exosmosis",
                    "The cells double in size due to endosmosis",
                    "The cell wall dissolves completely"
                ],
                "ans": "B",
                "exp": "The 20% sucrose solution is hypertonic to the cell sap. Water moves out via exosmosis, causing the protoplast to shrink away from the rigid cell wall (plasmolysis)."
            },
            {
                "q": "What occupies the clear space between the shrunken protoplast and the cell wall in a plasmolysed plant cell?",
                "options": [
                    "A total vacuum",
                    "Pure air",
                    "The external 20% sucrose solution",
                    "Concentrated cytoplasm"
                ],
                "ans": "C",
                "exp": "The plant cell wall is freely permeable to water and dissolved sucrose, whereas the plasma membrane is semi-permeable. Hence, the hypertonic sucrose solution fills the gap."
            },
            {
                "q": "What happens when pure water is added to the plasmolysed cells of Slide 2 via irrigation?",
                "options": [
                    "The cells undergo permanent apoptosis",
                    "Water enters via endosmosis, restoring protoplast turgidity against the cell wall (deplasmolysis)",
                    "The cells burst instantly",
                    "The purple anthocyanin pigment precipitates into crystals"
                ],
                "ans": "B",
                "exp": "If placed back into a hypotonic medium (water) before dying, water rushes back in via endosmosis, reversing plasmolysis (deplasmolysis)."
            },
            {
                "q": "What was observed on Slide 3 (boiled leaf peel in 20% sucrose solution)?",
                "options": [
                    "Rapid violent plasmolysis",
                    "Zero plasmolysis; cells remained unchanged because boiling destroyed the living semi-permeable plasma membrane",
                    "The cells divided into two daughter cells",
                    "The purple color turned bright green"
                ],
                "ans": "B",
                "exp": "Boiling denatures membrane transport proteins and disrupts the phospholipid bilayer, killing the cells. Dead membranes cannot carry out selective osmosis."
            },
            {
                "q": "Which physical pressure is exerted by the swollen protoplast outward against the cell wall in a fully turgid plant cell?",
                "options": ["Suction pressure", "Turgor pressure", "Atmospheric pressure", "Capillary pressure"],
                "ans": "B",
                "exp": "Turgor pressure is the hydrostatic pressure exerted by the fluid contents of the vacuole and cytoplasm against the plasma membrane and cell wall."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Osmotic Fragility in Animal Cells (Erythrocytes)",
        "passage": "In a physiology experiment, mammalian red blood cells (RBCs) were suspended in test tubes containing sodium chloride ($NaCl$) solutions of varying molar concentrations at 37°C:<br>"
                   "• <b>Tube A:</b> 0.9% $NaCl$ solution (Isotonic saline)<br>"
                   "• <b>Tube B:</b> 0.2% $NaCl$ solution (Hypotonic)<br>"
                   "• <b>Tube C:</b> 2.0% $NaCl$ solution (Hypertonic)<br>"
                   "After 15 minutes, samples from each tube were examined under a light microscope and their optical absorbance was measured.",
        "questions": [
            {
                "q": "What is the physical appearance of the red blood cells in Tube A (0.9% saline)?",
                "options": [
                    "Swollen and spherical",
                    "Normal biconcave disc shape with zero net water movement",
                    "Shriveled and spiky",
                    "Completely lysed into fragments"
                ],
                "ans": "B",
                "exp": "0.9% NaCl is physiologically isotonic with mammalian intracellular cytoplasm; dynamic equilibrium exists with zero net gain or loss of water."
            },
            {
                "q": "What happens to the red blood cells placed in Tube B (0.2% NaCl hypotonic solution)?",
                "options": [
                    "They lose water and crenate",
                    "Water rapidly enters via endosmosis, causing cells to swell and burst (hemolysis)",
                    "They form a rigid cellulose wall",
                    "They divide via binary fission"
                ],
                "ans": "B",
                "exp": "Animal cells lack a rigid cell wall. In a hypotonic medium, endosmosis increases internal pressure until the plasma membrane ruptures, releasing hemoglobin (hemolysis)."
            },
            {
                "q": "What morphological term describes the shriveled, scalloped appearance of RBCs in Tube C (2.0% NaCl)?",
                "options": ["Turgid", "Crenated (Crenation)", "Plasmolysed", "Hypertrophied"],
                "ans": "B",
                "exp": "In animal cells, loss of water to a hypertonic medium causes cellular shrinkage and notched, spiky margins, termed crenation."
            },
            {
                "q": "Why do plant cells not burst when subjected to the same hypotonic conditions as Tube B?",
                "options": [
                    "Plant cells lack a plasma membrane",
                    "The rigid plant cell wall exerts an equal counter wall pressure that opposes increasing internal turgor pressure",
                    "Plant cells do not absorb water",
                    "Plant cell sap contains no solutes"
                ],
                "ans": "B",
                "exp": "The tough cellulose wall exerts inward wall pressure ($WP$) equal to outward turgor pressure ($TP$), preventing osmotic bursting."
            },
            {
                "q": "Which clinical medical practice directly relies on understanding isotonic saline concentrations?",
                "options": [
                    "Injecting pure distilled water directly into patient veins",
                    "Administering intravenous (IV) fluid drips matching 0.9% saline or 5% dextrose osmolarity",
                    "Prescribing concentrated sea water for dehydration",
                    "Boiling blood before transfusions"
                ],
                "ans": "B",
                "exp": "IV fluids must be strictly isotonic to human blood plasma (e.g., 0.9% normal saline) to prevent fatal hemolysis or crenation of red blood cells in vivo."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Cell Fractionation & Organelle Bioenergetics",
        "passage": "Biochemists homogenized fresh liver tissue in chilled isotonic buffer and subjected the cellular suspension to differential centrifugation at increasing centrifugal speeds:<br>"
                   "• <b>Pellet 1 (Low speed, 1,000 g):</b> Nuclei and unbroken cells sedimented.<br>"
                   "• <b>Pellet 2 (Medium speed, 10,000 g):</b> Mitochondria, lysosomes, and peroxisomes sedimented.<br>"
                   "• <b>Pellet 3 (High speed, 100,000 g):</b> Microsomes (fragments of ER and Golgi membranes) sedimented.<br>"
                   "• <b>Supernatant:</b> Soluble cytosol containing ribosomes and enzymes.<br>"
                   "Upon analyzing Pellet 2, researchers observed high rates of ATP synthesis in the presence of oxygen, pyruvate, and ADP.",
        "questions": [
            {
                "q": "Which organelle in Pellet 2 is responsible for generating ATP through cellular aerobic respiration?",
                "options": ["Lysosome", "Mitochondrion", "Peroxisome", "Centrosome"],
                "ans": "B",
                "exp": "Mitochondria are the powerhouses of eukaryotic cells, coupling electron transport and oxidative phosphorylation to synthesize ATP."
            },
            {
                "q": "What morphological adaptation of the inner mitochondrial membrane enhances its ATP production efficiency?",
                "options": [
                    "Pores made of cellulose fibers",
                    "Extensive inward foldings called cristae that substantially increase surface area for respiratory enzymes",
                    "A thick layer of hydrophobic wax",
                    "Complete absence of membrane proteins"
                ],
                "ans": "B",
                "exp": "Cristae greatly amplify the total surface area available for electron transport chain complexes and ATP synthase enzymes."
            },
            {
                "q": "Which unique genetic feature allows mitochondria to synthesize some of their own proteins?",
                "options": [
                    "They possess their own circular DNA and 70S ribosomes",
                    "They borrow mRNA from lysosomes",
                    "They have nuclear pores on their outer membrane",
                    "They contain linear chromosomes with histones"
                ],
                "ans": "A",
                "exp": "Mitochondria are semi-autonomous endosymbionts containing circular prokaryotic-like DNA and 70S ribosomes."
            },
            {
                "q": "If the lysosomes present in Pellet 2 are subjected to detergent lysis, which class of enzymes will be released?",
                "options": [
                    "Photosynthetic carboxylases",
                    "Acid hydrolytic digestive enzymes (proteases, nucleases, lipases)",
                    "DNA polymerases active at pH 9",
                    "Chlorophyll synthesis enzymes"
                ],
                "ans": "B",
                "exp": "Lysosomes are acidic hydrolytic vesicles containing enzymes that digest proteins, nucleic acids, lipids, and carbohydrates."
            },
            {
                "q": "Why was the tissue homogenization performed in a chilled, isotonic sucrose buffer rather than in pure warm water?",
                "options": [
                    "To prevent osmotic lysis of organelles and inhibit degradative enzymes through low temperature",
                    "To speed up chemical reactions",
                    "To dissolve the mitochondrial membranes",
                    "To boil away unwanted water"
                ],
                "ans": "A",
                "exp": "Isotonic buffer prevents organelles from swelling and bursting osmotically, while chilling (4°C) minimizes destructive enzymatic degradation."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Endomembrane Secretory Transport & Protein Targeting",
        "passage": "In a pulse-chase experiment, pancreatic acinar cells synthesizing digestive enzymes were briefly exposed ('pulse') to radioactively labeled amino acids ($^{3}H$-leucine) for 3 minutes, then incubated ('chase') with non-radioactive amino acids. Samples were fixed at intervals and examined by autoradiography under an electron microscope to track the intracellular route of the synthesized digestive enzymes:<br>"
                   "• At 3 minutes: Radioactivity concentrated exclusively on the Rough Endoplasmic Reticulum (RER).<br>"
                   "• At 20 minutes: Radioactivity shifted to the Golgi apparatus.<br>"
                   "• At 90 minutes: Radioactivity accumulated in secretory vesicles near the apical plasma membrane.",
        "questions": [
            {
                "q": "Which organelle component attached to the cytosolic surface of the RER synthesized the radioactive proteins?",
                "options": ["Ribosomes", "Lipid droplets", "Centrioles", "Microfilaments"],
                "ans": "A",
                "exp": "Ribosomes attached to the outer surface of the rough endoplasmic reticulum translate mRNA into secretory and membrane proteins."
            },
            {
                "q": "What is the primary processing function of the Golgi apparatus as proteins pass through its flattened cisternae?",
                "options": [
                    "Replication of genomic DNA",
                    "Modification, glycosylation, packaging, and sorting of proteins into membrane-bound vesicles",
                    "Direct synthesis of ATP via oxidative phosphorylation",
                    "Digestion of glucose into pyruvate"
                ],
                "ans": "B",
                "exp": "The Golgi apparatus modifies proteins (e.g., adding carbohydrates), packages them into vesicles, and directs them to their final cellular destinations."
            },
            {
                "q": "How does the Smooth Endoplasmic Reticulum (SER) differ biochemically and functionally from the RER?",
                "options": [
                    "SER contains ribosomes and makes RNA",
                    "SER lacks ribosomes and is specialized for lipid and steroid synthesis, as well as drug detoxification",
                    "SER is located inside the nucleus",
                    "SER performs cellular photosynthesis"
                ],
                "ans": "B",
                "exp": "Smooth ER is agranular (lacks ribosomes) and specializes in lipid/steroid biosynthesis and calcium storage/detoxification."
            },
            {
                "q": "By which transport mechanism do mature secretory vesicles release digestive enzymes across the cell's outer membrane into pancreatic ducts?",
                "options": ["Phagocytosis", "Exocytosis", "Endosmosis", "Simple diffusion"],
                "ans": "B",
                "exp": "Exocytosis is the process wherein intracellular secretory vesicles fuse with the plasma membrane to discharge their contents into extracellular space."
            },
            {
                "q": "Which organelle would degrade dysfunctional, worn-out Golgi or ER fragments inside the cell?",
                "options": ["Mitochondria", "Lysosomes (via autophagy)", "Chloroplasts", "Centrioles"],
                "ans": "B",
                "exp": "Autophagy is a lysosomal degradation pathway where damaged cellular organelles and cytoplasmic components are engulfed and digested."
            }
        ]
    }
]

CHAPTER_03_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Histological Examination of Plant Stems (T.S. of Dicot Stem)",
        "passage": "Students prepared a thin transverse section (T.S.) of a young sunflower stem using a sharp razor blade. They floated the thin sections in water, transferred the thinnest uniform slice to a watch glass, stained it with Safranin and Fast Green, and mounted it in glycerin.<br>"
                   "Under the microscope, they observed concentric tissue layers from outside to inside:<br>"
                   "1. Outer epidermis covered with a cuticular layer.<br>"
                   "2. Collenchymatous hypodermis at the corners.<br>"
                   "3. Parenchymatous cortex with intercellular spaces.<br>"
                   "4. A ring of vascular bundles with sclerenchymatous bundle caps (hard bast).<br>"
                   "5. Vascular bundles showing xylem towards the center and phloem towards the periphery, separated by cambium.",
        "questions": [
            {
                "q": "Which tissue in the hypodermis provides mechanical flexibility, allowing young stems to bend without breaking?",
                "options": ["Parenchyma", "Collenchyma", "Sclerenchyma", "Aerenchyma"],
                "ans": "B",
                "exp": "Collenchyma cells have localized pectin and cellulose thickenings at their cell corners, providing mechanical support and flexibility."
            },
            {
                "q": "How can sclerenchyma fibers in the bundle cap be distinguished microscopically from parenchyma cells?",
                "options": [
                    "Sclerenchyma cells are living with thin cellulose walls and large chloroplasts",
                    "Sclerenchyma cells are dead at maturity with narrow lumens and heavily lignified, thickened secondary walls",
                    "Sclerenchyma cells have large intercellular spaces filled with air",
                    "Sclerenchyma cells contain prominent central nuclei"
                ],
                "ans": "B",
                "exp": "Sclerenchyma consists of dead, elongated fiber cells with narrow obliterated lumens and thick walls impregnated with lignin."
            },
            {
                "q": "Which meristematic tissue strip present between xylem and phloem is responsible for secondary radial growth (increase in girth)?",
                "options": ["Apical meristem", "Intercalary meristem", "Vascular cambium (Lateral meristem)", "Protoderm"],
                "ans": "C",
                "exp": "Vascular cambium is a lateral meristem whose periclinal divisions produce secondary xylem and phloem, increasing stem girth."
            },
            {
                "q": "Which constituent of xylem tissue is the only living cell type present in mature dicot xylem?",
                "options": ["Xylem tracheids", "Xylem vessels", "Xylem parenchyma", "Xylem fibres"],
                "ans": "C",
                "exp": "Xylem parenchyma is the only living element; tracheids, vessels, and fibers are dead, hollow, lignified cells at functional maturity."
            },
            {
                "q": "Why does xylem stain intense red with Safranin stain?",
                "options": [
                    "Safranin reacts selectively with lignin present in xylem tracheid and vessel walls",
                    "Safranin stains only lipids",
                    "Xylem absorbs chlorophyll",
                    "Xylem is rich in starch"
                ],
                "ans": "A",
                "exp": "Safranin is a basic histological dye that binds specifically to poly-phenolic lignin polymers present in xylem cell walls."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Stomatal Distribution & Transpiration Investigation",
        "passage": "A botany student examined the distribution of stomata on the dorsal (upper) and ventral (lower) surfaces of a dorsiventral dicot leaf (*Hibiscus*).<br>"
                   "• She prepared epidermal peels from both leaf surfaces and counted stomata in five microscopic fields of view at 400x magnification.<br>"
                   "• <b>Upper Epidermis:</b> Average 12 stomata per field.<br>"
                   "• <b>Lower Epidermis:</b> Average 85 stomata per field.<br>"
                   "To verify the physiological consequence of this unequal distribution, she attached blue dry Cobalt Chloride ($CoCl_2$) paper strips to both surfaces of an intact living leaf using glass slides and clips, placed the plant in sunlight, and timed the color change from blue to pink.",
        "questions": [
            {
                "q": "On which leaf surface did the Cobalt Chloride paper turn pink first?",
                "options": [
                    "The upper surface, because it receives direct sunlight",
                    "The lower surface, because it contains a much higher density of stomata resulting in faster transpiration",
                    "Both surfaces turned pink at the exact same instant",
                    "Neither surface changed color"
                ],
                "ans": "B",
                "exp": "The lower epidermis has over 7 times higher stomatal density. Greater water vapor transpires through the lower surface, rapidly turning anhydrous blue $CoCl_2$ paper into pink hydrated form."
            },
            {
                "q": "What is the evolutionary biological advantage of having fewer stomata on the upper surface of terrestrial dicot leaves?",
                "options": [
                    "To prevent insects from eating the leaf",
                    "To reduce excessive water loss caused by direct solar irradiation and wind exposure",
                    "To block absorption of sunlight",
                    "To reduce oxygen intake"
                ],
                "ans": "B",
                "exp": "Positioning most stomata on the shaded lower surface reduces excessive transpirational water loss in hot, dry terrestrial environments."
            },
            {
                "q": "Which specialized epidermal cells control the opening and closing of each stomatal pore?",
                "options": ["Subsidiary parenchyma", "Guard cells", "Trichomes", "Lenticels"],
                "ans": "B",
                "exp": "Each stomatal pore is flanked by two kidney-shaped (or dumb-bell shaped in grasses) guard cells that regulate pore diameter."
            },
            {
                "q": "What physiological change causes a stomatal pore to open during the day?",
                "options": [
                    "Guard cells lose water and become flaccid",
                    "Guard cells absorb water via endosmosis, become turgid, and their thin outer walls stretch outwards, pulling open the thick inner walls",
                    "Guard cells shrink and detach from the epidermis",
                    "The pore fills with starch grains"
                ],
                "ans": "B",
                "exp": "When guard cells absorb water and swell, their differentially thickened walls (thin elastic outer wall, thick rigid inner wall) bow outward, opening the pore."
            },
            {
                "q": "What protective, hydrophobic chemical substance coats the outer surface of the leaf epidermis to minimize water loss?",
                "options": ["Suberin", "Cutin (forming the cuticle)", "Pectin", "Chitin"],
                "ans": "B",
                "exp": "Cutin is a waxy, hydrophobic lipid polymer secreted by epidermal cells to form the protective outer cuticle layer."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Phloem Translocation vs Xylem Ascent of Sap",
        "passage": "In a classical plant physiology investigation, students performed two experiments:<br>"
                   "• <b>Experiment A (Dye Tracing):</b> A leafy branch of a balsam plant was placed in a beaker containing water stained with red eosin dye for 3 hours. Thin cross-sections of the stem revealed that only vascular xylem vessels were stained red.<br>"
                   "• <b>Experiment B (Girdling / Ringing):</b> A complete ring of bark (outer tissue including phloem down to the cambium) was removed from the woody stem of a potted plant. After several weeks, a distinct swelling developed immediately above the girdle, while tissues below remained unthickened.",
        "questions": [
            {
                "q": "What conclusion is drawn from Experiment A regarding xylem tissue?",
                "options": [
                    "Xylem conducts organic sugars downward from leaves",
                    "Xylem is the vascular tissue responsible for unidirectional upward conduction of water and dissolved minerals (ascent of sap)",
                    "Xylem stores lipids in the bark",
                    "Xylem transports gases to roots"
                ],
                "ans": "B",
                "exp": "The selective red staining of tracheids and vessels demonstrates that water and dissolved mineral solutes ascend through xylem."
            },
            {
                "q": "Why did a swelling develop immediately above the girdle in Experiment B?",
                "options": [
                    "Water accumulated because xylem was blocked",
                    "Downward transport of photosynthesized organic nutrients (sucrose) was halted by removing phloem, causing food accumulation and cell division above the girdle",
                    "Bacterial infection attacked the exposed wood",
                    "Turgor pressure caused the stem to stretch"
                ],
                "ans": "B",
                "exp": "Girdling removes the phloem sieve tubes. Sugars synthesized by leaves above the ring cannot travel downward to roots, accumulating and causing cellular swelling."
            },
            {
                "q": "Which constituent of phloem tissue lacks a cell nucleus at maturity yet remains living and metabolically functional?",
                "options": ["Phloem parenchyma", "Sieve tube elements", "Companion cells", "Phloem fibers"],
                "ans": "B",
                "exp": "Mature sieve tube elements lack a nucleus, vacuole, and ribosomes, but remain alive through intimate plasmodesmatal connections with nucleated companion cells."
            },
            {
                "q": "Which phloem component regulates the metabolic transport activities of an adjacent enucleated sieve tube element?",
                "options": ["Companion cell", "Xylem vessel", "Tracheid", "Guard cell"],
                "ans": "A",
                "exp": "Companion cells are specialized parenchymatous cells with dense cytoplasm and large nuclei that load and unload sucrose into sieve tubes."
            },
            {
                "q": "Which driving physical force is primarily responsible for the rapid ascent of sap in tall trees during sunny daylight hours?",
                "options": ["Transpirational pull", "Root pressure alone", "Atmospheric pressure on leaves", "Active pumping by xylem fibers"],
                "ans": "A",
                "exp": "Transpiration of water vapor from leaf stomata generates a continuous negative hydrostatic pressure gradient (tension/pull) that draws continuous water columns up xylem."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Comparative Histology of Animal Muscular Tissues",
        "passage": "Students observed three prepared stained histological slides of mammalian muscle tissues under high power (400x) magnification:<br>"
                   "• <b>Slide 1:</b> Long, unbranched, cylindrical fibers with alternating dark and light cross-striations and multiple flattened nuclei located peripherally beneath the sarcolemma.<br>"
                   "• <b>Slide 2:</b> Spindle-shaped (fusiform) unbranched fibers with pointed ends, lacking striations, each having a single centrally positioned oval nucleus.<br>"
                   "• <b>Slide 3:</b> Cylindrical, branched fibers showing light striations, single central nuclei, and dark transverse junctional bands called intercalated discs.",
        "questions": [
            {
                "q": "Identify the muscular tissue observed on Slide 1:",
                "options": ["Smooth visceral muscle", "Skeletal (striated) muscle", "Cardiac muscle", "Adipose tissue"],
                "ans": "B",
                "exp": "Skeletal muscle fibers are voluntary, cylindrical, multinucleate (syncytial), with peripheral nuclei and prominent cross-striations."
            },
            {
                "q": "Where in the human body is the muscular tissue of Slide 2 (spindle-shaped, unstriated) typically located?",
                "options": [
                    "Biceps and quadriceps limbs",
                    "Walls of internal hollow organs such as stomach, intestine, and blood vessels",
                    "Heart wall (myocardium)",
                    "Tongue and pharynx"
                ],
                "ans": "B",
                "exp": "Smooth (unstriated, involuntary) muscle fibers line visceral organs such as the gastrointestinal tract, urinary bladder, uterus, and blood vessels."
            },
            {
                "q": "What is the critical physiological role of the intercalated discs observed on Slide 3 (Cardiac muscle)?",
                "options": [
                    "They store glycogen granules",
                    "They contain gap junctions that allow electrical impulses to spread rapidly, enabling synchronized rhythmic contractions of the heart chambers",
                    "They anchor muscles to skeletal bones",
                    "They secrete adrenaline hormone"
                ],
                "ans": "B",
                "exp": "Intercalated discs are specialized cell junctions containing desmosomes and gap junctions that electrically couple adjacent cardiomyocytes for coordinated contraction."
            },
            {
                "q": "Why does skeletal muscle experience fatigue after prolonged vigorous exercise, whereas cardiac muscle contracts tirelessly throughout life?",
                "options": [
                    "Skeletal muscle has more blood vessels than cardiac muscle",
                    "Cardiac muscle has an extraordinarily rich capillary supply, high mitochondrial density, and relies strictly on aerobic metabolism without accumulating lactic acid",
                    "Skeletal muscle lacks ATP",
                    "Cardiac muscle contracts only when a person is awake"
                ],
                "ans": "B",
                "exp": "Cardiomyocytes have abundant mitochondria (up to 40% of cell volume) and continuous oxygen supply, preventing anaerobic fatigue."
            },
            {
                "q": "Which of the three muscle types is categorized as under voluntary conscious nervous control?",
                "options": ["Skeletal muscle only", "Smooth muscle only", "Cardiac muscle only", "All three types"],
                "ans": "A",
                "exp": "Only skeletal muscle contractions can be initiated voluntarily via the somatic nervous system; smooth and cardiac muscles are involuntary."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Connective Tissue Mechanics & Human Blood Cytology",
        "passage": "During a sports medicine workshop, a physiotherapist discussed connective tissue injuries and microscopic hematology:<br>"
                   "• <b>Patient X:</b> A footballer suffered a severe joint sprain; MRI revealed a torn ligament at the knee.<br>"
                   "• <b>Patient Y:</b> A runner experienced acute heel pain diagnosed as Achilles tendinitis.<br>"
                   "• <b>Blood Smear Analysis:</b> A normal stained blood film examined under oil immersion magnification displayed biconcave enucleated red cells, white cells (neutrophils, lymphocytes, monocytes), and tiny cell fragments.",
        "questions": [
            {
                "q": "How do ligaments fundamentally differ from tendons in terms of their anatomical connections and fiber composition?",
                "options": [
                    "Ligaments connect bone to bone and contain elastic yellow fibers; tendons connect muscle to bone and are composed of inelastic white collagen fibers",
                    "Ligaments connect muscle to bone; tendons connect bone to bone",
                    "Ligaments are dead; tendons are living",
                    "Ligaments contain calcium phosphate; tendons contain liquid plasma"
                ],
                "ans": "A",
                "exp": "Ligaments join bone to bone with high elasticity (elastin fibers); tendons join muscle to bone with high tensile strength and limited elasticity (dense collagen)."
            },
            {
                "q": "Why do ligament tears heal much more slowly than fractured bones?",
                "options": [
                    "Ligaments contain no living cells",
                    "Bone has a rich vascular blood supply through Haversian canals, whereas dense fibrous ligament tissue has minimal blood supply",
                    "Bones are softer than ligaments",
                    "Ligaments dissolve in body fluids"
                ],
                "ans": "B",
                "exp": "Bone is richly vascularized with osteocytes continuously remodeled by blood flow; dense fibrous connective tissues like ligaments are poorly vascularized."
            },
            {
                "q": "Which formed cellular element in blood is enucleated at maturity and specializes in oxygen transport via hemoglobin?",
                "options": ["Neutrophil", "Erythrocyte (Red Blood Cell)", "Lymphocyte", "Platelet"],
                "ans": "B",
                "exp": "Mammalian erythrocytes lose their nucleus, mitochondria, and ER during maturation to maximize internal volume for oxygen-carrying hemoglobin molecules."
            },
            {
                "q": "Which blood component consists of cytoplasmic cell fragments derived from megakaryocytes that are essential for blood clotting?",
                "options": ["Platelets (Thrombocytes)", "Eosinophils", "Basophils", "Monocytes"],
                "ans": "A",
                "exp": "Platelets are enucleated discoid fragments that aggregate at injury sites and release clotting factors to form hemostatic fibrin plugs."
            },
            {
                "q": "Which connective tissue possesses a hard, rigid matrix composed of calcium and phosphorus compounds?",
                "options": ["Hyaline cartilage", "Areolar tissue", "Bone tissue", "Adipose tissue"],
                "ans": "C",
                "exp": "Bone matrix is composed of collagen fibers impregnated with mineral hydroxyapatite salts ($Ca_{10}(PO_4)_6(OH)_2$), conferring compressive strength."
            }
        ]
    }
]

CHAPTER_04_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Ticker-Timer Analysis of Linear Acceleration on an Incline",
        "passage": "Students set up an aluminum track inclined at an angle to the bench. A dynamic trolley was released from rest at the top of the ramp, pulling a paper tape through an electromagnetic ticker-tape timer vibrating at a frequency of 50 Hz (producing 50 dots per second).<br>"
                   "• Time between two consecutive dots = $1/50\\text{ s} = 0.02\\text{ s}$.<br>"
                   "The students analyzed a segment of tape where dot positions were clearly marked:<br>"
                   "• Distance between Dot 0 and Dot 5 ($t_1 = 0.10\\text{ s}$) = $2.0\\text{ cm}$<br>"
                   "• Distance between Dot 5 and Dot 10 ($t_2 = 0.10\\text{ s}$) = $6.0\\text{ cm}$<br>"
                   "• Distance between Dot 10 and Dot 15 ($t_3 = 0.10\\text{ s}$) = $10.0\\text{ cm}$<br>"
                   "• Distance between Dot 15 and Dot 20 ($t_4 = 0.10\\text{ s}$) = $14.0\\text{ cm}$",
        "questions": [
            {
                "q": "What is the average velocity of the trolley during the time interval between Dot 0 and Dot 5 ($0.00\\text{ s}$ to $0.10\\text{ s}$)?",
                "options": ["$0.10\\text{ m/s}$", "$0.20\\text{ m/s}$", "$0.40\\text{ m/s}$", "$0.02\\text{ m/s}$"],
                "ans": "B",
                "exp": "$v_1 = \\frac{\\Delta s_1}{\\Delta t} = \\frac{2.0\\text{ cm}}{0.10\\text{ s}} = 20.0\\text{ cm/s} = 0.20\\text{ m/s}$."
            },
            {
                "q": "What is the average velocity of the trolley during the interval between Dot 5 and Dot 10 ($0.10\\text{ s}$ to $0.20\\text{ s}$)?",
                "options": ["$0.20\\text{ m/s}$", "$0.60\\text{ m/s}$", "$0.40\\text{ m/s}$", "$0.80\\text{ m/s}$"],
                "ans": "B",
                "exp": "$v_2 = \\frac{6.0\\text{ cm}}{0.10\\text{ s}} = 60.0\\text{ cm/s} = 0.60\\text{ m/s}$."
            },
            {
                "q": "Calculate the constant acceleration ($a$) of the trolley down the inclined track:",
                "options": ["$2.0\\text{ m/s}^2$", "$4.0\\text{ m/s}^2$", "$0.4\\text{ m/s}^2$", "$9.8\\text{ m/s}^2$"],
                "ans": "B",
                "exp": "$a = \\frac{v_2 - v_1}{\\Delta t} = \\frac{0.60 - 0.20}{0.10} = \\frac{0.40\\text{ m/s}}{0.10\\text{ s}} = 4.0\\text{ m/s}^2$."
            },
            {
                "q": "What indicates that the trolley is moving with uniform acceleration rather than constant velocity?",
                "options": [
                    "The dots on the tape are spaced at equal distances",
                    "The distance between successive sets of dots increases by a constant difference of 4.0 cm every 0.10 s",
                    "The tape moves backward",
                    "The timer frequency fluctuates"
                ],
                "ans": "B",
                "exp": "Equal increments in displacement during successive equal time intervals ($\\Delta s = 4.0$ cm increase per interval) confirm constant acceleration."
            },
            {
                "q": "What would the velocity-time ($v$-$t$) graph for this trolley look like?",
                "options": [
                    "A horizontal line parallel to the time axis",
                    "A straight line sloping upwards with a positive slope of $4.0\\text{ m/s}^2$",
                    "A curve with decreasing slope",
                    "A vertical line perpendicular to the time axis"
                ],
                "ans": "B",
                "exp": "For uniform acceleration, velocity increases linearly with time ($v = u + at$), yielding a straight line with gradient equal to acceleration."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Automotive Braking Distance & Driver Reaction Dynamics",
        "passage": "A traffic safety research institute analyzed the total stopping distance of a car travelling at different initial speeds ($u$) on a dry asphalt highway.<br>"
                   "• Total Stopping Distance consists of two phases:<br>"
                   "1. <b>Thinking Distance ($d_{think}$):</b> Distance covered during the driver's physiological reaction time ($t_r = 0.60\\text{ s}$) before the brakes are engaged ($d_{think} = u \\times t_r$).<br>"
                   "2. <b>Braking Distance ($d_{brake}$):</b> Distance covered while the brakes apply a constant retarding deceleration of $a = -5.0\\text{ m/s}^2$ until the car comes to rest ($v=0$).<br>"
                   "• Data for two test speeds:<br>"
                   "• Car A speed: $36\\text{ km/h} = 10\\text{ m/s}$<br>"
                   "• Car B speed: $72\\text{ km/h} = 20\\text{ m/s}$",
        "questions": [
            {
                "q": "What is the thinking distance covered by Car A ($u = 10\\text{ m/s}$) before the driver presses the brake pedal?",
                "options": ["3.0 m", "6.0 m", "10.0 m", "12.0 m"],
                "ans": "B",
                "exp": "$d_{think} = u \\times t_r = 10\\text{ m/s} \\times 0.60\\text{ s} = 6.0\\text{ m}$."
            },
            {
                "q": "What is the actual braking distance ($d_{brake}$) required for Car A to come to a complete stop?",
                "options": ["5.0 m", "10.0 m", "20.0 m", "15.0 m"],
                "ans": "B",
                "exp": "Using $v^2 = u^2 + 2as \\Rightarrow 0^2 = 10^2 + 2(-5.0)d_{brake} \\Rightarrow 10 d_{brake} = 100 \\Rightarrow d_{brake} = 10.0\\text{ m}$."
            },
            {
                "q": "What is the total stopping distance (Thinking + Braking) for Car A?",
                "options": ["10.0 m", "16.0 m", "20.0 m", "26.0 m"],
                "ans": "B",
                "exp": "Total Stopping Distance $= d_{think} + d_{brake} = 6.0\\text{ m} + 10.0\\text{ m} = 16.0\\text{ m}$."
            },
            {
                "q": "For Car B travelling at double the speed ($72\\text{ km/h} = 20\\text{ m/s}$), what is its braking distance ($d_{brake}$)?",
                "options": ["20.0 m", "40.0 m", "30.0 m", "80.0 m"],
                "ans": "B",
                "exp": "$d_{brake} = \\frac{u^2}{2a} = \\frac{20^2}{2 \\times 5.0} = \\frac{400}{10} = 40.0\\text{ m}$. Notice that doubling speed quadruples braking distance ($10 \\times 4 = 40$ m)."
            },
            {
                "q": "Why does braking distance depend quadratically on initial speed ($d_{brake} \\propto u^2$)?",
                "options": [
                    "Because car mass doubles with speed",
                    "Because initial kinetic energy is proportional to $u^2$, and the braking work ($F \\times d$) must dissipate this kinetic energy",
                    "Because reaction time increases with speed",
                    "Because gravity increases with speed"
                ],
                "ans": "B",
                "exp": "According to the work-energy theorem, braking work equals kinetic energy: $F_{brake} \\times d = \\frac{1}{2}m u^2 \\Rightarrow d \\propto u^2$."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Free-Fall Kinematics & Precision Photogate Measurement of $g$",
        "passage": "In a modern school physics lab, students measured the acceleration due to gravity ($g$) using an automated free-fall apparatus equipped with two infrared photogates connected to a millisecond digital timer.<br>"
                   "• A steel sphere of mass 28 g was held by an electromagnet at height $h$ directly above Photogate 1 ($s=0$, $t=0$).<br>"
                   "• When released from rest ($u=0$), the ball interrupted Photogate 1 (starting the timer) and interrupted Photogate 2 positioned at a vertical distance $h$ below.<br>"
                   "• <b>Trial 1:</b> Vertical fall height $h = 0.450\\text{ m} \\rightarrow$ Measured fall time $t = 0.303\\text{ s}$<br>"
                   "• <b>Trial 2:</b> Vertical fall height $h = 0.800\\text{ m} \\rightarrow$ Measured fall time $t = 0.404\\text{ s}$<br>"
                   "• <b>Trial 3:</b> Vertical fall height $h = 1.250\\text{ m} \\rightarrow$ Measured fall time $t = 0.505\\text{ s}$",
        "questions": [
            {
                "q": "Which kinematic equation directly relates the vertical fall height $h$ and time $t$ for a body dropped from rest?",
                "options": [
                    "$h = ut + \\frac{1}{2}gt^2$ which simplifies to $h = \\frac{1}{2}gt^2$",
                    "$v = u + gt$",
                    "$v^2 = 2gh$",
                    "$h = \\frac{u+v}{t}$"
                ],
                "ans": "A",
                "exp": "Since the ball is released from rest ($u = 0$), $s = ut + \\frac{1}{2}at^2$ reduces directly to $h = \\frac{1}{2}gt^2$."
            },
            {
                "q": "Using the data from Trial 2 ($h = 0.800\\text{ m}$, $t = 0.404\\text{ s}$), calculate the experimental value of $g$:",
                "options": ["$9.80\\text{ m/s}^2$", "$9.65\\text{ m/s}^2$", "$10.2\\text{ m/s}^2$", "$9.40\\text{ m/s}^2$"],
                "ans": "A",
                "exp": "$g = \\frac{2h}{t^2} = \\frac{2 \\times 0.800}{(0.404)^2} = \\frac{1.600}{0.1632} \\approx 9.80\\text{ m/s}^2$."
            },
            {
                "q": "What is the instantaneous velocity of the steel sphere as it crosses Photogate 2 in Trial 3 ($h = 1.250\\text{ m}$, take $g = 9.80\\text{ m/s}^2$)?",
                "options": ["$4.95\\text{ m/s}$", "$2.45\\text{ m/s}$", "$7.00\\text{ m/s}$", "$9.80\\text{ m/s}$"],
                "ans": "A",
                "exp": "$v = \\sqrt{2gh} = \\sqrt{2 \\times 9.80 \\times 1.250} = \\sqrt{24.5} \\approx 4.95\\text{ m/s}$."
            },
            {
                "q": "If the 28 g steel sphere is replaced by a massive 150 g steel sphere dropped from the exact same height, how does the fall time change?",
                "options": [
                    "Fall time decreases to one-fifth",
                    "Fall time increases by five times",
                    "Fall time remains virtually identical",
                    "The heavier sphere stops mid-air"
                ],
                "ans": "C",
                "exp": "All bodies, regardless of mass, experience the identical gravitational acceleration ($a=g$) when aerodynamic drag is negligible."
            },
            {
                "q": "What would a graph of $h$ versus $t^2$ yield for a freely falling object?",
                "options": [
                    "A downward parabola",
                    "A straight line passing through the origin with slope equal to $\\frac{1}{2}g$",
                    "A hyperbolic curve",
                    "A horizontal line"
                ],
                "ans": "B",
                "exp": "Since $h = \\left(\\frac{1}{2}g\\right) t^2$, plotting $h$ on y-axis against $t^2$ on x-axis produces a straight line with slope $m = \\frac{1}{2}g$."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Multi-Stage Velocity-Time Graph Analysis of an Express Train",
        "passage": "An express train travels along a straight railway track between two stations, Station P and Station Q. The graph of its velocity ($v$ in m/s) against time ($t$ in seconds) is recorded over a 60-second journey:<br>"
                   "• <b>Stage 1 ($0\\text{ to }20\\text{ s}$):</b> Velocity increases uniformly from rest ($0\\text{ m/s}$) to $30\\text{ m/s}$.<br>"
                   "• <b>Stage 2 ($20\\text{ to }50\\text{ s}$):</b> The train maintains a constant cruise velocity of $30\\text{ m/s}$.<br>"
                   "• <b>Stage 3 ($50\\text{ to }60\\text{ s}$):</b> The brakes are applied uniformly, bringing the train to rest at $60\\text{ s}$ ($v=0$).",
        "questions": [
            {
                "q": "What is the acceleration of the train during Stage 1 ($0\\text{ to }20\\text{ s}$)?",
                "options": ["$1.5\\text{ m/s}^2$", "$3.0\\text{ m/s}^2$", "$0.75\\text{ m/s}^2$", "$2.0\\text{ m/s}^2$"],
                "ans": "A",
                "exp": "$a_1 = \\frac{v - u}{\\Delta t} = \\frac{30 - 0}{20} = 1.5\\text{ m/s}^2$."
            },
            {
                "q": "What is the acceleration of the train during Stage 2 ($20\\text{ to }50\\text{ s}$)?",
                "options": ["$1.5\\text{ m/s}^2$", "$0\\text{ m/s}^2$", "$30\\text{ m/s}^2$", "$-3.0\\text{ m/s}^2$"],
                "ans": "B",
                "exp": "Velocity is constant at 30 m/s; therefore, rate of change of velocity is zero ($a = 0$)."
            },
            {
                "q": "What is the retardation (deceleration) of the train during Stage 3 ($50\\text{ to }60\\text{ s}$)?",
                "options": ["$-1.5\\text{ m/s}^2$", "$3.0\\text{ m/s}^2$", "$6.0\\text{ m/s}^2$", "$0.3\\text{ m/s}^2$"],
                "ans": "B",
                "exp": "$a_3 = \\frac{0 - 30}{10} = -3.0\\text{ m/s}^2$. Retardation is the magnitude of deceleration, which is $3.0\\text{ m/s}^2$."
            },
            {
                "q": "What is the total displacement (distance between Station P and Station Q) covered by the train in 60 seconds?",
                "options": ["1200 m", "1350 m", "1500 m", "1800 m"],
                "ans": "B",
                "exp": "Total displacement equals the area of the trapezium beneath the $v$-$t$ graph: $\\text{Area} = \\frac{1}{2} \\times (\\text{sum of parallel sides}) \\times \\text{height} = \\frac{1}{2} \\times (60 + 30) \\times 30 = \\frac{1}{2} \\times 90 \\times 30 = 1350\\text{ m}$."
            },
            {
                "q": "What is the average speed of the train over the entire 60-second journey?",
                "options": ["$22.5\\text{ m/s}$", "$30.0\\text{ m/s}$", "$15.0\\text{ m/s}$", "$25.0\\text{ m/s}$"],
                "ans": "A",
                "exp": "$\\text{Average speed} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{1350\\text{ m}}{60\\text{ s}} = 22.5\\text{ m/s}$."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Centripetal Mechanics in Uniform Circular Motion",
        "passage": "In a physics laboratory investigation of circular motion, students whirled a rubber bung of mass $m = 0.050\\text{ kg}$ tied to a nylon string of radius $r = 0.80\\text{ m}$ in a horizontal circular path.<br>"
                   "• The string passed through a smooth glass tube, and its lower end supported a hanging counterweight of mass $M = 0.40\\text{ kg}$.<br>"
                   "• The students maintained steady horizontal rotation such that the hanging mass remained stationary at equilibrium ($T = M g = 0.40 \\times 9.8 = 3.92\\text{ N}$).<br>"
                   "• The rubber bung completed 20 revolutions in 20.0 seconds (period $T_{rev} = 1.0\\text{ s}$).",
        "questions": [
            {
                "q": "What is the linear speed ($v$) of the rubber bung moving along the circular path?",
                "options": ["$2.51\\text{ m/s}$", "$5.03\\text{ m/s}$", "$1.60\\text{ m/s}$", "$10.0\\text{ m/s}$"],
                "ans": "B",
                "exp": "$v = \\frac{2\\pi r}{T_{rev}} = \\frac{2 \\times 3.1416 \\times 0.80\\text{ m}}{1.0\\text{ s}} = 5.026\\text{ m/s} \\approx 5.03\\text{ m/s}$."
            },
            {
                "q": "What is the magnitude of the centripetal acceleration ($a_c$) experienced by the rotating bung?",
                "options": ["$6.28\\text{ m/s}^2$", "$31.6\\text{ m/s}^2$", "$15.8\\text{ m/s}^2$", "$9.80\\text{ m/s}^2$"],
                "ans": "B",
                "exp": "$a_c = \\frac{v^2}{r} = \\frac{(5.026)^2}{0.80} = \\frac{25.27}{0.80} \\approx 31.6\\text{ m/s}^2$."
            },
            {
                "q": "What provides the necessary centripetal force to keep the rubber bung moving in a circle?",
                "options": [
                    "The tension force in the nylon string",
                    "Gravitational force of the Earth pulling downward",
                    "Air friction pushing the bung forward",
                    "Magnetic attraction from the glass tube"
                ],
                "ans": "A",
                "exp": "The inward radial tension in the string pulls the revolving bung toward the center of rotation, providing the centripetal force."
            },
            {
                "q": "In which direction does the rubber bung fly if the nylon string snaps suddenly?",
                "options": [
                    "Radially inward toward the glass tube",
                    "Radially outward away from the center",
                    "Tangentially along a straight line in the direction of its instantaneous velocity",
                    "It stops and drops vertically downward"
                ],
                "ans": "C",
                "exp": "The moment centripetal tension disappears, the bung continues along its instantaneous tangential straight-line velocity due to inertia."
            },
            {
                "q": "Why is uniform circular motion classified as an accelerated motion even when its speed is strictly constant?",
                "options": [
                    "Because its mass is changing",
                    "Because the direction of the velocity vector is continuously changing at every point along the circular path",
                    "Because the radius increases continuously",
                    "Because time slows down during rotation"
                ],
                "ans": "B",
                "exp": "Velocity is a vector quantity. Even if its magnitude (speed) is constant, continuous turning of its direction produces continuous centripetal acceleration."
            }
        ]
    }
]
