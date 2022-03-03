# ParametricModels-Ansys
Parametric modelling and processing fluid dynamics with Ansys.

# Creating the parametric CAD models

## Installing the paramak
- You are able to read the docs at [Paramak](https://paramak.readthedocs.io/en/main/install.html).

On Ubuntu install The Paramak by issuing the following commands after installing [Anaconda](https://www.anaconda.com/) (or Miniconda):

```
conda create --name paramak_env python=3.8

conda activate paramak_env

conda install -c fusion-energy -c cadquery -c conda-forge paramak

pip install jupyter-cadquery==2.2.1
```

## Creating geometry and exporting STEP files
Run an example file for the Paramak:
```
python geometry.py
```
Or run the Jupyter Notebook through Jupyter Labs.

# ANSYS and geometry CFD analysis
