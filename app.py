from flask import Flask, request
import requests
import time
from collections import defaultdict
from waitress import serve

app = Flask(__name__)

# Dictionary to track UID like timestamps and request count
like_tracker = {}

@app.route('/<uid>', methods=['GET'])
def get_data(uid):
    url = f"https://freefire-virusteam.vercel.app/glfflike?uid={uid}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "Name" in data and "Region" in data and "Likes" in data:
            current_time = time.time()
            
            # Check if user already got likes within 24 hours
            if uid in like_tracker and (current_time - like_tracker[uid]) < 86400:  # 24 hours = 86400 seconds
                return "PLAYER ALREADY GOT LIKES. WAIT 24 HOURS....USE ANTOHER UID..!", 200, {'Content-Type': 'text/plain; charset=utf-8'}
            
            # Update last like time
            like_tracker[uid] = current_time
            
            return f"""PLAYER UID : {uid}
PLAYER NICKNAME : {data["Name"]}
PLAYER REGION : {data["Region"]}
PLAYER LIKES : {data["Likes"]}

PLAYER LIKES ADD : 1
JOIN - https://t.me/Freefirelikess""", 200, {'Content-Type': 'text/plain; charset=utf-8'}
        
        else:
            return "ERROR PLAYER MUST BE 8-10 DEGITS UID!", 404, {'Content-Type': 'text/plain; charset=utf-8'}
    
    except Exception as e:
        return f"Error: Server Error\nMessage: {str(e)}", 500, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("API is running 🔥")
    serve(app, host='0.0.0.0', port=8080)  # Use this for deployment
