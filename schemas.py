<<<<<<< HEAD
from pydantic import BaseModel, Field
from datetime import date

class PatientBase(BaseModel):
    patient_name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0, lt=120)
    gender: str
    disease: str
    doctor_name: str
    admission_date: date
    phone_number: str = Field(..., min_length=10, max_length=15)

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    patient_id: int

    class Config:
=======
from pydantic import BaseModel, Field
from datetime import date

class PatientBase(BaseModel):
    patient_name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0, lt=120)
    gender: str
    disease: str
    doctor_name: str
    admission_date: date
    phone_number: str = Field(..., min_length=10, max_length=15)

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    patient_id: int

    class Config:
>>>>>>> a22d4c2a3b779874262c440228fa660189ee1c28
        from_attributes = True