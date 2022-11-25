from santa.assign import santa, validate
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument(
    "--seed",
    type=str,
    help="Seed for the randomization. If no seed is provided, current time is used.",
)
parser.add_argument(
    "names", nargs="+", type=str, help="Names of the people to assign as Santas."
)

args = parser.parse_args()
if args.seed is None or len(args.seed) < 1:
    random.seed()
else:
    random.seed(args.seed)

pairs = santa(args.names)
for name, assigned in pairs.items():
    print(name, "->", assigned)
if not validate(pairs):
    raise RuntimeError("Failed to generate valid pairs.")
