from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).resolve().parent

readme = (HERE / 'README.rst').read_text("utf-8")

setup(
    author="Brénainn Woodsend",
    author_email='bwoodsend@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description=
    "A mind-numbingly simple wrapper around the plotly javascript library.",
    install_requires=[],
    extras_require={
        "test": ['pytest>=3', 'pytest-order', 'coverage', 'pytest-cov']
    },
    license="MIT license",
    long_description=readme,
    keywords='peccary',
    name='peccary',
    packages=find_packages(include=['peccary', 'peccary.*']),
    url='https://github.com/bwoodsend/peccary',
    version="0.1.0",
)
