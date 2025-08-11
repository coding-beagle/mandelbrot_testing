from setuptools import setup

setup(
    name="MandelTest",
    version="0.1",
    description="A sample Python package",
    author="coding-beagle",
    author_email="nicholasp.teague@gmail.com",
    packages=["MandelTest"],
    install_requires=["Click", "opencv-python", "numpy"],
    extras_require={
        "dev": ["pytest", "pytest-cov", "wheel"],
        "test": ["pytest", "pytest-cov"],
    },
    entry_points="""
        [console_scripts]
        mt=mandeltest.__main__:cli
    """,
)
