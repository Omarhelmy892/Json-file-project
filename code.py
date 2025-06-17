import json
from pathlib import Path

script_dir = Path(__file__).parent
main_dir = script_dir.parent
json_file = main_dir / "people.json"

if not json_file.exists():
    with open(json_file, "w") as f:
        json.dump({}, f)


file = {}
if json_file.exists() and json_file.stat().st_size > 1:
    try:
        with open(json_file, "r") as f:
            file = json.load(f)
        while True:
            username = input("Enter your profile username: ").lower().strip()
            if username in file:
                print(
                    f"Welcome back, {file[username]['name']}! You are {file[username]['age']} years old."
                )
                print("1-Update info")
                print("2-Delete profile")
                update_info = input("Enter 1 or 2 or exit: ").lower().strip()
                if update_info == "1":
                    name = input("Enter your name: ").lower().strip()
                    while True:
                        age = input("Enter your age: ").lower().strip()
                        if age.isdigit():
                            file[username] = {"name": name, "age": int(age)}
                            with open(json_file, "w") as f:
                                json.dump(file, f, indent=4)
                                print(
                                    "✅ Profile saved! Run the program again to see the greeting"
                                )
                                break
                        else:
                            print("Please enter a valid number: ")
                elif update_info == "2":
                    del file[username]
                    with open(json_file, "w") as f:
                        json.dump(file, f, indent=4)
                        print("🗑️ Profile deleted.")
                else:
                    print("Goodbye. Thanks for using my program")
                    input = ""
                    break
            else:
                print("Not a valid username")
                new_profile = (
                    input("Want to make a new profile or try another username(Y/N): ")
                    .strip()
                    .lower()
                )
                if new_profile == "yes" or new_profile == "y":
                    username = input("Enter your profile username: ").lower().strip()
                    name = input("Enter your name: ").lower().strip()
                    while True:
                        age = input("Enter your age: ").lower().strip()
                        if age.isdigit():
                            file[username] = {"name": name, "age": int(age)}

                            with open(json_file, "w") as f:
                                json.dump(file, f, indent=4)
                                print(
                                    "✅ Profile saved! Run the program again to see the greeting"
                                )
                                input = ""
                                break
                        else:
                            print("Please enter a valid number: ")

    except json.JSONDecodeError:
        print("⚠️ The file is corrupted. Recreating it...")
        json_file.unlink()
else:
    print("🆕 No profile found. Let's create one.")
    username = input("Enter your profile username: ").lower().strip()
    name = input("Enter your name: ").lower().strip()
    while True:
        age = input("Enter your age: ").lower().strip()
        if age.isdigit():
            with open(json_file, "r") as f:
                content = f.read().strip()
                if content:
                    file = json.load(f)
                else:
                    file = {}
            file[username] = {"name": name, "age": int(age)}
            with open(json_file, "w") as f:
                json.dump(file, f, indent=4)
                print("✅ Profile saved! Run the program again to see the greeting")
                input = ""
                break
        else:
            print("Please enter a valid number: ")
