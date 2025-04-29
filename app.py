import os
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration de la base de données SQLite
DB_PATH = os.getenv("DB_PATH", "/data/notes.db")

# Fonction pour se connecter à la base de données
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Initialisation de la base de données
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Création de la table notes si elle n'existe pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contenu TEXT NOT NULL,
        date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()
    print("Base de données SQLite initialisée avec succès!")

# Initialisation de la base de données au démarrage
init_db()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/notes', methods=['GET'])
def get_notes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT contenu FROM notes")
    notes = [row['contenu'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    note = data.get('note')
    
    if note:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (contenu) VALUES (?)", (note,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Note ajoutée"}), 201
    
    return jsonify({"error": "Note vide"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)