from fastapi import FastAPI, HTTPException, status
from typing import List
from models.db import db
from models.models import Sheep

app = FastAPI()

# Get all sheep
@app.get("/sheep/", response_model=List[Sheep])
async def read_all_sheep():
    return list(db.data.values())

# Get a single sheep by ID
@app.get("/sheep/{sheep_id}", response_model=Sheep)
async def read_sheep(sheep_id: int):
    if sheep_id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return db.data[sheep_id]

# Add a new sheep
@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
async def create_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")
    db.add_sheep(sheep)
    return sheep

# Update an existing sheep by ID
@app.put("/sheep/{sheep_id}", response_model=Sheep)
async def update_sheep(sheep_id: int, sheep: Sheep):
    if sheep_id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    updated_sheep = db.update_sheep(sheep_id, sheep)
    return updated_sheep

# Delete a sheep by ID
@app.delete("/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sheep(sheep_id: int):
    if sheep_id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    db.delete_sheep(sheep_id)
    return




