from models.models import Sheep
from typing import Dict, Optional

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {
            1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
            2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram"),
            3: Sheep(id=3, name="Deedee", breed="Jacobs Four Horns", sex="ram"),
            4: Sheep(id=4, name="Rommy", breed="Rommey", sex="ewe"),
            5: Sheep(id=5, name="Vala", breed="Valais Blacknose", sex="ewe"),
            6: Sheep(id=6, name="Esther", breed="Border Leicester", sex="ewe")
        }

    def get_sheep(self, sheep_id: int) -> Optional[Sheep]:
        return self.data.get(sheep_id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
        # Check if the sheep ID already exists
        if sheep.id in self.data:
            raise ValueError(f"Sheep with ID {sheep.id} already exists")
        # Add the new sheep to the database
        self.data[sheep.id] = sheep
        return sheep

    def update_sheep(self, sheep_id: int, updated_sheep: Sheep) -> Optional[Sheep]:
        if sheep_id in self.data:
            self.data[sheep_id] = updated_sheep
            return updated_sheep
        return None

    def delete_sheep(self, sheep_id: int) -> bool:
        if sheep_id in self.data:
            del self.data[sheep_id]
            return True
        return False

# Create an instance of FakeDB to use in main.py
db = FakeDB()

