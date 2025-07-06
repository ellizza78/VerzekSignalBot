from scanner import scan_all_markets
import time

if __name__ == "__main__":
    while True:
        scan_all_markets()
        time.sleep(300)  # Check every 5 minutes
