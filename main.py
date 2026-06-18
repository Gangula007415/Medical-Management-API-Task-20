from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI

from database import SessionLocal, engine
from models import Patient
from schemas import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medical Management API")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Medical Management API is running"}


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET ALL PATIENTS
@app.get("/patients", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients


# GET PATIENT BY ID
@app.get("/patients/{id}", response_model=PatientResponse)
def get_patient(id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(
        Patient.patient_id == id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# ADD NEW PATIENT
@app.post("/patients", response_model=PatientResponse)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    new_patient = Patient(**patient.model_dump())

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# UPDATE PATIENT
@app.put("/patients/{id}", response_model=PatientResponse)
def update_patient(
    id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db)
):
    existing_patient = db.query(Patient).filter(
        Patient.patient_id == id
    ).first()

    if not existing_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    for key, value in patient.model_dump().items():
        setattr(existing_patient, key, value)

    db.commit()
    db.refresh(existing_patient)

    return existing_patient


# DELETE PATIENT
@app.delete("/patients/{id}")
def delete_patient(
    id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.patient_id == id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient deleted successfully"
    }