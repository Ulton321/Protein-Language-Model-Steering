import papermill as pm

#List the notebook needs to be running

notebooks = [
    "notebooks/",
]

for nb in notebooks:
    output_nb = nb.replace(".ipynb", "_executed.ipynb")
    print(f"Running {nb} -> {output_nb}")
    pm.execute_notebook(nb, output_nb)
