def calculate_molecular_mass():
    elements = {
        "hydrogen": 1.008, "helium": 4.003, "lithium": 6.941, "beryllium": 9.012,
        "boron": 10.811, "carbon": 12.011, "nitrogen": 14.007, "oxygen": 15.999,
        "fluorine": 18.998, "neon": 20.180, "sodium": 22.990, "magnesium": 24.305,
        "aluminum": 26.982, "silicon": 28.086, "phosphorus": 30.974, "sulfur": 32.065,
        "chlorine": 35.453, "argon": 39.948, "potassium": 39.098, "calcium": 40.078,
        "scandium": 44.956, "titanium": 47.867, "vanadium": 50.942, "chromium": 51.996,
        "manganese": 54.938, "iron": 55.845, "cobalt": 58.933, "nickel": 58.693,
        "copper": 63.546, "zinc": 65.380, "gallium": 69.723, "germanium": 72.640,
        "arsenic": 74.922, "selenium": 78.960, "bromine": 79.904, "krypton": 83.800,
        "rubidium": 85.468, "strontium": 87.620, "yttrium": 88.906, "zirconium": 91.224,
        "niobium": 92.906, "molybdenum": 95.940, "technetium": 98.000, "ruthenium": 101.070,
        "rhodium": 102.906, "palladium": 106.420, "silver": 107.868, "cadmium": 112.411,
        "indium": 114.818, "tin": 118.710, "antimony": 121.760, "tellurium": 127.600,
        "iodine": 126.905, "xenon": 131.293, "cesium": 132.906, "barium": 137.327,
        "lanthanum": 138.906, "cerium": 140.116, "praseodymium": 140.908, "neodymium": 144.240,
        "promethium": 145.000, "samarium": 150.360, "europium": 151.964, "gadolinium": 157.250,
        "terbium": 158.925, "dysprosium": 162.500, "holmium": 164.930, "erbium": 167.259,
        "thulium": 168.934, "ytterbium": 173.040, "lutetium": 174.967, "hafnium": 178.490,
        "tantalum": 180.948, "tungsten": 183.840, "rhenium": 186.207, "osmium": 190.230,
        "iridium": 192.217, "platinum": 195.078, "gold": 196.967, "mercury": 200.590,
        "thallium": 204.383, "lead": 207.200, "bismuth": 208.980, "polonium": 209.000,
        "astatine": 210.000, "radon": 222.000, "francium": 223.000, "radium": 226.000,
        "actinium": 227.000, "thorium": 232.038, "protactinium": 231.036, "uranium": 238.029,
        "neptunium": 237.000, "plutonium": 244.000, "americium": 243.000, "curium": 247.000,
        "berkelium": 247.000, "californium": 251.000, "einsteinium": 252.000, "fermium": 257.000,
        "mendelevium": 258.000, "nobelium": 259.000, "lawrencium": 262.000, "rutherfordium": 267.000,
        "dubnium": 268.000, "seaborgium": 271.000, "bohrium": 272.000, "hassium": 270.000,
        "meitnerium": 276.000, "darmstadtium": 281.000, "roentgenium": 280.000, "copernicium": 285.000,
        "nihonium": 284.000, "flerovium": 289.000, "moscovium": 288.000, "livermorium": 293.000,
        "tennessine": 294.000, "oganesson": 294.000,
    }
    
    molecule = []
    total_mass = 0
    
    # Get number of elements in the compound
    num_elements = int(input("How many different elements does your compound have? "))
    
    # Gather information about each element in the molecule
    for i in range(num_elements):
        element_name = input(f"Enter element #{i+1} name: ").lower()
        
        # Validate element name
        if element_name not in elements:
            print(f"Error: {element_name} is not a valid element name.")
            continue
            
        num_atoms = int(input(f"Enter the number of {element_name} atoms: "))
        
        # Calculate the mass contribution of this element
        element_mass = elements[element_name] * num_atoms
        total_mass += element_mass
        
        # Store the element information
        molecule.append({"element": element_name, "atoms": num_atoms, "mass": element_mass})
    
    # Display the molecule information
    print("\nMolecule composition:")
    for item in molecule:
        print(f"{item['element'].capitalize()}: {item['atoms']} atoms × {elements[item['element']]} u = {item['mass']} u")
    
    print(f"\nTotal molecular mass: {total_mass} u")
    
    # Calculate moles if needed
    calculate_moles = input("\nDo you want to calculate moles from mass? (yes/no): ").lower()
    if calculate_moles == "yes":
        mass_of_substance = float(input("Enter the mass of the substance in grams: "))
        moles = mass_of_substance / total_mass
        print(f"Number of moles: {moles} mol")
        
        # Calculate number of molecules
        avogadro = 6.022e23
        molecules = moles * avogadro
        print(f"Number of molecules: {molecules:.4e}")

if __name__ == "__main__":
    print("Molecular Mass Calculator")
    print("-------------------------")
    calculate_molecular_mass()