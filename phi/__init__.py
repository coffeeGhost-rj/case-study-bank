# The package remains import-safe for the runtime entrypoints.
# The concrete sample data objects are loaded lazily from the sample_data module
# when the persistence layer needs an initial seed.

from .sample_data import doctors, patients, pStaff
__all__ = ["doctors", "patients", "pStaff"]