# Case Study Bank - Patient Vital Signs Monitor

This project is a small Python command-line prototype for monitoring patient vital signs, generating clinical-style status alerts, and simulating a hospital information workflow for doctors and patients.

## Project Purpose
The application demonstrates a lightweight hospital record workflow where:
- doctors can search for patients and open a doctor-driven menu
- patients can be retrieved through a patient access workflow
- vital-sign readings are validated and stored in each patient's reading history
- sample data can be loaded through the dataset/setup layer and saved back to a local binary data file

## Current Features
- `Patient`, `Doctor`, `VitalSigns`, and `AlertManager` model components
- `InPatient` and `OutPatient` subclasses using inheritance and polymorphism
- One-to-many patient-to-vital-sign association via `vitals_history`
- Patient-specific methods for returning report text, historical vital logs, and the latest reading
- Unique patient ID generation through the `Patient.p_ID` counter and ID strings such as `P1001`
- Doctor ID generation through the `Doctor.doc_ID` counter and ID strings such as `D101`
- Vital sign validation for temperature, pulse, and oxygen saturation
- Alert generation for each reading through `generateAlert()` and severity classification helpers
- Doctor-driven console operations for patient lookup, adding patients, and adding new readings
- Menu-driven access in the main program's top-level workflow
- Pickle-based persistence through `save_data()` and `load_data()` in the data handling layer

## Files in the Project
- [Main.py](Main.py) – application entry point and menu-driven console workflow
- [dataHandling.py](dataHandling.py) – local persistent data layer using pickle save/load helpers
- [sample_data.py](sample_data.py) – creates sample doctors, patients, and initial vital sign readings
- [Patient.py](Patient.py) – base `Patient` model plus `InPatient` and `OutPatient` subclasses
- [Doctor.py](Doctor.py) – doctor class with validation and display helpers
- [VitalSigns.py](VitalSigns.py) – vital-sign model with input validation and recorded timestamp support
- [AlertManager.py](AlertManager.py) – vital-sign checks and overall alert classification

## Current Behavior
1. The program attempts to load stored hospital data through `load_data()` from the persistent data layer.
2. It displays available doctors, available patients, and the current vital records for each patient.
3. The user can choose between doctor access, patient access, view-all-vitals summary, or program exit.
4. The doctor workflow supports patient lookup, adding a new patient, and inserting a fresh `VitalSigns` reading through the patient history list.
5. The patient workflow prints the selected patient's report and all historical readings with generated status alerts.
6. When the user exits the program, the current doctor and patient collections are saved via `save_data()` to a local binary file.

## Data Persistence
The latest implementation adds a persistence layer that serializes the in-memory hospital objects using Python's `pickle` module.

- The file used for persistence is `hospital_data.dat`.
- [dataHandling.py](dataHandling.py) contains the `save_data()` and `load_data()` functions.
- The `Main.py` program reads the saved doctor and patient records at startup and writes them back on exit.

## Example Alert Logic
- Temperature within a safe range is reported as `NORMAL`
- Slightly abnormal values are reported as `WARNING`
- Serious abnormal values are reported as `CRITICAL`
- Emergency-level values are reported as `EMERGENCY` with immediate-attention messaging

## Status
This is a working prototype and learning project rather than a production hospital system. It uses in-memory classes and a local serialized data file instead of a database or external API.

## Run the Project
From the project folder, run:

```bash
python Main.py
```


