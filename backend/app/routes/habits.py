# backend/app/routes/habits.py
import sqlite3
from flask import Blueprint, request, jsonify

habits_bp = Blueprint("habits", __name__)


@habits_bp.route("/habits/<int:habit_id>/complete", methods=["POST"])
def complete_habit(habit_id):
    conn = sqlite3.connect("database/habits.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO habit_logs (habit_id, date, completed)
        VALUES (?, date('now'), 1)
    """, (habit_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Habit marked as completed"})
