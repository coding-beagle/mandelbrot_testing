from setuptools import setup

setup(
    name="Module",
    version="0.1",
    description="A sample Python package",
    author="coding-beagle",
    author_email="nicholasp.teague@gmail.com",
    packages=["Module"],
    install_requires=["Click"],
    extras_require={
        "dev": ["pytest", "pytest-cov", "wheel"],
        "test": ["pytest", "pytest-cov"],
    },
    entry_points="""
        [console_scripts]
        module=module.__main__:cli
    """,
)
