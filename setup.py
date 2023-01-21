import cx_Freeze
from os import walk, path

exes = [cx_Freeze.Executable("main.py")]
includes = []
for root, d_names, f_names in walk("assets", True, None):
    for f in f_names:
        includes.append(path.join(root, f))

cx_Freeze.setup(
    name = "Catch the Primes",
    options={
        "build_exe": {
            "packages":["pygame", "stopwatch", "prime_sieve", "components.ui", "components.particleFx", "components.defaults", "components.ball"],
        },
    },
    executables = exes
)