# Case Study Bank - Patient Vital Signs Monitor

This project is a small Python command-line prototype for monitoring patient vital signs, generating clinical-style status alerts, and simulating hospital patient/doctor access workflows.

## Project Purpose
The application demonstrates an in-memory hospital information workflow where:
- doctors can access patient records and add new patients
- patients can be looked up through a patient access workflow
- vital signs are validated and attached to a patient’s reading history
- sample hospital records are loaded for quick demonstration in the console

## Current Features
- `Patient`, `Doctor`, `VitalSigns`, and `AlertManager` model components
- `InPatient` and `OutPatient` subclasses using inheritance and polymorphism
- One-to-many patient-to-vital-sign association via `vitals_history`
- Patient-specific methods for retrieving individual patient reports and the latest reading
- Unique patient ID generation per instance through the `Patient.p_ID` counter
- Vital sign validation for temperature, pulse, and oxygen saturation
- Alert generation for each vital-sign reading using `generateAlert()`
- Doctor-driven console operations for patient lookup, adding patients, and adding new readings
- Menu-based interaction in the main program

## Files in the Project
- [Main.py](Main.py) – application entry point and menu-driven console workflow
- [sample_data.py](sample_data.py) – creates sample doctors, patients, and initial vital sign records
- [Patient.py](Patient.py) – patient base class plus `InPatient` and `OutPatient` subclasses
- [Doctor.py](Doctor.py) – doctor class with validation and display helpers
- [VitalSigns.py](VitalSigns.py) – vital signs model with input validation
- [AlertManager.py](AlertManager.py) – alert checks and severity classification helpers

## Current Behavior
1. The program loads predefined doctor and patient objects from the sample dataset.
2. It displays available doctors, available patients, and the current stored vital readings.
3. The user chooses whether to enter the doctor workflow or patient workflow.
4. The doctor workflow supports patient access, adding a new patient, and adding new vital-sign readings.
5. The patient workflow prints the selected patient’s report and all historical readings with generated alerts.

## Recent Updates
The current implementation includes the following changes visible in the codebase:
- `patient_id` generation is instance-based and increments correctly for each object created.
- `Patient` objects now store a `vitals_history` list and can accept several `VitalSigns` readings over time.
- The main program now supports adding new patient records and inserting a new vital-sign reading through the doctor menu.
- Patient access can display both the summary information and each reading-specific alert result.

## Status
This is a working prototype and learning project rather than a production hospital system. It uses in-memory data structures and does not persist data to a database or external API.

## Run the Project
From the project folder, run:

```bash
python Main.py
```

## Example Alert Logic
- Temperature within a safe range is reported as `NORMAL`
- Slightly abnormal values are reported as `WARNING`
- Serious abnormal values are reported as `CRITICAL`
- Emergency-level values are reported as `EMERGENCY` with immediate-attention messaging

