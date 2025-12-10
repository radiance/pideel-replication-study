from hyper_config import ultimate_path
from codecarbon import OfflineEmissionsTracker

import warnings

import os

tracker = OfflineEmissionsTracker(country_iso_code="AUT", experiment_name="PiDeeL", output_dir=f'{ultimate_path}/emissions')
tracker.start()

print("Dataset Loading...")
os.chdir(f'{ultimate_path}/reproduce/reproduction_scripts/scripts')
tracker.start_task("Dataset Loading")
os.system('python load_targeted_data.py')
tracker.stop_task("Dataset Loading")
print("Dataset Loaded")

print("Survival analysis models")
print("Training...")

print("Baseline")

print("Cox-PH model")
os.chdir('baseline/coxph')
tracker.start_task("Survival - Baseline Cox-PH Model")
os.system('python main_grid.py')
tracker.stop_task("Survival - Baseline Cox-PH Model")

print("RSF model")
os.chdir('../rf')
tracker.start_task("Survival - Baseline RSF model")
os.system('python main_grid.py')
tracker.stop_task("Survival - Baseline RSF model")

print("2 layer fully connected network")
os.chdir('../../2layer/no_pathway')
tracker.start_task("Survival - 2 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Survival - 2 layer fully connected network")

print("2 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Survival - 2 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Survival - 2 layer pathway-informed network")

print("3 layer fully connected network")
os.chdir('../../3layer/no_pathway')
tracker.start_task("Survival - 3 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Survival - 3 layer fully connected network")

print("3 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Survival - 3 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Survival - 3 layer pathway-informed network")

print("4 layer fully connected network")
os.chdir('../../4layer/no_pathway')
tracker.start_task("Survival - 4 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Survival - 4 layer fully connected network")

print("4 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Survival - 4 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Survival - 4 layer pathway-informed network")

print("Survival analysis models - Training Finished")

print("Pathological classification models")
print("Training...")

print("2 layer fully connected network")
os.chdir('../../../tests/scripts/test5/2layer/no_pathway/')
tracker.start_task("Pathological - 2 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Pathological - 2 layer fully connected network")

print("2 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Pathological - 2 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Pathological - 2 layer pathway-informed network")

print("3 layer fully connected network")
os.chdir('../../3layer/no_pathway')
tracker.start_task("Pathological - 3 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Pathological - 3 layer fully connected network")

print("3 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Pathological - 3 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Pathological - 3 layer pathway-informed network")

print("4 layer fully connected network")
os.chdir('../../4layer/no_pathway')
tracker.start_task("Pathological - 4 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Pathological - 4 layer fully connected network")

print("4 layer pathway-informed network")
os.chdir('../pathway')
tracker.start_task("Pathological - 4 layer pathway-informed network")
os.system('python main.py')
tracker.stop_task("Pathological - 4 layer pathway-informed network")

print("Pathological classification models - Training Finished")

print("Multitask models")
print("Training...")

print("2 layer fully connected network")
os.chdir('../../../test7/2layer/pathway/')
tracker.start_task("Multitask - 2 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Multitask - 2 layer fully connected network")

print("3 layer fully connected network")
os.chdir('../../3layer/pathway')
tracker.start_task("Multitask - 3 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Multitask - 3 layer fully connected network")

print("4 layer fully connected network")
os.chdir('../../4layer/pathway')
tracker.start_task("Multitask - 4 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Multitask - 4 layer fully connected network")

print("Multitask models - Training Finished")

print("All models trained")

print("Ablation study 1")
print("Training...")

print("2 layer fully connected network")
os.chdir('../../../test1/2layer/no_pathway/')
tracker.start_task("Ablation study 1 - 2 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 1 - 2 layer fully connected network")

print("3 layer fully connected network")
os.chdir('../../3layer/no_pathway')
tracker.start_task("Ablation study 1 - 3 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 1 - 3 layer fully connected network")

print("4 layer fully connected network")
os.chdir('../../4layer/no_pathway')
tracker.start_task("Ablation study 1 - 4 layer fully connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 1 - 4 layer fully connected network")

print("Ablation study 1 - Training Finished")

print("Ablation study 2")
print("Training...")

print("2 layer randomly connected network")
os.chdir('../../../test2/2layer/no_pathway/')
tracker.start_task("Ablation study 2 - 2 layer randomly connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 2 - 2 layer randomly connected network")

print("3 layer randomly connected network")
os.chdir('../../3layer/no_pathway')
tracker.start_task("Ablation study 2 - 3 layer randomly connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 2 - 3 layer randomly connected network")

print("4 layer randomly connected network")
os.chdir('../../4layer/no_pathway')
tracker.start_task("Ablation study 2 - 4 layer randomly connected network")
os.system('python main.py')
tracker.stop_task("Ablation study 2 - 4 layer randomly connected network")

print("Ablation study 2 - Training Finished")

print("All training finished")

tracker.start_task("Logs & Plots")

print("Results:")
os.chdir('../../../../../logs/')
os.system('python analysis.py')
print("Results printed")
print("Boxplots:")
os.system('python boxplot.py')
print("Figure 1 saved")

os.system('python boxplot2.py')
print("Figure 2 saved")
os.system('python boxplot3.py')
print("Figure 3 saved")

tracker.stop_task("Logs & Plots")


print("SHAP analysis:")
os.chdir("../shap_analysis")
tracker.start_task("SHAP Analysis")
os.system("python shap_metabolites.py")
os.system("python shap_pathways.py")
tracker.stop_task("SHAP Analysis")
print("Shap analysis finished")
print("Figure 4 saved")

print("All done")

tracker.stop()
