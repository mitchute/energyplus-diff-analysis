from pathlib import Path

from setuptools import setup

from energyplus_diffs import VERSION

readme_file = Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="energyplus_diff_analysis",
    version=VERSION,
    packages=['energyplus_diffs'],
    description="A tool used for plotting and comparing separate EnergyPlus output CSV files.",
    install_requires=['click', 'matplotlib', 'pandas'],
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Matt Mitchell',
    author_email='mitchute@gmail.com',
    url='https://github.com/mitchute/energyplus-diff-analysis',
    license='MIT License',
    entry_points={
        'console_scripts': ['energyplus_diffs=energyplus_diffs.cli:cli']
    }
)
