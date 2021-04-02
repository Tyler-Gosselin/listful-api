from app import ma  
from app.models import User, Item, List
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "email", "lists", "id")
    
    lists = fields.List(fields.Nested(lambda: ListSchema(only=("id", "title",))))

class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")

class ListSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "items")

    items = fields.List(fields.Nested(lambda: ItemSchema(only=("id", "name",))))
    

user_schema = UserSchema()
users_schema = UserSchema(many=True)

list_schema = ListSchema()
lists_schema = ListSchema(many=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)