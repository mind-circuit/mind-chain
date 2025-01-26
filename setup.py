import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mind-chain",
    version="0.2.0",
    author="Mind Circuit",
    author_email="info@mindcircuit.example",
    description="A bridging framework integrating Sui Move contracts with Cosmos-based PoA and AI logic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YourOrg/mind_chain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        # Basic or additional libraries can be included or rely on requirements.txt
    ],
)
