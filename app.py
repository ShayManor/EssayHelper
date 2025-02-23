from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


from ask_ai import ask_ai

@app.route("/process_essay", methods=["POST"])
def process_essay():
    data = request.json
    essay = data.get('essay', '')
    prompt = f"Provide constructive feedback to improve the following essay:\n\n{essay}"
    feedback = ask_ai(prompt)
    return {"feedback": feedback}

@app.route("/example", methods=["GET"])
def get_example():
    example_essay = (
        "The impact of technology on education has been profound over the past few decades. "
        "With the advent of digital tools and online resources, learning has become more accessible and engaging. "
        "Students can now access a wealth of information at their fingertips, collaborate with peers remotely, "
        "and utilize interactive platforms to enhance their understanding of complex subjects. "
        "However, this technological advancement also presents challenges such as ensuring equal access for all students "
        "and maintaining the quality of education in a digital realm. Balancing these benefits and drawbacks is essential "
        "for the future of educational systems worldwide."
    )
    return {"example": example_essay}


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "templates/index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
