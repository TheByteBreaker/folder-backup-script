import shutil
import os
import datetime

# Replace these with real paths if running on your local Linux system
source_folder = "/home/yourname/Documents" 
backup_folder = "/home/yourname/Backups"   

# Create timestamped backup folder
date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
destination = os.path.join(backup_folder, f"backup_{date}")

try:
    shutil.copytree(source_folder, destination)
    print(f"[✔] Backup completed: {destination}")
except Exception as e:
    print(f"[❌] Backup failed: {e}")
