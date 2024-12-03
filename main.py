from fastapi import FastAPI, HTTPException


app = FastAPI()
users = []


@app.post("/add_user/{user_name}")
async def add_user(user_name: str):
    if user_name in users:
        raise HTTPException(status_code=400, detail="User with this name already exists")
    users.append(user_name)
    return {"user_name": user_name}


@app.get("/get_users")
async def get_users():
    return {"users": users}


@app.delete("/delete_user/{user_name}")
async def delete_user(user_name: str):
    if user_name not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user_name)
    return {"message": f"User {user_name} deleted successfully"}
