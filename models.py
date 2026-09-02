<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Date
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    disease = Column(String(100), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    admission_date = Column(Date, nullable=False)
=======
from sqlalchemy import Column, Integer, String, Date
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    disease = Column(String(100), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    admission_date = Column(Date, nullable=False)
>>>>>>> a22d4c2a3b779874262c440228fa660189ee1c28
    phone_number = Column(String(15), nullable=False)