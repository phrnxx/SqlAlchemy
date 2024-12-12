from marshmallow import Schema, fields, validate

class StoreSchema(Schema):
    id = fields.Int(dump_only=True)
    
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=80),
        error_messages={
            "required": "Название магазина обязательно",
            "validator_failed": "Название должно быть от 1 до 80 символов"
        }
    )
    
    description = fields.Str(validate=validate.Length(max=200))
    
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    items = fields.List(fields.Nested("ItemSchema", exclude=("store",)), dump_only=True)