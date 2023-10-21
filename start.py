import os

lock_file = "bot.lock"

def acquire_lock():
    try:
        # Try to create a lock file
        open(lock_file, "x").close()
        return True
    except FileExistsError:
        # Lock file already exists, so another instance is running
        return False

def release_lock():
    # Remove the lock file
    if os.path.exists(lock_file):
        os.remove(lock_file)

if __name__ == "__main__":
    if acquire_lock():
        print("Lock acquired. Starting your bot...")
        # Run your bot script here or any other code you want.
        # Replace the following line with the command to start your bot.
        os.system("python3 main.py")
        release_lock()
        print("Lock released.")
    else:
        print("Another instance of the bot is already running.")
