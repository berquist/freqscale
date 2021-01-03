from templates import header_gaussian, molecule_blocks


def write_output_gaussian(name: str, method: str, basis: str, path: str) -> None:
    with open(f"{name}.in", "w") as fh:
        molecule = molecule_blocks[name]
        fh.write(header)
        fh.write(f"{method}/{basis}\n")
        fh.write("\nt\n\n")
        fh.write(f"{molecule['charge']},{molecule['multiplicity']}\n")
        fh.write(molecule["block"])
        fh.write(f"\n{path}\n")
        fh.write("\n")

def write_output_qchem(name: str, method: str, basis: str, path: str) -> None:
    molecule = molecule_blocks[name]
    inp = f"""$rem
jobtype = opt
method = {method}
basis = {basis}
mem_static = 1000
mem_total = 4000
geom_opt_tol_energy = 1
geom_opt_tol_gradient = 40
$end

$molecule
{molecule['charge']} {molecule['multiplicity']}

{molecule['block']}
$end

@@@@

$rem
jobtype = freq
method = {method}
basis = {basis}
mem_static = 1000
mem_total = 4000
$end

$molecule
read
$end
"""
    with open(f"{name}.in", "w") as fh:
        fh.write(inp)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("program", choices=("gaussian", "qchem"))
    parser.add_argument("method")
    parser.add_argument("basisset")
    parser.add_argument("--basisset-path", default="")
    args = parser.parse_args()

    # TODO use pnictogen
    if args.program == "gaussian":
        writer = write_output_gaussian
    elif args.program == "qchem":
        writer = write_output_qchem

    for name in molecule_blocks:
        writer(name, args.method, args.basisset, args.basisset_path)
