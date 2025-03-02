# Roblox Status Sniper

Roblox Status Sniper is a Python script that tracks the online status of a specific Roblox user in real time. It checks if the user is online, in-game, or using Roblox Studio, and displays their location if applicable.

## Features
- Retrieves user ID from a given Roblox username
- Tracks and displays the user's online status
- Shows game location and Place ID if the user is in a game
- Updates in real-time every 5 seconds
- Handles rate-limiting from Roblox API

## Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation
1. Clone this repository:
   ```sh
   git clone git@github.com:Chromeyc/RBX-Status-tracker.git
   cd RBX-Status-tracker
   ```

2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
1. Run the script:
   ```sh
   python status.py
   ```
2. Enter the Roblox username you want to track.
3. The script will display the user's status and update in real time.

## Example Output
```
Enter Roblox username to snipe: ExampleUser
Starting status sniper for user: ExampleUser
Found user ID: 123456789

[2025-03-02 14:30:00]
Status: In-Game
Location: Adopt Me!
Place ID: 1234567890
```

## Notes
- The script will handle rate-limiting by waiting 30 seconds when necessary.
- Make sure you use this responsibly and follow Roblox's terms of service.

## License
This project is licensed under the MIT License.

## Disclaimer
This project is for educational purposes only. The developer is not responsible for any misuse of this script.

## Contributions
Pull requests are welcome! If you find any issues, feel free to open an issue on the repository.

---
Made with ❤️ by smh

