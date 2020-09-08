import setuptools


def get_long_desc():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


setuptools.setup(
    name="general_methods",
    version="0.0.1",
    author="Vishal Anand",
    author_email="vishalanandl177@gmail.com",
    description="A small general methods.",
    long_description=get_long_desc(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    license='GNU General Public License v3.0',
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
