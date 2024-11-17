import os

def create_log_file(file_name="logs.txt"):
    logs = [
        "INFO: User logged in at 2024-11-09 10:00:00",
        "ERROR: Failed to connect to database at 2024-11-09 10:05:00",
        "INFO: File uploaded at 2024-11-09 10:10:00",
        "WARNING: Low disk space at 2024-11-09 10:15:00",
        "ERROR: Unauthorized access attempt at 2024-11-09 10:20:00",
    ]
    with open(file_name, "w") as f:
        f.writelines(f"{log}\n" for log in logs)

if __name__ == "__main__":
    create_log_file()
    print(f"Log file created at {os.path.abspath('logs.txt')}")
