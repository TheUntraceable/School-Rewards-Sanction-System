from fastapi import FastAPI, status, Response
from models.teacher import Teacher
from models.student import Student
from typing import (
    Dict
)
from random import randint
from json import load

import motor.motor_asyncio

with open("../config.json","r") as f:
    contents = load(f)

app = FastAPI()

cluster = motor.motor_asyncio.AsyncIOMotorClient(contents["mongo_url"])
mongo = cluster["school"]["users"]
weekly_points = contents["teacher_weekly_points"]

@app.post("/new_student",status_code=201,description="Creates a new Student account.")
async def new_student(student : Student):

    await create_user(student)
    
    return {"error" : False, "message" : "Student account created successfully."}

@app.post("/new_teacher",status_code=201,description="Creates a new Teacher account.")
async def new_teacher(teacher : Teacher):
    await create_user(teacher)
    return {"error" : False, "message" : "Teacher account created successfully."}

@app.post("/add_point",status_code=200)
async def add_point(teacher : Teacher,student_id : int , amount : int, response : Response):

    data = await mongo.find_one({"id" : student_id})

    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : True, "message" : "No User can be found with that ID."}
    authoriser = await mongo.find_one({"id" : teacher["id"],"teacher" : True,"password" : teacher["password"]})
    if not authoriser:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : True, "message" : "No Teacher can be found with that ID."}        
    try:
        if data["teacher"]:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error" : True, "message" : "You can't add points to a teacher."}
    except:
        await mongo.update_one({"id" : id},{"$inc" : {"points" : amount}})
        return {"error" : False, "message" : f"Added points to user with ID: {id}."}



async def get_data(id):

    data = await mongo.find_one({"id" : id})

    if data:
        return data

    return None

async def create_user(data : Dict):

    async def gen_id():
        identifier = randint(999999999999999999)
        d = await get_data(identifier)
        if d is None:
            return identifier
        gen_id()

    identifier = await gen_id()

    payload = {}

    payload["id"] = identifier

    payload["name"] = data["name"]

    if data["teacher"]:
        payload["teacher"] = True
        
    payload["password"] = data["password"]
    
    payload["points"] = 0 if not data["teacher"] else weekly_points

    await mongo.insert_one(payload)