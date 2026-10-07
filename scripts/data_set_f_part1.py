"""
Data module for CBSE Class 9 Science - SET F (Rapid Fire Speed Test)
Part 1: Chapters 1 to 4 (25 Rapid Fire MCQs per Chapter = 100 MCQs total)
Strictly 100% CBSE English Medium.
"""

CHAPTER_01_QUESTIONS = [
    {
        "q": "What is the SI base unit of thermodynamic temperature?",
        "options": ["Degree Celsius (°C)", "Kelvin (K)", "Fahrenheit (°F)", "Joule (J)"],
        "ans": "B",
        "exp": "Kelvin (K) is the SI base unit of temperature. 0°C corresponds to 273.15 K."
    },
    {
        "q": "How many millimeters (mm) are there in 1 kilometer (km)?",
        "options": ["$10^3\\text{ mm}$", "$10^5\\text{ mm}$", "$10^6\\text{ mm}$", "$10^9\\text{ mm}$"],
        "ans": "C",
        "exp": "$1\\text{ km} = 1000\\text{ m} = 1000 \\times 1000\\text{ mm} = 10^6\\text{ mm}$."
    },
    {
        "q": "Which of the following physical quantities is a scalar quantity?",
        "options": ["Velocity", "Displacement", "Mass", "Acceleration"],
        "ans": "C",
        "exp": "Mass has only magnitude with no directional dependence, making it a scalar quantity."
    },
    {
        "q": "What is the least count of an ordinary school laboratory meter scale?",
        "options": ["1 cm", "1 mm (0.1 cm)", "0.1 mm", "0.01 cm"],
        "ans": "B",
        "exp": "A standard school meter rule is graduated in millimeters; its smallest division is 1 mm (0.1 cm)."
    },
    {
        "q": "If the effective length of a simple pendulum is made 4 times longer, its time period becomes:",
        "options": ["Half", "2 times", "4 times", "16 times"],
        "ans": "B",
        "exp": "$T = 2\\pi\\sqrt{L/g} \\propto \\sqrt{L}$. If length increases by 4 times, $T$ increases by $\\sqrt{4} = 2$ times."
    },
    {
        "q": "What is the density of pure liquid water at 4°C in SI units?",
        "options": ["$1\\text{ kg/m}^3$", "$100\\text{ kg/m}^3$", "$1000\\text{ kg/m}^3$", "$10000\\text{ kg/m}^3$"],
        "ans": "C",
        "exp": "Water has maximum density at 4°C: $1.00\\text{ g/cm}^3 = 1000\\text{ kg/m}^3$."
    },
    {
        "q": "Which physical quantity has the SI unit $\\text{kg}\\cdot\\text{m}^{-3}$?",
        "options": ["Pressure", "Density", "Force", "Momentum"],
        "ans": "B",
        "exp": "Density is mass per unit volume ($\\text{kg/m}^3 = \\text{kg}\\cdot\\text{m}^{-3}$)."
    },
    {
        "q": "What is the time period of a seconds pendulum?",
        "options": ["1.0 second", "2.0 seconds", "0.5 second", "4.0 seconds"],
        "ans": "B",
        "exp": "A seconds pendulum takes 1 second to swing from one extreme to the other; its full oscillation time period is exactly 2.0 seconds."
    },
    {
        "q": "Which laboratory apparatus is used to accurately measure a fixed volume of 25.0 mL of liquid?",
        "options": ["Beaker", "Volumetric Pipette", "Conical flask", "Test tube"],
        "ans": "B",
        "exp": "A volumetric pipette has a calibration mark delivering an exact volume (25.0 mL) with high precision."
    },
    {
        "q": "How many significant figures are in the measurement 0.05020 m?",
        "options": ["2", "3", "4", "5"],
        "ans": "C",
        "exp": "Leading zeros (0.0) are placeholders. '5', '0', '2', and the trailing '0' are significant (4 significant figures)."
    },
    {
        "q": "If an object sinks in water, its relative density is:",
        "options": ["Equal to 1", "Less than 1", "Greater than 1", "Zero"],
        "ans": "C",
        "exp": "An object sinks when its density exceeds the density of water (Relative density $> 1$)."
    },
    {
        "q": "The pitch of a micrometer screw gauge is 1 mm and it has 100 circular divisions. Its least count is:",
        "options": ["0.1 mm", "0.01 mm", "0.001 mm", "0.05 mm"],
        "ans": "B",
        "exp": "$\\text{Least count} = \\frac{1\\text{ mm}}{100} = 0.01\\text{ mm}$."
    },
    {
        "q": "Which flame color indicates complete combustion in a properly aerated Bunsen burner?",
        "options": ["Yellow luminous flame", "Non-luminous blue flame", "Green flame", "Smoky orange flame"],
        "ans": "B",
        "exp": "When the air collar is open, ample oxygen produces a roaring, non-luminous blue flame of complete combustion."
    },
    {
        "q": "What is the value of standard atmospheric pressure at sea level in Pascals (Pa)?",
        "options": ["$1.013 \\times 10^5\\text{ Pa}$", "$1.013 \\times 10^3\\text{ Pa}$", "$100\\text{ Pa}$", "$9.8\\text{ Pa}$"],
        "ans": "A",
        "exp": "$1\\text{ atm} = 760\\text{ mm of Hg} = 1.013 \\times 10^5\\text{ Pa}$ (approx. $101.3\\text{ kPa}$)."
    },
    {
        "q": "Which quantity remains constant during a fair controlled scientific experiment?",
        "options": ["Independent variable", "Dependent variable", "Controlled variables", "Random variable"],
        "ans": "C",
        "exp": "Controlled variables are kept strictly constant so that only the independent variable affects the dependent variable."
    },
    {
        "q": "Convert $25^\\circ\\text{C}$ to the Kelvin scale:",
        "options": ["248 K", "298 K", "300 K", "273 K"],
        "ans": "B",
        "exp": "$T(K) = 25 + 273 = 298\\text{ K}$."
    },
    {
        "q": "What is the volume of a cube having side length 2 cm?",
        "options": ["4 cm³", "6 cm³", "8 cm³", "16 cm³"],
        "ans": "C",
        "exp": "$\\text{Volume} = s^3 = (2\\text{ cm})^3 = 8\\text{ cm}^3$."
    },
    {
        "q": "What does a beam balance compare?",
        "options": ["Weights", "Gravitational masses", "Volumes", "Densities"],
        "ans": "B",
        "exp": "A beam balance compares an unknown gravitational mass against standard reference masses ($m_1 g = m_2 g \\Rightarrow m_1 = m_2$)."
    },
    {
        "q": "Parallax error is classified under which category of experimental errors?",
        "options": ["Instrumental zero error", "Personal observational error", "Environmental error", "Theoretical error"],
        "ans": "B",
        "exp": "Parallax is a personal observational error caused by the observer's line of sight not being perpendicular to the scale."
    },
    {
        "q": "What is the symbol for the SI prefix 'micro'?",
        "options": ["$m$", "$M$", "$\\mu$", "$n$"],
        "ans": "C",
        "exp": "Micro is denoted by the Greek letter $\\mu$ (mu) and represents $10^{-6}$."
    },
    {
        "q": "A piece of wood of volume 50 cm³ and density 0.8 g/cm³ has mass:",
        "options": ["40 g", "62.5 g", "50 g", "0.016 g"],
        "ans": "A",
        "exp": "$\\text{Mass} = \\text{Volume} \\times \\text{Density} = 50\\text{ cm}^3 \\times 0.8\\text{ g/cm}^3 = 40\\text{ g}$."
    },
    {
        "q": "Which unit is a derived SI unit?",
        "options": ["Meter", "Second", "Newton", "Kilogram"],
        "ans": "C",
        "exp": "Newton ($\\text{kg}\\cdot\\text{m/s}^2$) is a derived unit of force. Meter, second, and kilogram are base units."
    },
    {
        "q": "What is the acceleration due to gravity on the Moon compared to Earth?",
        "options": ["Identical", "Approx. $1/6\\text{th}$ of Earth", "Approx. 6 times Earth", "Zero"],
        "ans": "B",
        "exp": "Surface gravity on the Moon is about $1.63\\text{ m/s}^2$, which is approximately $1/6\\text{th}$ of Earth's $9.8\\text{ m/s}^2$."
    },
    {
        "q": "Which instrument is used to determine the specific gravity (relative density) of liquids directly?",
        "options": ["Barometer", "Hydrometer", "Manometer", "Anemometer"],
        "ans": "B",
        "exp": "A hydrometer floats in liquids to directly measure relative density based on its depth of immersion."
    },
    {
        "q": "If 10 vernier divisions equal 9 main scale divisions (1 MSD = 1 mm), what is the vernier constant?",
        "options": ["0.1 mm", "0.01 mm", "1.0 mm", "0.9 mm"],
        "ans": "A",
        "exp": "$\\text{VC} = 1\\text{ MSD} - 1\\text{ VSD} = 1\\text{ mm} - 0.9\\text{ mm} = 0.1\\text{ mm}$."
    }
]

CHAPTER_02_QUESTIONS = [
    {
        "q": "Who first discovered and named 'cells' while examining thin cork slices in 1665?",
        "options": ["Robert Brown", "Robert Hooke", "Anton van Leeuwenhoek", "Rudolf Virchow"],
        "ans": "B",
        "exp": "Robert Hooke observed dead honey-comb compartments in cork using an early microscope and coined the term 'cell'."
    },
    {
        "q": "Who first observed living, motile free cells (bacteria, protozoa) in pond water in 1674?",
        "options": ["Robert Hooke", "Anton van Leeuwenhoek", "Schleiden", "Schwann"],
        "ans": "B",
        "exp": "Anton van Leeuwenhoek improved microscopic lenses and discovered living microorganisms."
    },
    {
        "q": "Who formulated the aphorism 'Omnis cellula-e cellula' (all cells arise from pre-existing cells)?",
        "options": ["Rudolf Virchow", "Robert Brown", "Camillo Golgi", "Purkinje"],
        "ans": "A",
        "exp": "Rudolf Virchow expanded the cell theory in 1855 by stating that new cells arise from pre-existing cells by division."
    },
    {
        "q": "Which chemical compound makes up the bulk of the rigid plant cell wall?",
        "options": ["Chitin", "Cellulose", "Peptidoglycan", "Glycogen"],
        "ans": "B",
        "exp": "The primary structural component of plant cell walls is cellulose, a fibrous carbohydrate polymer."
    },
    {
        "q": "Which cell organelle is known as the 'powerhouse of the cell'?",
        "options": ["Ribosome", "Mitochondrion", "Golgi apparatus", "Lysosome"],
        "ans": "B",
        "exp": "Mitochondria generate cellular energy in the form of ATP through aerobic cellular respiration."
    },
    {
        "q": "Which cellular organelle is responsible for synthesizing structural and enzymatic proteins?",
        "options": ["Lysosome", "Ribosome", "Vacuole", "Centrosome"],
        "ans": "B",
        "exp": "Ribosomes are the macromolecular protein-synthesizing factories found in all living cells."
    },
    {
        "q": "Lysosomes are colloquially designated as:",
        "options": ["Kitchen of the cell", "Suicide bags of the cell", "Brain of the cell", "Powerhouse of the cell"],
        "ans": "B",
        "exp": "Lysosomes contain hydrolytic digestive enzymes that digest the cell itself if damaged, earning the name 'suicide bags'."
    },
    {
        "q": "The primary site of photosynthesis in green plant cells is the:",
        "options": ["Leucoplast", "Chromoplast", "Chloroplast", "Amyloplast"],
        "ans": "C",
        "exp": "Chloroplasts contain chlorophyll pigments and thylakoid membranes that capture light to perform photosynthesis."
    },
    {
        "q": "Which organelle plays a primary role in lipid synthesis and drug detoxification in liver cells?",
        "options": ["Rough ER", "Smooth Endoplasmic Reticulum (SER)", "Golgi apparatus", "Nucleolus"],
        "ans": "B",
        "exp": "Smooth ER lacks ribosomes and specializes in lipid/steroid biosynthesis and hepatic detoxification."
    },
    {
        "q": "Which organelle processes, packages, and sorts macromolecules received from the ER?",
        "options": ["Golgi apparatus", "Peroxisome", "Vacuole", "Centriole"],
        "ans": "A",
        "exp": "Camillo Golgi discovered the Golgi apparatus, which packages and modifies proteins for secretion."
    },
    {
        "q": "What happens to a plant cell placed in a hypertonic solution?",
        "options": ["It swells and bursts", "It undergoes plasmolysis (shrinks)", "It doubles in size", "It divides by mitosis"],
        "ans": "B",
        "exp": "Water exits via exosmosis, causing the protoplast to shrink away from the cell wall (plasmolysis)."
    },
    {
        "q": "Which transport process describes the spontaneous movement of water across a semi-permeable membrane?",
        "options": ["Active transport", "Diffusion", "Osmosis", "Endocytosis"],
        "ans": "C",
        "exp": "Osmosis is the net movement of water molecules across a selectively permeable membrane along a concentration gradient."
    },
    {
        "q": "Prokaryotic cells lack which of the following cellular features?",
        "options": ["Plasma membrane", "Ribosomes", "A membrane-bound nucleus", "Cytoplasm"],
        "ans": "C",
        "exp": "Prokaryotes lack a nuclear membrane; their genetic material lies naked in a region called the nucleoid."
    },
    {
        "q": "Which cellular organelle possesses its own DNA and ribosomes, enabling semi-autonomous replication?",
        "options": ["Mitochondria and Chloroplasts", "Golgi apparatus", "Lysosomes", "Vacuoles"],
        "ans": "A",
        "exp": "Both mitochondria and chloroplasts contain circular DNA and 70S ribosomes, reflecting endosymbiotic prokaryotic origin."
    },
    {
        "q": "Which structure provides mechanical turgidity to mature plant cells, occupying up to 90% of cell volume?",
        "options": ["Central Vacuole", "Centrosome", "Nucleolus", "Lysosome"],
        "ans": "A",
        "exp": "The large central sap vacuole maintains hydrostatic turgor pressure against the plant cell wall."
    },
    {
        "q": "Amoeba engulfs its food particles from the surrounding water by:",
        "options": ["Exocytosis", "Endocytosis (Phagocytosis)", "Plasmolysis", "Active secretion"],
        "ans": "B",
        "exp": "Plasma membrane flexibility enables Amoeba to form pseudopodia and engulf food via endocytosis."
    },
    {
        "q": "What is chromatin chemically composed of?",
        "options": ["RNA and lipids", "DNA and histone proteins", "Carbohydrates and minerals", "Phospholipids only"],
        "ans": "B",
        "exp": "Chromatin consists of double-stranded DNA coiled around basic histone protein octamers."
    },
    {
        "q": "The membrane that encloses the plant central vacuole is called the:",
        "options": ["Plasmalemma", "Tonoplast", "Periderm", "Pellicle"],
        "ans": "B",
        "exp": "The selectively permeable membrane surrounding the large central plant vacuole is the tonoplast."
    },
    {
        "q": "Which cellular structure is present in animal cells but absent in higher plant cells?",
        "options": ["Cell wall", "Chloroplast", "Centrosome / Centriole", "Mitochondria"],
        "ans": "C",
        "exp": "Centrosomes and centrioles are animal cell organelles that organize spindle fibers during mitotic division."
    },
    {
        "q": "Which stain is commonly used to stain plant cells like onion peel?",
        "options": ["Safranin", "Sudan III", "Benedict's reagent", "Silver nitrate"],
        "ans": "A",
        "exp": "Safranin stains plant cell walls and nuclei bright pink/red for clear microscopic examination."
    },
    {
        "q": "What is the full biological form of ATP?",
        "options": [
            "Adenosine Triphosphate",
            "Adenine Tetra-Phosphate",
            "Ammonium Tri-Phosphate",
            "Adenosine Tartrate Phosphate"
        ],
        "ans": "A",
        "exp": "ATP stands for Adenosine Triphosphate, the universal chemical energy storage molecule of cells."
    },
    {
        "q": "What is the typical diameter of a human red blood cell (RBC)?",
        "options": ["7–8 μm", "70 μm", "1 mm", "0.1 μm"],
        "ans": "A",
        "exp": "Human erythrocytes have an average diameter of approximately 7.2 to 7.8 micrometers (μm)."
    },
    {
        "q": "Which organelle is responsible for synthesizing ribosomes inside the eukaryotic nucleus?",
        "options": ["Nucleolus", "Nuclear pore", "Chromatin", "Nuclear envelope"],
        "ans": "A",
        "exp": "The nucleolus is the dense subnuclear site of ribosomal RNA (rRNA) transcription and ribosome subunit assembly."
    },
    {
        "q": "Which plastid is responsible for storing starch grains in potato tubers?",
        "options": ["Chloroplast", "Chromoplast", "Amyloplast (Leucoplast)", "Carotenoid"],
        "ans": "C",
        "exp": "Amyloplasts are specialized non-pigmented leucoplasts that synthesize and store starch in storage organs."
    },
    {
        "q": "What is the basic molecular composition of the fluid mosaic cell membrane?",
        "options": [
            "Cellulose fibers only",
            "Phospholipid bilayer with embedded proteins",
            "Solid wax layer",
            "Pure glycogen mesh"
        ],
        "ans": "B",
        "exp": "Singer and Nicolson proposed the Fluid Mosaic Model: a phospholipid bilayer with embedded floating proteins."
    }
]

CHAPTER_03_QUESTIONS = [
    {
        "q": "Which meristematic tissue is located at the growing root tips and shoot apex?",
        "options": ["Lateral meristem", "Apical meristem", "Intercalary meristem", "Vascular cambium"],
        "ans": "B",
        "exp": "Shoot and root apical meristems are located at terminal tips and drive primary longitudinal growth."
    },
    {
        "q": "The increase in girth (diameter) of a tree trunk is due to:",
        "options": ["Apical meristem", "Lateral meristem (Cambium)", "Intercalary meristem", "Parenchyma"],
        "ans": "B",
        "exp": "Lateral meristems (vascular and cork cambium) produce radial secondary growth, increasing trunk girth."
    },
    {
        "q": "Which plant tissue contains living cells with localized wall thickenings of pectin at cell corners?",
        "options": ["Sclerenchyma", "Collenchyma", "Parenchyma", "Xylem vessels"],
        "ans": "B",
        "exp": "Collenchyma cells have corner pectin-cellulose thickenings that provide flexibility and support to growing organs."
    },
    {
        "q": "Coconut husk is made of which dead mechanical tissue?",
        "options": ["Collenchyma", "Aerenchyma", "Sclerenchyma fibres", "Xylem parenchyma"],
        "ans": "C",
        "exp": "Coir from coconut husk is composed of dead sclerenchyma fibers with heavily lignified, cemented walls."
    },
    {
        "q": "Which simple permanent tissue forms the bulk of soft plant organs and stores food?",
        "options": ["Parenchyma", "Sclerenchyma", "Collenchyma", "Phloem fibers"],
        "ans": "A",
        "exp": "Parenchyma is the most abundant unspecialized ground tissue, performing storage, photosynthesis, and secretion."
    },
    {
        "q": "Aerenchyma tissue provides buoyancy to aquatic plants because it contains:",
        "options": ["Large air cavities", "Dense oil droplets", "Lignin deposits", "Calcium oxalate crystals"],
        "ans": "A",
        "exp": "Aerenchyma is modified parenchyma with large interconnected intercellular air spaces that help water plants float."
    },
    {
        "q": "Which component of phloem tissue conducts organic nutrients (sucrose) through perforated end walls?",
        "options": ["Sieve tubes", "Phloem fibers", "Tracheids", "Xylem vessels"],
        "ans": "A",
        "exp": "Sieve tube elements connect longitudinally with perforated sieve plates to translocate photosynthesized sugars."
    },
    {
        "q": "Which xylem component is the only living element in mature xylem?",
        "options": ["Tracheids", "Xylem vessels", "Xylem fibres", "Xylem parenchyma"],
        "ans": "D",
        "exp": "Tracheids, vessels, and fibers are dead at maturity; only xylem parenchyma remains living for lateral storage."
    },
    {
        "q": "Which epithelial tissue lines the alveoli of the lungs and capillary blood vessels for rapid diffusion?",
        "options": ["Simple Squamous Epithelium", "Ciliated Columnar", "Stratified Cuboidal", "Glandular Epithelium"],
        "ans": "A",
        "exp": "Simple squamous epithelium forms an ultra-thin, smooth sheet of pavement-like cells optimizing gaseous diffusion."
    },
    {
        "q": "Which tissue lines the respiratory windpipe (trachea) to sweep trapped dust and mucus outward?",
        "options": ["Ciliated Columnar Epithelium", "Squamous Epithelium", "Hyaline Cartilage", "Areolar Tissue"],
        "ans": "A",
        "exp": "Ciliated columnar cells bear beating hair-like cilia that sweep mucus and trapped particulates up the respiratory tract."
    },
    {
        "q": "Tendons are tough fibrous connective tissues that connect:",
        "options": ["Bone to bone", "Skeletal muscle to bone", "Nerve to muscle", "Cartilage to muscle"],
        "ans": "B",
        "exp": "Tendons connect muscle to bone; ligaments connect bone to bone across movable joints."
    },
    {
        "q": "Ligaments join:",
        "options": ["Muscle to bone", "Bone to bone", "Skin to muscle", "Cartilage to tendon"],
        "ans": "B",
        "exp": "Ligaments are elastic fibrous cords containing elastin that stabilize joints by binding bones together."
    },
    {
        "q": "Which tissue stores fat beneath the skin and around internal organs, serving as a thermal insulator?",
        "options": ["Adipose tissue", "Areolar tissue", "Dense regular tissue", "Squamous tissue"],
        "ans": "A",
        "exp": "Adipose tissue contains adipocytes packed with fat globules, providing energy storage and thermal insulation."
    },
    {
        "q": "The matrix of bone tissue is made exceptionally hard and rigid by deposits of:",
        "options": ["Calcium and Phosphorus salts", "Sodium and Potassium chlorides", "Iron and Magnesium", "Cellulose and lignin"],
        "ans": "A",
        "exp": "Bone matrix consists of collagen fibers mineralized with calcium phosphate (hydroxyapatite) crystals."
    },
    {
        "q": "Cartilage is present at all the following anatomical sites EXCEPT:",
        "options": ["Ear pinna", "Tip of the nose", "Tracheal rings", "Kidney tubules"],
        "ans": "D",
        "exp": "Kidney tubules are lined by cuboidal epithelium; ear pinna, nose tip, larynx, and trachea contain cartilage."
    },
    {
        "q": "Which type of muscle tissue exhibits branched fibers and intercalated discs?",
        "options": ["Skeletal muscle", "Smooth muscle", "Cardiac muscle", "Visceral muscle"],
        "ans": "C",
        "exp": "Cardiac muscle fibers are involuntary, cylindrical, branched, and joined by electrical intercalated discs."
    },
    {
        "q": "Smooth (unstriated) muscle tissue is found in:",
        "options": ["Leg biceps", "Wall of the stomach and blood vessels", "Tongue", "Forearm triceps"],
        "ans": "B",
        "exp": "Involuntary unstriated spindle-shaped smooth muscle lines internal visceral organs such as the gut and blood vessels."
    },
    {
        "q": "The functional transmitting cell of nervous tissue is the:",
        "options": ["Nephron", "Neuron (Nerve cell)", "Neuroglia", "Sarcomere"],
        "ans": "B",
        "exp": "Neurons are electrically excitable cells specialized to receive, conduct, and transmit nerve impulses."
    },
    {
        "q": "The long, slender conducting cytoplasmic projection extending from the neuron's cell body is the:",
        "options": ["Dendrite", "Axon", "Synapse", "Myelin"],
        "ans": "B",
        "exp": "The axon conducts electrical action potentials away from the neuronal soma (cell body) toward synaptic terminals."
    },
    {
        "q": "The junctional gap between two adjacent communicating neurons is called a:",
        "options": ["Centrosome", "Synapse", "Intercalated disc", "Node of Ranvier"],
        "ans": "B",
        "exp": "The synapse is the microscopic gap across which neurotransmitters diffuse to propagate electrical signals between neurons."
    },
    {
        "q": "Which cellular component of mammalian blood lacks a cell nucleus at maturity?",
        "options": ["White Blood Cell (Leukocyte)", "Red Blood Cell (Erythrocyte)", "Macrophage", "Osteocyte"],
        "ans": "B",
        "exp": "Mature mammalian RBCs are enucleated biconcave discs optimized to carry oxygen bound to hemoglobin."
    },
    {
        "q": "Which formed blood element is essential for initiating blood clot formation at a wound site?",
        "options": ["Platelets (Thrombocytes)", "Erythrocytes", "Eosinophils", "Lymphocytes"],
        "ans": "A",
        "exp": "Platelets aggregate at vascular lesions and release thromboplastin to trigger the coagulation cascade."
    },
    {
        "q": "The waxy, waterproof chemical substance deposited on the cork cell walls of tree bark is:",
        "options": ["Cutin", "Suberin", "Pectin", "Chitin"],
        "ans": "B",
        "exp": "Suberin is a hydrophobic waxy biopolymer that makes mature dead cork cells impermeable to water and gases."
    },
    {
        "q": "Which tissue acts as a packing and binding filler tissue between skin and underlying muscles?",
        "options": ["Areolar connective tissue", "Dense regular tissue", "Stratified epithelium", "Hyaline cartilage"],
        "ans": "A",
        "exp": "Areolar tissue is loose connective tissue that fills spaces inside organs, supports internal organs, and helps tissue repair."
    },
    {
        "q": "Desert plants (xerophytes) minimize transpiration primarily by having a thick outer coating of:",
        "options": ["Lignin", "Cutin (Cuticle)", "Suberin", "Cellulose"],
        "ans": "B",
        "exp": "A thick waxy cuticle layer of cutin coats the epidermal surface of desert plants to drastically curtail water loss."
    }
]

CHAPTER_04_QUESTIONS = [
    {
        "q": "The shortest straight-line distance between the initial and final positions of a moving body is its:",
        "options": ["Distance", "Displacement", "Speed", "Trajectory length"],
        "ans": "B",
        "exp": "Displacement is the vector distance representing the straight-line directed path from start to finish."
    },
    {
        "q": "What is the SI unit of acceleration?",
        "options": ["$\\text{m/s}$", "$\\text{m/s}^2$", "$\\text{km/h}$", "$\\text{m}\\cdot\\text{s}$"],
        "ans": "B",
        "exp": "Acceleration is rate of change of velocity: $[\\text{m/s}] / [\\text{s}] = \\text{m/s}^2$."
    },
    {
        "q": "What does the slope of a distance-time ($s$-$t$) graph represent?",
        "options": ["Acceleration", "Speed", "Displacement", "Force"],
        "ans": "B",
        "exp": "Slope $= \\frac{\\Delta s}{\\Delta t}$, which is the definition of speed."
    },
    {
        "q": "What does the slope of a velocity-time ($v$-$t$) graph represent?",
        "options": ["Distance", "Acceleration", "Displacement", "Momentum"],
        "ans": "B",
        "exp": "Slope of $v$-$t$ graph $= \\frac{\\Delta v}{\\Delta t}$, which gives the acceleration."
    },
    {
        "q": "What does the area enclosed beneath a velocity-time graph represent?",
        "options": ["Acceleration", "Total displacement", "Average speed", "Instantaneous power"],
        "ans": "B",
        "exp": "Area $= v \\times t$, which dimensional analysis and integration show equals displacement."
    },
    {
        "q": "A car accelerates uniformly from rest ($0\\text{ m/s}$) to $20\\text{ m/s}$ in $5\\text{ s}$. Its acceleration is:",
        "options": ["$2\\text{ m/s}^2$", "$4\\text{ m/s}^2$", "$5\\text{ m/s}^2$", "$100\\text{ m/s}^2$"],
        "ans": "B",
        "exp": "$a = \\frac{v - u}{t} = \\frac{20 - 0}{5} = 4\\text{ m/s}^2$."
    },
    {
        "q": "Convert a speed of $72\\text{ km/h}$ into meters per second (m/s):",
        "options": ["$15\\text{ m/s}$", "$20\\text{ m/s}$", "$25\\text{ m/s}$", "$36\\text{ m/s}$"],
        "ans": "B",
        "exp": "$72 \\times \\frac{5}{18} = 4 \\times 5 = 20\\text{ m/s}$."
    },
    {
        "q": "An athlete completes one circular round of track of radius $R$ in $40\\text{ s}$. His displacement after $40\\text{ s}$ is:",
        "options": ["$2\\pi R$", "$2R$", "Zero", "$\\pi R$"],
        "ans": "C",
        "exp": "After one full round, the athlete returns to the exact starting position; net displacement is zero."
    },
    {
        "q": "An odometer installed in a motorcycle measures:",
        "options": ["Instantaneous speed", "Average velocity", "Cumulative distance travelled", "Engine acceleration"],
        "ans": "C",
        "exp": "An odometer measures distance covered in km; a speedometer measures instantaneous speed."
    },
    {
        "q": "Which kinematic equation correctly relates final velocity, initial velocity, acceleration, and distance?",
        "options": ["$v = u + at$", "$s = ut + \\frac{1}{2}at^2$", "$v^2 - u^2 = 2as$", "$v^2 + u^2 = 2as$"],
        "ans": "C",
        "exp": "The third kinematic equation of uniformly accelerated motion is $v^2 - u^2 = 2as$ (or $v^2 = u^2 + 2as$)."
    },
    {
        "q": "A ball is thrown vertically upward with speed $19.6\\text{ m/s}$. How long does it take to reach maximum height ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["1.0 s", "2.0 s", "3.0 s", "4.0 s"],
        "ans": "B",
        "exp": "At the peak, $v = 0$. Using $v = u - gt \\Rightarrow 0 = 19.6 - 9.8 t \\Rightarrow t = 19.6 / 9.8 = 2.0\\text{ s}$."
    },
    {
        "q": "A horizontal distance-time graph line parallel to the time axis indicates that the object is:",
        "options": ["Moving with uniform speed", "At rest (stationary)", "Accelerating rapidly", "Moving backwards"],
        "ans": "B",
        "exp": "A zero slope (horizontal line) on an $s$-$t$ graph means position is not changing with time; the object is at rest."
    },
    {
        "q": "In uniform circular motion, the direction of linear velocity at any given point is:",
        "options": ["Radially inward towards the center", "Radially outward", "Tangential to the circular path", "Zero"],
        "ans": "C",
        "exp": "The instantaneous velocity vector is always directed tangentially to the circular trajectory."
    },
    {
        "q": "Negative acceleration is commonly known as:",
        "options": ["Retardation or Deceleration", "Terminal velocity", "Impulse", "Inertia"],
        "ans": "A",
        "exp": "When acceleration opposes the direction of velocity, speed decreases, termed retardation or deceleration."
    },
    {
        "q": "Can average velocity be zero while average speed is positive?",
        "options": [
            "Yes, if the body returns to its starting point",
            "No, average velocity is always equal to average speed",
            "No, velocity can never be zero",
            "Only in vacuum"
        ],
        "ans": "A",
        "exp": "If displacement is zero (round trip), $\\text{average velocity} = 0$, but total distance $> 0$ gives a positive average speed."
    },
    {
        "q": "What is the acceleration of an object moving with a constant velocity of $50\\text{ m/s}$?",
        "options": ["$50\\text{ m/s}^2$", "$0\\text{ m/s}^2$", "$9.8\\text{ m/s}^2$", "$25\\text{ m/s}^2$"],
        "ans": "B",
        "exp": "Velocity is not changing; $\\Delta v = 0 \\Rightarrow a = 0$."
    },
    {
        "q": "A body dropped freely from rest falls for $3\\text{ s}$. What distance does it fall ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["29.4 m", "44.1 m", "88.2 m", "14.7 m"],
        "ans": "B",
        "exp": "$s = \\frac{1}{2}gt^2 = 0.5 \\times 9.8 \\times (3)^2 = 4.9 \\times 9 = 44.1\\text{ m}$."
    },
    {
        "q": "Which of the following is a vector quantity?",
        "options": ["Distance", "Speed", "Velocity", "Time"],
        "ans": "C",
        "exp": "Velocity specifies both magnitude (speed) and direction of motion, making it a vector."
    },
    {
        "q": "The motion of a freely swinging pendulum bob is an example of:",
        "options": ["Uniform motion", "Non-uniform accelerated motion", "Circular motion with constant velocity", "Zero acceleration"],
        "ans": "B",
        "exp": "The bob speeds up toward the center and slows down toward the extremes, undergoing non-uniform periodic acceleration."
    },
    {
        "q": "What is the speed of an object that travels 100 meters in 4 seconds?",
        "options": ["$20\\text{ m/s}$", "$25\\text{ m/s}$", "$40\\text{ m/s}$", "$400\\text{ m/s}$"],
        "ans": "B",
        "exp": "$\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}} = \\frac{100\\text{ m}}{4\\text{ s}} = 25\\text{ m/s}$."
    },
    {
        "q": "If a car travels the first half of distance at speed $v_1$ and the second half at speed $v_2$, its average speed is:",
        "options": [
            "$\\frac{v_1 + v_2}{2}$",
            "$\\frac{2 v_1 v_2}{v_1 + v_2}$",
            "$\\sqrt{v_1 v_2}$",
            "$\\frac{v_1 v_2}{2}$"
        ],
        "ans": "B",
        "exp": "Average speed over equal distance segments is the harmonic mean: $v_{avg} = \\frac{2 v_1 v_2}{v_1 + v_2}$."
    },
    {
        "q": "What is the angle between velocity and centripetal acceleration in uniform circular motion?",
        "options": ["0°", "45°", "90°", "180°"],
        "ans": "C",
        "exp": "Velocity is tangential while centripetal acceleration is directed radially inward; they are mutually perpendicular (90°)."
    },
    {
        "q": "A train slows down from $30\\text{ m/s}$ to rest in $15\\text{ s}$. Its retardation is:",
        "options": ["$1\\text{ m/s}^2$", "$2\\text{ m/s}^2$", "$0.5\\text{ m/s}^2$", "$4.5\\text{ m/s}^2$"],
        "ans": "B",
        "exp": "$a = \\frac{0 - 30}{15} = -2\\text{ m/s}^2$. Retardation $= +2\\text{ m/s}^2$."
    },
    {
        "q": "If the velocity of a particle is given by $v = 4t$, its motion is:",
        "options": ["Uniform motion", "Motion with uniform acceleration", "Motion with non-uniform acceleration", "Stationary"],
        "ans": "B",
        "exp": "Acceleration is constant: $a = \\frac{dv}{dt} = 4\\text{ m/s}^2$, representing uniform acceleration."
    },
    {
        "q": "Which graph represents uniform motion?",
        "options": [
            "A distance-time graph that is a straight line sloping upward from the origin",
            "A distance-time graph that is curved like a parabola",
            "A velocity-time graph with a steep positive slope",
            "A distance-time graph that curves downward"
        ],
        "ans": "A",
        "exp": "A straight-line $s$-$t$ graph passing through the origin indicates constant slope, meaning uniform speed."
    }
]
