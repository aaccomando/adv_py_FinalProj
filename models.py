from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

import requests
import json

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    pwdhash = db.Column(db.String(54), nullable=False)

    recipes = db.relationship("Recipe", secondary="user_recipes", backref="users")

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Recipe(db.Model):
    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    ingredients = db.Column(db.JSON, nullable=False)
    url = db.Column(db.String(300), nullable=False)

    def query(self, ingredient="chiken"):
        app_id = "10c14d98"
        app_key = "86d7e3941b844f481d623c56ffab1c03"

        query_url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key)

        results = requests.get(query_url)
        data = results.json()
        recipes = data["hits"]

        recipe_list = []
        for recipe in recipes:
            name = recipe["recipe"]["label"]
            image = recipe["recipe"]["image"]
            ingredients = recipe["recipe"]["ingredientLines"]
            url = recipe["recipe"]["url"]


            d = {
                "name": name,
                "image": image,
                "ingredients": ingredients,
                "url": url
            }
            recipe_list.append(d)

        return recipe_list[:5]

class User_Recipe(db.Model):
    __tablename__ = "user_recipes"

    user_recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)
