from setuptools import setup, find_packages

setup(
    name="agentar",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "antlr4-python3-runtime>=4.9.3",
        "rich>=13.0.0",
        "numpy>=1.21.0",
        "antlr4-tools==0.2.2",
        "psutil>=5.8.0",
    ],
    entry_points={
        "console_scripts": [
            "agentar = cli:main",  # Komenda 'agentar' będzie wywoływać funkcję main() z cli.py
        ],
    },
    python_requires=">=3.8",
)