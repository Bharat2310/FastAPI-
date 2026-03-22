from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data

@app.get("/")
def heloo():
    return {"messagae": "patient managment system api"}

@app.get("/about")
def about():
    return {"messgage": "system to manage the patients in a hospital"}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description="ID of the patient you want to see", example="P001") ):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of weigth, height or bmi"),
                  order_by: str = Query("asc", description="order by ac or desc")):
    
    if sort_by not in ["height", "weight", "bmi" ] or order_by not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="select valid values from weight, height and bmi and asc, desc")
    
    order = True if order_by == "desc" else False

    data = load_data()
    
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by,0), reverse=order)

    return sorted_data