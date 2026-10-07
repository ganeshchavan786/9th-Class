"""
Data module for CBSE Class 9 Science - SET E (Case Study & Practical Experiments)
Part 2: Chapters 5 to 8 (5 Case Studies per Chapter = 25 questions each, 100 MCQs total)
Strictly 100% CBSE English Medium.
"""

CHAPTER_05_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Comparative Optical & Filtration Analysis: Solution, Colloid & Suspension",
        "passage": "Students were provided with three unlabeled beakers containing mixtures in water:<br>"
                   "• <b>Beaker A:</b> 5 g of Copper Sulfate ($CuSO_4$) dissolved in 100 mL of water.<br>"
                   "• <b>Beaker B:</b> 2 g of fine Starch powder boiled and cooled in 100 mL of water.<br>"
                   "• <b>Beaker C:</b> 5 g of finely crushed Chalk powder stirred in 100 mL of water.<br>"
                   "The students conducted three diagnostic practical tests:<br>"
                   "1. <b>Tyndall Effect:</b> Directing a red laser beam through each beaker in a dark room.<br>"
                   "2. <b>Filtration:</b> Passing each mixture through Whatman No. 1 filter paper.<br>"
                   "3. <b>Stability:</b> Leaving the beakers undisturbed for 30 minutes.",
        "questions": [
            {
                "q": "In which beaker(s) was the luminous path of the laser beam distinctly visible from the side (Tyndall effect)?",
                "options": [
                    "Beaker A only",
                    "Beaker B and Beaker C (while suspended)",
                    "Beaker A and Beaker B only",
                    "None of the beakers"
                ],
                "ans": "B",
                "exp": "Colloidal particles in Beaker B (starch sol, 1–100 nm) and suspended particles in Beaker C scatter visible light. True solutions in Beaker A (< 1 nm) do not show Tyndall effect."
            },
            {
                "q": "What was retained on the filter paper after filtering the contents of Beaker C (Chalk and water)?",
                "options": [
                    "Zero residue; the mixture passed through completely",
                    "White insoluble chalk powder residue, while clear water passed as filtrate",
                    "Blue copper sulfate crystals",
                    "A jelly-like starch sol"
                ],
                "ans": "B",
                "exp": "Chalk particles in a suspension are larger than 100 nm and cannot pass through the microscopic pores of filter paper, leaving solid residue."
            },
            {
                "q": "What happened to the three mixtures after standing undisturbed for 30 minutes?",
                "options": [
                    "Beakers A and B remained completely homogeneous; Beaker C showed chalk settling to the bottom",
                    "All three mixtures settled completely to the bottom",
                    "Beaker B separated into two distinct liquid layers",
                    "Beaker A evaporated completely"
                ],
                "ans": "A",
                "exp": "True solutions (Beaker A) and colloids (Beaker B) are stable and do not settle; suspensions (Beaker C) are unstable and settle under gravity."
            },
            {
                "q": "How is Beaker B (Starch in water) accurately classified in colloid chemistry?",
                "options": ["Gel (liquid in solid)", "Sol (solid dispersed in liquid)", "Emulsion (liquid in liquid)", "Aerosol (solid in gas)"],
                "ans": "B",
                "exp": "Starch powder consists of solid macromolecules dispersed in a liquid dispersion medium (water), which defines a sol."
            },
            {
                "q": "What microscopic kinetic phenomenon keeps colloidal particles in Beaker B from settling over time?",
                "options": [
                    "Continuous random zigzag Brownian motion caused by collisions with solvent molecules",
                    "Magnetic attraction to the glass",
                    "Gravitational repulsion",
                    "Capillary ascent"
                ],
                "ans": "A",
                "exp": "Erratic, continuous collisions between colloidal starch particles and rapidly moving water molecules (Brownian motion) counteract gravitational sedimentation."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Solubility Curve & Crystallization of Copper Sulfate",
        "passage": "A chemistry student investigated the temperature dependence of solubility of Copper Sulfate ($CuSO_4$) in water.<br>"
                   "• <b>Solubility Data (g of $CuSO_4$ per 100 g of water):</b><br>"
                   "  - At 20°C: $21.0\\text{ g}$<br>"
                   "  - At 40°C: $29.0\\text{ g}$<br>"
                   "  - At 60°C: $40.0\\text{ g}$<br>"
                   "  - At 80°C: $55.0\\text{ g}$<br>"
                   "The student prepared a saturated solution by dissolving $55.0\\text{ g}$ of $CuSO_4$ in $100.0\\text{ g}$ of water at 80°C. She filtered the hot solution to remove insoluble impurities and allowed the clear filtrate to cool slowly undisturbed to 20°C.",
        "questions": [
            {
                "q": "What mass of solid Copper Sulfate crystals precipitates out of solution as it cools from 80°C to 20°C?",
                "options": ["21.0 g", "34.0 g", "55.0 g", "14.0 g"],
                "ans": "B",
                "exp": "Mass precipitated $= \\text{Solubility at 80°C} - \\text{Solubility at 20°C} = 55.0\\text{ g} - 21.0\\text{ g} = 34.0\\text{ g}$."
            },
            {
                "q": "Why is slow cooling preferred over rapid chilling with ice during crystallization?",
                "options": [
                    "To prevent the beaker from cracking",
                    "Slow cooling allows well-formed, large, highly pure geometric crystals to grow without trapping solvent impurities",
                    "To evaporate all the water",
                    "To prevent chemical decomposition of copper"
                ],
                "ans": "B",
                "exp": "Slow, undisturbed cooling allows solute molecules to arrange methodically into a pure crystal lattice, excluding foreign impurities."
            },
            {
                "q": "Why is crystallization superior to simple evaporation to dryness for purifying salts?",
                "options": [
                    "Evaporation requires zero heat",
                    "During evaporation to dryness, heat-sensitive compounds can decompose or char, and soluble impurities remain mixed with the dried solid",
                    "Crystallization takes less time than evaporation",
                    "Crystallization converts the salt into an element"
                ],
                "ans": "B",
                "exp": "Evaporation leaves all soluble contaminants behind with the dried product; crystallization purifies the compound by selectively forming pure crystal lattices."
            },
            {
                "q": "What is the mass percentage of $CuSO_4$ in the saturated solution at 20°C ($21.0\\text{ g}$ solute in $100.0\\text{ g}$ water)?",
                "options": ["21.0%", "17.36%", "26.58%", "19.0%"],
                "ans": "B",
                "exp": "$\\text{Mass percentage} = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100 = \\frac{21.0}{21.0 + 100.0} \\times 100 = \\frac{21.0}{121.0} \\times 100 \\approx 17.36\\%$."
            },
            {
                "q": "What type of solution is formed immediately if a hot saturated solution at 80°C is cooled to 40°C without any crystal nucleation occurring?",
                "options": ["Unsaturated solution", "Supersaturated solution", "Dilute solution", "Colloidal suspension"],
                "ans": "B",
                "exp": "A solution that temporarily holds more dissolved solute than its thermodynamic saturation equilibrium at that temperature is supersaturated."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Paper Chromatography of Synthetic Black Ink",
        "passage": "In a forensic chemistry laboratory practical, students analyzed water-soluble black marker ink using ascending paper chromatography.<br>"
                   "1. A pencil baseline was drawn 2 cm from the bottom edge of a Whatman chromatography paper strip.<br>"
                   "2. A small concentrated spot of black ink was applied on the baseline using a capillary tube and allowed to dry.<br>"
                   "3. The strip was suspended vertically in a chromatography jar containing water as the mobile solvent, with the solvent level 1 cm below the pencil line.<br>"
                   "4. As the solvent ascended by capillary action, the single black spot separated into three distinct color bands: Yellow, Red, and Blue.<br>"
                   "5. When the solvent front reached 10.0 cm from the baseline, the strip was removed and dried:<br>"
                   "   - Yellow dye travelled: $3.0\\text{ cm}$<br>"
                   "   - Red dye travelled: $6.0\\text{ cm}$<br>"
                   "   - Blue dye travelled: $8.5\\text{ cm}$",
        "questions": [
            {
                "q": "Why was the reference baseline drawn with a graphite pencil rather than an ordinary ballpoint ink pen?",
                "options": [
                    "Pencil graphite is insoluble in the running mobile solvent (water) and will not dissolve or interfere with the chromatogram",
                    "Pencil graphite conducts electricity",
                    "Pencil lines are darker than ink",
                    "Pencil reacts chemically with paper"
                ],
                "ans": "A",
                "exp": "Graphite is insoluble in water and organic solvents; ink from a pen would dissolve and migrate, ruining the chromatographic baseline."
            },
            {
                "q": "Calculate the Retention Factor ($R_f$) value for the Red dye:",
                "options": ["0.30", "0.60", "0.85", "1.67"],
                "ans": "B",
                "exp": "$R_f = \\frac{\\text{Distance travelled by solute component}}{\\text{Distance travelled by solvent front}} = \\frac{6.0\\text{ cm}}{10.0\\text{ cm}} = 0.60$."
            },
            {
                "q": "Which of the three dye components had the highest solubility in the mobile solvent (water) and lowest adsorption to the cellulose paper?",
                "options": ["Yellow dye", "Red dye", "Blue dye", "All three had identical solubility"],
                "ans": "C",
                "exp": "The Blue dye migrated the farthest ($8.5$ cm, $R_f = 0.85$), indicating greatest solubility in mobile water and weakest affinity for stationary paper fibers."
            },
            {
                "q": "Why must the solvent level in the developing chamber be kept below the pencil baseline spot?",
                "options": [
                    "To prevent the paper from getting wet",
                    "To prevent the ink spot from directly dissolving into the reservoir solvent before capillary migration begins",
                    "To allow air bubbles to escape",
                    "To keep the chamber at low temperature"
                ],
                "ans": "B",
                "exp": "If submerged below the solvent surface, the ink spot simply washes out into the solvent pool instead of migrating up the paper strip."
            },
            {
                "q": "Which of the following mixtures cannot be separated using paper chromatography?",
                "options": [
                    "Amino acids in a protein hydrolysate",
                    "Plant leaf pigments (chlorophyll a, chlorophyll b, xanthophyll, carotene)",
                    "Dyes in confectionery food coloring",
                    "A mixture of sand and iron filings"
                ],
                "ans": "D",
                "exp": "Sand and iron filings are macroscopic insoluble solids separated mechanically using a magnet; chromatography separates molecular solutes."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Extraction of Immiscible Liquids using a Separating Funnel",
        "passage": "In a separation science experiment, a student was tasked with separating a 150 mL mixture of kerosene oil and water.<br>"
                   "• Density of kerosene oil = $0.80\\text{ g/cm}^3$<br>"
                   "• Density of pure water = $1.00\\text{ g/cm}^3$<br>"
                   "The student poured the heterogeneous mixture into a glass separating funnel supported on a ring stand, stoppered it, inverted and vented it, and then left it undisturbed for 15 minutes.<br>"
                   "Two distinct transparent layers formed with a sharp horizontal interface.<br>"
                   "She carefully opened the stopcock to collect the lower liquid layer into Beaker 1 and closed it just as the interface touched the stopcock, then poured the upper liquid layer out through the top neck into Beaker 2.",
        "questions": [
            {
                "q": "Which liquid formed the lower layer in the separating funnel and was collected first in Beaker 1?",
                "options": [
                    "Kerosene oil, because it is lighter",
                    "Water, because it has higher density ($1.00 > 0.80\\text{ g/cm}^3$)",
                    "An emulsion of both liquids",
                    "Air bubbles"
                ],
                "ans": "B",
                "exp": "The denser liquid (water, $1.00\\text{ g/cm}^3$) sinks to the bottom, while the less dense liquid (kerosene, $0.80\\text{ g/cm}^3$) floats on top."
            },
            {
                "q": "Why is the upper liquid layer (kerosene) poured out through the top opening rather than drained through the bottom stopcock?",
                "options": [
                    "To prevent the stopcock from rusting",
                    "To avoid contaminating the purified upper liquid with droplets of the denser lower liquid clinging to the stopcock bore",
                    "Because kerosene cannot flow through a narrow nozzle",
                    "To allow kerosene to evaporate faster"
                ],
                "ans": "B",
                "exp": "Draining the upper liquid through the bottom stopcock would wash residual droplets of the lower liquid into the clean beaker, causing cross-contamination."
            },
            {
                "q": "Why was the student instructed to invert the stoppered separating funnel and open the stopcock briefly (venting)?",
                "options": [
                    "To release internal vapor pressure built up during shaking",
                    "To allow external air to react chemically with kerosene",
                    "To stir the mixture thoroughly",
                    "To clean the nozzle"
                ],
                "ans": "A",
                "exp": "Shaking volatile liquids builds up internal vapor pressure that can pop the glass stopper; venting releases the pressure safely."
            },
            {
                "q": "Which physical property is the fundamental basis for separation using a separating funnel?",
                "options": [
                    "Difference in boiling points",
                    "Difference in solubilities in alcohol",
                    "Immiscibility and difference in liquid densities",
                    "Difference in magnetic properties"
                ],
                "ans": "C",
                "exp": "Separating funnels are used exclusively for immiscible liquids that do not dissolve in each other and form distinct layers due to density differences."
            },
            {
                "q": "Which of the following liquid pairs can be separated using a separating funnel?",
                "options": [
                    "Ethanol and water",
                    "Mustard oil and water",
                    "Acetone and water",
                    "Acetic acid and water"
                ],
                "ans": "B",
                "exp": "Mustard oil and water are completely immiscible and separate into two distinct layers; ethanol, acetone, and acetic acid are completely miscible with water."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Mixture vs Compound: Heating Iron Filings and Sulfur Powder",
        "passage": "Students investigated the difference between a physical mixture and a chemical compound using iron filings and sulfur powder in a mass ratio of $7:4$.<br>"
                   "• <b>Sample 1 (Mixture):</b> Iron filings and sulfur powder were thoroughly ground together in a mortar at room temperature.<br>"
                   "• <b>Sample 2 (Compound):</b> An identical mixture was placed in a hard glass test tube and heated strongly over a Bunsen flame. A reddish glow spread through the mass, forming a hard black crystalline lump.<br>"
                   "The students tested both samples with a bar magnet, Carbon Disulfide ($CS_2$) solvent, and dilute Hydrochloric Acid ($HCl$).",
        "questions": [
            {
                "q": "What happened when a bar magnet was brought near Sample 1 (Mixture) and Sample 2 (Compound)?",
                "options": [
                    "Both samples were attracted completely to the magnet",
                    "In Sample 1, iron filings were attracted to the magnet, leaving yellow sulfur behind; Sample 2 was not attracted to the magnet",
                    "Neither sample was attracted to the magnet",
                    "Sample 2 was repelled by the magnet with violent sparks"
                ],
                "ans": "B",
                "exp": "In a mixture, iron retains its magnetic properties. In the compound Iron Sulfide (FeS), iron is chemically bonded in a crystal lattice and loses its ferromagnetism."
            },
            {
                "q": "What was observed when Carbon Disulfide ($CS_2$) solvent was added to Sample 1?",
                "options": [
                    "Iron dissolved, leaving sulfur",
                    "Yellow sulfur dissolved completely, leaving grey iron filings behind; upon evaporation of $CS_2$, yellow sulfur crystals reformed",
                    "The mixture exploded",
                    "Zero dissolution occurred"
                ],
                "ans": "B",
                "exp": "Sulfur is readily soluble in non-polar carbon disulfide ($CS_2$), while iron is insoluble. This is a physical separation method for the mixture."
            },
            {
                "q": "What gas was evolved when dilute $HCl$ was added to Sample 1 (Mixture of Fe and S)?",
                "options": [
                    "Sulfur dioxide gas ($SO_2$)",
                    "Colorless, odorless Hydrogen gas ($H_2$) that burns with a 'pop' sound",
                    "Hydrogen sulfide gas ($H_2S$) smelling like rotten eggs",
                    "Chlorine gas ($Cl_2$)"
                ],
                "ans": "B",
                "exp": "In the mixture, iron reacts independently with dilute acid: $Fe + 2HCl \\rightarrow FeCl_2 + H_2 \\uparrow$. Hydrogen is odorless and burns with a pop."
            },
            {
                "q": "What gas was evolved when dilute $HCl$ was added to Sample 2 (Compound FeS)?",
                "options": [
                    "Hydrogen gas ($H_2$)",
                    "Colorless Hydrogen Sulfide gas ($H_2S$) having a characteristic foul smell of rotten eggs",
                    "Oxygen gas ($O_2$)",
                    "Carbon dioxide gas ($CO_2$)"
                ],
                "ans": "B",
                "exp": "Iron sulfide reacts chemically: $FeS + 2HCl \\rightarrow FeCl_2 + H_2S \\uparrow$. Hydrogen sulfide is toxic and smells like rotten eggs."
            },
            {
                "q": "Why is the formation of Iron Sulfide from iron and sulfur classified as an exothermic chemical change?",
                "options": [
                    "Because it can be easily reversed using a magnet",
                    "Because new chemical bonds form with release of energy (red-hot glow) and the product FeS has properties entirely different from iron and sulfur",
                    "Because no heat was involved",
                    "Because the mass decreased by 50%"
                ],
                "ans": "B",
                "exp": "Chemical reaction: $Fe + S \\rightarrow FeS + \\text{Heat}$. It is irreversible, forms a new stoichiometric compound, and releases significant chemical energy."
            }
        ]
    }
]

CHAPTER_06_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Verification of Newton's Second Law ($F = ma$) with Dynamic Trolley",
        "passage": "In a physics mechanics practical, students verified Newton's second law using a low-friction dynamic trolley of mass $M = 0.80\\text{ kg}$ on a horizontal runway.<br>"
                   "• A light inextensible string tied to the trolley passed over a smooth pulley at the edge of the bench, carrying a hanging accelerating mass $m$.<br>"
                   "• The total mass of the accelerating system was kept strictly constant at $(M + m) = 1.00\\text{ kg}$ by transferring slotted masses between the trolley and the hanging holder.<br>"
                   "• Acceleration ($a$) was measured using ticker-timer tapes for four different accelerating weights ($F = mg$, where $g = 9.8\\text{ m/s}^2$):<br>"
                   "  - Trial 1: $F_1 = 0.49\\text{ N} \\rightarrow a_1 = 0.49\\text{ m/s}^2$<br>"
                   "  - Trial 2: $F_2 = 0.98\\text{ N} \\rightarrow a_2 = 0.98\\text{ m/s}^2$<br>"
                   "  - Trial 3: $F_3 = 1.47\\text{ N} \\rightarrow a_3 = 1.47\\text{ m/s}^2$<br>"
                   "  - Trial 4: $F_4 = 1.96\\text{ N} \\rightarrow a_4 = 1.96\\text{ m/s}^2$",
        "questions": [
            {
                "q": "What mathematical relationship between applied accelerating force $F$ and acceleration $a$ is validated by the experimental data?",
                "options": [
                    "Acceleration is inversely proportional to force ($a \\propto 1/F$)",
                    "Acceleration is directly proportional to applied force ($a \\propto F$) for constant system mass",
                    "Acceleration is independent of applied force",
                    "Acceleration is proportional to the square of force ($a \\propto F^2$)"
                ],
                "ans": "B",
                "exp": "The ratio $\\frac{F}{a} = \\frac{0.49}{0.49} = \\frac{0.98}{0.98} = 1.00\\text{ kg}$ is constant, proving $a \\propto F$."
            },
            {
                "q": "What is the slope of the graph plotted between applied force $F$ (y-axis) and acceleration $a$ (x-axis)?",
                "options": ["$0.50\\text{ kg}$", "$1.00\\text{ kg}$", "$2.00\\text{ kg}$", "$9.8\\text{ kg}$"],
                "ans": "B",
                "exp": "Since $F = ma$, plotting $F$ against $a$ yields slope $m_{total} = \\frac{\\Delta F}{\\Delta a} = 1.00\\text{ kg}$."
            },
            {
                "q": "Why was it crucial to transfer slotted masses from the trolley to the hanging hanger rather than simply adding new masses to the hanger?",
                "options": [
                    "To prevent the string from snapping",
                    "To keep the total accelerated mass of the system $(M + m)$ strictly constant while systematically varying the accelerating force",
                    "To reduce air resistance",
                    "To make the trolley roll faster"
                ],
                "ans": "B",
                "exp": "To verify $a \\propto F$ via fair testing, the total mass must be held constant. Transferring masses ensures $(M+m)$ remains invariant."
            },
            {
                "q": "How did the students compensate for resistive friction along the runway before collecting data?",
                "options": [
                    "By pouring water onto the track",
                    "By slightly tilting the runway so the component of gravity down the slope ($mg\\sin\\theta$) exactly cancels friction",
                    "By pushing the trolley continuously by hand",
                    "By using rough sandpaper on the wheels"
                ],
                "ans": "B",
                "exp": "Friction-compensating the runway involves tilting it just enough so the trolley rolls down at constant velocity when given a slight tap."
            },
            {
                "q": "If the accelerating force is held constant at $1.0\\text{ N}$ while the total mass is doubled from $1.0\\text{ kg}$ to $2.0\\text{ kg}$, what will the new acceleration be?",
                "options": ["$0.50\\text{ m/s}^2$", "$1.00\\text{ m/s}^2$", "$2.00\\text{ m/s}^2$", "$0.25\\text{ m/s}^2$"],
                "ans": "A",
                "exp": "$a = \\frac{F}{m} = \\frac{1.0\\text{ N}}{2.0\\text{ kg}} = 0.50\\text{ m/s}^2$. Acceleration is inversely proportional to mass."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Impulse-Momentum Theorem & Automotive Crash Attenuation",
        "passage": "Automotive safety engineers conducted crash-test simulations using sensor-equipped crash test dummies to assess passenger survival during head-on collisions.<br>"
                   "• In the simulation, a car of mass 1200 kg travelling at $54\\text{ km/h} = 15\\text{ m/s}$ struck a rigid barrier and came to rest ($v=0$).<br>"
                   "• <b>Unprotected Passenger (Dummy X):</b> Struck the rigid steering column directly, bringing head momentum to zero in a collision duration of $\\Delta t_1 = 0.010\\text{ s}$.<br>"
                   "• <b>Protected Passenger (Dummy Y):</b> Protected by a deployed airbag and front crumple zone, extending the head deceleration duration to $\\Delta t_2 = 0.150\\text{ s}$.<br>"
                   "The head mass of both dummies was $m_{head} = 5.0\\text{ kg}$.",
        "questions": [
            {
                "q": "What is the initial linear momentum of the dummy's head prior to impact?",
                "options": ["$50\\text{ kg}\\cdot\\text{m/s}$", "$75\\text{ kg}\\cdot\\text{m/s}$", "$150\\text{ kg}\\cdot\\text{m/s}$", "$18000\\text{ kg}\\cdot\\text{m/s}$"],
                "ans": "B",
                "exp": "$p = m_{head} \\times u = 5.0\\text{ kg} \\times 15\\text{ m/s} = 75\\text{ kg}\\cdot\\text{m/s}$."
            },
            {
                "q": "What is the magnitude of the impulse ($\Delta p$) experienced by the dummy's head during the collision?",
                "options": ["$75\\text{ N}\\cdot\\text{s}$", "$150\\text{ N}\\cdot\\text{s}$", "$0\\text{ N}\\cdot\\text{s}$", "$500\\text{ N}\\cdot\\text{s}$"],
                "ans": "A",
                "exp": "Impulse $= \\Delta p = |p_f - p_i| = |0 - 75| = 75\\text{ N}\\cdot\\text{s}$ (or $\\text{kg}\\cdot\\text{m/s}$)."
            },
            {
                "q": "What peak average impact force acted on the head of Dummy X (unprotected, $\\Delta t_1 = 0.010\\text{ s}$)?",
                "options": ["750 N", "7500 N", "75 N", "1500 N"],
                "ans": "B",
                "exp": "$F_1 = \\frac{\\Delta p}{\\Delta t_1} = \\frac{75\\text{ N}\\cdot\\text{s}}{0.010\\text{ s}} = 7500\\text{ N}$ (sufficient to cause fatal skull fracture)."
            },
            {
                "q": "What peak average impact force acted on the head of Dummy Y (protected by airbag, $\\Delta t_2 = 0.150\\text{ s}$)?",
                "options": ["500 N", "7500 N", "1500 N", "75 N"],
                "ans": "A",
                "exp": "$F_2 = \\frac{\\Delta p}{\\Delta t_2} = \\frac{75\\text{ N}\\cdot\\text{s}}{0.150\\text{ s}} = 500\\text{ N}$ (reduced by 15-fold, preventing fatal trauma)."
            },
            {
                "q": "Which athletic technique in cricket directly applies this exact impulse-momentum principle?",
                "options": [
                    "A bowler running fast to bowl",
                    "A fielder pulling his hands backwards while catching a fast cricket ball to prolong impact time and reduce hand force",
                    "A batsman hitting a six",
                    "An umpire raising his finger"
                ],
                "ans": "B",
                "exp": "Drawing hands backward increases the time $\\Delta t$ over which the ball's momentum drops to zero, reducing the impact force $F = \\Delta p / \\Delta t$ on the hands."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Verification of Conservation of Linear Momentum on an Air Track",
        "passage": "Students verified the law of conservation of linear momentum using two gliders on a near-frictionless linear air track equipped with photogate timers.<br>"
                   "• <b>Glider 1:</b> Mass $m_1 = 0.300\\text{ kg}$, travelling towards Glider 2 with velocity $u_1 = +0.80\\text{ m/s}$.<br>"
                   "• <b>Glider 2:</b> Mass $m_2 = 0.500\\text{ kg}$, initially stationary at rest ($u_2 = 0\\text{ m/s}$).<br>"
                   "The gliders were fitted with velcro bumpers so that upon colliding, they stuck together and moved as a single combined mass ($m_1 + m_2$) with common final velocity $V$.",
        "questions": [
            {
                "q": "What is the total linear momentum of the two-glider system before the collision?",
                "options": ["$0.150\\text{ kg}\\cdot\\text{m/s}$", "$0.240\\text{ kg}\\cdot\\text{m/s}$", "$0.400\\text{ kg}\\cdot\\text{m/s}$", "$0\\text{ kg}\\cdot\\text{m/s}$"],
                "ans": "B",
                "exp": "$p_{total} = m_1 u_1 + m_2 u_2 = (0.300 \\times 0.80) + (0.500 \\times 0) = 0.240\\text{ kg}\\cdot\\text{m/s}$."
            },
            {
                "q": "According to the law of conservation of momentum, what is the common final velocity $V$ of the combined gliders after collision?",
                "options": ["$+0.30\\text{ m/s}$", "$+0.48\\text{ m/s}$", "$+0.24\\text{ m/s}$", "$+0.80\\text{ m/s}$"],
                "ans": "A",
                "exp": "$p_f = (m_1 + m_2)V = (0.300 + 0.500)V = 0.800 V$. By conservation: $0.800 V = 0.240 \\Rightarrow V = \\frac{0.240}{0.800} = +0.30\\text{ m/s}$."
            },
            {
                "q": "What was the total kinetic energy of the system before the collision?",
                "options": ["0.096 J", "0.192 J", "0.048 J", "0.240 J"],
                "ans": "A",
                "exp": "$E_{k, initial} = \\frac{1}{2} m_1 u_1^2 = \\frac{1}{2}(0.300)(0.80)^2 = 0.150 \\times 0.64 = 0.096\\text{ J}$."
            },
            {
                "q": "What was the total kinetic energy of the combined gliders after the inelastic collision?",
                "options": ["0.096 J", "0.036 J", "0.072 J", "0.018 J"],
                "ans": "B",
                "exp": "$E_{k, final} = \\frac{1}{2}(m_1 + m_2)V^2 = \\frac{1}{2}(0.800)(0.30)^2 = 0.400 \\times 0.09 = 0.036\\text{ J}$."
            },
            {
                "q": "Why is total kinetic energy not conserved in this collision, even though linear momentum is conserved?",
                "options": [
                    "Because momentum was destroyed",
                    "Because in an inelastic collision, some mechanical kinetic energy is converted into internal thermal energy and sound during deformation",
                    "Because the air track lost pressure",
                    "Because gravity increased"
                ],
                "ans": "B",
                "exp": "Total linear momentum is strictly conserved in all collisions without net external force. However, in inelastic collisions, kinetic energy is partially dissipated as heat, sound, and material deformation."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Action-Reaction Force Verification using Interconnected Spring Balances",
        "passage": "To investigate Newton's third law of motion, students linked two identical spring balances, Balance A and Balance B, hook-to-hook.<br>"
                   "• The ring of Balance A was anchored firmly to a rigid wall hook.<br>"
                   "• A student held the ring of Balance B and pulled it horizontally to the right with varying forces.<br>"
                   "• The force readings on both scales were recorded simultaneously:<br>"
                   "  - Reading 1: Balance B pulled to $5.0\\text{ N} \\rightarrow$ Balance A read $5.0\\text{ N}$<br>"
                   "  - Reading 2: Balance B pulled to $12.0\\text{ N} \\rightarrow$ Balance A read $12.0\\text{ N}$<br>"
                   "  - Reading 3: Balance B pulled to $20.0\\text{ N} \\rightarrow$ Balance A read $20.0\\text{ N}$",
        "questions": [
            {
                "q": "What fundamental law of physics is directly validated by the identical readings on both spring balances?",
                "options": [
                    "Newton's First Law of Motion",
                    "Newton's Third Law of Motion (To every action there is an equal and opposite reaction)",
                    "Law of Conservation of Mass",
                    "Pascal's Principle"
                ],
                "ans": "B",
                "exp": "The pull exerted by Balance B on Balance A (action) is matched by an equal and opposite pull exerted by Balance A on Balance B (reaction)."
            },
            {
                "q": "If Action and Reaction forces are always equal in magnitude and opposite in direction, why do they not cancel each other to produce zero acceleration?",
                "options": [
                    "Because action force is always stronger than reaction force",
                    "Because Action and Reaction forces act simultaneously on two different, distinct physical bodies",
                    "Because reaction force occurs after a time delay",
                    "Because they act at an angle of 90°"
                ],
                "ans": "B",
                "exp": "Forces cancel only when acting on the same single body. Action acts on body 1 while reaction acts on body 2; hence, they cannot cancel each other."
            },
            {
                "q": "Which of the following real-world phenomena is an application of Newton's third law of motion?",
                "options": [
                    "A rocket lifting off by expelling high-velocity exhaust gases downward",
                    "Recoil of a rifle when a bullet is fired",
                    "A swimmer pushing water backward to propel himself forward",
                    "All of the above"
                ],
                "ans": "D",
                "exp": "Rocket thrust, rifle recoil, and swimming propulsion all operate on mutual equal-and-opposite action-reaction pairs between interacting bodies."
            },
            {
                "q": "When a person of mass 60 kg stands on horizontal ground, what is the reaction force exerted by the ground on his feet ($g = 9.8\\text{ m/s}^2$)?",
                "options": ["0 N", "588 N upward", "588 N downward", "60 N upward"],
                "ans": "B",
                "exp": "The person's feet exert a downward normal contact force of $mg = 60 \\times 9.8 = 588\\text{ N}$ on the ground. By Newton's third law, the ground exerts an equal upward normal reaction of 588 N."
            },
            {
                "q": "If the wall anchor breaks and both interconnected balances are pulled horizontally to the right accelerating across a frictionless floor, will their mutual contact readings still be equal?",
                "options": [
                    "No, the front balance will read zero",
                    "Yes, Newton's third law applies universally whether bodies are at rest or accelerating",
                    "The rear balance will read twice as much",
                    "Both balances will break"
                ],
                "ans": "B",
                "exp": "Newton's third law is an invariant law of nature; interaction forces between two bodies are instantaneously equal and opposite at every instant, accelerating or at rest."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Limiting Static Friction & Kinetic Friction on an Inclined Plane",
        "passage": "Students placed a wooden block of mass $m = 0.50\\text{ kg}$ on an adjustable wooden ramp to investigate friction.<br>"
                   "• The angle of inclination ($\theta$) of the ramp was gradually increased from 0° until the block just began to slide down spontaneously.<br>"
                   "• The critical angle where sliding initiated was recorded as $\\theta_s = 30^\\circ$ (Angle of Repose).<br>"
                   "• Once sliding, the ramp angle was adjusted to $\\theta_k = 25^\\circ$ so the block slid down with uniform constant velocity.<br>"
                   "• Take $g = 9.8\\text{ m/s}^2$, $\\sin 30^\\circ = 0.50$, $\\cos 30^\\circ = 0.866$, $\\tan 30^\\circ = 0.577$, $\\tan 25^\\circ = 0.466$.",
        "questions": [
            {
                "q": "What is the coefficient of limiting static friction ($\mu_s$) between the wooden block and the ramp surface?",
                "options": ["0.500", "0.577", "0.866", "0.466"],
                "ans": "B",
                "exp": "At the angle of repose, component of gravity equals limiting static friction: $mg\\sin\\theta_s = \\mu_s mg\\cos\\theta_s \\Rightarrow \\mu_s = \\tan\\theta_s = \\tan 30^\\circ \\approx 0.577$."
            },
            {
                "q": "What is the coefficient of kinetic friction ($\mu_k$) between the sliding block and the ramp?",
                "options": ["0.466", "0.577", "0.250", "0.980"],
                "ans": "A",
                "exp": "When sliding at constant velocity, net force is zero: $\\mu_k = \\tan\\theta_k = \\tan 25^\\circ \\approx 0.466$."
            },
            {
                "q": "Why is the coefficient of kinetic friction ($\mu_k = 0.466$) smaller than the coefficient of static friction ($\mu_s = 0.577$)?",
                "options": [
                    "Because mass decreases when moving",
                    "Because once an object is in motion, microscopic surface irregularities do not have sufficient time to interlock as deeply as when stationary",
                    "Because gravity decreases during motion",
                    "Because air pushes the object"
                ],
                "ans": "B",
                "exp": "Static friction requires breaking cold welds between microscopic surface asperities; once in motion, asperities skip over each other, reducing kinetic friction."
            },
            {
                "q": "What is the normal reaction force ($N$) exerted by the ramp on the 0.50 kg block at $\\theta = 30^\\circ$?",
                "options": ["$4.90\\text{ N}$", "$4.24\\text{ N}$", "$2.45\\text{ N}$", "$9.80\\text{ N}$"],
                "ans": "B",
                "exp": "$N = mg\\cos 30^\\circ = (0.50 \\times 9.8) \\times 0.866 = 4.90 \\times 0.866 \\approx 4.24\\text{ N}$."
            },
            {
                "q": "What net downward accelerating force acts on the block if the incline is raised to 45° (take $\\sin 45^\\circ = \\cos 45^\\circ = 0.707$ and $\\mu_k = 0.466$)?",
                "options": ["$1.85\\text{ N}$", "$3.46\\text{ N}$", "$0.50\\text{ N}$", "$4.90\\text{ N}$"],
                "ans": "A",
                "exp": "$F_{net} = mg\\sin 45^\\circ - \\mu_k mg\\cos 45^\\circ = mg\\sin 45^\\circ (1 - \\mu_k) = (4.90 \\times 0.707) \\times (1 - 0.466) = 3.464 \\times 0.534 \\approx 1.85\\text{ N}$."
            }
        ]
    }
]

CHAPTER_07_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Conservation of Mechanical Energy in a Roller Coaster Loop",
        "passage": "In a physics amusement park dynamics study, a model roller coaster cart of mass $m = 200\\text{ kg}$ was analyzed along a smooth vertical track (neglecting friction and air resistance):<br>"
                   "• <b>Point A (Starting Hill):</b> Height $h_A = 20.0\\text{ m}$ above ground; cart is released from rest ($u_A = 0\\text{ m/s}$).<br>"
                   "• <b>Point B (Bottom of Loop):</b> Ground level ($h_B = 0.0\\text{ m}$).<br>"
                   "• <b>Point C (Top of Circular Loop):</b> Height $h_C = 15.0\\text{ m}$ above ground.<br>"
                   "• Acceleration due to gravity $g = 9.8\\text{ m/s}^2$.",
        "questions": [
            {
                "q": "What is the total mechanical energy ($E_{mech} = E_k + E_p$) of the cart at Point A?",
                "options": ["0 J", "39,200 J", "19,600 J", "40,000 J"],
                "ans": "B",
                "exp": "$E_{mech} = mgh_A + \\frac{1}{2}m u_A^2 = 200\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 20.0\\text{ m} + 0 = 39,200\\text{ J}$."
            },
            {
                "q": "What is the speed ($v_B$) of the roller coaster cart as it reaches the lowest point, Point B ($h_B = 0$)?",
                "options": ["$14.0\\text{ m/s}$", "$19.8\\text{ m/s}$", "$9.8\\text{ m/s}$", "$25.0\\text{ m/s}$"],
                "ans": "B",
                "exp": "By conservation of energy: $\\frac{1}{2}m v_B^2 = mgh_A \\Rightarrow v_B = \\sqrt{2gh_A} = \\sqrt{2 \\times 9.8 \\times 20.0} = \\sqrt{392} \\approx 19.8\\text{ m/s}$."
            },
            {
                "q": "What is the gravitational potential energy of the cart at Point C ($h_C = 15.0\\text{ m}$)?",
                "options": ["29,400 J", "39,200 J", "9,800 J", "14,700 J"],
                "ans": "A",
                "exp": "$E_p = mgh_C = 200 \\times 9.8 \\times 15.0 = 29,400\\text{ J}$."
            },
            {
                "q": "What is the kinetic energy ($E_{k, C}$) and speed ($v_C$) of the cart at Point C?",
                "options": [
                    "$E_k = 9,800\\text{ J}$; $v_C = 9.9\\text{ m/s}$",
                    "$E_k = 39,200\\text{ J}$; $v_C = 19.8\\text{ m/s}$",
                    "$E_k = 0\\text{ J}$; $v_C = 0\\text{ m/s}$",
                    "$E_k = 19,600\\text{ J}$; $v_C = 14.0\\text{ m/s}$"
                ],
                "ans": "A",
                "exp": "$E_{k, C} = E_{total} - E_{p, C} = 39,200 - 29,400 = 9,800\\text{ J}$. Speed: $v_C = \\sqrt{\\frac{2 E_k}{m}} = \\sqrt{\\frac{2 \\times 9800}{200}} = \\sqrt{98} \\approx 9.9\\text{ m/s}$."
            },
            {
                "q": "If track friction dissipated 4,200 J of energy as heat during the descent from A to B, what would the actual kinetic energy at Point B be?",
                "options": ["39,200 J", "35,000 J", "43,400 J", "19,600 J"],
                "ans": "B",
                "exp": "Actual $E_k = E_{initial} - E_{friction} = 39,200\\text{ J} - 4,200\\text{ J} = 35,000\\text{ J}$."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Lifting vs Dragging: Work Done Against Gravity and Friction",
        "passage": "A warehouse worker needs to move a heavy packing crate of mass $m = 60\\text{ kg}$ into a delivery truck whose bed is at a vertical height $h = 1.5\\text{ m}$ above the ground ($g = 9.8\\text{ m/s}^2$).<br>"
                   "• <b>Method 1 (Direct Vertical Lift):</b> Lifting the crate straight up onto the truck bed.<br>"
                   "• <b>Method 2 (Inclined Ramp):</b> Pushing the crate up a smooth wooden ramp of length $L = 5.0\\text{ m}$ inclined at an angle $\\theta$ (where $\\sin\\theta = 1.5/5.0 = 0.30$). The friction force resisting motion along the ramp is $f = 80\\text{ N}$.",
        "questions": [
            {
                "q": "What is the minimum work done by the worker against gravity in Method 1 (Direct Vertical Lift)?",
                "options": ["600 J", "882 J", "90 J", "450 J"],
                "ans": "B",
                "exp": "$W_{gravity} = mgh = 60\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 1.5\\text{ m} = 882\\text{ J}$."
            },
            {
                "q": "In Method 2, what is the work done solely to overcome friction ($W_{friction}$) along the 5.0 m ramp?",
                "options": ["400 J", "80 J", "882 J", "120 J"],
                "ans": "A",
                "exp": "$W_{friction} = f \\times L = 80\\text{ N} \\times 5.0\\text{ m} = 400\\text{ J}$."
            },
            {
                "q": "What is the total work done by the worker in pushing the crate up the ramp in Method 2?",
                "options": ["882 J", "1282 J", "400 J", "482 J"],
                "ans": "B",
                "exp": "$W_{total} = W_{gravity} + W_{friction} = 882\\text{ J} + 400\\text{ J} = 1282\\text{ J}$."
            },
            {
                "q": "If Method 2 requires more total energy (1282 J vs 882 J), why does the worker choose to use the ramp?",
                "options": [
                    "Because it saves electricity",
                    "Because the ramp reduces the required muscular pushing effort (force) by spreading the work over a longer distance",
                    "Because gravity is zero on a ramp",
                    "Because it takes less time"
                ],
                "ans": "B",
                "exp": "Simple machines act as force multipliers: Lifting requires $588\\text{ N}$, while pushing up the ramp requires only $F = mg\\sin\\theta + f = (60 \\times 9.8 \\times 0.30) + 80 = 176.4 + 80 = 256.4\\text{ N}$."
            },
            {
                "q": "What is the mechanical efficiency ($\eta$) of the inclined ramp as a machine in Method 2?",
                "options": ["100%", "68.8%", "45.2%", "31.2%"],
                "ans": "B",
                "exp": "$\\text{Efficiency} = \\frac{\\text{Useful Work Output (against gravity)}}{\\text{Total Work Input}} \\times 100 = \\frac{882\\text{ J}}{1282\\text{ J}} \\times 100 \\approx 68.8\\%$."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Electric Motor Power & Overhead Water Pumping Efficiency",
        "passage": "A residential building uses an electric water pump to fill an overhead water storage tank on the roof.<br>"
                   "• Tank capacity: $V = 1000\\text{ Liters} = 1.0\\text{ m}^3$ (mass of water $m = 1000\\text{ kg}$).<br>"
                   "• Vertical height of the tank above the ground sump: $h = 18.0\\text{ m}$.<br>"
                   "• Time taken by the pump to fill the tank completely: $t = 5\\text{ minutes} = 300\\text{ seconds}$.<br>"
                   "• Electric power rating of the pump motor: $P_{in} = 1000\\text{ W} = 1.0\\text{ kW}$.<br>"
                   "• Acceleration due to gravity $g = 9.8\\text{ m/s}^2$.",
        "questions": [
            {
                "q": "What is the useful mechanical work output ($W_{out}$) performed by the pump in lifting the 1000 kg of water?",
                "options": ["18,000 J", "176,400 J", "180,000 J", "300,000 J"],
                "ans": "B",
                "exp": "$W_{out} = mgh = 1000\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 18.0\\text{ m} = 176,400\\text{ J}$ (176.4 kJ)."
            },
            {
                "q": "What is the useful mechanical power output ($P_{out}$) of the pump during the operation?",
                "options": ["588 W", "1000 W", "352.8 W", "176.4 W"],
                "ans": "A",
                "exp": "$P_{out} = \\frac{W_{out}}{t} = \\frac{176,400\\text{ J}}{300\\text{ s}} = 588\\text{ W}$."
            },
            {
                "q": "What is the total electrical energy consumed by the 1000 W motor in 5 minutes (300 s)?",
                "options": ["300,000 J", "176,400 J", "50,000 J", "600,000 J"],
                "ans": "A",
                "exp": "$E_{consumed} = P_{in} \\times t = 1000\\text{ W} \\times 300\\text{ s} = 300,000\\text{ J} = 300\\text{ kJ}$."
            },
            {
                "q": "Calculate the percentage efficiency ($\eta$) of the water pumping system:",
                "options": ["100%", "58.8%", "72.4%", "85.0%"],
                "ans": "B",
                "exp": "$\\text{Efficiency} = \\frac{P_{out}}{P_{in}} \\times 100 = \\frac{588\\text{ W}}{1000\\text{ W}} \\times 100 = 58.8\\%$."
            },
            {
                "q": "How many commercial units of electrical energy (kilowatt-hours, kWh) are consumed by the pump during this 5-minute run?",
                "options": ["0.083 kWh", "1.0 kWh", "0.5 kWh", "0.05 kWh"],
                "ans": "A",
                "exp": "Energy in $\\text{kWh} = \\text{Power (kW)} \\times \\text{Time (hours)} = 1.0\\text{ kW} \\times \\left(\\frac{5}{60}\\text{ h}\\right) = \\frac{1}{12}\\text{ kWh} \\approx 0.0833\\text{ kWh}$."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Principle of Moments & Mechanical Advantage of Levers",
        "passage": "Students conducted an experiment on a 1.00 m uniform meter stick pivoted at its center (fulcrum $F$ at the 50.0 cm mark) to study levers and the principle of moments.<br>"
                   "• <b>Class 1 Lever Investigation:</b><br>"
                   "  - A load of mass $M = 300\\text{ g}$ ($W = 3.0\\text{ N}$) was hung at the 10.0 cm mark (Load arm $d_L = 50.0 - 10.0 = 40.0\\text{ cm}$).<br>"
                   "  - An effort force was applied by hanging slotted masses at the 90.0 cm mark (Effort arm $d_E = 90.0 - 50.0 = 40.0\\text{ cm}$) to restore rotational equilibrium.<br>"
                   "• Next, the effort was moved to the 100.0 cm mark ($d_E = 50.0\\text{ cm}$) while keeping the load fixed at 10.0 cm.",
        "questions": [
            {
                "q": "According to the Principle of Moments, what condition governs rotational equilibrium?",
                "options": [
                    "Total clockwise moment equals total anticlockwise moment about the fulcrum",
                    "Mass on the right must be larger than mass on the left",
                    "Velocity ratio must equal zero",
                    "Effort force must equal zero"
                ],
                "ans": "A",
                "exp": "A lever is in rotational equilibrium when the algebraic sum of all moments about the pivot equals zero: $\\text{Anticlockwise Moment} = \\text{Clockwise Moment}$."
            },
            {
                "q": "What effort force ($E$) is required to balance the 3.0 N load when the effort is at the 100.0 cm mark ($d_E = 50.0\\text{ cm}$, $d_L = 40.0\\text{ cm}$)?",
                "options": ["3.0 N", "2.4 N", "1.5 N", "4.0 N"],
                "ans": "B",
                "exp": "$\\text{Effort} \\times d_E = \\text{Load} \\times d_L \\Rightarrow E \\times 50.0 = 3.0 \\times 40.0 \\Rightarrow E = \\frac{120.0}{50.0} = 2.4\\text{ N}$."
            },
            {
                "q": "What is the Mechanical Advantage ($\text{MA} = \text{Load}/\text{Effort}$) of this lever when $E = 2.4\\text{ N}$ and $\text{Load} = 3.0\\text{ N}$?",
                "options": ["1.0", "1.25", "0.80", "2.0"],
                "ans": "B",
                "exp": "$\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{3.0\\text{ N}}{2.4\\text{ N}} = 1.25$ (or $\\text{MA} = \\frac{d_E}{d_L} = \\frac{50}{40} = 1.25$)."
            },
            {
                "q": "Which common tool operates as a Class 2 lever where the load lies between the fulcrum and the effort?",
                "options": ["A pair of scissors", "A wheelbarrow or nutcracker", "A pair of laboratory tweezers", "A crowbar"],
                "ans": "B",
                "exp": "In a wheelbarrow and nutcracker, the load is in the middle (between fulcrum and effort), giving a mechanical advantage always greater than 1."
            },
            {
                "q": "Why is the mechanical advantage of a Class 3 lever (such as a fishing rod or human forearm) always less than 1?",
                "options": [
                    "Because the effort arm is shorter than the load arm ($d_E < d_L$), sacrificing force to gain speed and displacement",
                    "Because of friction",
                    "Because energy is destroyed",
                    "Because it is broken"
                ],
                "ans": "A",
                "exp": "In Class 3 levers, the effort is applied between the fulcrum and load ($d_E < d_L$). While $\\text{MA} < 1$ requires more force, it multiplies speed and displacement."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Mechanical Advantage & Efficiency of Pulley Systems",
        "passage": "Students set up two pulley arrangements to lift a heavy block of mass $m = 20.0\\text{ kg}$ (Load $W = 196\\text{ N}$):<br>"
                   "• <b>System A (Single Fixed Pulley):</b> A single pulley fixed to an overhead rigid ceiling support. A student pulls downward on the rope to raise the load vertically upward.<br>"
                   "• <b>System B (Block and Tackle with 4 Pulleys):</b> Two pulleys in the upper fixed block and two pulleys in the lower movable block. The load is suspended from the lower block. The total mass of the lower block and hooks is $w_{pulley} = 2.0\\text{ kg}$ ($19.6\\text{ N}$).",
        "questions": [
            {
                "q": "What is the Velocity Ratio ($\text{VR}$) and Ideal Mechanical Advantage of System A (Single Fixed Pulley)?",
                "options": ["1", "2", "4", "0.5"],
                "ans": "A",
                "exp": "In a single fixed pulley, the effort moves the exact same distance as the load ($\\text{VR} = 1$). It changes the direction of effort without multiplying force."
            },
            {
                "q": "What is the primary mechanical advantage of using a single fixed pulley if it does not reduce the required effort force?",
                "options": [
                    "It creates energy",
                    "It allows effort to be applied in a convenient downward direction (using the worker's own body weight) rather than lifting upward",
                    "It multiplies velocity by 10",
                    "It eliminates gravity"
                ],
                "ans": "B",
                "exp": "Pulling downward allows the worker to utilize body weight effectively and ergonomically to raise loads upward."
            },
            {
                "q": "In System B (Block and Tackle with 4 pulleys), how many parallel rope segments support the movable load block?",
                "options": ["2", "4", "6", "1"],
                "ans": "B",
                "exp": "In a 4-pulley system (2 fixed, 2 movable), the load is shared equally among $n = 4$ supporting segments of the continuous rope, making $\\text{VR} = 4$."
            },
            {
                "q": "What ideal effort ($E$) is required in System B to lift the 196 N load if pulley weight and friction are neglected?",
                "options": ["196 N", "98 N", "49 N", "24.5 N"],
                "ans": "C",
                "exp": "$E = \\frac{\\text{Load}}{n} = \\frac{196\\text{ N}}{4} = 49\\text{ N}$."
            },
            {
                "q": "If the lower movable pulley block has a weight of 19.6 N, what actual effort ($E_{actual}$) is required (neglecting axle friction)?",
                "options": ["49 N", "53.9 N", "98 N", "44.1 N"],
                "ans": "B",
                "exp": "Total weight lifted $= \\text{Load} + w_{pulley} = 196 + 19.6 = 215.6\\text{ N}$. Actual effort $= \\frac{215.6}{4} = 53.9\\text{ N}$."
            }
        ]
    }
]

CHAPTER_08_CASES = [
    {
        "case_id": 1,
        "title": "Case Study 1: Geiger-Marsden Alpha Particle Scattering Experiment",
        "passage": "In 1911, under the direction of Ernest Rutherford, Hans Geiger and Ernest Marsden conducted their landmark alpha particle scattering experiment.<br>"
                   "• A radioactive bismuth source emitted a narrow beam of high-energy positively charged alpha ($\alpha$) particles ($m \\approx 4\\text{ u}$, charge $+2e$).<br>"
                   "• The $\alpha$-beam struck an extremely thin gold foil of thickness approximately $100\\text{ nm}$ ($10^{-7}\\text{ m}$, about 1000 atoms thick).<br>"
                   "• A movable zinc sulfide (ZnS) phosphorescent detector screen and microscope recorded scintillations produced by scattered particles at various angles ($\theta$).<br>"
                   "• <b>Observations:</b><br>"
                   "  1. Over $99.8\\%$ of the $\alpha$-particles passed straight through the foil with zero or negligible deflection.<br>"
                   "  2. A small fraction (about $0.14\\%$) were deflected by angles greater than 1°.<br>"
                   "  3. Only about 1 in 12,000 particles suffered massive deflection (> 90°) or rebounded backwards at nearly 180°.",
        "questions": [
            {
                "q": "What major atomic structural conclusion did Rutherford deduce from the observation that most $\alpha$-particles passed undeflected?",
                "options": [
                    "Atoms are solid indivisible spheres like billiard balls",
                    "Most of the internal space within an atom is completely empty",
                    "Electrons are located at the center of the atom",
                    "Gold atoms contain zero electrons"
                ],
                "ans": "B",
                "exp": "Since over 99.8% of alpha particles traversed the foil undeflected, Rutherford concluded that the vast majority of atomic volume is empty space."
            },
            {
                "q": "Why did Rutherford deduce that the positive charge and nearly all atomic mass reside in a tiny concentrated 'nucleus'?",
                "options": [
                    "Because alpha particles were attracted towards the center",
                    "Because only a massive, highly concentrated positive core could exert sufficient electrostatic Coulomb repulsion to reverse the trajectory of fast alpha particles at 180°",
                    "Because electrons are positively charged",
                    "Because gold is yellow in color"
                ],
                "ans": "B",
                "exp": "To deflect a fast, massive alpha particle backwards, the positive charge and mass must be concentrated in a minuscule, dense central nucleus."
            },
            {
                "q": "Why was gold chosen as the target foil metal rather than aluminum or iron?",
                "options": [
                    "Gold is radioactive",
                    "Gold is the most malleable of all metals, allowing hammering into ultra-thin sheets only a few hundred atoms thick",
                    "Gold has no electrons",
                    "Gold does not conduct electricity"
                ],
                "ans": "B",
                "exp": "Malleability allows fabrication of foils ~100 nm thick, ensuring alpha particles encounter at most a single atomic collision."
            },
            {
                "q": "Rutherford estimated that the radius of the nucleus is approximately how many orders of magnitude smaller than the radius of the atom?",
                "options": ["10 times", "100 times", "$10^5$ times (100,000 times)", "$10^{10}$ times"],
                "ans": "C",
                "exp": "Atomic radius is $\\sim 10^{-10}$ m; nuclear radius is $\\sim 10^{-15}$ m. The ratio is $10^{-10} / 10^{-15} = 10^5$."
            },
            {
                "q": "What was the fatal theoretical limitation of Rutherford's planetary model of the atom according to classical physics?",
                "options": [
                    "It could not explain radioactivity",
                    "According to classical electrodynamics, an accelerating orbiting electron should continuously radiate energy and spiral into the nucleus in $10^{-8}$ s, making atoms unstable",
                    "It predicted that electrons have positive charge",
                    "It violated the law of conservation of mass"
                ],
                "ans": "B",
                "exp": "Accelerating charges radiate electromagnetic waves. An orbiting electron would lose kinetic energy and collapse into the nucleus, contradicting atomic stability."
            }
        ]
    },
    {
        "case_id": 2,
        "title": "Case Study 2: Cathode Rays, Canal Rays & Subatomic Particle Discovery",
        "passage": "In the late 19th and early 20th centuries, physicists explored electrical discharge through rarefied gases in evacuated glass discharge tubes (Crookes tubes):<br>"
                   "• <b>J.J. Thomson's Cathode Ray Experiment (1897):</b> High voltage ($10\\text{ kV}$) applied across electrodes at low pressure ($0.001\\text{ mm Hg}$) generated rays travelling from cathode to anode. The rays cast sharp shadows of obstacles, rotated light mica paddle wheels, and deflected towards the positive plate in an electric field. The charge-to-mass ratio was invariant ($e/m = 1.76 \\times 10^{11}\\text{ C/kg}$).<br>"
                   "• <b>E. Goldstein's Canal Ray Experiment (1886):</b> Using a perforated cathode, luminous rays travelled in the opposite direction from anode to cathode, carrying positive charges whose $e/m$ ratio depended on the gas in the tube.",
        "questions": [
            {
                "q": "Which subatomic particle was discovered by J.J. Thomson through cathode ray investigations?",
                "options": ["Proton", "Neutron", "Electron", "Positron"],
                "ans": "C",
                "exp": "Thomson proved cathode rays are streams of negatively charged fundamental particles, which were named electrons."
            },
            {
                "q": "What experimental evidence proved that cathode rays possess mechanical kinetic energy and momentum?",
                "options": [
                    "They cause fluorescence on ZnS screens",
                    "They can mechanically rotate a delicate mica paddle wheel placed in their path",
                    "They cast sharp shadows",
                    "They penetrate thin paper"
                ],
                "ans": "B",
                "exp": "Rotating a paddle wheel demonstrates that cathode rays consist of particles possessing mass and momentum ($p = mv$)."
            },
            {
                "q": "Why was the charge-to-mass ratio ($e/m$) of canal rays dependent on the specific gas present in the discharge tube?",
                "options": [
                    "Because canal rays are not fundamental particles",
                    "Because canal rays are residual gas cations formed when gas atoms lose electrons, and different gas ions possess different atomic masses",
                    "Because electrons change mass in different gases",
                    "Because the voltage fluctuated"
                ],
                "ans": "B",
                "exp": "Canal rays are positive ions ($M^+$). Since hydrogen, helium, and nitrogen ions have different atomic masses, their $e/m$ ratios vary."
            },
            {
                "q": "Which gas in the discharge tube yielded positive ions with the highest $e/m$ ratio (lightest mass), leading to the identification of the proton?",
                "options": ["Helium", "Hydrogen gas ($H_2$)", "Neon", "Oxygen"],
                "ans": "B",
                "exp": "Hydrogen produces the lightest positive ion ($H^+$), having charge $+e$ and mass $\\approx 1\\text{ u}$, identified as the proton."
            },
            {
                "q": "Who discovered the third fundamental subatomic particle, the neutron, in 1932 by bombarding beryllium with alpha particles?",
                "options": ["James Chadwick", "Niels Bohr", "John Dalton", "Robert Millikan"],
                "ans": "A",
                "exp": "James Chadwick discovered the uncharged neutron ($^1_0n$) via the reaction $^9_4Be + ^4_2\alpha \\rightarrow ^{12}_6C + ^1_0n$."
            }
        ]
    },
    {
        "case_id": 3,
        "title": "Case Study 3: Bohr-Bury Electronic Configurations & Energy Shell Quantum Levels",
        "passage": "To resolve the instability of Rutherford's atomic model, Niels Bohr proposed quantized stationary orbits in 1913. The Bohr-Bury scheme governs the arrangement of electrons in shells (designated K, L, M, N... with principal quantum numbers $n = 1, 2, 3, 4$):<br>"
                   "1. Maximum electrons in shell $n = 2n^2$.<br>"
                   "2. Maximum electrons in the outermost valence shell = 8 (Octet rule).<br>"
                   "3. Electrons do not occupy a new shell until the inner shells are completely filled (stepwise filling).<br>"
                   "• Sodium ($Z=11$): Electronic configuration $2, 8, 1$<br>"
                   "• Argon ($Z=18$): Electronic configuration $2, 8, 8$<br>"
                   "• Potassium ($Z=19$): Electronic configuration $2, 8, 8, 1$<br>"
                   "• Calcium ($Z=20$): Electronic configuration $2, 8, 8, 2$",
        "questions": [
            {
                "q": "What is the maximum theoretical electron capacity of the M-shell ($n=3$) according to the $2n^2$ rule?",
                "options": ["8", "18", "32", "2"],
                "ans": "B",
                "exp": "Capacity $= 2n^2 = 2(3)^2 = 2 \\times 9 = 18$ electrons."
            },
            {
                "q": "Why does potassium ($Z=19$) have the configuration $2, 8, 8, 1$ rather than $2, 8, 9$?",
                "options": [
                    "Because M-shell capacity is only 8",
                    "Because according to the Bohr-Bury rule, the outermost valence shell cannot hold more than 8 electrons; hence, the 19th electron enters the N-shell",
                    "Because potassium is an inert gas",
                    "Because potassium has no neutrons"
                ],
                "ans": "B",
                "exp": "Rule 2 dictates that the outermost shell cannot exceed 8 electrons. Once the M-shell reaches 8, additional electrons begin filling the N-shell."
            },
            {
                "q": "What happens when an electron absorbs a discrete quantum of energy (photon)?",
                "options": [
                    "It spirals into the nucleus",
                    "It jumps (is excited) from a lower stationary energy level to a higher permissible energy level",
                    "It splits into two positrons",
                    "Its mass doubles"
                ],
                "ans": "B",
                "exp": "Electrons absorb energy to transition to higher discrete energy states (excitation) and emit photons when returning to lower ground states."
            },
            {
                "q": "Why do noble gases like Argon ($2, 8, 8$) exhibit chemical inertness under standard conditions?",
                "options": [
                    "They have zero protons",
                    "Their valence shell contains a complete stable octet of 8 electrons, requiring extremely high energy to gain or lose electrons",
                    "They exist only at absolute zero",
                    "They lack mass"
                ],
                "ans": "B",
                "exp": "A complete valence octet confers maximal thermodynamic stability, preventing spontaneous chemical reactions."
            },
            {
                "q": "Which subatomic particle distribution represents the neutral atom of Aluminum ($Z=13$, Mass number $A=27$)?",
                "options": [
                    "13 protons, 14 neutrons, 13 electrons (config: $2, 8, 3$)",
                    "14 protons, 13 neutrons, 14 electrons (config: $2, 8, 4$)",
                    "13 protons, 27 neutrons, 13 electrons (config: $2, 8, 3$)",
                    "27 protons, 13 neutrons, 27 electrons"
                ],
                "ans": "A",
                "exp": "Atomic number $Z = 13$ (13 protons, 13 electrons with config $2, 8, 3$). Neutrons $N = A - Z = 27 - 13 = 14$."
            }
        ]
    },
    {
        "case_id": 4,
        "title": "Case Study 4: Valency Dynamics & Chemical Formula Formulation",
        "passage": "Students tabulated atomic numbers, electron configurations, valence electrons, and valency for elements from $Z=1$ to $Z=17$ to understand chemical bonding:<br>"
                   "• <b>Element P (Lithium, $Z=3$):</b> Config $2, 1 \\rightarrow$ Valence electrons = 1 $\\rightarrow$ Valency = 1<br>"
                   "• <b>Element Q (Nitrogen, $Z=7$):</b> Config $2, 5 \\rightarrow$ Valence electrons = 5 $\\rightarrow$ Valency = $8 - 5 = 3$<br>"
                   "• <b>Element R (Magnesium, $Z=12$):</b> Config $2, 8, 2 \\rightarrow$ Valence electrons = 2 $\\rightarrow$ Valency = 2<br>"
                   "• <b>Element S (Chlorine, $Z=17$):</b> Config $2, 8, 7 \\rightarrow$ Valence electrons = 7 $\\rightarrow$ Valency = $8 - 7 = 1$",
        "questions": [
            {
                "q": "How is the valency of non-metallic elements with 4 or more valence electrons (such as Nitrogen and Chlorine) determined?",
                "options": [
                    "Valency = Number of valence electrons",
                    "Valency = $8 - (\\text{Number of valence electrons})$",
                    "Valency = Atomic number divided by 2",
                    "Valency = Mass number minus 8"
                ],
                "ans": "B",
                "exp": "Non-metals complete their octet by gaining or sharing $(8 - V)$ electrons, where $V$ is the number of valence electrons."
            },
            {
                "q": "What is the chemical formula of the compound formed between Element R (Magnesium, valency 2) and Element S (Chlorine, valency 1)?",
                "options": ["$RS$", "$RS_2$ ($MgCl_2$)", "$R_2S$ ($Mg_2Cl$)", "$R_2S_3$"],
                "ans": "B",
                "exp": "Criss-crossing valencies ($Mg^{2+}$ and $Cl^{1-}$) yields $MgCl_2$."
            },
            {
                "q": "What is the chemical formula of the compound formed between Element R (Magnesium, valency 2) and Element Q (Nitrogen, valency 3)?",
                "options": ["$R_3Q_2$ ($Mg_3N_2$, Magnesium nitride)", "$RQ$ ($MgN$)", "$R_2Q_3$", "$RQ_2$"],
                "ans": "A",
                "exp": "Criss-crossing valencies ($Mg^{2+}$ and $N^{3-}$) gives $Mg_3N_2$ (Magnesium nitride)."
            },
            {
                "q": "Why does Helium ($Z=2$, config $2$) have a valency of 0, whereas Magnesium ($Z=12$, config $2, 8, 2$) has a valency of 2?",
                "options": [
                    "Helium has an unstable nucleus",
                    "For Helium ($n=1$), its single K-shell has maximum capacity of 2 (stable duplet), whereas Magnesium has 2 easily lost valence electrons outside a stable octet",
                    "Helium is a solid metal",
                    "Magnesium has zero neutrons"
                ],
                "ans": "B",
                "exp": "K-shell capacity is 2; Helium has a completely filled shell (duplet), giving valency 0. Magnesium has 2 valence electrons in M-shell, which it loses to form $Mg^{2+}$."
            },
            {
                "q": "What type of chemical bond is formed when Magnesium transfers its 2 valence electrons to Oxygen ($Z=8$, config $2, 6$)?",
                "options": ["Covalent bond", "Ionic (electrovalent) bond", "Metallic bond", "Hydrogen bond"],
                "ans": "B",
                "exp": "Complete electron transfer from a metal ($Mg \\rightarrow Mg^{2+} + 2e^-$) to a non-metal ($O + 2e^- \\rightarrow O^{2-}$) forms an ionic electrovalent bond."
            }
        ]
    },
    {
        "case_id": 5,
        "title": "Case Study 5: Isotopes, Isobars & Applications in Medicine and Industry",
        "passage": "Mass spectrometry reveals that many chemical elements occur in nature as mixtures of stable isotopes:<br>"
                   "• <b>Chlorine:</b> Consists of $^{35}_{17}Cl$ (atomic mass $35\\text{ u}$, abundance $75\\%$) and $^{37}_{17}Cl$ (atomic mass $37\\text{ u}$, abundance $25\\%$).<br>"
                   "• <b>Hydrogen:</b> Occurs as Protium ($^1_1H$), Deuterium ($^2_1H$), and Tritium ($^3_1H$).<br>"
                   "• <b>Isobars:</b> Argon ($^{40}_{18}Ar$) and Calcium ($^{40}_{20}Ca$) possess identical mass numbers ($A=40$) despite having different atomic numbers ($Z=18$ and $Z=20$).<br>"
                   "Radioactive isotopes (radioisotopes) find extensive use in medicine, agriculture, and nuclear power.",
        "questions": [
            {
                "q": "Calculate the average relative atomic mass of natural chlorine:",
                "options": ["35.0 u", "35.5 u", "36.0 u", "37.0 u"],
                "ans": "B",
                "exp": "$\\text{Average Mass} = \\frac{(35 \\times 75) + (37 \\times 25)}{100} = \\frac{2625 + 925}{100} = \\frac{3550}{100} = 35.5\\text{ u}$."
            },
            {
                "q": "How do isotopes of an element differ in their subatomic composition?",
                "options": [
                    "They have different numbers of protons",
                    "They have identical numbers of protons and electrons, but different numbers of neutrons",
                    "They have different electron configurations",
                    "They have different nuclear charges"
                ],
                "ans": "B",
                "exp": "Isotopes share the same atomic number $Z$ (same protons and electrons) but differ in neutron count ($N = A - Z$)."
            },
            {
                "q": "Why do all isotopes of chlorine exhibit identical chemical reactivity with sodium?",
                "options": [
                    "Because they have the same mass number",
                    "Because chemical reactivity is governed exclusively by valence electrons and electronic configuration, which are identical across isotopes",
                    "Because neutrons react with sodium",
                    "Because both isotopes are radioactive"
                ],
                "ans": "B",
                "exp": "Chemical bonding involves valence electrons. Since all isotopes have identical electronic structure ($2, 8, 7$), their chemical properties are identical."
            },
            {
                "q": "Which radioisotope is universally utilized in medical radiotherapy to treat malignant cancerous tumors?",
                "options": ["Cobalt-60 ($^{60}Co$)", "Carbon-14 ($^{14}C$)", "Uranium-238 ($^{238}U$)", "Sodium-23 ($^{23}Na$)"],
                "ans": "A",
                "exp": "Cobalt-60 emits high-energy penetrating gamma rays ($\gamma$) that destroy rapidly dividing malignant cancer cells."
            },
            {
                "q": "Which radioisotope is used in clinical medicine for the diagnosis and treatment of goitre and thyroid gland disorders?",
                "options": ["Iodine-131 ($^{131}I$)", "Cobalt-60 ($^{60}Co$)", "Uranium-235 ($^{235}U$)", "Phosphorus-32 ($^{32}P$)"],
                "ans": "A",
                "exp": "The thyroid gland selectively absorbs iodine from the bloodstream. Iodine-131 is used as a radiotracer and therapeutic agent for thyroid disorders."
            }
        ]
    }
]
