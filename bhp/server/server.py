from flask import Flask, request, jsonify, render_template
import util
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "client"),
    static_folder=os.path.join(BASE_DIR, "client"),
    static_url_path="/client" 
)

# Load model ONCE when server starts
util.load_saved_artifacts()
@app.route("/")
def home():
    return render_template("app.html")
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({
        'locations': util.get_location_names()
    })

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    return jsonify({
        'estimated_price': util.get_estimated_price(
            location, total_sqft, bhk, bath
        )
    })
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)