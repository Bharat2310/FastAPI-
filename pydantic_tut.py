# pydantic - for type validation and data validation
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional
class Patient(BaseModel):
    name : str = Field(max_length=50)
    age : int 
    email : EmailStr
    LinkedIn : AnyUrl
    weight : float = Field(gt = 0, lt=100, max_digits=2)
    married: bool = False
    contact_info : Dict[str, str]
    # for making this parameter optional
    allergies : Optional[List[str]] = None 

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.contact_info)
    print(patient.allergies)

    print("done")



patient_info = {"name": "Bharat", "age": 90, "weight": 90.1, "married": True, "contact_info": {"email": "hello@.mai.c", "numbrrt": 9087}, "allergies": ["1", "2"]}
patient1 = Patient(**patient_info)
insert_patient(patient1)