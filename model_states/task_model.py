from pydantic import BaseModel, StrictInt


class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    task_id : StrictInt
    title: str
    description: str
   

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

class TaskUpdateResponse(BaseModel):
    title: str
    description: str
    status: str

class GetTask(BaseModel):
    task_id : int

class GetDeleteTask(BaseModel):
    task_id :StrictInt
