import subprocess
import time
import sys
import os

# Define the services to run for the Admin domain
services = [
    {"name": "Auth Service", "path": "backend/auth-service/app.py", "port": 5001},
    {"name": "Management Service", "path": "backend/management-service.py", "port": 6000},
]

processes = []

def run_services():
    print("--- Starting Veloura Lighting: Admin Services ---")
    for service in services:
        print(f"Starting {service['name']} on port {service['port']}...")
        script_path = os.path.join(os.path.dirname(__file__), service['path'])
        proc = subprocess.Popen([sys.executable, script_path])
        processes.append(proc)
        time.sleep(1)
    
    # Start Frontend Server
    print("Starting Frontend Server on port 4000...")
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    frontend_proc = subprocess.Popen([sys.executable, "-m", "http.server", "4000"], cwd=frontend_dir)
    processes.append(frontend_proc)
    
    print("\n" + "="*50)
    print(f"VELOURA LIGHTING - ADMIN INTERFACE")
    print(f"Access the admin panel at: http://localhost:4000/login.html")
    print("="*50 + "\n")
    
    print("All Admin services are running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping services...")
        for proc in processes:
            proc.terminate()
        print("All services stopped.")

if __name__ == "__main__":
    run_services()
