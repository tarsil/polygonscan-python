from setuptools import setup

setup(
    name="polygonscan-python",
    version="1.0.2",
    description="A minimal, complete, python API for polygonscan.com.",
    url="https://github.com/tarsil/polygonscan-python",
    author="Tiago A. Silva",
    license="MIT",
    packages=[
        "polygonscan",
        "polygonscan.configs",
        "polygonscan.core",
        "polygonscan.enums",
        "polygonscan.modules",
        "polygonscan.utils",
    ],
    python_requires='>=3.8',
    install_requires=["aiohttp", "requests"],
    include_package_data=True,
    zip_safe=False,
)
