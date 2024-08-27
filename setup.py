from setuptools import setup, find_packages

install_requires = []
with open("requirements.txt", encoding="utf-8") as requirements_file:
    reqs = [r.strip() for r in requirements_file.readlines()]
    reqs = [r for r in reqs if r and r[0] != "#"]
    install_requires.extend(reqs)

setup(
    name="rope-assimetric",
    version="0.1",
    packages=find_packages(),  # Automatically finds all packages and subpackages
    install_requires=install_requires,  # Use the requirements from requirements.txt
    url='https://github.com/JPSchettino/rope-assimetric/',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
