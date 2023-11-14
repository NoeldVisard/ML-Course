import pandas as pd
import random

import numpy as np
import matplotlib as mpl

diseases = pd.read_csv('disease.csv', delimiter=';')
symptoms = pd.read_csv('symptom.csv', delimiter=';')

patient_symptoms = []
for patient_symptom in symptoms['symptom']:
    if random.randint(0, 6) == 0:
        patient_symptoms.append(patient_symptom)
for patient_symptom in patient_symptoms:
    print(patient_symptom)

print('------------')

disease_probability = []
# for disease in diseases['количество пациентов']:
for disease in diseases[diseases.columns[-1]][:-1]:
    print(disease)
    disease_probability.append(disease)

print('------------')

for patient_symptom in patient_symptoms:
    for symptom in symptoms.iterrows():
        if symptom[1]['symptom'] == patient_symptom:
            for i in range(1, len(symptom[1])):
                disease_probability[i-1] *= symptom[1][i]

disease_index = 0
max_probability = 0
for i in range(len(disease_probability)):
    if disease_probability[i] > disease_index:
        disease_index = i
        max_probability = disease_probability[i]

print(diseases['disease'][disease_index])