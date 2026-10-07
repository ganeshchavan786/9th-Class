"""
Data module for CBSE Class 9 Science - SET G (Final Mastery & Grand Challenge Test)
Part 2: Chapters 5 to 8 (25 Grand Challenge MCQs per Chapter = 100 MCQs total)
Strictly 100% CBSE English Medium.
"""

CHAPTER_05_QUESTIONS = [
    {
        "q": "What is the mass of pure water required to dissolve 50 g of sodium chloride ($NaCl$) to produce a 20% (by mass) solution?",
        "options": ["200 g", "250 g", "150 g", "100 g"],
        "ans": "A",
        "exp": "$\\text{Mass \\%} = \\frac{m_{solute}}{m_{solute} + m_{water}} \\times 100 \\Rightarrow 20 = \\frac{50}{50 + m_{water}} \\times 100 \\Rightarrow 50 + m_{water} = 250 \\Rightarrow m_{water} = 200\\text{ g}$."
    },
    {
        "q": "Which of the following is classified as a sol rather than a gel?",
        "options": ["Cheese", "Jelly", "Paints", "Butter"],
        "ans": "C",
        "exp": "Paints are sols (solid pigment particles dispersed in liquid vehicle). Cheese, jelly, and butter are gels (liquid trapped in solid)."
    },
    {
        "q": "During fractional distillation of liquid air, which gas boils off first due to having the lowest boiling point?",
        "options": [
            "Nitrogen (boiling point $-196^\\circ\\text{C}$)",
            "Argon (boiling point $-186^\\circ\\text{C}$)",
            "Oxygen (boiling point $-183^\\circ\\text{C}$)",
            "Carbon dioxide (boiling point $-78^\\circ\\text{C}$)"
        ],
        "ans": "A",
        "exp": "Nitrogen has the lowest boiling point ($-196^\\circ\\text{C}$) and distills off first at the top of the fractionating column."
    },
    {
        "q": "A mixture containing 5.0 g of sand, 3.0 g of common salt ($NaCl$), and 2.0 g of ammonium chloride ($NH_4Cl$) can be separated into pure components by:",
        "options": [
            "Sublimation $\\rightarrow$ Dissolution in water & filtration $\\rightarrow$ Evaporation/Crystallization",
            "Filtration $\\rightarrow$ Distillation $\\rightarrow$ Chromatography",
            "Magnetic separation $\\rightarrow$ Sublimation $\\rightarrow$ Centrifugation",
            "Fractional distillation directly"
        ],
        "ans": "A",
        "exp": "1. Sublimation separates $NH_4Cl$. 2. Dissolving remainder in water and filtering leaves sand on filter paper. 3. Evaporating water leaves pure salt."
    },
    {
        "q": "Why does a colloidal sol of ferric hydroxide ($Fe(OH)_3$) coagulate (precipitate) upon addition of sodium sulfate ($Na_2SO_4$)?",
        "options": [
            "Sulfate anions ($SO_4^{2-}$) neutralize the positive zeta-potential charge on the colloidal particles (Hardy-Schulze rule)",
            "Sulfate absorbs all water",
            "Iron dissolves completely",
            "Temperature drops to absolute zero"
        ],
        "ans": "A",
        "exp": "According to the Hardy-Schulze rule, oppositely charged polyvalent ions ($SO_4^{2-}$) neutralize colloidal surface charges, inducing coagulation."
    },
    {
        "q": "How does the solubility of calcium oxide ($CaO$) in water behave with increasing temperature?",
        "options": [
            "Increases rapidly",
            "Decreases, because dissolution of calcium oxide/hydroxide is highly exothermic",
            "Remains strictly constant",
            "Becomes infinite"
        ],
        "ans": "B",
        "exp": "Dissolution of $CaO$ and $Ca(OH)_2$ is strongly exothermic; by Le Chatelier's principle, adding heat decreases solubility."
    },
    {
        "q": "What is the Retention Factor ($R_f$) of a solute that does not dissolve in the mobile solvent and remains stationary at the baseline?",
        "options": ["1.0", "Zero (0.0)", "0.5", "Infinity"],
        "ans": "B",
        "exp": "$R_f = \\frac{\\text{Distance travelled by solute}}{\\text{Distance travelled by solvent front}} = \\frac{0}{d_{solvent}} = 0.0$."
    },
    {
        "q": "Which of the following processes represents an endothermic physical change?",
        "options": ["Freezing of water", "Sublimation of dry ice (solid $CO_2$)", "Condensation of steam", "Rusting of iron"],
        "ans": "B",
        "exp": "Sublimation requires absorption of latent heat to break intermolecular bonds without changing chemical identity."
    },
    {
        "q": "A saturated solution of sugar at 80°C contains 360 g of sugar per 100 g of water. At 20°C, solubility is 200 g per 100 g of water. If 230 g of the saturated solution at 80°C is cooled to 20°C, what mass of sugar crystals precipitates?",
        "options": ["160 g", "80 g", "100 g", "50 g"],
        "ans": "B",
        "exp": "At 80°C, total mass of solution $= 360 + 100 = 460\\text{ g}$. A 230 g sample contains half the amounts: $180\\text{ g}$ sugar and $50\\text{ g}$ water. At 20°C, 50 g of water holds $100\\text{ g}$ sugar. Precipitated crystals $= 180 - 100 = 80\\text{ g}$."
    },
    {
        "q": "Which optical phenomenon proves that milk is a colloidal dispersion rather than a true solution?",
        "options": ["Total internal reflection", "Tyndall scattering", "Refraction of light", "Dispersion into a rainbow spectrum"],
        "ans": "B",
        "exp": "The Tyndall effect illuminates the light path through milk, proving the presence of colloidal fat and protein micelles."
    },
    {
        "q": "What is the primary role of the fractionating column packed with glass beads in fractional distillation?",
        "options": [
            "To filter impurities",
            "To provide a large surface area for repeated cycles of condensation and revaporization, sharpening component separation",
            "To react chemically with vapors",
            "To cool the boiling flask"
        ],
        "ans": "B",
        "exp": "The column packing creates a thermal gradient where rising vapor undergoes multiple theoretical condensation-vaporization plates."
    },
    {
        "q": "Which of the following is classified as an emulsion?",
        "options": ["Cod liver oil in water", "Shaving cream", "Pumice stone", "Smoke"],
        "ans": "A",
        "exp": "Cod liver oil dispersed in water is an emulsion (liquid dispersed in liquid)."
    },
    {
        "q": "A mixture of acetone (boiling point 56°C) and water (boiling point 100°C) is best separated by:",
        "options": ["Simple distillation", "Separating funnel", "Crystallization", "Filtration"],
        "ans": "A",
        "exp": "Acetone and water are miscible with a boiling point difference $> 25^\\circ\\text{C}$ (44°C difference), suitable for simple distillation."
    },
    {
        "q": "Which property indicates that air is a mixture rather than a chemical compound?",
        "options": [
            "Its composition varies with altitude and location",
            "Its components retain their individual chemical properties",
            "It can be separated by physical methods (liquefaction and fractional distillation)",
            "All of the above"
        ],
        "ans": "D",
        "exp": "Variable composition, retention of individual constituent properties, and physical separability are hallmarks of a mixture."
    },
    {
        "q": "What is the mass percentage of solute in a solution prepared by dissolving 25 g of glucose in 175 g of water?",
        "options": ["12.5%", "14.3%", "25.0%", "10.0%"],
        "ans": "A",
        "exp": "$\\text{Mass \\%} = \\frac{25}{25 + 175} \\times 100 = \\frac{25}{200} \\times 100 = 12.5\\%$."
    },
    {
        "q": "Which state of matter has neither definite shape nor definite volume, and consists of ionized gas at extremely high temperatures?",
        "options": ["Solid", "Liquid", "Gas", "Plasma"],
        "ans": "D",
        "exp": "Plasma is the fourth state of matter consisting of superheated ionized gas and free electrons (found in stars, lightning, neon tubes)."
    },
    {
        "q": "Bose-Einstein Condensate (BEC) is formed by:",
        "options": [
            "Heating gas to millions of degrees",
            "Cooling a gas of extremely low density to ultra-low temperatures near absolute zero",
            "Compressing liquid water to 10,000 atmospheres",
            "Subjecting solid ice to high voltage"
        ],
        "ans": "B",
        "exp": "BEC forms when a low-density boson gas is cooled to near absolute zero ($< 10^{-6}\\text{ K}$), collapsing atoms into a single quantum state."
    },
    {
        "q": "Which gas is evolved when pure iron sulfide (FeS) reacts with dilute sulfuric acid ($H_2SO_4$)?",
        "options": ["$H_2$", "$H_2S$ (Hydrogen sulfide)", "$SO_2$", "$O_2$"],
        "ans": "B",
        "exp": "$FeS + H_2SO_4 \\rightarrow FeSO_4 + H_2S \\uparrow$. Hydrogen sulfide smells like rotten eggs."
    },
    {
        "q": "Why does a diamond have an extremely high melting point (~3500°C) even though carbon is a non-metal?",
        "options": [
            "It has metallic bonding",
            "It consists of a 3D giant covalent network lattice where each carbon is tetrahedrally bonded to four others by strong covalent bonds",
            "It contains ionic calcium",
            "It is magnetic"
        ],
        "ans": "B",
        "exp": "Diamond's rigid 3D covalent network requires massive thermal energy to break strong $C-C$ covalent bonds."
    },
    {
        "q": "Which separation method separates blood proteins by utilizing an electric field?",
        "options": ["Centrifugation", "Gel Electrophoresis", "Chromatography", "Sublimation"],
        "ans": "B",
        "exp": "Gel electrophoresis separates charged biological macromolecules (proteins, DNA) based on molecular size and charge."
    },
    {
        "q": "What is the physical state of the dispersed phase and dispersion medium in butter?",
        "options": [
            "Dispersed phase: Liquid (water); Dispersion medium: Solid (fat)",
            "Dispersed phase: Solid; Dispersion medium: Liquid",
            "Both are gases",
            "Both are solids"
        ],
        "ans": "A",
        "exp": "Butter is a water-in-oil emulsion / gel where liquid water droplets are dispersed within solid fat matrix."
    },
    {
        "q": "Which of the following represents a purely physical change?",
        "options": ["Sublimation of camphor", "Digestion of starch by amylase", "Electrolysis of water into $H_2$ and $O_2$", "Burning of magnesium ribbon"],
        "ans": "A",
        "exp": "Sublimation changes only the physical state from solid to vapor without altering chemical composition."
    },
    {
        "q": "If 10 mL of alcohol is dissolved in 90 mL of water, the volume percentage concentration of alcohol is:",
        "options": ["10%", "11.1%", "9%", "100%"],
        "ans": "A",
        "exp": "$\\text{Volume \\%} = \\frac{10}{10 + 90} \\times 100 = \\frac{10}{100} \\times 100 = 10\\%$."
    },
    {
        "q": "Why is fractional crystallization effective for separating two soluble salts with different solubility curves?",
        "options": [
            "Because the less soluble salt crystallizes out first upon cooling, leaving the more soluble salt in the mother liquor",
            "Because one salt evaporates",
            "Because one salt becomes a gas",
            "Because of magnetic fields"
        ],
        "ans": "A",
        "exp": "Fractional crystallization exploits differential temperature-solubility coefficients to selectively harvest separate crystalline phases."
    },
    {
        "q": "Which colloid has solid as the dispersed phase and solid as the dispersion medium?",
        "options": ["Ruby glass / colored gemstones (Solid sol)", "Cheese", "Pumice", "Smoke"],
        "ans": "A",
        "exp": "Colored gemstone glasses and minerals are solid sols (solid particles dispersed in solid matrix)."
    }
]

CHAPTER_06_QUESTIONS = [
    {
        "q": "A constant net force of 12 N acts on a body of mass 3 kg initially at rest for 4 seconds. What is the final kinetic energy acquired by the body?",
        "options": ["96 J", "192 J", "384 J", "48 J"],
        "ans": "C",
        "exp": "$a = F/m = 12/3 = 4\\text{ m/s}^2$. Final velocity $v = at = 4 \\times 4 = 16\\text{ m/s}$. Kinetic energy $E_k = \\frac{1}{2}mv^2 = 0.5 \\times 3 \\times (16)^2 = 1.5 \\times 256 = 384\\text{ J}$."
    },
    {
        "q": "A machine gun fires 20 bullets per second, each of mass 30 g with muzzle velocity $500\\text{ m/s}$. What average backward force must the gunner exert to hold the gun stationary?",
        "options": ["150 N", "300 N", "600 N", "15 N"],
        "ans": "B",
        "exp": "Force $= \\frac{\\Delta p}{\\Delta t} = n \\times m \\times v = 20 \\times 0.030\\text{ kg} \\times 500\\text{ m/s} = 300\\text{ N}$."
    },
    {
        "q": "A body of mass $m$ strikes a rigid vertical wall perpendicularly with speed $v$ and rebounds elastically with the same speed $v$. What is the magnitude of the impulse imparted to the wall?",
        "options": ["0", "$mv$", "$2mv$", "$\\frac{1}{2}mv$"],
        "ans": "C",
        "exp": "Impulse $= |p_f - p_i| = |(-mv) - (+mv)| = 2mv$."
    },
    {
        "q": "A rocket of initial mass $M_0 = 1000\\text{ kg}$ expels exhaust gas at a constant velocity $u = 2000\\text{ m/s}$ relative to the rocket. What rate of fuel consumption ($dm/dt$) is required just to overcome Earth's gravity at liftoff ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["$4.9\\text{ kg/s}$", "$9.8\\text{ kg/s}$", "$2.45\\text{ kg/s}$", "$19.6\\text{ kg/s}$"],
        "ans": "A",
        "exp": "Thrust $F = u \\frac{dm}{dt} = M_0 g \\Rightarrow \\frac{dm}{dt} = \\frac{M_0 g}{u} = \\frac{1000 \\times 9.8}{2000} = 4.9\\text{ kg/s}$."
    },
    {
        "q": "Two masses $m_1 = 4\\text{ kg}$ and $m_2 = 6\\text{ kg}$ connected by a light string over a frictionless pulley (Atwood machine) are released. What is their common acceleration ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["$1.96\\text{ m/s}^2$", "$9.8\\text{ m/s}^2$", "$4.9\\text{ m/s}^2$", "$0.98\\text{ m/s}^2$"],
        "ans": "A",
        "exp": "$a = \\frac{m_2 - m_1}{m_1 + m_2} g = \\frac{6 - 4}{6 + 4} (9.8) = \\frac{2}{10} (9.8) = 1.96\\text{ m/s}^2$."
    },
    {
        "q": "A man of mass 70 kg stands on a weighing scale inside an elevator accelerating downwards at $2.8\\text{ m/s}^2$. What apparent weight is indicated by the scale ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["686 N", "490 N", "882 N", "196 N"],
        "ans": "B",
        "exp": "$N = m(g - a) = 70 \\times (9.8 - 2.8) = 70 \\times 7.0 = 490\\text{ N}$."
    },
    {
        "q": "What apparent weight does the same man experience if the elevator cable snaps and the elevator falls freely in free fall?",
        "options": ["686 N", "Zero (apparent weightlessness)", "490 N", "1372 N"],
        "ans": "B",
        "exp": "In free fall, $a = g \\Rightarrow N = m(g - g) = 0\\text{ N}$ (weightlessness)."
    },
    {
        "q": "A ball of mass 0.2 kg falling vertically from a height of 5 m rebounds to a height of 3.2 m after striking the floor. What is the impulse imparted by the floor ($g = 10\\text{ m/s}^2$)?",
        "options": ["$1.8\\text{ N}\\cdot\\text{s}$", "$3.6\\text{ N}\\cdot\\text{s}$", "$0.4\\text{ N}\\cdot\\text{s}$", "$2.0\\text{ N}\\cdot\\text{s}$"],
        "ans": "B",
        "exp": "Impact velocity $v_1 = \\sqrt{2gh_1} = \\sqrt{2 \\times 10 \\times 5} = 10\\text{ m/s}$ downward. Rebound velocity $v_2 = \\sqrt{2gh_2} = \\sqrt{2 \\times 10 \\times 3.2} = 8\\text{ m/s}$ upward. Impulse $= m(v_2 - (-v_1)) = 0.2 \\times (8 + 10) = 0.2 \\times 18 = 3.6\\text{ N}\\cdot\\text{s}$."
    },
    {
        "q": "A block of mass 10 kg resting on a rough horizontal floor ($\mu = 0.4$) is pulled with a horizontal force of 30 N. What is the acceleration of the block ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["$3.0\\text{ m/s}^2$", "$0\\text{ m/s}^2$", "$0.92\\text{ m/s}^2$", "$1.5\\text{ m/s}^2$"],
        "ans": "B",
        "exp": "Limiting static friction $f_s = \\mu N = 0.4 \\times (10 \\times 9.8) = 39.2\\text{ N}$. Since the applied force (30 N) is less than 39.2 N, the block does not move ($a = 0$)."
    },
    {
        "q": "Two bodies of masses 1 kg and 4 kg have equal kinetic energies. What is the ratio of their linear momentums ($p_1 : p_2$)?",
        "options": ["$1 : 4$", "$1 : 2$", "$2 : 1$", "$1 : 16$"],
        "ans": "B",
        "exp": "$p = \\sqrt{2m E_k}$. For equal $E_k$: $\\frac{p_1}{p_2} = \\sqrt{\\frac{m_1}{m_2}} = \\sqrt{\\frac{1}{4}} = \\frac{1}{2}$."
    },
    {
        "q": "Two bodies of masses 1 kg and 4 kg have equal linear momentums. What is the ratio of their kinetic energies ($E_{k1} : E_{k2}$)?",
        "options": ["$4 : 1$", "$1 : 4$", "$2 : 1$", "$1 : 2$"],
        "ans": "A",
        "exp": "$E_k = \\frac{p^2}{2m}$. For equal $p$: $\\frac{E_{k1}}{E_{k2}} = \\frac{m_2}{m_1} = \\frac{4}{1}$."
    },
    {
        "q": "A 1000 kg car travelling at $20\\text{ m/s}$ collides with a stationary 2000 kg truck and locks together. What is their common speed after the collision?",
        "options": ["$6.67\\text{ m/s}$", "$10.0\\text{ m/s}$", "$5.0\\text{ m/s}$", "$13.3\\text{ m/s}$"],
        "ans": "A",
        "exp": "$m_1 u_1 = (m_1 + m_2)V \\Rightarrow 1000 \\times 20 = (1000 + 2000)V \\Rightarrow 20000 = 3000 V \\Rightarrow V = 20/3 \\approx 6.67\\text{ m/s}$."
    },
    {
        "q": "What is the angle between action and reaction forces?",
        "options": ["0°", "90°", "180°", "45°"],
        "ans": "C",
        "exp": "Action and reaction forces act in exactly opposite directions along the same line of action (180°)."
    },
    {
        "q": "A water jet from a hose pipe of cross-section $10\\text{ cm}^2$ strikes a vertical wall normally at speed $15\\text{ m/s}$ and drops dead. What force does the water exert on the wall (density of water $= 1000\\text{ kg/m}^3$)?",
        "options": ["150 N", "225 N", "1500 N", "75 N"],
        "ans": "B",
        "exp": "$F = \\rho A v^2 = 1000\\text{ kg/m}^3 \\times (10 \\times 10^{-4}\\text{ m}^2) \\times (15\\text{ m/s})^2 = 1 \\times 225 = 225\\text{ N}$."
    },
    {
        "q": "A 2 kg stone is dropped from a balloon ascending at $5\\text{ m/s}$. At the instant of release, the stone's velocity is:",
        "options": ["Zero", "$5\\text{ m/s}$ upward", "$5\\text{ m/s}$ downward", "$9.8\\text{ m/s}$ downward"],
        "ans": "B",
        "exp": "Due to inertia of motion, the released stone inherits the balloon's instantaneous velocity of $5\\text{ m/s}$ upward."
    },
    {
        "q": "What is the kinetic energy of an object of momentum $p$ and mass $m$?",
        "options": ["$\\frac{p^2}{2m}$", "$\\frac{p}{2m}$", "$2mp$", "$\\frac{1}{2}mp^2$"],
        "ans": "A",
        "exp": "$E_k = \\frac{1}{2}mv^2 = \\frac{(mv)^2}{2m} = \\frac{p^2}{2m}$."
    },
    {
        "q": "An object of mass 5 kg moves in a horizontal circle of radius 2 m at a constant speed of $4\\text{ m/s}$. What is the net force acting on the object?",
        "options": ["Zero", "40 N towards the center", "20 N tangentially", "10 N outward"],
        "ans": "B",
        "exp": "$F_c = \\frac{m v^2}{r} = \\frac{5 \\times (4)^2}{2} = \\frac{5 \\times 16}{2} = 40\\text{ N}$ directed radially towards the center."
    },
    {
        "q": "If the earth suddenly shrinks to half its current radius with mass remaining constant, the value of acceleration due to gravity on its surface will become:",
        "options": ["Half", "Double", "4 times", "Same"],
        "ans": "C",
        "exp": "$g = \\frac{GM}{R^2}$. If $R \\rightarrow R/2$, $g' = \\frac{GM}{(R/2)^2} = 4g$."
    },
    {
        "q": "A cricket ball of mass 150 g moving at $20\\text{ m/s}$ is caught by a fielder in $0.1\\text{ s}$. The average force exerted on the fielder's hands is:",
        "options": ["30 N", "300 N", "3 N", "15 N"],
        "ans": "A",
        "exp": "$F = \\frac{\\Delta p}{\\Delta t} = \\frac{0.150\\text{ kg} \\times 20\\text{ m/s}}{0.1\\text{ s}} = \\frac{3.0}{0.1} = 30\\text{ N}$."
    },
    {
        "q": "Why does a swimming duck propel itself forward through water?",
        "options": [
            "It pushes water backward with webbed feet, and water pushes forward with an equal reaction force",
            "Water pulls the duck",
            "Gravity pushes it",
            "Air pushes it"
        ],
        "ans": "A",
        "exp": "Newton's third law: The backward force exerted by the feet on water produces an equal forward reaction push on the duck."
    },
    {
        "q": "If linear momentum of a body increases by 50%, what is the percentage increase in its kinetic energy?",
        "options": ["50%", "100%", "125%", "225%"],
        "ans": "C",
        "exp": "$E_k \\propto p^2$. If $p' = 1.5 p$, $E_k' = (1.5)^2 E_k = 2.25 E_k$. Percentage increase $= (2.25 - 1) \\times 100 = 125\\%$."
    },
    {
        "q": "A passenger sitting in an open railway carriage on a train moving with uniform velocity tosses a coin vertically upward. The coin lands:",
        "options": [
            "Exactly in his hand",
            "Behind him",
            "In front of him",
            "To the side"
        ],
        "ans": "A",
        "exp": "Due to inertia of motion, the coin maintains the forward horizontal velocity of the train and returns to the thrower's hand."
    },
    {
        "q": "What happens if the same coin is tossed while the train is accelerating forward?",
        "options": [
            "It falls behind his hand",
            "It falls in his hand",
            "It falls in front of his hand",
            "It floats mid-air"
        ],
        "ans": "A",
        "exp": "The train speeds up while the coin is in the air, leaving the coin to fall behind the passenger's hand."
    },
    {
        "q": "Two identical blocks of mass 5 kg each are connected by a cord on a frictionless table. A force of 20 N pulls the leading block. What is the tension in the connecting cord?",
        "options": ["20 N", "10 N", "5 N", "Zero"],
        "ans": "B",
        "exp": "System acceleration $a = \\frac{20}{5 + 5} = 2\\text{ m/s}^2$. Tension accelerates the trailing 5 kg mass: $T = m a = 5 \\times 2 = 10\\text{ N}$."
    },
    {
        "q": "Why do tires of automobiles have deep grooved treads?",
        "options": [
            "To look aesthetic",
            "To maintain optimum road grip by providing channels for rainwater evacuation, preventing hydroplaning skids",
            "To decrease fuel consumption",
            "To make the car lighter"
        ],
        "ans": "B",
        "exp": "Tread patterns channel water away from the contact patch, maintaining high static frictional grip on wet roads."
    }
]

CHAPTER_07_QUESTIONS = [
    {
        "q": "A variable force $F = 4x$ (in Newtons) acts on a particle, displacing it from $x = 0$ to $x = 3\\text{ m}$. What is the work done?",
        "options": ["12 J", "18 J", "36 J", "6 J"],
        "ans": "B",
        "exp": "$W = \\int_0^3 4x dx = [2x^2]_0^3 = 2(3)^2 = 2 \\times 9 = 18\\text{ J}$."
    },
    {
        "q": "A body of mass 1 kg is whirled in a vertical circle of radius 1 m. What is the minimum speed required at the top of the loop for the string not to go slack ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["$3.13\\text{ m/s}$", "$4.42\\text{ m/s}$", "$9.8\\text{ m/s}$", "$1.0\\text{ m/s}$"],
        "ans": "A",
        "exp": "$v_{top} = \\sqrt{gr} = \\sqrt{9.8 \\times 1} \\approx 3.13\\text{ m/s}$."
    },
    {
        "q": "What is the minimum speed required at the bottom of the vertical circle for the same body to complete the loop?",
        "options": ["$3.13\\text{ m/s}$", "$7.0\\text{ m/s}$", "$9.8\\text{ m/s}$", "$5.0\\text{ m/s}$"],
        "ans": "B",
        "exp": "$v_{bottom} = \\sqrt{5gr} = \\sqrt{5 \\times 9.8 \\times 1} = \\sqrt{49} = 7.0\\text{ m/s}$."
    },
    {
        "q": "A spring of spring constant $k = 200\\text{ N/m}$ is compressed by 10 cm ($0.10\\text{ m}$). What elastic potential energy is stored in the spring?",
        "options": ["1.0 J", "2.0 J", "10 J", "20 J"],
        "ans": "A",
        "exp": "$E_p = \\frac{1}{2} k x^2 = 0.5 \\times 200 \\times (0.10)^2 = 100 \\times 0.01 = 1.0\\text{ J}$."
    },
    {
        "q": "A crane lifts an 800 kg car vertically through 15 m in 20 seconds. What is the average power developed by the crane engine ($g = 9.8\\text{ m/s}^2$)?",
        "options": ["5880 W", "6000 W", "117.6 kW", "2940 W"],
        "ans": "A",
        "exp": "$P = \\frac{mgh}{t} = \\frac{800 \\times 9.8 \\times 15}{20} = \\frac{117600}{20} = 5880\\text{ W}$ ($5.88\\text{ kW}$)."
    },
    {
        "q": "An electric heater rated 1500 W operates 4 hours daily for 30 days. At a rate of ₹6.00 per unit (kWh), what is the monthly electricity cost?",
        "options": ["₹540", "₹1080", "₹720", "₹360"],
        "ans": "B",
        "exp": "Energy $= 1.5\\text{ kW} \\times 4\\text{ h} \\times 30 = 180\\text{ kWh}$. Cost $= 180 \\times 6 = \\text{₹}1080$."
    },
    {
        "q": "A bullet of mass 10 g moving at $400\\text{ m/s}$ penetrates 20 cm into a wooden target. What is the average resistive force exerted by the wood?",
        "options": ["4000 N", "8000 N", "2000 N", "800 N"],
        "ans": "A",
        "exp": "Work-energy theorem: $F \\times s = \\frac{1}{2}mv^2 \\Rightarrow F \\times 0.20 = 0.5 \\times 0.010 \\times (400)^2 = 0.005 \\times 160000 = 800\\text{ J} \\Rightarrow F = 800/0.20 = 4000\\text{ N}$."
    },
    {
        "q": "A block and tackle pulley system has 5 pulleys and an efficiency of 80%. What effort is required to lift a load of 1000 N?",
        "options": ["200 N", "250 N", "125 N", "500 N"],
        "ans": "B",
        "exp": "$\\text{VR} = 5$. $\\text{MA} = \\eta \\times \\text{VR} = 0.80 \\times 5 = 4.0$. Effort $= \\frac{\\text{Load}}{\\text{MA}} = \\frac{1000}{4.0} = 250\\text{ N}$."
    },
    {
        "q": "If the kinetic energy of a body becomes 9 times its initial value, what happens to its momentum?",
        "options": ["Triples (3 times)", "9 times", "81 times", "$\\sqrt{3}$ times"],
        "ans": "A",
        "exp": "$p = \\sqrt{2m E_k}$. If $E_k$ increases by 9 times, $p$ increases by $\\sqrt{9} = 3$ times."
    },
    {
        "q": "Work done by a centripetal force on an object moving along a curved circular path is always:",
        "options": ["Zero", "Positive", "Negative", "Variable"],
        "ans": "A",
        "exp": "Centripetal force is perpendicular to the displacement at every point along the circular trajectory ($W = 0$)."
    },
    {
        "q": "A simple pendulum released from an angle $\theta$ has mass $m$ and length $L$. What is the tension in the string at the lowest point if released from horizontal ($\theta = 90^\circ$)?",
        "options": ["$mg$", "$2mg$", "$3mg$", "$5mg$"],
        "ans": "C",
        "exp": "Velocity at bottom: $v = \\sqrt{2gL}$. Tension $T = mg + \\frac{mv^2}{L} = mg + \\frac{m(2gL)}{L} = 3mg$."
    },
    {
        "q": "Two bodies A and B of masses 2 kg and 8 kg have identical linear momentum. Which body has greater kinetic energy?",
        "options": [
            "Body A (lighter body)",
            "Body B (heavier body)",
            "Both have identical kinetic energy",
            "Neither has kinetic energy"
        ],
        "ans": "A",
        "exp": "$E_k = \\frac{p^2}{2m}$. For equal $p$, kinetic energy is inversely proportional to mass; the lighter mass has greater $E_k$."
    },
    {
        "q": "A pump can raise 7200 kg of water per hour to a height of 10 m. What is the power output of the pump ($g = 10\\text{ m/s}^2$)?",
        "options": ["200 W", "720 W", "2000 W", "72 kW"],
        "ans": "A",
        "exp": "$P = \\frac{mgh}{t} = \\frac{7200 \\times 10 \\times 10}{3600\\text{ s}} = 200\\text{ W}$."
    },
    {
        "q": "A lever of length 150 cm has its fulcrum at 30 cm from the load. What is its ideal mechanical advantage?",
        "options": ["5", "4", "0.25", "2"],
        "ans": "B",
        "exp": "Load arm $= 30\\text{ cm}$. Effort arm $= 150 - 30 = 120\\text{ cm}$. $\\text{MA} = \\frac{\\text{Effort arm}}{\\text{Load arm}} = \\frac{120}{30} = 4$."
    },
    {
        "q": "Which of the following is an example of non-conservative force?",
        "options": ["Gravitational force", "Kinetic friction force", "Electrostatic force", "Ideal spring restoring force"],
        "ans": "B",
        "exp": "Friction dissipates mechanical energy into heat; its work depends on path length, making it non-conservative."
    },
    {
        "q": "What power is required for an automobile of mass 1000 kg to climb a 1 in 20 incline at a constant speed of $15\\text{ m/s}$ (neglecting friction, $g = 9.8\\text{ m/s}^2$)?",
        "options": ["7350 W", "14700 W", "735 W", "9800 W"],
        "ans": "A",
        "exp": "$F = mg\\sin\\theta = 1000 \\times 9.8 \\times (1/20) = 490\\text{ N}$. Power $P = F v = 490 \\times 15 = 7350\\text{ W}$ ($7.35\\text{ kW}$)."
    },
    {
        "q": "When a force acts at an acute angle ($0 < \\theta < 90^\\circ$) to displacement, the work done is:",
        "options": ["Positive", "Negative", "Zero", "Maximum"],
        "ans": "A",
        "exp": "For $0 \\le \\theta < 90^\\circ$, $\\cos\\theta > 0$, making work done positive."
    },
    {
        "q": "A mass of 0.5 kg attached to a spring oscillates on a frictionless table with amplitude 0.2 m and spring constant $50\\text{ N/m}$. What is the maximum speed of the mass?",
        "options": ["$1.0\\text{ m/s}$", "$2.0\\text{ m/s}$", "$4.0\\text{ m/s}$", "$0.5\\text{ m/s}$"],
        "ans": "B",
        "exp": "$\\frac{1}{2}m v_{max}^2 = \\frac{1}{2}k A^2 \\Rightarrow v_{max} = A\\sqrt{k/m} = 0.2\\sqrt{50/0.5} = 0.2\\sqrt{100} = 0.2 \\times 10 = 2.0\\text{ m/s}$."
    },
    {
        "q": "The commercial energy consumption of a factory is 500 kWh. In Joules, this is:",
        "options": ["$1.8 \\times 10^9\\text{ J}$", "$5 \\times 10^5\\text{ J}$", "$3.6 \\times 10^6\\text{ J}$", "$1.8 \\times 10^6\\text{ J}$"],
        "ans": "A",
        "exp": "$500\\text{ kWh} = 500 \\times 3.6 \\times 10^6\\text{ J} = 1.8 \\times 10^9\\text{ J}$ (1.8 GigaJoules)."
    },
    {
        "q": "A body is moved along a closed loop back to its initial position in a gravitational field. Total work done by gravity is:",
        "options": ["Zero", "Positive", "Negative", "$mgh$"],
        "ans": "A",
        "exp": "Gravity is a conservative force; the net work done along any closed path is zero."
    },
    {
        "q": "What is the mechanical advantage of a pair of pliers used to cut wire if effort arm is 12 cm and load arm is 2 cm?",
        "options": ["6", "0.16", "24", "10"],
        "ans": "A",
        "exp": "$\\text{MA} = \\frac{\\text{Effort arm}}{\\text{Load arm}} = \\frac{12\\text{ cm}}{2\\text{ cm}} = 6$."
    },
    {
        "q": "A tennis ball dropped from 2.0 m rebounds to 1.28 m. What percentage of its mechanical energy was dissipated on impact?",
        "options": ["36%", "64%", "28%", "72%"],
        "ans": "A",
        "exp": "Energy retained $= \\frac{1.28}{2.00} = 64\\%$. Energy dissipated $= 100 - 64 = 36\\%$."
    },
    {
        "q": "A force $\\vec{F} = 3\\hat{i} + 4\\hat{j}\\text{ N}$ displaces an object through $\\vec{s} = 2\\hat{i} + 5\\hat{j}\\text{ m}$. What is the work done?",
        "options": ["26 J", "15 J", "7 J", "30 J"],
        "ans": "A",
        "exp": "$W = \\vec{F} \\cdot \\vec{s} = (3 \\times 2) + (4 \\times 5) = 6 + 20 = 26\\text{ J}$."
    },
    {
        "q": "What happens to the potential energy of a system when two like positive electric charges are brought closer together?",
        "options": ["Increases", "Decreases", "Remains constant", "Becomes zero"],
        "ans": "A",
        "exp": "Work must be done against electrostatic repulsive forces to bring like charges closer, increasing electrostatic potential energy."
    },
    {
        "q": "If an engine does 1000 J of useful work in 2 seconds, its power is:",
        "options": ["500 W", "2000 W", "250 W", "1000 W"],
        "ans": "A",
        "exp": "$P = W/t = 1000/2 = 500\\text{ W}$."
    }
]

CHAPTER_08_QUESTIONS = [
    {
        "q": "In Rutherford's alpha scattering experiment, what is the relationship between the number of scattered particles $N$ and scattering angle $\theta$?",
        "options": [
            "$N \\propto \\frac{1}{\\sin^4(\\theta/2)}$",
            "$N \\propto \\sin(\\theta/2)$",
            "$N \\propto \\frac{1}{\\cos^2\\theta}$",
            "$N \\propto \\theta^2$"
        ],
        "ans": "A",
        "exp": "Rutherford's classical scattering differential cross-section formula: $N(\\theta) \\propto \\csc^4(\\theta/2) = \\frac{1}{\\sin^4(\\theta/2)}$."
    },
    {
        "q": "What is the distance of closest approach ($d$) of an alpha particle of kinetic energy $E_k$ head-on to a gold nucleus ($Z = 79$)?",
        "options": [
            "$d = \\frac{1}{4\\pi\\varepsilon_0} \\frac{2 Z e^2}{E_k}$",
            "$d = \\frac{Z e^2}{E_k^2}$",
            "$d = \\frac{E_k}{Z e}$",
            "$d = 2 Z e E_k$"
        ],
        "ans": "A",
        "exp": "At closest approach, kinetic energy converts to electrostatic potential energy: $E_k = \\frac{1}{4\\pi\\varepsilon_0} \\frac{(2e)(Ze)}{d} \\Rightarrow d = \\frac{1}{4\\pi\\varepsilon_0} \\frac{2Ze^2}{E_k}$."
    },
    {
        "q": "According to Bohr's postulate, what is the quantized orbital angular momentum ($L$) of an electron in the $n$-th shell?",
        "options": [
            "$L = \\frac{n h}{2\\pi}$",
            "$L = n h \\pi$",
            "$L = \\frac{h}{2\\pi n}$",
            "$L = n^2 h$"
        ],
        "ans": "A",
        "exp": "Bohr's quantum condition: Angular momentum is an integral multiple of $h/2\\pi$ ($mvr = \\frac{nh}{2\\pi}$)."
    },
    {
        "q": "What is the wavelength ($\lambda$) of radiation emitted when an electron jumps from higher energy $E_2$ to lower energy $E_1$ ($h$ is Planck's constant, $c$ is speed of light)?",
        "options": [
            "$\\lambda = \\frac{h c}{E_2 - E_1}$",
            "$\\lambda = \\frac{E_2 - E_1}{h c}$",
            "$\\lambda = h(E_2 - E_1)$",
            "$\\lambda = \\frac{c}{E_2 - E_1}$"
        ],
        "ans": "A",
        "exp": "$\\Delta E = E_2 - E_1 = h\\nu = \\frac{hc}{\\lambda} \\Rightarrow \\lambda = \\frac{hc}{E_2 - E_1}$."
    },
    {
        "q": "How many neutrons are present in the nucleus of a neutral atom of Thorium-232 ($^{232}_{90}Th$)?",
        "options": ["90", "142", "232", "322"],
        "ans": "B",
        "exp": "Number of neutrons $N = A - Z = 232 - 90 = 142$."
    },
    {
        "q": "An atom has 15 protons, 16 neutrons, and 18 electrons. What is the identity and charge of this species?",
        "options": [
            "Phosphide anion ($P^{3-}$)",
            "Phosphorus neutral atom ($P$)",
            "Sulfur cation ($S^{2+}$)",
            "Argon atom ($Ar$)"
        ],
        "ans": "A",
        "exp": "$Z = 15$ identifies Phosphorus. It has 3 extra electrons ($18 - 15 = 3$), giving a trivalent anion $P^{3-}$."
    },
    {
        "q": "Which pair represents isobars?",
        "options": [
            "$^{40}_{18}Ar$ and $^{40}_{20}Ca$",
            "$^{12}_6C$ and $^{14}_6C$",
            "$^1_1H$ and $^2_1H$",
            "$^{35}_{17}Cl$ and $^{37}_{17}Cl$"
        ],
        "ans": "A",
        "exp": "Isobars have different atomic numbers but identical mass numbers ($A = 40$ in Argon and Calcium)."
    },
    {
        "q": "Which pair represents isotones (atoms having identical numbers of neutrons)?",
        "options": [
            "$^{14}_6C$ and $^{16}_8O$",
            "$^{12}_6C$ and $^{14}_7N$",
            "$^{40}_{18}Ar$ and $^{40}_{20}Ca$",
            "$^1_1H$ and $^2_1H$"
        ],
        "ans": "A",
        "exp": "In $^{14}_6C$, $N = 14 - 6 = 8$. In $^{16}_8O$, $N = 16 - 8 = 8$. Identical neutron count defines isotones."
    },
    {
        "q": "Naturally occurring boron consists of two isotopes: $^{10}B$ (mass 10 u) and $^{11}B$ (mass 11 u). If average atomic mass is 10.8 u, what is the abundance of $^{10}B$?",
        "options": ["20%", "80%", "50%", "10%"],
        "ans": "A",
        "exp": "$10 x + 11(1 - x) = 10.8 \\Rightarrow 10x + 11 - 11x = 10.8 \\Rightarrow 11 - x = 10.8 \\Rightarrow x = 0.20 = 20\\%$."
    },
    {
        "q": "What is the maximum number of electrons in an atom that can have principal quantum number $n = 4$?",
        "options": ["16", "32", "18", "64"],
        "ans": "B",
        "exp": "Capacity $= 2n^2 = 2(4)^2 = 2 \\times 16 = 32$ electrons."
    },
    {
        "q": "Which isotope is used in carbon dating to estimate the archaeological age of ancient wooden fossils?",
        "options": ["$^{14}C$", "$^{12}C$", "$^{13}C$", "$^{16}O$"],
        "ans": "A",
        "exp": "Carbon-14 ($^{14}C$) is a beta-emitting radioactive isotope with a half-life of 5,730 years used in radiocarbon dating."
    },
    {
        "q": "Why does a hydrogen atom ($Z=1$) exhibit multiple distinct spectral emission lines in its absorption/emission spectrum?",
        "options": [
            "A hydrogen atom contains multiple electrons",
            "A sample contains billions of hydrogen atoms where single electrons transition between multiple quantized energy levels ($n=1, 2, 3, 4...$)",
            "Hydrogen splits into protons",
            "Hydrogen has isotopes only"
        ],
        "ans": "B",
        "exp": "Different atoms in the macroscopic gas sample undergo electronic transitions across different energy levels, producing distinct spectral lines."
    },
    {
        "q": "What is the charge and mass of an electron in SI units?",
        "options": [
            "$-1.602 \\times 10^{-19}\\text{ C}$, $9.109 \\times 10^{-31}\\text{ kg}$",
            "$+1.602 \\times 10^{-19}\\text{ C}$, $1.672 \\times 10^{-27}\\text{ kg}$",
            "Zero, $9.109 \\times 10^{-31}\\text{ kg}$",
            "$-1.602 \\times 10^{-19}\\text{ C}$, $1.675 \\times 10^{-27}\\text{ kg}$"
        ],
        "ans": "A",
        "exp": "An electron has fundamental negative charge $e = -1.602 \\times 10^{-19}$ C and rest mass $9.109 \\times 10^{-31}$ kg."
    },
    {
        "q": "What is the valency of Silicon ($Z = 14$, config $2, 8, 4$)?",
        "options": ["4", "2", "6", "8"],
        "ans": "A",
        "exp": "Silicon shares 4 valence electrons to complete its octet, exhibiting a valency of 4 (tetravalent)."
    },
    {
        "q": "What is the chemical formula of Aluminum Sulfate (Aluminum valency 3, Sulfate radical $SO_4^{2-}$ valency 2)?",
        "options": ["$AlSO_4$", "$Al_2(SO_4)_3$", "$Al_3(SO_4)_2$", "$Al_2SO_4$"],
        "ans": "B",
        "exp": "Criss-crossing valencies ($Al^{3+}$ and $SO_4^{2-}$) gives $Al_2(SO_4)_3$."
    },
    {
        "q": "What is the chemical formula of Ammonium Carbonate (Ammonium $NH_4^+$, Carbonate $CO_3^{2-}$)?",
        "options": ["$(NH_4)_2CO_3$", "$NH_4(CO_3)_2$", "$NH_4CO_3$", "$N_2H_8CO_3$"],
        "ans": "A",
        "exp": "Criss-crossing valencies ($NH_4^{1+}$ and $CO_3^{2-}$) gives $(NH_4)_2CO_3$."
    },
    {
        "q": "Which subatomic particle has approximately zero rest mass and zero charge, and was postulated by Wolfgang Pauli to conserve energy in beta decay?",
        "options": ["Neutrino ($\\nu$)", "Neutron", "Positron", "Proton"],
        "ans": "A",
        "exp": "Neutrinos are neutral leptons with near-zero rest mass emitted during radioactive beta decay."
    },
    {
        "q": "The radius of an atomic nucleus of mass number $A$ is proportional to:",
        "options": ["$A^{1/3}$", "$A^3$", "$A$", "$A^{1/2}$"],
        "ans": "A",
        "exp": "Nuclear radius $R = R_0 A^{1/3}$, where $R_0 \\approx 1.2 \\times 10^{-15}\\text{ m}$ (1.2 fermi)."
    },
    {
        "q": "What is the mass defect in a nuclear reaction?",
        "options": [
            "Difference between total mass of constituent nucleons and actual bound nuclear mass ($E = \\Delta m c^2$)",
            "Instrumental scale error",
            "Mass of lost electrons",
            "Weight of neutrons"
        ],
        "ans": "A",
        "exp": "Mass defect $\\Delta m$ represents binding energy released when protons and neutrons bind to form a nucleus."
    },
    {
        "q": "Which element has atomic number 19 and config $2, 8, 8, 1$?",
        "options": ["Potassium ($K$)", "Sodium ($Na$)", "Calcium ($Ca$)", "Argon ($Ar$)$"],
        "ans": "A",
        "exp": "Potassium ($K$, $Z = 19$) has 19 electrons arranged as $2, 8, 8, 1$."
    },
    {
        "q": "Why is the average atomic mass of a chemical element rarely an exact whole number integer?",
        "options": [
            "Because mass of an electron fluctuates",
            "Because natural elements exist as mixtures of isotopes with different mass numbers in varying percentage abundances",
            "Because measuring balances are inaccurate",
            "Because neutrons dissolve"
        ],
        "ans": "B",
        "exp": "Weighted averaging across multiple isotopic fractions yields fractional atomic weights (e.g., Cl = 35.5 u)."
    },
    {
        "q": "Which isotope of hydrogen is radioactive and decays by beta emission?",
        "options": ["Tritium ($^3_1H$)", "Protium ($^1_1H$)", "Deuterium ($^2_1H$)", "All isotopes"],
        "ans": "A",
        "exp": "Tritium ($^3_1H$) has 1 proton and 2 neutrons ($N/Z = 2$), making it an unstable beta-emitter with half-life 12.3 years."
    },
    {
        "q": "What is heavy water chemically?",
        "options": ["Deuterium oxide ($D_2O$ or $^2H_2O$)", "Water saturated with salt", "Water under 100 atmospheres", "Hydrogen peroxide ($H_2O_2$)"],
        "ans": "A",
        "exp": "Heavy water is deuterium oxide ($D_2O$), where hydrogen is replaced by its heavier isotope deuterium ($^2_1H$)."
    },
    {
        "q": "What did J.J. Thomson's 'plum pudding' model fail to explain?",
        "options": [
            "Large angle deflections of alpha particles in Rutherford's scattering experiment",
            "Electrical neutrality of atoms",
            "Presence of electrons",
            "Mass of atoms"
        ],
        "ans": "A",
        "exp": "Thomson's diffuse positive cloud could not exert the concentrated Coulomb repulsion required to deflect alpha particles at large angles."
    },
    {
        "q": "Which quantum energy state corresponds to the lowest possible energy configuration of an electron in an atom?",
        "options": ["Ground state ($n=1$)", "Excited state", "Ionized state", "Stationary transition"],
        "ans": "A",
        "exp": "The ground state ($n=1$, K-shell) is the lowest energy, thermodynamically most stable electronic state."
    }
]
