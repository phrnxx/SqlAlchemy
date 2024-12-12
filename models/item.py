from db import db
from models.base import BaseModel

class ItemModel(BaseModel):
    __tablename__ = "items"  
    name = db.Column(db.String(80), nullable=False) 
    price = db.Column(db.Float(precision=2), nullable=False) 
    
    store_id = db.Column(
        db.Integer,
        db.ForeignKey("stores.id"),  
        nullable=False  
    )
    
    store = db.relationship(
        "StoreModel",
        back_populates="items" )

    def __repr__(self):
        return f"<Item {self.name}>"