# Case Study Bank - Patient Vital Signs Monitor

This project is a small Python command-line prototype for monitoring patient vital signs and generating alert-based health summaries.

## Project Purpose
The application simulates a basic hospital information workflow where:
- doctors can access patient reports
- patients can read their own report
- vital signs are validated and categorized into alert levels
- sample records are loaded in memory for quick demonstration

## Current Features
- `Patient`, `Doctor`, and `VitalSigns` model classes
- Sample seed data for doctors and patients
- Patient subclass support for inpatient and outpatient records
- Unique patient ID generation per instance
- Vital sign validation and report display
- Alert generation for temperature, pulse, and oxygen saturation
- Simple menu-based console interaction in the main program

## Files in the Project
- [Main.py](Main.py) – application entry point and menu-driven user flow
- [database.py](database.py) – creates the sample doctors, patient objects, and vital sign records
- [Patient.py](Patient.py) – patient base class plus `InPatient` and `OutPatient` subclasses
- [Doctor.py](Doctor.py) – doctor class with validation and display helpers
- [VitalSigns.py](VitalSigns.py) – vital signs model with input validation
- [AlertManager.py](AlertManager.py) – logic for producing severity alerts

## Current Behavior
1. The program loads predefined doctor and patient records.
2. It displays doctors, patients, and current vital reports.
3. The user selects either doctor access or patient access.
4. The selected patient’s details are printed with ward/bed or consultation-room information depending on patient type.
5. Vital alerts are generated using the latest vital sign values.

## Recent Update
The patient display logic has been corrected so each created patient now shows its own unique generated `patient_id` in the final output, instead of reusing a shared class-level value.

## Status
This is a working prototype and learning project, not a full production hospital system. It uses in-memory objects and does not persist data to a real database.

## Run the Project
From the project folder, run:

```bash
python Main.py
```

## Example Alert Logic
- Temperature within safe range: normal
- Slightly abnormal values: warning
- Serious abnormal values: critical
- Emergency-level values: immediate attention required

