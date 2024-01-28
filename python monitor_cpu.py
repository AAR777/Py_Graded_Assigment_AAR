import psutil
import time

def monitor_cpu(threshold):
    try:
        while True:
            # Get CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            print(f"Current CPU Usage: {cpu_usage}%")

            # Check if CPU usage exceeds the predefined threshold
            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeds {threshold}%!")

            # Sleep for a short duration before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Set the predefined threshold for CPU usage (e.g., 80%)
    cpu_threshold = 80

    print(f"Monitoring CPU usage with a threshold of {cpu_threshold}%...\n")
    monitor_cpu(cpu_threshold)
