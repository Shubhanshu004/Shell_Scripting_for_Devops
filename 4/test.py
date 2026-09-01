import requests
import subprocess

# File handling
with open("output.txt", "w") as f:
    f.write("Hello from Python\n")

with open("output.txt", "r") as f:
    print("File content:", f.read())

# API request
response = requests.get("http://localhost")
print("Status code:", response.status_code)

# Run a shell command
result = subprocess.run(["whoami"], capture_output=True, text=True)
print("Whoami output:", result.stdout)
