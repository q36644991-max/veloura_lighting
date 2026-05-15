import subprocess
import time
import sys
import os

# Define the services to run for the User domain
services = [
    {"name": "Gateway", "path": "backend/gateway/app.py", "port": 5000},
    {"name": "Product Service", "path": "backend/product_service/app.py", "port": 5002},
    {"name": "Booking Service", "path": "backend/booking_service/app.py", "port": 5003},
    {"name": "Portfolio Service", "path": "backend/portfolio_service/app.py", "port": 5004},
    {"name": "Email Service", "path": "backend/email_service/app.py", "port": 5005},
]

processes = []

def run_services():
    print("--- Starting Veloura Lighting: User Services ---")
    for service in services:
        print(f"Starting {service['name']} on port {service['port']}...")
        # Get absolute path for reliability
        script_path = os.path.join(os.path.dirname(__file__), service['path'])
        proc = subprocess.Popen([sys.executable, script_path])
        processes.append(proc)
        time.sleep(1) # Small delay to avoid port conflicts during startup
    
    # Start Frontend Server
    print("Starting Frontend Server on port 3000...")
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    frontend_proc = subprocess.Popen([sys.executable, "-m", "http.server", "3000"], cwd=frontend_dir)
    processes.append(frontend_proc)
    
    print("\n" + "="*50)
    print(f"VELOURA LIGHTING - USER INTERFACE")
    print(f"Access the showroom at: http://localhost:3000")
    print("="*50 + "\n")
    
    print("All User services are running. Press Ctrl+C to stop.")
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
