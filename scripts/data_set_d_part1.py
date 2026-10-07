"""
Data module for CBSE Class 9 Science - SET D (Assertion - Reasoning Special)
Part 1: Chapters 1 to 4 (100 Assertion-Reasoning Questions)
Strictly 100% CBSE English Medium.
"""

CHAPTER_01_QUESTIONS = [
    # SECTION A: Core Theoretical Principles & Definitions (Q1 - Q10)
    {
        "a": "The International System of Units (SI) is adopted universally across global scientific communities.",
        "r": "The SI system is built upon coherent, standardized base-10 decimal units that eliminate arbitrary regional conversion errors.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains why SI units are universally standard across scientific disciplines."
    },
    {
        "a": "A simple pendulum of mass 50 g and another of mass 100 g having identical length exhibit the exact same time period of oscillation at a given place.",
        "r": "The time period of a simple pendulum is strictly independent of the mass and material of the oscillating bob.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly explains the formula $T = 2\\pi \\sqrt{L/g}$, which contains no mass term."
    },
    {
        "a": "Relative density of a solid substance has no physical unit.",
        "r": "Relative density is defined as the ratio of the density of the substance to the density of water at 4°C, causing all units to cancel out.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains why a ratio of two identical physical quantities is dimensionless."
    },
    {
        "a": "A measurement of 5.00 cm is more precise than a measurement of 5.0 cm.",
        "r": "Precision is determined by the least count of the measuring instrument; 5.00 cm indicates measurement up to two decimal places.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains that higher decimal resolution reflects finer instrument least count."
    },
    {
        "a": "The period of oscillation of a simple pendulum increases when taken to the top of Mount Everest.",
        "r": "The acceleration due to gravity $g$ decreases with increasing altitude above the Earth's surface.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains the formula $T = 2\\pi \\sqrt{L/g}$; as $g$ decreases at high altitudes, $T$ increases."
    },
    {
        "a": "Parallax error occurs when an observer views the pointer or meniscus of a measuring instrument at an oblique angle.",
        "r": "To obtain an accurate reading, the observer's line of sight must always be positioned perpendicularly to the instrument scale.",
        "ans": "B",
        "exp": "Both statements are scientifically true, but Reason states the prevention procedure rather than explaining the optical cause of parallax displacement."
    },
    {
        "a": "The density of an iron nail is greater than the density of a massive wooden log.",
        "r": "Iron atoms possess greater atomic mass and are packed much more densely in a crystalline lattice than organic wood fibers.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the microscopic structural explanation for the higher macroscopic density of iron."
    },
    {
        "a": "A piece of cork floats on water, whereas an iron nail of the same volume sinks immediately.",
        "r": "Water exerts an upward buoyant force only on light objects like cork and exerts zero buoyant force on heavy objects like iron.",
        "ans": "C",
        "exp": "Assertion is true. Reason is false: Water exerts buoyant force on all submerged objects; the nail sinks because its weight exceeds the buoyant force."
    },
    {
        "a": "In scientific laboratory investigations, multiple trials of an experiment are recorded and averaged.",
        "r": "Averaging repeated measurements minimizes random observational errors and enhances experimental reliability.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains the statistical purpose of taking repeated readings."
    },
    {
        "a": "When measuring the volume of water in a graduated cylinder, the reading should be taken at the upper convex meniscus.",
        "r": "Water wets the glass surface, forming a concave meniscus due to strong adhesive forces between water and glass molecules.",
        "ans": "D",
        "exp": "Assertion is false (water readings must be taken at the lowest point of the concave meniscus). Reason is true (water forms a concave meniscus due to adhesive forces)."
    },

    # SECTION B: Experimental Observations & Phenomenological Inferences (Q11 - Q18)
    {
        "a": "A graph plotted between $T^2$ (square of time period) and $L$ (length) for a simple pendulum is a straight line passing through the origin.",
        "r": "The square of the time period of a simple pendulum is directly proportional to its effective length ($T^2 \\propto L$).",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains the linear relationship $T^2 = (4\\pi^2/g)L$ represented on the graph."
    },
    {
        "a": "A vernier caliper can measure internal diameter, external diameter, and depth of a hollow cylinder.",
        "r": "A vernier caliper is equipped with upper jaws, lower jaws, and a metallic depth probe strip.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly explains the mechanical construction enabling multi-dimensional measurements."
    },
    {
        "a": "If a pendulum clock is transported from the North Pole to the Equator, it runs slower and loses time.",
        "r": "The value of $g$ is slightly smaller at the Equator than at the Poles due to the Earth's equatorial bulge and rotational centrifugal effect.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why $T$ increases at the equator, causing the pendulum to oscillate fewer times per day (losing time)."
    },
    {
        "a": "Zero error in a screw gauge is a systematic error that can be mathematically corrected by addition or subtraction.",
        "r": "Systematic errors consistently skew measurements in a single direction and arise from faulty calibration or zero offset.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly defines systematic errors and justifies algebraic correction."
    },
    {
        "a": "A wire gauze with an asbestos or ceramic center is placed between a Bunsen burner flame and a glass beaker.",
        "r": "Direct exposure to concentrated flame causes localized uneven expansion of glass, leading to thermal fracture.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how the wire gauze conducts and disperses heat uniformly to prevent thermal shock."
    },
    {
        "a": "A body of mass 10 kg has a weight of 98 N on Earth and a weight of 0 N in deep interstellar space.",
        "r": "Mass is an invariant intrinsic property of matter, while weight is a gravitational force dependent on local acceleration due to gravity.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and clearly explains the fundamental distinction between mass and weight in different gravitational fields."
    },
    {
        "a": "Water can never be used to extinguish a burning oil or petrol fire in the laboratory.",
        "r": "Water reacts violently with petrol to produce toxic chlorine gas.",
        "ans": "C",
        "exp": "Assertion is true. Reason is false: Water does not react chemically to make chlorine gas; rather, petrol is lighter than water and floats on top, spreading the fire."
    },
    {
        "a": "A block of wood floats with 60% of its volume submerged in water. Its density is $0.6\\text{ g/cm}^3$.",
        "r": "According to the principle of floatation, a floating body displaces a volume of liquid whose weight equals the total weight of the body.",
        "ans": "A",
        "exp": "Assertion is true ($V_{sub}/V = \\rho_{body}/\\rho_{liquid} = 0.60$). Reason is true and correctly provides the governing law of floatation."
    },

    # SECTION C: Advanced Conceptual Nuances & Misconceptions (Q19 - Q25)
    {
        "a": "The amplitude of oscillation of a simple pendulum in a school lab must be kept small (under 10°).",
        "r": "The mathematical formula $T = 2\\pi \\sqrt{L/g}$ is strictly derived using the small-angle approximation $\\sin\\theta \\approx \\theta$.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the mathematical requirement for simple harmonic motion."
    },
    {
        "a": "While heating a test tube containing chemicals, its mouth should never be directed towards oneself or lab partners.",
        "r": "Boiling liquids in test tubes can superheat and violently eject hot reactive chemicals due to sudden vapor bubble formation (bumping).",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the physical hazard of sudden boiling/bumping in narrow glassware."
    },
    {
        "a": "If the length of a simple pendulum is increased by four times, its time period doubles.",
        "r": "The time period of a simple pendulum is inversely proportional to the square root of its length.",
        "ans": "C",
        "exp": "Assertion is true ($T \\propto \\sqrt{L}$; $\\sqrt{4} = 2$). Reason is false: $T$ is directly proportional to $\\sqrt{L}$, not inversely proportional."
    },
    {
        "a": "A hydrometer sinks deeper in kerosene than in pure water.",
        "r": "Kerosene has a lower density than water, requiring a larger volume of kerosene to be displaced to balance the hydrometer's weight.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains how hydrometers indicate lower liquid density by greater depth of submersion."
    },
    {
        "a": "The least count of an instrument can be decreased indefinitely without any practical physical limit.",
        "r": "Decreasing least count always increases the precision of any measurement.",
        "ans": "D",
        "exp": "Assertion is false (material imperfections, thermal expansion, and quantum/optical diffraction impose strict physical limits). Reason is true (smaller least count yields higher precision)."
    },
    {
        "a": "During an experiment to determine the boiling point of water, pumice stones are added to the boiling flask.",
        "r": "Pumice stones introduce nucleation sites, promoting steady, smooth boiling and preventing explosive superheating.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the functional mechanism of anti-bumping boiling granules."
    },
    {
        "a": "In a controlled scientific experiment, only one independent variable should be altered at a time while holding all other variables constant.",
        "r": "If multiple variables are changed simultaneously, it becomes scientifically impossible to determine which specific factor caused the observed effect.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the fundamental criterion of scientific fair testing."
    }
]

CHAPTER_02_QUESTIONS = [
    # SECTION A: Core Theoretical Principles & Definitions (Q1 - Q10)
    {
        "a": "The plasma membrane is referred to as a selectively permeable membrane.",
        "r": "It permits the entry and exit of certain specific substances while preventing the passage of other materials across the cell.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly defines the biological property of selective permeability."
    },
    {
        "a": "Plant cells can withstand much greater changes in the surrounding hypotonic medium than animal cells without bursting.",
        "r": "Plant cells possess a rigid, tensile cell wall made of cellulose that exerts counter wall pressure against incoming turgor pressure.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how the cellulosic cell wall prevents osmotic lysis in plant cells."
    },
    {
        "a": "Mitochondria are often designated as the 'powerhouses of the cell'.",
        "r": "Mitochondria synthesize adenosine triphosphate (ATP), the universal chemical energy currency required for cellular metabolic activities.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains the biochemical origin of the nickname 'powerhouse'."
    },
    {
        "a": "Lysosomes are commonly known as the 'suicide bags' of the cell.",
        "r": "When a cell suffers irreparable metabolic damage or dies, its lysosomes rupture, releasing powerful hydrolytic enzymes that digest the host cell.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and describes autolysis, which justifies the term 'suicide bags'."
    },
    {
        "a": "Ribosomes are found in both prokaryotic and eukaryotic cells.",
        "r": "Ribosomes are membrane-bound organelles containing hydrolytic digestive enzymes.",
        "ans": "C",
        "exp": "Assertion is true. Reason is false: Ribosomes are non-membrane-bound ribonucleoprotein complexes that synthesize proteins, not hydrolytic enzymes."
    },
    {
        "a": "Mitochondria and chloroplasts are considered semi-autonomous organelles.",
        "r": "They contain their own circular DNA and 70S ribosomes, enabling them to synthesize some of their own structural proteins and replicate independently.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly justifies why they are designated as semi-autonomous endosymbionts."
    },
    {
        "a": "Chromosomes are visible as distinct rod-shaped structures only when a cell is actively preparing to divide.",
        "r": "In a non-dividing cell, genetic material exists in the form of an uncoiled, entangled thread-like network called chromatin.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how chromatin condenses into distinct chromosomes during cell division."
    },
    {
        "a": "The inner mitochondrial membrane is extensively folded into finger-like projections called cristae.",
        "r": "Cristae substantially increase the total surface area available for ATP-generating respiratory enzyme complexes.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the biological advantage of folded cristae in cellular respiration."
    },
    {
        "a": "Prokaryotic cells lack a defined, membrane-bound nuclear region.",
        "r": "The undefined nuclear region containing naked nucleic acids in prokaryotes is designated as a nucleoid.",
        "ans": "B",
        "exp": "Both statements are factually true, but Reason names the structure rather than explaining the evolutionary/structural cause of why prokaryotes lack a nuclear envelope."
    },
    {
        "a": "Smooth Endoplasmic Reticulum (SER) plays a crucial role in detoxifying many poisons and drugs in liver cells of vertebrates.",
        "r": "SER contains enzyme complexes that chemically convert lipid-soluble toxins into water-soluble compounds for excretion.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the enzymatic mechanism of hepatic detoxification by SER."
    },

    # SECTION B: Experimental Observations & Phenomenological Inferences (Q11 - Q18)
    {
        "a": "When dry raisins are soaked in pure water, they swell up after several hours.",
        "r": "Water enters the raisin cells via endosmosis because the external pure water is hypotonic relative to the concentrated cell sap.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly identifies endosmosis driven by a hypotonic water concentration gradient."
    },
    {
        "a": "When swollen raisins are subsequently transferred into a concentrated salt solution, they shrink.",
        "r": "Water molecules move out of the raisin cells into the hypertonic external medium via exosmosis.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains exosmosis occurring across the semi-permeable membrane into a hypertonic solution."
    },
    {
        "a": "A peel of <i>Rhoeo</i> leaf mounted in strong sugar solution displays plasmolysis under a microscope.",
        "r": "Severe loss of water via exosmosis causes the plant protoplast to shrink and pull away from the rigid cellulose cell wall.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly describes the cytological mechanism of plasmolysis."
    },
    {
        "a": "Boiled <i>Rhoeo</i> leaf cells do not undergo plasmolysis when placed in a concentrated sugar solution.",
        "r": "Boiling kills the plant cells, destroying the semi-permeable properties of the cell membrane and denaturing transport proteins.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why dead cells cannot undergo selective osmosis."
    },
    {
        "a": "Red blood cells (RBCs) swell and burst (lyse) when placed in a hypotonic salt solution.",
        "r": "Animal cells lack a rigid cell wall to withstand increasing hydrostatic internal turgor pressure.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why RBCs burst while walled plant cells remain intact."
    },
    {
        "a": "Amoeba acquires its food from the external aquatic environment through the process of endocytosis.",
        "r": "The plasma membrane of Amoeba is flexible and dynamic, allowing it to engulf external food particles by forming pseudopodia.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how plasma membrane fluidity enables phagocytosis/endocytosis."
    },
    {
        "a": "The Golgi apparatus is directly involved in the synthesis of structural proteins from amino acids.",
        "r": "Golgi apparatus consists of membrane-bound parallel stacks of flattened cisternae.",
        "ans": "D",
        "exp": "Assertion is false: Ribosomes synthesize proteins, not Golgi (Golgi packages and modifies them). Reason is true (cisternae description is accurate)."
    },
    {
        "a": "Chloroplasts are known as the kitchen of plant cells.",
        "r": "Chloroplasts contain chlorophyll pigments and photosynthetic machinery that synthesize glucose using sunlight, water, and $CO_2$.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly explains why chloroplasts are termed the cell's 'kitchen'."
    },

    # SECTION C: Advanced Conceptual Nuances & Misconceptions (Q19 - Q25)
    {
        "a": "Endoplasmic Reticulum and Golgi apparatus operate in functional coordination within the eukaryotic endomembrane system.",
        "r": "Proteins and lipids synthesized in the ER are transported to the Golgi apparatus for chemical modification, packaging, and dispatch.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and details the integrated secretory pathway of the eukaryotic endomembrane system."
    },
    {
        "a": "Leucoplasts are primary sites for photosynthesis in plant stems.",
        "r": "Leucoplasts are specialized colorless plastids that store starch, oils, and protein granules in non-photosynthetic plant tissues.",
        "ans": "D",
        "exp": "Assertion is false: Chloroplasts perform photosynthesis, leucoplasts do not. Reason is true: Leucoplasts are storage plastids."
    },
    {
        "a": "Large central vacuoles occupy 50% to 90% of the volume of mature plant cells.",
        "r": "The central vacuole maintains turgidity and rigidity in plant cells and serves as a reservoir for cellular waste and nutrients.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the structural and physiological significance of the large central vacuole."
    },
    {
        "a": "Diffusion is an active transport process that requires continuous breakdown of cellular ATP molecules.",
        "r": "In diffusion, molecules move spontaneously from a region of higher concentration to a region of lower concentration along a gradient.",
        "ans": "D",
        "exp": "Assertion is false: Diffusion is passive transport and requires zero ATP. Reason is true: It follows a spontaneous concentration gradient."
    },
    {
        "a": "The cell is recognized as the structural and functional unit of all living organisms.",
        "r": "All basic metabolic processes of life (respiration, nutrition, excretion) can be independently performed by a single individual cell.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the biological justification for the cell theory postulate."
    },
    {
        "a": "Nuclear membrane contains microscopic pores called nuclear pores.",
        "r": "Nuclear pores facilitate regulated bidirectional exchange of RNA and proteins between the nucleoplasm and cytoplasm.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the physiological function of nuclear pore complexes."
    },
    {
        "a": "Viruses do not show characteristics of life until they enter a living host cell.",
        "r": "Viruses lack cellular machinery and membranes of their own and utilize the host cell's metabolic machinery to multiply.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why viruses are classified on the borderline of living and non-living."
    }
]

CHAPTER_03_QUESTIONS = [
    # SECTION A: Core Theoretical Principles & Definitions (Q1 - Q10)
    {
        "a": "Meristematic tissues in plants are characterized by continuously dividing, undifferentiated cells.",
        "r": "Meristematic cells possess dense cytoplasm, thin cellulose walls, prominent nuclei, and lack vacuoles.",
        "ans": "B",
        "exp": "Both statements are true, but Reason describes the cytological features rather than explaining why they continuously divide."
    },
    {
        "a": "Apical meristem is responsible for the increase in length of plant stems and roots.",
        "r": "Apical meristem is located at the growing tips of stems and roots and adds new primary cells longitudinally.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the primary growth function of the shoot and root apical meristems."
    },
    {
        "a": "The girth (thickness) of the stem or root of a woody dicot plant increases due to lateral meristem (cambium).",
        "r": "Lateral meristems undergo periclinal cell divisions, adding secondary xylem and phloem radially to the vascular cylinder.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the mechanism of secondary thickening."
    },
    {
        "a": "Sclerenchyma cells provide immense mechanical strength and rigidity to plant organs.",
        "r": "Sclerenchyma tissues are composed of dead cells with uniformly thick walls heavily impregnated with lignin.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how lignified, thick dead walls provide mechanical support (e.g. coconut husk)."
    },
    {
        "a": "Collenchyma provides both mechanical support and flexibility to young dicot stems and leaf petioles.",
        "r": "Collenchyma cells have localized wall thickenings of cellulose, hemicellulose, and pectin at their cell corners.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the structural basis of bending without breaking."
    },
    {
        "a": "Xylem is classified as a complex permanent tissue in vascular plants.",
        "r": "Xylem consists of multiple distinct types of cells (tracheids, vessels, xylem parenchyma, and xylem fibres) working together as a functional unit.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and defines why it is classified as a 'complex' tissue rather than simple tissue."
    },
    {
        "a": "Blood is classified as a connective tissue.",
        "r": "Blood has a fluid matrix called plasma in which RBCs, WBCs, and platelets are suspended, connecting organ systems via transport.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why blood fulfills the histological definition of connective tissue."
    },
    {
        "a": "Cardiac muscle tissue can contract rhythmically throughout a person's life without ever experiencing muscular fatigue.",
        "r": "Cardiac muscle fibers are involuntary, cylindrical, branched, uninucleate, and richly supplied with mitochondria and capillaries.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how continuous energy supply and branched syncytial structure prevent fatigue."
    },
    {
        "a": "Skeletal muscles are also termed voluntary striated muscles.",
        "r": "Their contractions are under conscious voluntary nervous control and display alternating dark and light bands under a light microscope.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains both descriptive terms: 'voluntary' and 'striated'."
    },
    {
        "a": "Tendons connect bone to bone across a movable joint.",
        "r": "Tendons are tough, fibrous connective tissues with high tensile strength and limited elasticity.",
        "ans": "D",
        "exp": "Assertion is false: Ligaments connect bone to bone; tendons connect muscle to bone. Reason is true (tendons are tough fibrous cords with limited elasticity)."
    },

    # SECTION B: Experimental Observations & Phenomenological Inferences (Q11 - Q18)
    {
        "a": "Aquatic plants like <i>Hydrilla</i> and water hyacinth float effortlessly on the surface of water.",
        "r": "Parenchyma in aquatic plants modifies into aerenchyma containing large interconnected air cavities that provide buoyancy.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how aerenchyma air pockets reduce density and impart buoyancy."
    },
    {
        "a": "The husk of a dry coconut is extremely tough, stiff, and fibrous.",
        "r": "Coconut husk is made of dense sclerenchymatous fibres with heavily lignified, cemented cell walls.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the structural tissue responsible for the fibrous rigidity of coconut husk."
    },
    {
        "a": "Stomata in the leaf epidermis open and close during gas exchange and transpiration.",
        "r": "Each stomatal pore is bounded by two kidney-shaped guard cells whose turgor changes cause stomatal opening and closing.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the biomechanical action of guard cells regulating stomatal aperture."
    },
    {
        "a": "Desert plants (xerophytes) have a thick waxy cuticle layer of cutin covering their outer epidermis.",
        "r": "The hydrophobic waxy cutin layer drastically minimizes excessive water loss through transpiration in arid environments.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the adaptive physiological function of cutin."
    },
    {
        "a": "A fractured bone can repair itself over time, whereas severe cartilage wear at joint surfaces heals very poorly.",
        "r": "Bone is richly vascularized with living osteocytes and blood capillaries in Haversian canals, whereas cartilage is largely avascular.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why bone has high regenerative capacity while avascular cartilage heals slowly."
    },
    {
        "a": "Ciliated columnar epithelium lines the human respiratory tract and fallopian tubes.",
        "r": "The rhythmic, coordinated beating of cilia moves mucus and trapped foreign particles outwards along the tract surface.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and directly explains the directional transport function of ciliated epithelial cells."
    },
    {
        "a": "Mature sieve tube elements in phloem can conduct organic nutrients even though they lack a cell nucleus.",
        "r": "Each sieve tube element is intimately connected to an adjacent nucleated companion cell that regulates its metabolic activities.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the vital symbiotic dependence of enucleated sieve tubes on companion cells."
    },
    {
        "a": "Cork acts as an impervious protective outer covering on mature tree trunks.",
        "r": "The cell walls of mature dead cork tissue contain suberin, a chemical that makes them completely impermeable to water and gases.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how suberin deposition creates a protective, waterproof barrier."
    },

    # SECTION C: Advanced Conceptual Nuances & Misconceptions (Q19 - Q25)
    {
        "a": "Smooth (unstriated) muscles are present in the walls of the stomach, intestine, and blood vessels.",
        "r": "The contractions of visceral internal organs are involuntary and do not show cross-striations under a microscope.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why these visceral structures contain unstriated, involuntary smooth muscle fibers."
    },
    {
        "a": "Ligaments are strong, flexible connective tissues that hold bones together at joints.",
        "r": "Ligaments contain a high proportion of elastin fibres, imparting considerable elasticity while preventing joint dislocation.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and describes how elastin provides flexibility and joint stabilization."
    },
    {
        "a": "Xylem parenchyma is the only living component in the xylem tissue of angiosperms.",
        "r": "Tracheids, vessels, and xylem fibres are all dead, lignified cells at functional maturity.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and confirms that all other three xylem elements are dead at maturity."
    },
    {
        "a": "Nerve impulses travel rapidly over long distances across the human body.",
        "r": "Neurons possess a long transmitting cytoplasmic extension called the axon, often covered with an insulating myelin sheath.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains how axonal architecture enables rapid electrical conduction."
    },
    {
        "a": "Adipose tissue acts as an efficient thermal insulator beneath the skin.",
        "r": "Adipocytes store fat globules, and subcutaneous fat is a poor conductor of heat, preventing heat loss from the core body.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the physiological thermal insulation mechanism of adipose tissue."
    },
    {
        "a": "Intercalary meristem present at the base of leaves or internodes allows grasses to regenerate quickly after grazing by herbivores.",
        "r": "Intercalary meristem cells divide actively, regenerating lost shoot tissue from below the clipped tip.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the evolutionary advantage of intercalary meristem in grass survival."
    },
    {
        "a": "Epithelial tissue forms a continuous protective sheet with no intercellular spaces or blood vessels.",
        "r": "Epithelial cells rest on an extracellular basement membrane that separates them from underlying connective tissue.",
        "ans": "B",
        "exp": "Both statements are true facts of epithelial histology, but Reason describes the basement membrane attachment rather than explaining why cells are packed tightly without intercellular gaps."
    }
]

CHAPTER_04_QUESTIONS = [
    # SECTION A: Core Theoretical Principles & Definitions (Q1 - Q10)
    {
        "a": "The displacement of an object can be zero even when the total distance travelled by it is non-zero.",
        "r": "Displacement is a vector quantity representing the shortest straight-line path between initial and final positions; returning to the start yields zero displacement.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly explains the vector definition of displacement."
    },
    {
        "a": "The magnitude of displacement can never exceed the total distance covered by a moving body.",
        "r": "Distance is the actual path length, and the straight line connecting two endpoints is always the shortest possible distance between them.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the geometrical basis: $|\\text{displacement}| \\le \\text{distance}$."
    },
    {
        "a": "An object moving with uniform speed can still possess acceleration.",
        "r": "Velocity is a vector quantity having both magnitude and direction; continuously changing the direction of motion causes acceleration even if speed is constant.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains uniform circular motion where speed is constant but direction continuously turns."
    },
    {
        "a": "The slope of a distance-time graph represents the speed of the moving object.",
        "r": "Slope is calculated as $\\frac{\\Delta s}{\\Delta t}$, which is the rate of change of distance with respect to time.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the mathematical definition of slope matching speed."
    },
    {
        "a": "The area enclosed beneath a velocity-time graph and the time axis gives the displacement of the object.",
        "r": "Displacement equals velocity multiplied by time ($s = v \\times t$); the product of the dimensions of the axes ($[\\text{m/s}] \\times [\\text{s}] = [\\text{m}]$) represents area.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the dimensional and calculus justification for area under $v$-$t$ graph."
    },
    {
        "a": "A car moving on a crowded city street undergoes non-uniform motion.",
        "r": "The car covers unequal distances in equal intervals of time due to traffic signals, pedestrian crossings, and turns.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and defines non-uniform motion in real-world scenarios."
    },
    {
        "a": "A body can have zero velocity and non-zero acceleration simultaneously.",
        "r": "At the highest point of its vertical trajectory, an object thrown vertically upward stops momentarily ($v=0$) while gravity $g = 9.8\\text{ m/s}^2$ acts downward.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the classic physics example of projectile motion at maximum height."
    },
    {
        "a": "Negative acceleration is commonly referred to as retardation or deceleration.",
        "r": "Retardation occurs when the direction of the acceleration vector is opposite to the direction of the velocity vector, causing speed to decrease.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and defines the vector relationship responsible for decelerating a moving object."
    },
    {
        "a": "The motion of artificial satellites revolving around the Earth in circular orbits is an accelerated motion.",
        "r": "Satellites continuously change their direction of velocity towards the Earth due to centripetal gravitational acceleration.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains circular orbital motion as continuous centripetal acceleration."
    },
    {
        "a": "Average speed can be zero for a moving body.",
        "r": "Average speed is defined as total distance travelled divided by total time taken.",
        "ans": "D",
        "exp": "Assertion is false: Since distance for a moving body is always positive ($>0$), average speed cannot be zero (only average velocity can be zero). Reason is true."
    },

    # SECTION B: Experimental Observations & Phenomenological Inferences (Q11 - Q18)
    {
        "a": "If the distance-time graph of a body is a straight line parallel to the time axis, the body is at rest.",
        "r": "The position of the body does not change with the passage of time, meaning its velocity (slope) is zero.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why a horizontal slope indicates zero speed (stationary state)."
    },
    {
        "a": "An athlete running once around a circular track of radius $r$ completes the lap in time $t$. His average velocity is zero.",
        "r": "The initial and final positions of the athlete coincide after one full lap, making his net displacement vector zero.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains why $\\text{Average Velocity} = \\frac{\\text{Net Displacement}}{\\text{Total Time}} = \\frac{0}{t} = 0$."
    },
    {
        "a": "The equations of motion ($v = u + at$, $s = ut + \\frac{1}{2}at^2$, $v^2 = u^2 + 2as$) are valid only for motion with uniform acceleration.",
        "r": "These three kinematic equations are derived on the strict mathematical condition that acceleration $a$ remains constant throughout.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and highlights the vital prerequisite condition for using kinematic equations."
    },
    {
        "a": "The velocity-time graph of a freely falling body dropped from rest is a straight line passing through the origin with a positive slope.",
        "r": "A freely falling body experiences constant downward gravitational acceleration ($g = 9.8\\text{ m/s}^2$).",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the linear increase in velocity $v = gt$ from rest."
    },
    {
        "a": "An odometer installed in an automobile measures its instantaneous speed.",
        "r": "A speedometer measures instantaneous speed in km/h, whereas an odometer records total cumulative distance travelled.",
        "ans": "D",
        "exp": "Assertion is false: The odometer records distance, not instantaneous speed (which is read by the speedometer). Reason is true."
    },
    {
        "a": "In uniform circular motion, the direction of linear velocity at any instant is along the tangent to the circular path.",
        "r": "If a stone tied to a string being whirled in a circle breaks loose, it flies off tangentially along a straight line.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides experimental proof of tangential instantaneous velocity."
    },
    {
        "a": "A train moving at 90 km/h is moving faster than a car moving at 25 m/s.",
        "r": "To convert km/h to m/s, multiply by $5/18$; $90 \\times (5/18) = 25\\text{ m/s}$.",
        "ans": "D",
        "exp": "Assertion is false: Both vehicles are moving at the exact same speed (90 km/h = 25 m/s). Reason is true."
    },
    {
        "a": "The slope of a velocity-time graph represents the acceleration of the moving body.",
        "r": "Slope is given by $\\frac{\\Delta v}{\\Delta t}$, which is the rate of change of velocity per unit time.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and provides the mathematical definition of acceleration."
    },

    # SECTION C: Advanced Conceptual Nuances & Misconceptions (Q19 - Q25)
    {
        "a": "A particle travelling with constant acceleration can never reverse its direction of motion.",
        "r": "A constant force always acts in a fixed spatial direction.",
        "ans": "D",
        "exp": "Assertion is false: An object thrown upwards has constant downward acceleration $g$ and reverses direction at the peak. Reason is true (constant acceleration implies constant unidirectional force)."
    },
    {
        "a": "During uniform circular motion of radius $R$ and period $T$, the magnitude of acceleration is $a = \\frac{v^2}{R} = \\frac{4\\pi^2 R}{T^2}$.",
        "r": "The acceleration in uniform circular motion is directed radially inwards towards the center of curvature (centripetal acceleration).",
        "ans": "B",
        "exp": "Both statements are true, but Reason specifies the direction of centripetal acceleration rather than deriving the mathematical formula for its magnitude."
    },
    {
        "a": "If the displacement-time graph of a body is a curve curving upwards with increasing slope, the body is accelerating.",
        "r": "The instantaneous slope of a position-time graph represents velocity, so an increasing slope indicates increasing velocity with time.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and correctly links upward curvature on $s$-$t$ graph to positive acceleration."
    },
    {
        "a": "A person sitting inside a train moving with uniform velocity throws an apple vertically upwards; the apple lands directly back into his hands.",
        "r": "Due to inertia of motion, the apple maintains the same horizontal forward velocity as the train and the passenger throughout its flight.",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and explains the relative projectile mechanics and inertia of horizontal motion."
    },
    {
        "a": "When a ball bounces off a hard wall with the same speed, its velocity does not change.",
        "r": "Velocity is a vector quantity that depends on both speed and direction.",
        "ans": "D",
        "exp": "Assertion is false: Reversing direction completely changes the velocity vector (from $+v$ to $-v$, change $\\Delta v = 2v$). Reason is true."
    },
    {
        "a": "Two stones of masses 1 kg and 5 kg dropped simultaneously from the same height in a vacuum reach the ground at the exact same instant.",
        "r": "In a vacuum, the acceleration due to gravity $g$ is independent of the mass of the falling object ($a = g$).",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and confirms Galileo's principle of universal gravitational acceleration in the absence of air resistance."
    },
    {
        "a": "An object can have a northward velocity while simultaneously experiencing a southward acceleration.",
        "r": "When brakes are applied to a car heading north, the retarding acceleration vector points in the opposite direction (south).",
        "ans": "A",
        "exp": "Assertion is true. Reason is true and gives a concrete physics example where velocity and acceleration vectors point in opposite directions."
    }
]
