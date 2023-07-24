import uuid
from flask import Flask, request, jsonify

from db.connection import connect_to_db

def create_post(data: dict):
    id = str(uuid.uuid4())

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO post (id, title, description) VALUES (%s, %s, %s)",
                       (id, data['title'], data['description']))
        cursor.execute("SELECT * FROM post WHERE id=%s", (id,))
        values = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            "status": True,
            "message": "Post is created successfully!",
            "post": values
        })
    except Exception as e:
        return jsonify({
            "status": False,
            "message": "Failed to create the post!",
            "error": str(e)
        })
    
def list_posts():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("select * from post")
    values = cursor.fetchall()
    cursor.close()
    conn.close()

    # posts = [dict(i) for i in values]

    return jsonify({
        "status":True,
        "posts":values
    })
