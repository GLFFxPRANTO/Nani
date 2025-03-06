from flask import Flask, jsonify
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/<uid>', methods=['GET'])
def get_data(uid):
    url = f"https://freefire-virusteam.vercel.app/glfflike?uid={uid}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if "Name" in data and "Region" in data and "Likes" in data:
            result = f"""PLAYER UID : {uid}
PLAYER NICKNAME : {data["Name"]}
PLAYER REGION : {data["Region"]}
PLAYER LIKES : {data["Likes"]}
PLAYER LIKES ADD : 1"""  # Fake likes add message
            return result, 200, {'Content-Type': 'text/plain; charset=utf-8'}
        else:
            return "Error: Name, Region, or Likes not found!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("API is running 🔥")
    # app.run(host='127.0.0.1', port=8080)  # For local testing
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
