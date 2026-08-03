# Case Study Bank - Patient Vital Signs Monitor

This project is a small Python command-line prototype for monitoring patient vital signs and generating basic medical alerts.

## Project Purpose
The application simulates a simple hospital workflow where:
- doctors can access patient reports
- patients can view their own report
- vital values are checked and classified into alert levels

## Current Features
- Patient, doctor, and vital sign model classes
- Sample in-memory hospital data
- Doctor-to-patient assignment
- Vital data validation
- Alert generation for temperature, pulse, and oxygen saturation
- Console-based menu-driven interaction

## Files in the Project
- [Main.py](Main.py) – entry point of the application and user menu
- [database.py](database.py) – creates sample patients, doctors, and vital records
- [Patient.py](Patient.py) – patient class with validation and display methods
- [Doctor.py](Doctor.py) – doctor class with validation and details display
- [VitalSigns.py](VitalSigns.py) – vital signs class with range validation
- [AlertManager.py](AlertManager.py) – alert categorization logic

## How it Works
1. The program loads predefined doctor and patient records.
2. It displays the list of doctors, patients, and current vital records.
3. The user chooses whether to access the system as a doctor or patient.
4. The selected patient’s report and vital signs are displayed.
5. Alerts are generated based on the patient’s temperature, pulse, and oxygen saturation.

## Status
This is a working prototype and learning project rather than a full production healthcare system. It currently uses in-memory objects and does not persist data to a real database.

## Run the Project
From the project folder, run:

```bash
python Main.py
```

## Example Alert Logic
- Temperature within safe limits: normal
- Slightly abnormal values: warning
- Serious abnormal values: critical
- Emergency-level values: immediate attention required

