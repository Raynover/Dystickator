import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import run_calculation

app = Flask(__name__)
CORS(app)  # Enables local browser testing without security blocks

# Set up the uploads folder path (relative to this app.py file)
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Calculate
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    
    # Extract inputs safely with defaults if empty
    try:
        horiz = int(data.get('horiz', 50))
        vert = int(data.get('vert', 50))
        userquant = int(data.get('quantity', 400))
        
        # Guard rails for inputs
        if horiz <= 0 or vert <= 0 or userquant <= 0:
            return jsonify({"error": "Inputs must be positive numbers"}), 400
            
        # Run calculation
        results = run_calculation(horiz, vert, userquant)
        return jsonify(results)
        
    except ValueError:
        return jsonify({"error": "Invalid format provided"}), 400

# Upload
@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    # Check actual file size (5MB limit safeguard)
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)  # Reset pointer back to the beginning so we can save it
    
    if size > 5 * 1024 * 1024:
        return jsonify({"error": "File size exceeds 5MB limit"}), 400
        
    # Securely save file inside the uploads directory
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    return jsonify({
        "message": "File uploaded successfully",
        "filename": file.filename
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
