
from log_reader import LogFileReader
from log_filter import filter_logs

def main():
    log_file = "logs.txt"
    reader = LogFileReader(log_file)
    print("Welcome to the Log Analyzer")

    while True:
        print("\nMenu:")
        print("1. View All Logs")
        print("2. View Logs by Severity (INFO, WARNING, ERROR)")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for log in reader:
                print(log)
        elif choice == "2":
            severity = input("Enter severity level (INFO, WARNING, ERROR): ").upper()
            filtered_logs = filter_logs(iter(reader), severity)
            print(f"--- {severity} Logs ---")
            for log in filtered_logs:
                print(log)
        elif choice == "3":
            print("Exiting Log Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
