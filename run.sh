
#!/bin/bash

# Install Flask and Flask-CORS if not installed
pip install flask flask-cors

# Install additional required packages from requirements.txt
pip install -r requirements.txt

# Run the Flask application
python app.py
