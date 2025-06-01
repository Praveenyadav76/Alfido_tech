tasks = []

def show_menu():
    print("\n🧾 What would you like to do?")
    print("1️⃣  Add a task")
    print("2️⃣  Remove a task")
    print("3️⃣  View my to-do list")
    print("4️⃣  Exit")

def add_task():
    task = input("\n✍️  What's the task you'd like to add? ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Got it! '{task}' has been added to your list.")
    else:
        print("⚠️ Hmm, looks like you didn’t type anything. Try again!")

def remove_task():
    if not tasks:
        print("\n📭 Nothing to remove — your list is empty.")
        return

    view_tasks()
    try:
        index = int(input("\n🗑️  Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️  Removed: '{removed}'. One less thing to worry about!")
        else:
            print("❌ That number doesn’t match any task. Give it another shot.")
    except ValueError:
        print("🚫 That’s not a number. Try again with a valid task number.")

def view_tasks():
    if not tasks:
        print("\n📭 Your to-do list is looking squeaky clean. Nothing here yet!")
    else:
        print("\n📝 Here's what's on your list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    print("👋 Hey there! Ready to conquer your tasks?")
    while True:
        show_menu()
        choice = input("\n🔢 Pick an option (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("\n👋 All done? Nice work. See you next time!")
            break
        else:
            print("🤷 Oops! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
