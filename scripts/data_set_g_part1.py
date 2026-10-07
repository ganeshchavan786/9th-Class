"""
Data module for CBSE Class 9 Science - SET G (Final Mastery & Grand Challenge Test)
Part 1: Chapters 1 to 4 (25 Grand Challenge MCQs per Chapter = 100 MCQs total)
Strictly 100% CBSE English Medium.
"""

CHAPTER_01_QUESTIONS = [
    {
        "q": "The side of a small cube is measured as $x = (10.0 \\pm 0.1)\\text{ cm}$. What is the maximum estimated percentage error in its calculated volume?",
        "options": ["1.0%", "2.0%", "3.0%", "0.1%"],
        "ans": "C",
        "exp": "Volume $V = x^3$. The relative percentage error is $\\frac{\\Delta V}{V} \\times 100 = 3 \\times \\left(\\frac{\\Delta x}{x}\\right) \\times 100 = 3 \\times \\left(\\frac{0.1}{10.0}\\right) \\times 100 = 3.0\\%$."
    },
    {
        "q": "If the slope of the $T^2$ versus $L$ graph for a simple pendulum is found to be $4.00\\text{ s}^2\\text{/m}$, what is the experimental local value of $g$ (take $\\pi = 3.1416$)?",
        "options": ["$9.87\\text{ m/s}^2$", "$9.80\\text{ m/s}^2$", "$10.0\\text{ m/s}^2$", "$9.65\\text{ m/s}^2$"],
        "ans": "A",
        "exp": "$\\text{Slope} = \\frac{4\\pi^2}{g} \\Rightarrow g = \\frac{4\\pi^2}{\\text{Slope}} = \\frac{4(3.1416)^2}{4.00} = (3.1416)^2 \\approx 9.87\\text{ m/s}^2$."
    },
    {
        "q": "A hollow metallic sphere of external radius $R$ and internal radius $r$ has mass $M$. What is the density of the metal?",
        "options": [
            "$\\frac{3M}{4\\pi(R^3 - r^3)}$",
            "$\\frac{3M}{4\\pi(R^3 + r^3)}$",
            "$\\frac{M}{\\frac{4}{3}\\pi R^3}$",
            "$\\frac{M}{4\\pi(R - r)^3}$"
        ],
        "ans": "A",
        "exp": "Volume of metal in hollow sphere $= \\frac{4}{3}\\pi R^3 - \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi(R^3 - r^3)$. Density $\\rho = \\frac{\\text{Mass}}{\\text{Volume}} = \\frac{3M}{4\\pi(R^3 - r^3)}$."
    },
    {
        "q": "A simple pendulum has time period $T$ on Earth. What is its time period when placed inside an artificial satellite orbiting Earth in free fall?",
        "options": ["$T$", "$T/6$", "Zero", "Infinitely large (it does not oscillate)"],
        "ans": "D",
        "exp": "Inside an orbiting satellite, effective gravity $g_{eff} = 0$ (weightlessness). $T = 2\\pi\\sqrt{L/0} \\rightarrow \\infty$; the pendulum does not oscillate."
    },
    {
        "q": "What is the least count of a vernier caliper if 1 main scale division is 0.5 mm and 20 vernier divisions coincide with 19 main scale divisions?",
        "options": ["0.025 mm", "0.05 mm", "0.01 mm", "0.1 mm"],
        "ans": "A",
        "exp": "$\\text{LC} = \\frac{1\\text{ MSD}}{n} = \\frac{0.5\\text{ mm}}{20} = 0.025\\text{ mm}$."
    },
    {
        "q": "An iceberg floats in seawater (density $1.03\\text{ g/cm}^3$) with pure ice density $0.92\\text{ g/cm}^3$. What percentage of the iceberg's total volume remains hidden underwater?",
        "options": ["89.3%", "10.7%", "92.0%", "80.0%"],
        "ans": "A",
        "exp": "Fraction submerged $= \\frac{\\rho_{ice}}{\\rho_{seawater}} = \\frac{0.92}{1.03} \\approx 0.893 = 89.3\\%$."
    },
    {
        "q": "A solid block of mass 120 g has dimensions $4\\text{ cm} \\times 5\\text{ cm} \\times 6\\text{ cm}$. When dropped into water, what fraction of its volume is submerged?",
        "options": ["100% (it sinks completely)", "100% (it barely floats)", "80%", "50%"],
        "ans": "A",
        "exp": "Volume $= 4 \\times 5 \\times 6 = 120\\text{ cm}^3$. Density $= 120\\text{ g} / 120\\text{ cm}^3 = 1.00\\text{ g/cm}^3$. Being equal to water density, it remains fully submerged in equilibrium (100%)."
    },
    {
        "q": "A pendulum clock that keeps correct time at sea level is taken to a high mountain peak where $g$ is $0.2\\%$ less. The clock will:",
        "options": ["Gain time by 86.4 s/day", "Lose time by 86.4 s/day", "Lose time by 172.8 s/day", "Keep identical time"],
        "ans": "B",
        "exp": "Fractional period change $\\frac{\\Delta T}{T} = -\\frac{1}{2}\\frac{\\Delta g}{g} = +0.1\\%$. Time lost per day $= 0.001 \\times 86400\\text{ s} = 86.4\\text{ seconds}$."
    },
    {
        "q": "The zero mark on the circular thimble of a screw gauge lies 5 divisions above the baseline when closed. It has least count 0.01 mm. The zero error is:",
        "options": ["$+0.05$ mm", "$-0.05$ mm", "$+0.01$ mm", "$-0.01$ mm"],
        "ans": "B",
        "exp": "When the circular scale zero is above the reference line, the error is negative ($-5 \\times 0.01 = -0.05\\text{ mm}$) and must be added to observed readings."
    },
    {
        "q": "Which fundamental physical constant has SI units $\\text{N}\\cdot\\text{m}^2\\cdot\\text{kg}^{-2}$?",
        "options": ["Universal Gravitational Constant ($G$)", "Acceleration due to gravity ($g$)", "Planck's constant", "Electric permittivity"],
        "ans": "A",
        "exp": "From $F = G \\frac{m_1 m_2}{r^2} \\Rightarrow G = \\frac{F r^2}{m_1 m_2}$, unit is $\\text{N}\\cdot\\text{m}^2/\\text{kg}^2$."
    },
    {
        "q": "In scientific scientific notation, how is the mass of an electron recorded ($9.109 \\times 10^{-31}\\text{ kg}$)?",
        "options": ["4 significant figures", "3 significant figures", "31 significant figures", "1 significant figure"],
        "ans": "A",
        "exp": "All digits in the mantissa (9, 1, 0, 9) are significant; the power of ten does not affect significant figure count (4 significant figures)."
    },
    {
        "q": "A student measures length of a rod using three instruments: (A) Meter rule, (B) Vernier Calipers, (C) Screw gauge. Which order of precision is correct?",
        "options": ["A > B > C", "C > B > A", "B > C > A", "A = B = C"],
        "ans": "B",
        "exp": "Screw gauge (LC 0.01 mm) > Vernier (LC 0.1 mm) > Meter rule (LC 1 mm). Finer least count equals higher precision."
    },
    {
        "q": "What is the dimensional formula of density?",
        "options": ["$[\\text{ML}^{-3}]$", "$[\\text{ML}^{-2}]$", "$[\\text{MLT}^{-1}]$", "$[\\text{M}^0\\text{L}^{-3}]$"],
        "ans": "A",
        "exp": "$\\text{Density} = \\text{Mass} / \\text{Volume} = [\\text{M}] / [\\text{L}^3] = [\\text{ML}^{-3}]$."
    },
    {
        "q": "If a solid metal cube of side $L$ expands linearly by $0.1\\%$ upon heating, what is the fractional increase in its volume?",
        "options": ["0.1%", "0.2%", "0.3%", "0.001%"],
        "ans": "C",
        "exp": "Volumetric expansion is 3 times linear expansion: $\\frac{\\Delta V}{V} \\approx 3 \\times \\frac{\\Delta L}{L} = 3 \\times 0.1\\% = 0.3\\%$."
    },
    {
        "q": "A beaker containing water is placed on a sensitive pan balance. An iron ball suspended from an external stand by a thread is lowered into the water without touching the beaker. The balance reading:",
        "options": ["Remains unchanged", "Increases by the mass of water displaced", "Decreases", "Becomes zero"],
        "ans": "B",
        "exp": "By Newton's third law, if water exerts an upward buoyant force $F_b$ on the ball, the ball exerts an equal downward force $F_b$ on the water, increasing the scale reading."
    },
    {
        "q": "A simple pendulum of length $L$ has period $T$. If the acceleration due to gravity increases by $4\\%$, its period approximately:",
        "options": ["Increases by 4%", "Decreases by 2%", "Increases by 2%", "Decreases by 4%"],
        "ans": "B",
        "exp": "Since $T \\propto g^{-1/2}$, fractional change $\\frac{\\Delta T}{T} \\approx -\\frac{1}{2} \\frac{\\Delta g}{g} = -\\frac{1}{2}(+4\\%) = -2\\%$."
    },
    {
        "q": "A body floats in liquid A with half its volume submerged, and in liquid B with $2/3$ of its volume submerged. What is the ratio of densities of liquid A to liquid B?",
        "options": ["$3:4$", "$4:3$", "$1:2$", "$3:2$"],
        "ans": "B",
        "exp": "$\\frac{1}{2} \\rho_A = \\frac{2}{3} \\rho_B \\Rightarrow \\frac{\\rho_A}{\\rho_B} = \\frac{2/3}{1/2} = \\frac{4}{3}$."
    },
    {
        "q": "Which of the following measurements is recorded with the greatest precision?",
        "options": ["4.0 m", "4.00 m", "4.000 m", "40 m"],
        "ans": "C",
        "exp": "'4.000 m' measures to the nearest millimeter (0.001 m), representing the smallest least count and highest precision."
    },
    {
        "q": "When calculating the area of a rectangle of sides 12.2 cm and 3.4 cm, the final answer rounded to proper significant figures is:",
        "options": ["41.48 cm²", "41.5 cm²", "41 cm²", "42 cm²"],
        "ans": "C",
        "exp": "$12.2 \\times 3.4 = 41.48\\text{ cm}^2$. The least number of significant figures in the data is 2 (in 3.4 cm), so the result is rounded to 2 significant figures: 41 cm²."
    },
    {
        "q": "A piece of ice floats in a beaker filled to the brim with water. When the ice melts completely, the water level:",
        "options": ["Overflows", "Drops noticeably", "Remains exactly the same", "First drops then overflows"],
        "ans": "C",
        "exp": "Floating ice displaces water equal to its own mass. When melted, the resulting water volume exactly equals the submerged volume it previously displaced."
    },
    {
        "q": "What is the time period of a simple pendulum of length $L = 9.8\\text{ m}$ where $g = 9.8\\text{ m/s}^2$?",
        "options": ["$2\\pi\\text{ seconds} \\approx 6.28\\text{ s}$", "1.0 s", "2.0 s", "3.14 s"],
        "ans": "A",
        "exp": "$T = 2\\pi \\sqrt{9.8 / 9.8} = 2\\pi(1) = 2\\pi \\approx 6.28\\text{ s}$."
    },
    {
        "q": "A vernier caliper has 50 divisions on its vernier scale coinciding with 49 mm of main scale. Its least count is:",
        "options": ["0.02 mm", "0.01 mm", "0.05 mm", "0.1 mm"],
        "ans": "A",
        "exp": "$\\text{Least count} = \\frac{1\\text{ mm}}{50} = 0.02\\text{ mm}$."
    },
    {
        "q": "If density of gold is $19.3\\text{ g/cm}^3$, what is its density in SI units?",
        "options": ["$193\\text{ kg/m}^3$", "$1930\\text{ kg/m}^3$", "$19300\\text{ kg/m}^3$", "$1.93\\text{ kg/m}^3$"],
        "ans": "C",
        "exp": "$1\\text{ g/cm}^3 = 1000\\text{ kg/m}^3 \\Rightarrow 19.3 \\times 1000 = 19300\\text{ kg/m}^3$."
    },
    {
        "q": "A hydrometer stem is calibrated with divisions from top to bottom. The markings indicate:",
        "options": [
            "Higher densities at the top, lower at the bottom",
            "Lower densities at the top, higher densities towards the bottom",
            "Uniform density throughout",
            "Temperature rather than density"
        ],
        "ans": "B",
        "exp": "In denser liquids, the hydrometer floats higher (sinks less), so lower numerical readings are at the top and higher readings at the bottom."
    },
    {
        "q": "Which experimental measurement has zero systematic instrumental error?",
        "options": [
            "An uncalibrated ruler",
            "A stopwatch with broken spring",
            "An ideal digital counter counting discrete events (e.g., number of full oscillations)",
            "A warped measuring tape"
        ],
        "ans": "C",
        "exp": "Counting discrete whole events (integers) has no instrumental scale error, unlike analog continuous scale instruments."
    }
]

CHAPTER_02_QUESTIONS = [
    {
        "q": "Which organelle forms the primary site of ribosome subunit synthesis inside the eukaryotic cell?",
        "options": ["Centrosome", "Nucleolus", "Golgi apparatus", "Endoplasmic reticulum"],
        "ans": "B",
        "exp": "The nucleolus is the specialized nuclear sub-compartment where ribosomal RNA (rRNA) is transcribed and combined with ribosomal proteins."
    },
    {
        "q": "What is the biochemical nature of the middle lamella that cements adjacent plant cell walls together?",
        "options": ["Calcium and Magnesium pectate", "Lignin and suberin", "Pure cellulose microfibrils", "Starch granules"],
        "ans": "A",
        "exp": "The middle lamella is an extracellular cementing layer composed of sticky calcium and magnesium pectate."
    },
    {
        "q": "Which cellular transport mechanism consumes metabolic ATP energy to pump ions against an electrochemical concentration gradient?",
        "options": ["Facilitated diffusion", "Active transport", "Simple diffusion", "Osmosis"],
        "ans": "B",
        "exp": "Active transport moves ions against concentration gradients using membrane protein pumps powered by ATP hydrolysis."
    },
    {
        "q": "What unique biochemical feature distinguishes the mitochondrial inner membrane from other eukaryotic membranes?",
        "options": [
            "It contains cellulose",
            "It has an unusually high protein-to-lipid ratio (around 75% protein) and contains cardiolipin",
            "It lacks any transport proteins",
            "It is completely impermeable to water"
        ],
        "ans": "B",
        "exp": "The inner mitochondrial membrane is packed with respiratory chain enzyme complexes and ATP synthases, giving it a 3:1 protein-to-lipid ratio."
    },
    {
        "q": "When ripe tomatoes turn from green to bright red during ripening, which organellar transformation occurs?",
        "options": [
            "Leucoplasts transform into chloroplasts",
            "Chloroplasts transform into chromoplasts as chlorophyll breaks down and lycopene carotenoids accumulate",
            "Vacuoles turn into mitochondria",
            "Ribosomes synthesize hemoglobin"
        ],
        "ans": "B",
        "exp": "Ripening involves chloroplast degradation and synthesis of red/orange carotenoid pigments within chromoplasts."
    },
    {
        "q": "Which cytoplasmic organelle is directly responsible for organizing mitotic spindle microtubules in animal cells?",
        "options": ["Centrosome (Centrioles)", "Lysosome", "Peroxisome", "Nucleolus"],
        "ans": "A",
        "exp": "Centrosomes contain a pair of centrioles that serve as the main microtubule-organizing centers (MTOCs) during animal cell mitosis."
    },
    {
        "q": "Which specialized microbody in plant cells converts stored fatty acids into carbohydrates during seed germination?",
        "options": ["Glyoxysome", "Lysosome", "Centriole", "Ribosome"],
        "ans": "A",
        "exp": "Glyoxysomes are specialized plant peroxisomes that run the glyoxylate cycle to convert stored lipids into sucrose."
    },
    {
        "q": "What is the primary function of plasmodesmata in plant tissues?",
        "options": [
            "To prevent water loss",
            "To provide microscopic cytoplasmic channels connecting adjacent plant cells for intercellular transport and signaling",
            "To synthesize starch",
            "To anchor roots to soil"
        ],
        "ans": "B",
        "exp": "Plasmodesmata are membrane-lined trans-wall pores that maintain cytoplasmic continuity (symplast) across adjacent plant cells."
    },
    {
        "q": "Which organelle acts as a dynamic intracellular calcium ($Ca^{2+}$) reservoir in skeletal muscle fibers?",
        "options": ["Sarcoplasmic Reticulum (modified Smooth ER)", "Mitochondria", "Lysosomes", "Nucleus"],
        "ans": "A",
        "exp": "The sarcoplasmic reticulum is specialized smooth ER that sequesters and releases $Ca^{2+}$ ions to regulate muscle contraction."
    },
    {
        "q": "Which eukaryotic organelle lacks a surrounding lipid membrane entirely?",
        "options": ["Peroxisome", "Ribosome", "Lysosome", "Vacuole"],
        "ans": "B",
        "exp": "Ribosomes are non-membrane-bound ribonucleoprotein complexes found in both prokaryotes and eukaryotes."
    },
    {
        "q": "Why does a plant cell not undergo cytolysis (bursting) when placed in a hypotonic medium where internal turgor pressure reaches 15 atmospheres?",
        "options": [
            "Water stops entering at 1 atm",
            "The cellulose cell wall exerts an equal inward mechanical wall pressure, maintaining structural integrity",
            "Cell sap is non-osmotic",
            "The tonoplast dissolves"
        ],
        "ans": "B",
        "exp": "The tensile strength of the cellulosic cell wall provides counter wall pressure ($WP = TP$), preventing osmotic lysis."
    },
    {
        "q": "What constitutes the 'nucleoid' of a bacterium?",
        "options": [
            "A membrane-bound nucleus with multiple chromosomes",
            "A single circular double-stranded DNA molecule without a nuclear envelope or histone proteins",
            "A clump of ribosomes",
            "A protein capsule"
        ],
        "ans": "B",
        "exp": "The bacterial nucleoid is a region containing naked, uncompartmentalized, circular genomic DNA."
    },
    {
        "q": "Which organelle contains hydrolytic enzymes that function optimally at an acidic pH of ~4.5 to 5.0?",
        "options": ["Lysosome", "Peroxisome", "Mitochondrial matrix", "Chloroplast stroma"],
        "ans": "A",
        "exp": "Lysosomal acid hydrolases require an acidic luminal pH maintained by proton-pumping v-type ATPases."
    },
    {
        "q": "The stacks of flattened disc-like thylakoid sacs inside a chloroplast are termed:",
        "options": ["Cristae", "Grana", "Cisternae", "Stroma"],
        "ans": "B",
        "exp": "Thylakoids are organized into membranous stacks called grana (singular: granum), where light reactions occur."
    },
    {
        "q": "The trans-face of the Golgi apparatus is also known as the:",
        "options": ["Forming face", "Maturing / Exit face", "Inner face", "Entry cis-face"],
        "ans": "B",
        "exp": "Cis-face is the receiving/forming face facing the ER; trans-face is the exit/maturing face that pinches off secretory vesicles."
    },
    {
        "q": "Which antibiotic inhibits bacterial cell wall synthesis by blocking peptidoglycan cross-linking?",
        "options": ["Penicillin", "Insulin", "Adrenaline", "Aspirin"],
        "ans": "A",
        "exp": "Penicillin targets transpeptidase enzymes that cross-link peptidoglycan in bacterial cell walls, causing bacterial lysis without harming human cells."
    },
    {
        "q": "Which cellular organelle is responsible for decomposing toxic hydrogen peroxide ($H_2O_2$) into water and oxygen using catalase?",
        "options": ["Peroxisome", "Ribosome", "Golgi apparatus", "Centrosome"],
        "ans": "A",
        "exp": "Peroxisomes contain catalase and oxidases to detoxify hydrogen peroxide and break down long-chain fatty acids."
    },
    {
        "q": "A cell that has lost its nucleus, ribosomes, and mitochondria yet remains metabolically active in vascular transport for years is the:",
        "options": ["Sieve tube element in phloem", "Xylem vessel", "Tracheid", "Guard cell"],
        "ans": "A",
        "exp": "Phloem sieve tube elements lack nuclei at maturity but stay alive through metabolic support from companion cells."
    },
    {
        "q": "The proteinaceous core structure that holds sister chromatids together at the centromere and binds spindle microtubules is the:",
        "options": ["Kinetochore", "Centrosome", "Telomere", "Chromomere"],
        "ans": "A",
        "exp": "Kinetochores are disc-shaped protein complexes assembled on centromeric DNA where spindle fibers attach."
    },
    {
        "q": "Which type of cell division produces four non-identical haploid gametes from a diploid progenitor cell?",
        "options": ["Mitosis", "Meiosis", "Amitosis", "Binary fission"],
        "ans": "B",
        "exp": "Meiosis is reduction division consisting of two successive nuclear divisions yielding four haploid gametes."
    },
    {
        "q": "What happens when a cell's lysosomes rupture en masse under pathological stress?",
        "options": [
            "The cell synthesizes more ATP",
            "Autolysis (self-digestion) occurs, leading to programmed necrosis of the cell",
            "The cell becomes immortal",
            "The cell wall thickens"
        ],
        "ans": "B",
        "exp": "Widespread lysosomal leakage releases acid hydrolases into the neutral cytosol, digesting cellular components (autolysis)."
    },
    {
        "q": "What is the structural diameter of a eukaryotic 80S ribosome?",
        "options": ["20–30 nm", "2 μm", "200 μm", "1 mm"],
        "ans": "A",
        "exp": "Ribosomes are nanometer-scale complexes measuring roughly 20 to 30 nanometers in diameter."
    },
    {
        "q": "Which of the following cellular structures is present in prokaryotes, fungi, and plants, but entirely absent in animals?",
        "options": ["Mitochondria", "Cell wall", "Plasma membrane", "Ribosomes"],
        "ans": "B",
        "exp": "Cell walls occur in bacteria (peptidoglycan), fungi (chitin), and plants (cellulose), but never in animal cells."
    },
    {
        "q": "The liquid ground substance filling the chloroplast interior surrounding thylakoids is the:",
        "options": ["Matrix", "Stroma", "Cytosol", "Tonoplasm"],
        "ans": "B",
        "exp": "The stroma contains soluble enzymes (e.g., RuBisCO) that catalyze the dark reactions of the Calvin cycle."
    },
    {
        "q": "Which specialized lipid molecule stabilizes plasma membrane fluidity across varying temperatures in mammalian cells?",
        "options": ["Cellulose", "Cholesterol", "Triglyceride", "Starch"],
        "ans": "B",
        "exp": "Cholesterol intercalates between phospholipids, preventing membrane crystallization at low temperatures and excessive fluidity at high temperatures."
    }
]

CHAPTER_03_QUESTIONS = [
    {
        "q": "Which meristematic tissue is responsible for regenerating clipped grass blades after lawn-mowing or grazing?",
        "options": ["Apical meristem", "Intercalary meristem", "Cork cambium", "Lateral meristem"],
        "ans": "B",
        "exp": "Intercalary meristems located at the bases of internodes and leaf blades divide actively to regenerate lost foliage."
    },
    {
        "q": "What complex aromatic polymer impregnates the secondary cell walls of sclerenchyma, imparting compressive strength and waterproofing?",
        "options": ["Pectin", "Lignin", "Cellulose", "Suberin"],
        "ans": "B",
        "exp": "Lignin is a rigid polyphenolic polymer that reinforces xylem and sclerenchyma cell walls."
    },
    {
        "q": "Which type of xylem vessel perforation facilitates rapid, bulk longitudinal water flow in angiosperms compared to gymnosperms?",
        "options": [
            "Pitted imperforate tracheids",
            "Perforation plates at vessel element end walls",
            "Suberin casparian strips",
            "Sieve pore fields"
        ],
        "ans": "B",
        "exp": "Angiosperm vessel elements have completely open or scalariform perforation plates, providing low-resistance conduits."
    },
    {
        "q": "What is the primary histological function of companion cells in angiosperm phloem?",
        "options": [
            "Mechanical support via thick lignin walls",
            "Active loading and unloading of sugars into enucleated sieve tube elements via proton symport",
            "Water storage",
            "Secretion of latex"
        ],
        "ans": "B",
        "exp": "Companion cells utilize $H^+$-ATPase symporters to actively load sucrose into sieve tube elements."
    },
    {
        "q": "Which epidermal modification in roots drastically increases total absorptive surface area for water and mineral uptake?",
        "options": ["Trichomes", "Root hairs (unicellular extensions)", "Stomata", "Cuticle"],
        "ans": "B",
        "exp": "Root hairs are delicate tubular outgrowths of root epidermal (epiblema) cells that amplify surface area."
    },
    {
        "q": "Which tissue lines the human urinary bladder, allowing dramatic stretching and distension as urine accumulates?",
        "options": ["Transitional Epithelium (Urothelium)", "Ciliated Columnar", "Simple Squamous", "Stratified Keratinized"],
        "ans": "A",
        "exp": "Transitional epithelium has multilayered rounded cells that flatten upon distension without tearing."
    },
    {
        "q": "The microscopic structural functional unit of compact mammalian bone tissue is the:",
        "options": ["Osteon (Haversian System)", "Chondrocyte lacuna", "Sarcomere", "Nephron"],
        "ans": "A",
        "exp": "Compact bone is organized into concentric cylindrical osteons centered on neurovascular Haversian canals."
    },
    {
        "q": "Which non-collagenous protein fiber imparts reversible elastic stretchability to ligaments and arterial walls?",
        "options": ["Keratin", "Elastin", "Fibrin", "Myosin"],
        "ans": "B",
        "exp": "Elastin forms branched elastic fibers capable of stretching up to 1.5 times their length and snapping back."
    },
    {
        "q": "Which cell type in human blood develops into antibody-secreting plasma cells during adaptive immune responses?",
        "options": ["B-Lymphocytes", "Neutrophils", "Erythrocytes", "Platelets"],
        "ans": "A",
        "exp": "B-lymphocytes recognize specific antigens and differentiate into plasma cells that secrete circulating antibodies."
    },
    {
        "q": "What is the primary organic matrix protein synthesized by chondrocytes in hyaline cartilage?",
        "options": ["Type II Collagen and Chondroitin sulfate proteoglycans", "Hydroxyapatite", "Keratin", "Myosin"],
        "ans": "A",
        "exp": "Cartilage matrix consists of Type II collagen fibrils embedded in hydrated chondroitin sulfate proteoglycan gel."
    },
    {
        "q": "Which muscular tissue displays syncytial multinucleate fibers with peripherally located nuclei?",
        "options": ["Skeletal muscle", "Smooth muscle", "Cardiac muscle", "Myoepithelium"],
        "ans": "A",
        "exp": "Skeletal muscle fibers arise from fusion of embryonic myoblasts, creating long syncytial multinucleated fibers."
    },
    {
        "q": "The insulating lipid-rich sheath surrounding many vertebrate nerve axons that accelerates impulse conduction is the:",
        "options": ["Myelin sheath", "Sarcolemma", "Perichondrium", "Perineurium"],
        "ans": "A",
        "exp": "Schwann cells (PNS) and oligodendrocytes (CNS) produce myelin sheaths enabling saltatory conduction."
    },
    {
        "q": "The gaps along a myelinated axon where voltage-gated sodium channels concentrate are called:",
        "options": ["Nodes of Ranvier", "Synapses", "Dendritic spines", "Intercalated discs"],
        "ans": "A",
        "exp": "Nodes of Ranvier are periodic gaps in myelin where action potentials regenerate rapidly via saltatory conduction."
    },
    {
        "q": "Which plant ground tissue contains cells that are dead at maturity and possess branched stone-cell morphologies (sclereids)?",
        "options": ["Collenchyma", "Sclerenchyma (Brachysclereids)", "Aerenchyma", "Chlorenchyma"],
        "ans": "B",
        "exp": "Sclereids (grit cells in pear fruit) are short, thick, lignified sclerenchyma cells providing compressive hardness."
    },
    {
        "q": "The Casparian strip in the plant root endodermis is impregnated with which hydrophobic substance to force water into symplastic entry?",
        "options": ["Suberin", "Cutin", "Cellulose", "Pectin"],
        "ans": "A",
        "exp": "Suberin deposition in endodermal radial walls forms the Casparian strip, blocking apoplastic water movement."
    },
    {
        "q": "Which white blood cell type is the most abundant phagocyte in circulating human blood, arriving first at bacterial infection sites?",
        "options": ["Neutrophils", "Eosinophils", "Basophils", "Monocytes"],
        "ans": "A",
        "exp": "Neutrophils make up 60–70% of circulating WBCs and act as primary phagocytes during acute bacterial inflammation."
    },
    {
        "q": "Mast cells located in areolar connective tissue secrete which vasoactive substance responsible for inflammatory vasodilation and allergies?",
        "options": ["Histamine", "Insulin", "Pepsin", "Hemoglobin"],
        "ans": "A",
        "exp": "Mast cells degranulate to release histamine and heparin during allergic reactions and tissue injury."
    },
    {
        "q": "Which specialized epithelial tissue possesses goblet cells that secrete protective viscous mucus?",
        "options": ["Columnar epithelium (e.g., intestinal lining)", "Squamous epithelium", "Dense regular tissue", "Stratified cuboidal"],
        "ans": "A",
        "exp": "Simple columnar epithelium of the stomach and intestine contains goblet cells that secrete protective mucus."
    },
    {
        "q": "The contractile unit of a muscle myofibril bounded by two adjacent Z-lines is the:",
        "options": ["Sarcomere", "Sarcolemma", "Osteon", "Synapse"],
        "ans": "A",
        "exp": "The sarcomere is the basic repeating structural and functional contractile unit containing actin and myosin filaments."
    },
    {
        "q": "Which blood plasma protein is essential for maintaining intravascular colloidal osmotic (oncotic) pressure?",
        "options": ["Serum Albumin", "Fibrinogen", "Gamma globulin", "Hemoglobin"],
        "ans": "A",
        "exp": "Albumin constitutes ~60% of total plasma protein and prevents fluid from leaking out of capillaries into tissues."
    },
    {
        "q": "In woody stems, lenticels are specialized aerating pores located in the:",
        "options": ["Bark (Periderm)", "Woody xylem core", "Leaf petiole", "Root tip"],
        "ans": "A",
        "exp": "Lenticels are loose, non-suberized cellular openings in tree bark that permit gas exchange in mature woody organs."
    },
    {
        "q": "Which cellular component of blood releases serotonin and thromboxane $A_2$ to cause localized vasoconstriction following vascular laceration?",
        "options": ["Platelets", "RBCs", "T-cells", "Plasma albumin"],
        "ans": "A",
        "exp": "Activated platelets release vasoconstrictors to minimize blood loss while building the primary hemostatic plug."
    },
    {
        "q": "Chondrocytes are located within fluid-filled microscopic matrix cavities called:",
        "options": ["Lacunae", "Haversian canals", "Canaliculi", "Ventricles"],
        "ans": "A",
        "exp": "Living cartilage cells (chondrocytes) occupy isolated spaces within the extracellular matrix termed lacunae."
    },
    {
        "q": "Which muscle type contracts automatically under the control of pacemaker nodes without requiring conscious neural input?",
        "options": ["Cardiac muscle (Sinoatrial node pacing)", "Skeletal muscle", "Tongue muscle", "Diaphragm muscle"],
        "ans": "A",
        "exp": "Cardiac muscle possesses myogenic autorhythmicity initiated by the heart's natural pacemaker (SA node)."
    },
    {
        "q": "Which epithelial type forms the dry, impermeable, abrasion-resistant outer epidermis of mammalian skin?",
        "options": ["Stratified Keratinized Squamous Epithelium", "Simple Cuboidal", "Ciliated Columnar", "Pseudostratified"],
        "ans": "A",
        "exp": "Keratinized stratified squamous epithelium consists of dead superficial cellular layers packed with tough insoluble keratin."
    }
]

CHAPTER_04_QUESTIONS = [
    {
        "q": "A particle moves along a circular path of radius $R$. What is the ratio of distance to displacement magnitude after completing a semi-circle ($180^\\circ$)?",
        "options": ["$\\pi : 2$", "$2 : \\pi$", "$\\pi : 1$", "$1 : 1$"],
        "ans": "A",
        "exp": "Distance along semicircle $= \\pi R$. Displacement across diameter $= 2R$. Ratio $= \\frac{\\pi R}{2R} = \\frac{\\pi}{2}$."
    },
    {
        "q": "A stone dropped from the top of a tower of height $H$ reaches the ground in time $t$. Where is the stone at time $t/2$?",
        "options": ["At height $H/2$", "At height $3H/4$ above ground", "At height $H/4$ above ground", "At ground level"],
        "ans": "B",
        "exp": "Distance fallen in $t/2$: $s = \\frac{1}{2}g(t/2)^2 = \\frac{1}{4}(\\frac{1}{2}gt^2) = \\frac{1}{4}H$. Height remaining above ground $= H - \\frac{1}{4}H = \\frac{3}{4}H$."
    },
    {
        "q": "A car accelerates uniformly from rest at $2\\text{ m/s}^2$ for $10\\text{ s}$, then coasts at constant speed for $20\\text{ s}$, and finally brakes to rest in $5\\text{ s}$. Total distance covered is:",
        "options": ["100 m", "550 m", "600 m", "450 m"],
        "ans": "B",
        "exp": "$v_{max} = 2 \\times 10 = 20\\text{ m/s}$. Phase 1: $s_1 = \\frac{1}{2}(2)(10)^2 = 100\\text{ m}$. Phase 2: $s_2 = 20 \\times 20 = 400\\text{ m}$. Phase 3: $s_3 = \\frac{1}{2}(20)(5) = 50\\text{ m}$. Total $= 100 + 400 + 50 = 550\\text{ m}$."
    },
    {
        "q": "A body starts from rest and moves with uniform acceleration. The ratio of distances covered in the 1st, 2nd, and 3rd seconds of motion is:",
        "options": ["$1 : 2 : 3$", "$1 : 4 : 9$", "$1 : 3 : 5$ (Galileo's odd numbers law)", "$1 : 1 : 1$"],
        "ans": "C",
        "exp": "Distance in $n$-th second $s_n = u + \\frac{1}{2}a(2n - 1)$. For $u = 0$, $s_n \\propto (2n - 1)$, giving ratios $1 : 3 : 5 : 7...$"
    },
    {
        "q": "If the displacement of a body is proportional to the square of time ($s \\propto t^2$), the body is moving with:",
        "options": ["Uniform velocity", "Uniform acceleration", "Increasing acceleration", "Zero velocity"],
        "ans": "B",
        "exp": "Since $s = \\frac{1}{2}at^2$, $s \\propto t^2$ implies that acceleration $a$ is strictly constant."
    },
    {
        "q": "A bullet moving at $200\\text{ m/s}$ penetrates a wooden block to a depth of 10 cm before stopping. What is its average deceleration inside the block?",
        "options": ["$2 \\times 10^5\\text{ m/s}^2$", "$4 \\times 10^5\\text{ m/s}^2$", "$2 \\times 10^4\\text{ m/s}^2$", "$10^5\\text{ m/s}^2$"],
        "ans": "A",
        "exp": "$v^2 = u^2 + 2as \\Rightarrow 0 = (200)^2 + 2a(0.10) \\Rightarrow 0.20 a = -40000 \\Rightarrow a = -200,000\\text{ m/s}^2 = -2 \\times 10^5\\text{ m/s}^2$."
    },
    {
        "q": "A wheel of radius $0.5\\text{ m}$ rotates at 120 revolutions per minute (rpm). What is the linear speed of a point on the rim?",
        "options": ["$\\pi\\text{ m/s} \\approx 3.14\\text{ m/s}$", "$2\\pi\\text{ m/s} \\approx 6.28\\text{ m/s}$", "$60\\text{ m/s}$", "$120\\text{ m/s}$"],
        "ans": "B",
        "exp": "Frequency $f = 120/60 = 2\\text{ rev/s}$. Speed $v = 2\\pi r f = 2\\pi(0.5)(2) = 2\\pi \\approx 6.28\\text{ m/s}$."
    },
    {
        "q": "Two trains of length 150 m each travel on parallel tracks in opposite directions with speeds $36\\text{ km/h}$ and $54\\text{ km/h}$. Time taken to completely cross each other is:",
        "options": ["12 s", "15 s", "20 s", "30 s"],
        "ans": "A",
        "exp": "Relative speed $= 36 + 54 = 90\\text{ km/h} = 90 \\times (5/18) = 25\\text{ m/s}$. Total distance to cross $= 150 + 150 = 300\\text{ m}$. Time $= 300/25 = 12\\text{ s}$."
    },
    {
        "q": "An object thrown vertically upward reaches a peak height $H$. What is its speed at half the peak height ($H/2$)?",
        "options": ["$u/2$", "$u/\\sqrt{2}$", "$\\sqrt{2} u$", "$u/4$"],
        "ans": "B",
        "exp": "$v^2 = u^2 - 2g(H/2) = u^2 - gH$. Since $H = \\frac{u^2}{2g}$, $gH = \\frac{u^2}{2}$. Thus $v^2 = u^2 - \\frac{u^2}{2} = \\frac{u^2}{2} \\Rightarrow v = \\frac{u}{\\sqrt{2}}$."
    },
    {
        "q": "Can a body have a constant speed and a changing velocity simultaneously?",
        "options": [
            "Yes, in uniform circular motion",
            "No, if speed is constant, velocity must be constant",
            "Only in deep space",
            "Only when acceleration is zero"
        ],
        "ans": "A",
        "exp": "In uniform circular motion, speed is constant while the direction of motion continuously turns, continuously altering velocity."
    },
    {
        "q": "What does a negative slope on a velocity-time graph indicate?",
        "options": ["Increasing acceleration", "Retardation (deceleration)", "Zero velocity", "Infinite speed"],
        "ans": "B",
        "exp": "A negative slope $\\Delta v / \\Delta t < 0$ means velocity is decreasing with time, representing retardation."
    },
    {
        "q": "The displacement $s$ of a particle varies with time as $s = 3t + 2t^2$. Its initial velocity ($t=0$) and acceleration are:",
        "options": [
            "$u = 3\\text{ m/s}$, $a = 4\\text{ m/s}^2$",
            "$u = 0$, $a = 2\\text{ m/s}^2$",
            "$u = 2\\text{ m/s}$, $a = 3\\text{ m/s}^2$",
            "$u = 3\\text{ m/s}$, $a = 2\\text{ m/s}^2$"
        ],
        "ans": "A",
        "exp": "Comparing with $s = ut + \\frac{1}{2}at^2$: $u = 3\\text{ m/s}$, and $\\frac{1}{2}a = 2 \\Rightarrow a = 4\\text{ m/s}^2$."
    },
    {
        "q": "If a body covers distance $x$ in time $t$ such that $x = at^3$, its acceleration is:",
        "options": ["Constant", "Decreasing", "Proportional to time ($a \\propto t$)", "Zero"],
        "ans": "C",
        "exp": "$v = \\frac{dx}{dt} = 3at^2$, and $a_{acc} = \\frac{dv}{dt} = 6at \\propto t$. Acceleration increases linearly with time."
    },
    {
        "q": "A ball dropped from height $h$ bounces back to height $h/4$. What is the coefficient of restitution $e$?",
        "options": ["0.25", "0.50", "0.75", "0.10"],
        "ans": "B",
        "exp": "Rebound height $h' = e^2 h$. Here $h/4 = e^2 h \\Rightarrow e^2 = 1/4 \\Rightarrow e = 0.50$."
    },
    {
        "q": "A particle moves with constant acceleration $a = 2\\text{ m/s}^2$. If its velocity after 5 seconds is 15 m/s, what was its initial velocity?",
        "options": ["$5\\text{ m/s}$", "$10\\text{ m/s}$", "$25\\text{ m/s}$", "$0\\text{ m/s}$"],
        "ans": "A",
        "exp": "$v = u + at \\Rightarrow 15 = u + (2 \\times 5) \\Rightarrow u = 15 - 10 = 5\\text{ m/s}$."
    },
    {
        "q": "Under what condition is the magnitude of average velocity equal to average speed?",
        "options": [
            "When the body moves along a straight line in a fixed single direction without reversing",
            "When the body moves in a closed circle",
            "When acceleration is zero only",
            "Never"
        ],
        "ans": "A",
        "exp": "Average velocity equals average speed only when total distance equals displacement magnitude (unidirectional straight-line path)."
    },
    {
        "q": "What is the centripetal acceleration of an Earth satellite orbiting at speed $v = 8000\\text{ m/s}$ at orbital radius $r = 6.4 \\times 10^6\\text{ m}$?",
        "options": ["$10.0\\text{ m/s}^2$", "$9.8\\text{ m/s}^2$", "$1.0\\text{ m/s}^2$", "$0\\text{ m/s}^2$"],
        "ans": "A",
        "exp": "$a_c = \\frac{v^2}{r} = \\frac{(8000)^2}{6.4 \\times 10^6} = \\frac{64 \\times 10^6}{6.4 \\times 10^6} = 10.0\\text{ m/s}^2$."
    },
    {
        "q": "A car travelling at speed $v$ stops in distance $d$ when braking force $F$ is applied. If the car's initial speed is $3v$, what is the new stopping distance under the same braking force?",
        "options": ["$3d$", "$6d$", "$9d$", "$d/3$"],
        "ans": "C",
        "exp": "Stopping distance $d \\propto v^2$. If speed triples ($3v$), braking distance increases by $3^2 = 9$ times ($9d$)."
    },
    {
        "q": "A body is projected vertically upwards with velocity $u$. What is its velocity when it returns to the point of projection (neglecting air resistance)?",
        "options": ["$+u$", "$-u$ (same magnitude, opposite direction)", "Zero", "$u/2$"],
        "ans": "B",
        "exp": "By conservation of mechanical energy, impact speed equals projection speed, directed downward ($-u$)."
    },
    {
        "q": "What is the ratio of average speed to average velocity for a body that travels along the circumference of a circle and returns to the start?",
        "options": ["1", "Zero", "Undefined (division by zero)", "$\\pi$"],
        "ans": "C",
        "exp": "Net displacement is zero; average velocity is 0. Dividing non-zero average speed by 0 is mathematically undefined."
    },
    {
        "q": "A particle travelling with uniform acceleration covers 20 m in the 2nd second and 30 m in the 3rd second. What is its acceleration?",
        "options": ["$5\\text{ m/s}^2$", "$10\\text{ m/s}^2$", "$2.5\\text{ m/s}^2$", "$15\\text{ m/s}^2$"],
        "ans": "B",
        "exp": "$s_n = u + a(n - 0.5)$. Difference $s_3 - s_2 = a \\Rightarrow 30 - 20 = 10\\text{ m/s}^2$."
    },
    {
        "q": "What is the instantaneous velocity of a body thrown vertically upwards when it reaches the peak of its trajectory?",
        "options": ["$9.8\\text{ m/s}$", "Zero", "Infinitely large", "$u/2$"],
        "ans": "B",
        "exp": "At the peak apex, the object momentarily halts ($v=0$) before reversing its vertical trajectory."
    },
    {
        "q": "What is the acceleration of the same body at the peak of its trajectory?",
        "options": ["Zero", "$9.8\\text{ m/s}^2$ downward", "$9.8\\text{ m/s}^2$ upward", "Undefined"],
        "ans": "B",
        "exp": "Even though instantaneous velocity is zero, gravitational acceleration $g = 9.8\\text{ m/s}^2$ downward acts continuously."
    },
    {
        "q": "A graph of $v^2$ versus $s$ for a particle starting from rest and moving with uniform acceleration is a:",
        "options": [
            "Straight line passing through the origin with slope $2a$",
            "Parabola curving upwards",
            "Hyperbola",
            "Horizontal line"
        ],
        "ans": "A",
        "exp": "From $v^2 = 2as$, plotting $v^2$ on y-axis against $s$ on x-axis produces a straight line $y = mx$ with slope $m = 2a$."
    },
    {
        "q": "Which property of motion is strictly relative and depends on the observer's frame of reference?",
        "options": ["Rest and motion", "Velocity", "Displacement", "All of the above"],
        "ans": "D",
        "exp": "Rest, motion, displacement, and velocity are all defined relative to a specified frame of reference."
    }
]
