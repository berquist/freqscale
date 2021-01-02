# This program is used to generate gaussian input files for the full model (with 15 molecules)

# read in functional, basis set, and path of the basis set
functional = str(input("Which method are you going to choose? "))
basis = str(input("Which basis set are you going to choose? "))
path = str(input("What is the path of your basis set? "))

from templates import header, molecule_blocks

def generate_output(name: str, basis: str, path: str) -> None:
    with open(f"{name}.in", "w") as fh:
        fh.write(header)
        fh.write(f"{functional}/{basis}\n")
        fh.write("\nt\n\n")
        fh.write(molecule_blocks[name])
        fh.write(f"\n{path}\n")
        fh.write("\n")

for name in molecule_blocks:
    generate_output(name, basis, path)
