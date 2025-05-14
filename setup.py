"""Installation script for the 'factoryIsaac' Python package."""

from setuptools import setup

# Package metadata (hardcoded)
PACKAGE_NAME = "isaacWork"
VERSION = "0.1.0"
AUTHOR = "hdh"
MAINTAINER = "zhiyuan"
MAINTAINER_EMAIL = "xiangkonyue@gmail.com"
DESCRIPTION = "Manipulation Extension Template for isaacLab"
REPOSITORY = ""
KEYWORDS = ["extension", "isaacLab"]

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "psutil",  # NOTE: Add additional dependencies here
]

# Setup the package installation
setup(
    # Package name and metadata
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    keywords=KEYWORDS,
    url=REPOSITORY,
    license="BSD-3-Clause",
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
    packages=[PACKAGE_NAME],  # Package directory
)
