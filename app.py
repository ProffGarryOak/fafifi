from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

questions = [
    {"question": "Arrange these colors in the rainbow order:", "options": ["Red", "Blue", "Green", "Yellow"], "correct_order": ["Red", "Yellow", "Green", "Blue"]},
    {"question": "Arrange these planets in the correct order from the Sun:", "options": ["Earth", "Mars", "Venus", "Mercury"], "correct_order": ["Mercury", "Venus", "Earth", "Mars"]},
    {"question": "Arrange these numbers in ascending order:", "options": ["10", "1", "5", "7"], "correct_order": ["1", "5", "7", "10"]},
    {"question": "Arrange these animals by size (small to large):", "options": ["Elephant", "Mouse", "Horse", "Cat"], "correct_order": ["Mouse", "Cat", "Horse", "Elephant"]},
    {"question": "Arrange these days of the week in order:", "options": ["Wednesday", "Monday", "Friday", "Tuesday"], "correct_order": ["Monday", "Tuesday", "Wednesday", "Friday"]},
    {"question": "Arrange these fruits in order of sweetness (least to most):", "options": ["Lemon", "Apple", "Banana", "Mango"], "correct_order": ["Lemon", "Apple", "Banana", "Mango"]},
    {"question": "Arrange these planets by size (smallest to largest):", "options": ["Mars", "Venus", "Earth", "Jupiter"], "correct_order": ["Mars", "Venus", "Earth", "Jupiter"]},
    {"question": "Arrange these numbers in descending order:", "options": ["8", "3", "1", "5"], "correct_order": ["8", "5", "3", "1"]},
    {"question": "Arrange these books by publication year (oldest to newest):", "options": ["1984", "Harry Potter", "The Hobbit", "The Catcher in the Rye"], "correct_order": ["The Catcher in the Rye", "1984", "The Hobbit", "Harry Potter"]},
    {"question": "Arrange these colors in the correct order for a traffic light:", "options": ["Green", "Red", "Yellow", "Orange"], "correct_order": ["Red", "Yellow", "Green"]}
]

@app.route('/')
def index():
    # Randomize the order of options for each question
    for question in questions:
        question["shuffled_options"] = random.sample(question["options"], len(question["options"]))
    return render_template('index.html', questions=questions)

@app.route('/check_sequence/<int:question_id>/<sequence>')
def check_sequence(question_id, sequence):
    question = questions[question_id]
    correct_order = ",".join(question['correct_order'])
    
    if sequence == correct_order:
        return jsonify({"status": "correct"})
    else:
        return jsonify({"status": "incorrect", "correct_order": correct_order})

if __name__ == "__main__":
    app.run(debug=True)
