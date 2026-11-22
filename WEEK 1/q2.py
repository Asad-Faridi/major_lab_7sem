user_preferences = {
    "theme": "dark",
    "notifications": True,
    "language": "en-US",
    "font_size": 14
}
print(user_preferences.get("currency","USD"))
user_preferences["font_size"] = 16
print(user_preferences)
user_preferences.pop("notifications")
print(user_preferences)
for key, value in user_preferences.items():
    print(key, ":", value)