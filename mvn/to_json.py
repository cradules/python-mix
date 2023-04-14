import json


def maven_command_to_json(maven_command):
    parts = maven_command.split()
    json_obj = {}

    for i, part in enumerate(parts):
        if part.startswith("-D"):
            key_value = part[2:].split("=", 1)
            json_key = key_value[0]
            json_value = key_value[1]
            json_obj[json_key] = json_value

    return json_obj


# Read commands from a file
filename = "maven_commands.txt"
with open(filename, "r") as file:
    maven_commands = file.read().splitlines()

json_list = []

# Loop through commands and convert each to JSON object
for command in maven_commands:
    json_obj = maven_command_to_json(command)
    json_list.append(json_obj)

# Print JSON objects
for json_obj in json_list:
    json_string = json.dumps(json_obj, indent=2)
    print(json_string + ",")
    print()