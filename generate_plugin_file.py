import json

with open("plugin.json", "r") as f:
    data = json.load(f)

data["ID"] = "5f48576d-efe7-4562-a4ed-fe64455f1ac1"
data["Name"] = "Flow Load Notification"
data["Website"] = (
    f"https://github.com/cibere/Flow.Launcher.Plugin.FlowLoadNotification/tree/v{data['Version']}"
)

with open("plugin.json", "w") as f:
    json.dump(data, f)

print("New plugin.json contents:")
print(json.dumps(data, indent=4))
