from marshmallow import Schema, fields, validate

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=80),
        error_messages={
            "required": "Название товара обязательно",
            "validator_failed": "Название должно быть от 1 до 80 символов"
        }
    )
    
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0.01),
        error_messages={
            "required": "Цена товара обязательна",
            "validator_failed": "Цена должна быть больше 0"
        }
    )
    
    store_id = fields.Int(
        required=True,
        error_messages={"required": "ID магазина обязателен"}
    )
    
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    store = fields.Nested("StoreSchema", exclude=("items",), dump_only=True)