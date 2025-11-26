from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="yanami_sisters",   # pip install 時に使う名前
    version="0.1.0",
    description="To create synthetic voice",
    long_description=long_description,
    long_description_content_type="text/markdown",  # PyPIでREADMEをMarkdown表示
    author="neutrino-dot",
    license="MIT",
    url="https://github.com/neutrino-dot/yanami_sisters",  # GitHub リポジトリ
    project_urls={
        "Source Code": "https://github.com/neutrino-dot/yanami_sisters"
    },
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
    ],
)