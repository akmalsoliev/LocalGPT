import json

def load_sys_message(sys_message_path, json_path):
    txt_message = open(sys_message_path, "r").readlines()

    with open(json_path, "r") as f:
        json_file = json.load(f)

    json_file["content"] = txt_message

    with open(json_path, "w") as f:
        json.dump(json_file, f)
    

if __name__ == "__main__":
    sys_path = "config/system_message.txt"
    json_path = "config/settings.json"
    load_sys_message(sys_path, json_path)

