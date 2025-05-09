from setuptools import setup, find_packages

setup(
    name="agentar",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "antlr4-python3-runtime>=4.9.3",
    ],
    entry_points={
        "console_scripts": [
            "agentar = agentar:main",  # Komenda 'agentar' będzie wywoływać funkcję main() z agenter.py
        ],
    },
    python_requires=">=3.8",
)