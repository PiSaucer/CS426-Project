# CS426-Project

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

## Our Project
With diabetes prevalence on the rise, it's essential that we identify demographic and behavioral indicators for early and accurate screenings. Our project utilizes NHANES 2021-23 data to identify strong predictors for diabetes. In this project we use a mixture of machine learning models and feature selection to not only predict diabetes, but also to find the most influential features driving those predictions.

## The Files
- `all_data`: contains all the non-diabetes NHANES datasets
- `cleaned`: contains a cleaned version of the diabetes dataset
- `diabetes_data`: contains the NHANES diabetes dataset as both a .xpt and .csv file
- `img`: contains various images saved from our project
- `all_data.csv`: csv that contains all of the NHANES datasets and the diabetes dataset
- `diabetes.ipynb`: jupyter notebook containing the code for our project
- `requirements.txt`: required libraries