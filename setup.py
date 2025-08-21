from setuptools import setup, find_packages

setup(
    name="fdl_metacore",
    version="1.0.0",
    description="Σ-FDL::MetaCore — Resonant Framework for Agentic Intelligence",
    author="Fravahr Ormazd",
    author_email="ngoisigma@gmail.com",
    url="https://github.com/NgoiSigma/FDL-MetaCore",
    packages=find_packages(),
    install_requires=[
        "openai>=1.3.0",
        "streamlit>=1.34.0",
        "python-telegram-bot>=20.0",
        "rich>=13.0.0",
        "typer>=0.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)
