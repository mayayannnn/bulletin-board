from peewee import *

db = SqliteDatabase('Todo.db')

class Todo(Model):
    memo = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Todo])