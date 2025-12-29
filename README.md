# HCAI Miniproject -  ML Efficiency of Cancer Survival Prediction

## About The Project

This project was initially part of a HCAI SS2024 course at Graz Technical University, Austria, 
and was later on prepared for publication in MDPI Applied Sciences and will be available 2026 under DOI [10.3390/app1010000](https://doi.org/10.3390/app1010000).
The study was intended to reproduce a published model named [PiDeeL](https://github.com/ciceklab/PiDeeL), 
a pathway-informed deep learning model for survival analysis and pathological classification of gliomas, 
and an analysis of the emissions caused by running this reproduction on two different systems.

## About The Repository
 
The `main` branch contains a copy of the original PiDeeL repository (last updated 2024-07-02). The only exception
is the PiDeeL README file, which has been renamed to README_PiDeeL.md, and the PiDeeL license, which has been renamed to 
LICENSE_PiDeeL.

The `dev` branch contains the starting state of the code that was used to run the reproduction and measure emissions. This includes
some minor fixes to the original PiDeeL code, as well as the integration of [CodeCarbon](https://codecarbon.io/) functionality in the 
reproduction script (reproduce/run_reproduction.py). After adding data and setting the path in hyper_config.py as
described in the PiDeeL README, reproduce/run_and_log.sh can be used to run the reproduction including the emissions 
evaluation and save all output to a log file. 

The `system1` and `system2` branches contain the final state after a run on the respective system, including
the data used to train the model (reproduce/data/), the PiDeeL results (reproduce/reproduction_scripts/ subfolders), as 
well as the emission results (emissions/).

Project results are summarized in a spreadsheet containing the 
documentation of the results and figures ("codecarbon_results_evaluation.xlsx") can be 
found on all branches. Furthermore, a scientific publication in preparation will be reporting on replication study insights.
