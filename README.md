# CS426 Project

## Our Project

With diabetes prevalence on the rise, it's essential that we identify demographic and behavioral indicators for early and accurate screenings. Our project utilizes NHANES 2021-23 data to identify strong predictors for diabetes. In this project we use a mixture of machine learning models and feature selection to not only predict diabetes, but also to find the most influential features driving those predictions.

## Installation Instructions

Git clone the repository and install the requirements:

```bash
# Clone the repository and enter the repo
git clone https://github.com/pisaucer/cs426-project.git
cd cs426-project

# Setup Python environment and install requirements
python3 -m venv ./.venv
chmod +x ./.venv/bin/activate
source ./.venv/bin/activate
pip install -r requirements.txt
```

### Use Instructions

Open the notebook:

```bash
jupyter notebook diabetes.ipynb
```

## Files

- [`all_data`](all_data/): Contains all the non-diabetes NHANES datasets.
- [`cleaned`](cleaned/): Contains a cleaned version of the diabetes dataset.
- [`diabetes_data`](diabetes_data/): Contains the NHANES diabetes dataset as both a `.xpt` and `.csv` files
- [`img`](img/): Contains various images saved from our project.
- [`all_data.csv`](all_data.csv): `csv` that contains all of the NHANES datasets and the diabetes dataset.
- [`diabetes.ipynb`](diabetes.ipynb): Jupyter notebook containing the code for our project
- [`requirements.txt`](requirements.txt): Required libraries
- [`zipper.py`](zipper.py): Python script that zips everything for submission.

## Contact Information

```plaintext
Alan Saucer
Email: asaucer@vols.utk.edu
GH: PiSaucer
```

```plaintext
Constance Wilson
Email: cwils163@vols.utk.edu
GH: cwils163
```

## Acknowledgments

This assignment is for COSC 426 (Intro to Data Engineering) at the University of Tennessee, Knoxville.
