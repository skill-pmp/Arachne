# backend/app/routes/progress.py
import sqlite3
from flask import Blueprint, jsonify

progress_bp = Blueprint("progress", __name__)


@progress_bp.route("/progress", methods=["GET"])
def get_progress():
    conn = sqlite3.connect("database/habits.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.name, COUNT(l.completed) as completions
        FROM habits h
        LEFT JOIN habit_logs l ON h.id = l.habit_id AND l.completed = 1
        GROUP BY h.id
    """)
    rows = cursor.fetchall()
    conn.close()

    progress = [{"habit": row[0], "completions": row[1]} for row in rows]
    return jsonify(progress)
