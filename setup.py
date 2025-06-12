from setuptools import setup, find_packages

setup(
    name='pec4',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    	"pandas",
		"matplotlib",
		"setuptools",
        "DateTime",
        "scipy",
        "pytest",
        "pytest-cov",
        "pylint",
        "pdoc3",
    ],
    author='Lia Diaz Jimenez',
    python_requires='>=3.12',
)