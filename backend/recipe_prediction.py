from flask import Blueprint, request, jsonify
from recipes_recommender import recommend_recipes
import sqlite3
from datetime import datetime
from flask_cors import cross_origin

recipe_bp = Blueprint('recipe_bp', __name__)

def get_user_pantry(user_id):
    """
    Fetch pantry ingredients and their expiry info from the SQLite database.
    Database: pantrypal.db, table: pantry_items.
    expiry_date is stored as text ("YYYY-MM-DD").
    Returns:
      - ingredients: list of item names.
      - expiry_info: dict mapping item_name to days until expiry.
    """
    conn = sqlite3.connect("pantrypal.db")
    cursor = conn.cursor()
    query = "SELECT item_name, expiry_date FROM pantry_items WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    
    ingredients = []
    expiry_info = {}
    today = datetime.today()
    for item_name, expiry_date_str in rows:
        ingredients.append(item_name)
        try:
            expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
            days_until = (expiry_date - today).days
            expiry_info[item_name] = days_until
        except Exception:
            expiry_info[item_name] = 30  # Default value if parsing fails.
    return ingredients, expiry_info

@recipe_bp.route('/get-recipes', methods=['GET'])
@cross_origin(origins="*")
def get_recipes():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing 'user_id' parameter."}), 400

    pantry, expiry_info = get_user_pantry(user_id)
    if not pantry:
        return jsonify({"error": "No pantry ingredients found for this user."}), 404

    recommendations = recommend_recipes(pantry, expiry_info, top_n=10)
    # 'recommendations' is an array (list) of recipe dictionaries.
    return jsonify({"recipes": recommendations})
