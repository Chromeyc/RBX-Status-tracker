import requests
import time
from datetime import datetime

class RobloxStatusSniper:
    def __init__(self, username):
        self.username = username
        self.last_status = None
        self.user_id_url = "https://users.roblox.com/v1/usernames/users"
        self.presence_url = "https://presence.roblox.com/v1/presence/users"
        
    def get_user_id(self):
        try:
            payload = {
                "usernames": [self.username],
                "excludeBannedUsers": True
            }
            response = requests.post(self.user_id_url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                if data["data"]:
                    return data["data"][0]["id"]
            return None
        except Exception as e:
            print(f"Error getting user ID: {e}")
            return None
    
    def get_status(self, user_id):
        try:
            payload = {"userIds": [user_id]}
            response = requests.post(self.presence_url, json=payload)
            
            if response.status_code == 200:
                data = response.json()["userPresences"][0]
                presence_type = data.get("userPresenceType", 0)
                status_types = {
                    0: "Offline",
                    1: "Online (Website)",
                    2: "In-Game",
                    3: "In-Studio"
                }
                
                return {
                    "online": presence_type != 0,
                    "presence": status_types.get(presence_type, "Unknown"),
                    "game": data.get("lastLocation", "Unknown"),
                    "placeId": data.get("placeId", None),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            elif response.status_code == 429:
                print("Rate limited! Waiting 30 seconds...")
                time.sleep(30)
                return None
            else:
                print(f"Error: Status code {response.status_code}")
                return None
        except Exception as e:
            print(f"Error checking status: {e}")
            return None

    def start_sniping(self):
        print(f"Starting status sniper for user: {self.username}")
        user_id = self.get_user_id()
        
        if not user_id:
            print(f"Could not find user: {self.username}")
            return
            
        print(f"Found user ID: {user_id}")
        
        while True:
            status = self.get_status(user_id)
            
            if status:
                if status != self.last_status:
                    print(f"\n[{status['timestamp']}]")
                    print(f"Status: {status['presence']}")
                    print(f"Location: {status['game']}")
                    if status['placeId']:
                        print(f"Place ID: {status['placeId']}")
                    self.last_status = status
            
            time.sleep(5)

if __name__ == "__main__":
    username = input("Enter Roblox username to snipe: ")
    sniper = RobloxStatusSniper(username)
    sniper.start_sniping()
