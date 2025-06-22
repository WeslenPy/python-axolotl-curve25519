from setuptools import setup, Extension
from glob import glob

sources = [
    "curve25519module.c",
    "curve/curve25519-donna.c",
    *glob("curve/ed25519/*.c"),
    *glob("curve/ed25519/additions/*.c"),
    *glob("curve/ed25519/nacl_sha512/*.c"),
]

include_dirs = [
    "curve/ed25519/nacl_includes",
    "curve/ed25519/additions",
    "curve/ed25519"
]

compile_args = ["-march=native", "-O3", "-msse", "-msse2", "-mfma", "-mfpmath=sse"]

extensions = [
    Extension(
        name="axolotl_curve25519",
        sources=sources,
        include_dirs=include_dirs,
        extra_compile_args=compile_args,
        libraries=["m"],
    )
]

setup(
    name="python-axolotl-curve25519",
    version="1.0.2",
    author="Tarek Galal",
    author_email="tare2.galal@gmail.com",
    description="curve25519 with ed25519 signatures, used by libaxolotl",
    license="GPLv3",
    install_requires=[
        "setuptools>=71.0.4"
    ],
    ext_modules = [extensions],
)
