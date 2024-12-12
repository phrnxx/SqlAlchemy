from db import db
from models.base import BaseModel

class StoreModel(BaseModel):
    __tablename__ = "stores"  

    name = db.Column(db.String(80), unique=True, nullable=False) 
    description = db.Column(db.String(200)) 
    
    items = db.relationship(
        "ItemModel",
        back_populates="store",  
        lazy="dynamic",  
        cascade="all, delete")

    def __repr__(self):
        return f"<Store {self.name}>"