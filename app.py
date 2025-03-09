from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase Setup
cred = credentials.Certificate("path_to_your_firebase_adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# FastAPI App
app = FastAPI()

# Request Model
class TaskRequest(BaseModel):
    user_id: str
    prompt: str

@app.post("/execute_task")
def execute_task(request: TaskRequest):
    try:
        # Save Prompt to Firebase
        task_ref = db.collection("tasks").document()
        task_ref.set({
            "user_id": request.user_id,
            "prompt": request.prompt,
            "status": "pending"
        })
        
        # AI Task Execution Logic (Placeholder for Future Development)
        ai_response = f"AI executed task for prompt: {request.prompt}"
        
        return {"message": "Task received", "ai_response": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run Locally: uvicorn filename:app --reload
