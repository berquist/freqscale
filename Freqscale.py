import json
from pathlib import Path
from typing import Iterable, Tuple

import numpy as np

from cclib.io import ccread
from cclib.parser.utils import convertor

_SCALE_ZPE = 1.0
_SCALE_HARM = 1.014
_SCALE_FUND = 0.974

COMPUTED_DATA_FILENAME = "computed_data.json"


def extract_and_dump_computed_data(systems: Iterable[str]) -> None:
    with open(COMPUTED_DATA_FILENAME, "w") as fh:
        json.dump(
            {system: extract_computed_zpe(f"{system}.out") for system in systems}, fh
        )


def extract_computed_zpe(filename: str) -> float:
    """Get the computed ZPVE from the given quantum chemical output filename in
    units of kcal/mol.
    """
    return convertor(ccread(filename).zpve, "hartree", "kcal/mol")


def calculate_lambda(
    experimental_zpves: Iterable[float], computed_zpves: Iterable[float]
) -> float:
    return np.dot(experimental_zpves, computed_zpves) / np.sum(
        np.asanyarray(computed_zpves) ** 2.0
    )


def form_scaling_factors(lmbda: float) -> Tuple[float, float, float]:
    return lmbda * _SCALE_ZPE, lmbda * _SCALE_HARM, lmbda * _SCALE_FUND


def format_output(scaling_factors: Tuple[float, float, float]) -> str:
    return "\n".join(
        [
            "FREQ: A PROGRAM FOR OPTIMIZING SCALE FACTORS (Version 1",
            "                 written by                 ",
            "Haoyu S. Yu, Lucas J. Fiedler, I.M. Alecu, and Donald G. Truhlar",
            "Department of Chemistry and Supercomputing Institute",
            "University of Minnesota, Minnesota 55455-0431",
            f"Scale Factor for Zero-Point Energies     = {scaling_factors[0]}",
            f"Scale Factor for Harmonic Frequencies    = {scaling_factors[1]}",
            f"Scale Factor for Fundamental Frequencies = {scaling_factors[2]}",
            "CITATIONS:",
            "1. Alecu, I.M., Zheng, J., Zhao, Y., and Truhlar, D.G. J. Chem. Theory Comput. 2010, 6, 2872",
            "2. Yu, S.H., Fiedler, L.J., Alecu, I.M., and Truhlar, D.G. Comput. Phys.Commun. submittted 2016",
        ]
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("dump", "compute"))
    parser.add_argument("model_type", choices=("full", "reduced"))
    args = parser.parse_args()

    systems = json.loads(Path(f"molecules_{args.model_type}.json").read_text())

    if args.action == "dump":
        extract_and_dump_computed_data(systems)
    elif args.action == "compute":
        all_experimental_zpves = json.loads(Path("experimental_data.json").read_text())
        used_experimental_zpves = [all_experimental_zpves[system] for system in systems]
        all_computed_zpves = json.loads(Path(COMPUTED_DATA_FILENAME).read_text())
        used_computed_zpves = [all_computed_zpves[system] for system in systems]

        lmbda = calculate_lambda(used_experimental_zpves, used_computed_zpves)
        scaling_factors = form_scaling_factors(lmbda)
        # scale_zpe, scale_harm, scale_fund = scaling_factors
        print(format_output(scaling_factors))
