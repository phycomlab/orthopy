import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "orthopy", "__about__.py"), "rb") as f:
    exec(f.read(), about)


setup(
    name="orthopy",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/orthopy",
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=["numpy", "sympy"],
    extras_require={
        "all": ["matplotlib", "meshio", "meshzoo", "dmsh", "cplot"],
        "disk-plot": ["dmsh"],
        "plot": ["matplotlib"],
        "sphere-plot": ["meshzoo", "meshio", "cplot"],
    },
    description="Tools for orthogonal polynomials, Gaussian quadrature",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
