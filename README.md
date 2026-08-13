# Case Study Bank - Patient Vital Signs Monitor

This project is a small Python command-line prototype for monitoring patient vital signs, generating clinical-style status alerts, and simulating a hospital information workflow for doctors and patients.

## Project Purpose
The application demonstrates a lightweight hospital record workflow where:
- doctors can search for patients and open a doctor-driven menu
- patients can be retrieved through a patient access workflow
- vital-sign readings are validated and stored in each patient's reading history
- sample data can be loaded through the dataset/setup layer and saved back to a local binary data file

## Current Features
- `Patient`, `Doctor`, `PermittedStaff`, `VitalSigns`, and `AlertManager` model components
- `InPatient` and `OutPatient` subclasses using inheritance and polymorphism
- One-to-many patient-to-vital-sign association via `vitals_history`
- Patient-specific methods for returning report text, historical vital logs, and the latest reading
- Unified user lookup contract: doctors, patients, and permitted staff expose a `u_id` attribute used by the shared `findUser()` lookup routine
- Unique patient ID generation through the `Patient.p_ID` counter and `patient_id` attributes such as `P1001`
- Doctor ID generation through the `Doctor.doc_ID` counter and `doc_ID` attributes such as `D101`
- Staff ID generation through `PermittedStaff.pms_ID` and `u_id` aliases for the staff lookup layer
- `u_id` is populated from the concrete identifiers so doctor, patient, and staff records can be resolved through a single lookup function
- Vital sign validation for temperature, pulse, and oxygen saturation
- Alert generation for each reading through `generateAlert()` and severity classification helpers
- Doctor-driven console operations for patient lookup, adding patients, and adding new readings
- Permitted-staff workflow via `pmsAccess()` to open a staff console with patient access and patient-record updates
- Menu-driven access in the main program's top-level workflow
- Pickle-based persistence through `save_data()` and `load_data()` in the data handling layer, now returning `doctors`, `patients`, and `pStaff`

## Files in the Project
- [Main.py](Main.py) – application entry point and menu-driven console workflow
- [Functions/dataHandling.py](Functions/dataHandling.py) – local persistent data layer using pickle save/load helpers
- [Functions/accessability.py](Functions/accessability.py) – user-facing access workflows such as `findUser()`, `showDoctors()`, `showPatients()`, `showVitals()`, and `pmsAccess()`
- [phi/sample_data.py](phi/sample_data.py) – creates sample doctors, patients, initial vital sign readings, and permitted staff records
- [Users/Patient.py](Users/Patient.py) – base `Patient` model plus `InPatient` and `OutPatient` subclasses
- [Users/Doctor.py](Users/Doctor.py) – doctor class with validation and display helpers
- [Users/PermittedStaff.py](Users/PermittedStaff.py) – permitted-staff model with `pms_ID` and `u_id` aliasing
- [Functions/VitalSigns.py](Functions/VitalSigns.py) – vital-sign model with input validation and recorded timestamp support
- [Functions/AlertManager.py](Functions/AlertManager.py) – vital-sign checks and overall alert classification

## Current Behavior
1. **Program Initialization:** The program attempts to load stored hospital data through `load_data()` from the persistent data layer. On first run, it generates initial sample data via `phi/sample_data.py` and saves it to `hospital_data.dat`. On subsequent runs, it loads existing doctor, patient, and permitted staff records.
2. **Initial Display:** Upon startup, the program displays all available doctors and patients with their current vital records using the shared `u_id` contract.
3. **Main Menu:** The user can choose between doctor access, patient access, permitted staff access, or program exit.
4. **Doctor Workflow:** Doctors can search for patients using `findUser()`, add new vital sign readings with validation, and review patient data including historical vital logs and the latest readings.
5. **Patient Workflow:** Patients can view their own medical report and complete historical vital sign readings with generated status alerts showing overall patient status.
6. **Permitted Staff Workflow:** Staff members enter with their staff ID and access a staff-only menu that mirrors doctor access options for patient retrieval and vital sign record updates.
7. **Vital Sign Display:** The vital-sign display logic safely handles legacy records that may not include a `recorded_by` staff reference by using `getattr()` to avoid runtime attribute errors.
8. **Data Persistence:** When the user exits the program, the current doctor, patient, and permitted staff collections are saved via `save_data()` to the `hospital_data.dat` binary persistence file.

## Data Persistence
The latest implementation adds a persistence layer that serializes the in-memory hospital objects using Python's `pickle` module.

- The file used for persistence is `hospital_data.dat`.
- [Functions/dataHandling.py](Functions/dataHandling.py) contains the `save_data()` and `load_data()` functions.
- The `load_data()` routine now returns a three-part tuple: `doctors`, `patients`, and `pStaff`.
- The `save_data()` routine stores those three collections under the same top-level persistence schema.
- The `Main.py` program reads the saved doctor, patient, and permitted staff records at startup and writes them back on exit.

## Object Identifiers and Unified Lookup System

All users in the system are assigned unique identifiers through auto-incrementing counters:

### Patient IDs
- **Format:** `P` + 4-digit number (e.g., `P1001`, `P1002`)
- **Counter:** Class-level `Patient.p_ID` incremented for each new patient
- **Unified ID:** Each patient's `u_id` attribute mirrors their `patient_id` for consistent lookups

### Doctor IDs
- **Format:** `D` + 3-digit number (e.g., `D101`, `D102`)
- **Counter:** Class-level `Doctor._doc_ID` incremented for each new doctor
- **Unified ID:** Each doctor's `u_id` attribute mirrors their `doc_ID` for consistent lookups

### Staff IDs
- **Format:** `S` + 3-digit number (e.g., `S101`, `S102`)
- **Counter:** Class-level `PermittedStaff._pms_ID` incremented for each new staff member
- **Unified ID:** Each staff member's `u_id` attribute mirrors their `pms_ID` for consistent lookups

### Unified User Lookup
The `findUser(uid, datalist)` function in [Functions/accessability.py](Functions/accessability.py) provides a unified lookup mechanism. It searches through any collection of users (doctors, patients, or staff) by comparing the provided `uid` with each object's `u_id` attribute. This contract allows the same lookup logic to work seamlessly across different user types:

```python
doctor_obj = findUser("D101", doctors)      # Find doctor by ID
patient_obj = findUser("P1001", patients)   # Find patient by ID  
staff_obj = findUser("S101", pStaff)        # Find staff by ID
```

## Class Design and OOP Concepts

The project demonstrates several core object-oriented programming principles:

### Encapsulation
All model classes use setter methods with input validation:
- `Patient` class: `set_pname()`, `set_age()`, `set_gender()`, `set_bg()`
- `Doctor` class: `setName()`, `setSpeciality()`
- `PermittedStaff` class: `setName()`, `setDesignation()`
- `VitalSigns` class: `setTemp()`, `setPulse()`, `setOxygen()`

This ensures that invalid data is rejected at the point of assignment, maintaining data integrity throughout the application.

### Inheritance and Polymorphism
The `Patient` class serves as a base class with two subclasses:
- `InPatient` - represents admitted patients requiring extended monitoring
- `OutPatient` - represents patients visiting for check-ups or consultations

Both subclasses inherit the core patient functionality while allowing specialized behavior for inpatient vs. outpatient workflows.

### Associations
The `Patient` class maintains a **one-to-many association** with `VitalSigns` through the `vitals_history` list. Each patient can have multiple vital sign readings, and each reading is a separate `VitalSigns` object with its own timestamp and optional staff attribution. This models the real-world scenario where a patient's vital signs are monitored over time.

## Vital Sign Validation

The `VitalSigns` class enforces strict validation ranges for all recorded measurements:

- **Temperature:** 30°C to 45°C (range for patient survival and clinical monitoring)
- **Pulse:** 20 to 250 bpm (normal adult resting: 60–100 bpm)
- **Oxygen Saturation (SpO₂):** 0 to 100% (normal clinical range: ≥95%)

Each reading is automatically timestamped with the exact date and time of recording via `recorded_time`. When a vital sign reading is added by a permitted staff member, the `recorded_by` attribute links the reading to the staff member's full record (name, staff ID, and designation).

## Alert Logic and Severity Classification

The `AlertManager` module evaluates each vital sign against clinical thresholds and generates severity alerts:

### Temperature Alert Rules
- **NORMAL:** 36.5°C to 37.5°C  
- **WARNING:** 37.5°C to 38.5°C or below 36°C  
- **CRITICAL:** Above 38.5°C  

### Pulse Alert Rules
- **NORMAL:** 60 to 100 bpm  
- **WARNING:** 50 to 59 bpm or 100 to 120 bpm  
- **CRITICAL:** Below 50 bpm or above 120 bpm  

### Oxygen Saturation Alert Rules
- **NORMAL:** 95% or higher  
- **WARNING:** 90% to 94%  
- **EMERGENCY:** Below 90%  

### Overall Alert Classification
The `generateAlert()` function combines individual vital sign alerts to determine overall patient status:
- **EMERGENCY:** Immediate attention required (any EMERGENCY-level reading)  
- **CRITICAL:** Doctor review required (any CRITICAL-level reading without EMERGENCY)  
- **WARNING:** Monitor patient (any WARNING-level reading without CRITICAL or EMERGENCY)  
- **NORMAL:** Patient stable (all readings within normal ranges)

## Access Workflows

The application provides three separate access modes through the main menu:

### 1. Doctor Access (`doctorAccess()`)
Doctors can:
- Search for patients by patient ID using the unified `findUser()` lookup
- View complete patient information including demographics, diagnosis, and assigned doctor
- Add new vital sign readings for a patient with automatic validation
- View the patient's entire vital sign history with timestamps
- See the latest vital readings and alert status
- Review historical trends in patient vital signs

### 2. Patient Access (`patientAccess()`)
Patients can:
- Search for themselves by patient ID using the unified `findUser()` lookup
- View their own complete medical report including diagnosis and blood type
- Access their full historical vital sign log with all recorded readings
- See alert status and severity classifications for each reading
- Review timestamps indicating when each reading was recorded
- Note which staff member (if any) recorded each vital sign

### 3. Permitted Staff Access (`pmsAccess()`)
Staff members with proper authorization can:
- Enter the staff workflow using their staff ID
- Access a staff-only menu mirroring doctor access capabilities
- Search for patients and view patient records
- Add new vital sign readings with their staff credentials automatically recorded
- See which staff member recorded each reading with name, ID, and designation
- Update patient vital signs and contribute to clinical monitoring

## Status
This is a working prototype and learning project rather than a production hospital system. It uses in-memory classes and a local serialized data file instead of a database or external API.

## Run the Project
From the project folder, run:

```bash
python Main.py
```


