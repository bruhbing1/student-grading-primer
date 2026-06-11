from flask import Flask, jsonify, request
from flask_cors import CORS

import db
import math
app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students", methods=["GET"])
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """

    
    # TODO: replace with your implementation. This is a mock response
    return jsonify(db.get_all_students()), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    student_data = request.json
    ret = db.insert_student(student_data.get('name'), student_data.get('course'), student_data.get('mark'))

    if ret:
        return jsonify(ret), 200

    return jsonify({"error": "Not found"}), 500


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """

    student_data = request.json
    ret = db.update_student(student_id, student_data.get('name'), student_data.get('course'), student_data.get('mark'))
    
    if ret is not None:
        return jsonify(ret), 200

    return jsonify({"error": "Not found"}), 404

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """

    ret = db.delete_student(student_id)
    if ret is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(ret), 200



@app.route("/stats",  methods=["GET"])
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """
    allStudents = db.get_all_students()
    print(allStudents)
    if len(allStudents) == 0:
        return jsonify({
            'count': 0,
            'average': 0,
            'min': 0,
            'max': 0
        }), 200
  
    minMark = math.inf
    maxMark = 0
    totalMark = 0
    print(allStudents, flush=True)
    for i in allStudents:

        mark = i.get('mark')
        if mark is None:
            continue
        totalMark += mark

        if mark > maxMark:
            maxMark = mark
        if mark < minMark:
            minMark = mark
    average = totalMark / len(allStudents)

    return jsonify({'count': len(allStudents), 'average': average, 'min': minMark, 'max': maxMark}), 200



@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
