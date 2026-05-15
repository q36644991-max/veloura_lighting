# Veloura Lighting - Project Structure

The project is split into two main domains: `user` and `admin`. Each contains its own frontend and backend services.

## Directory Structure

```
/user
  /frontend     - Public-facing luxury showroom website
  /backend      - Public services (Gateway, Product, Booking, etc.)
/admin
  /frontend     - Administrative dashboard and login
  /backend      - Management and Authentication services
```

## Running the Project

### User Domain
- Navigate to the `user` folder.
- Run `python run.py` to start the backend and serve the frontend.
- **The showroom will be available at: http://localhost:3000**

### Admin Domain
- Navigate to the `admin` folder.
- Run `python run.py` to start the management services and serve the dashboard.
- **The admin panel will be available at: http://localhost:4000/login.html**

## Configuration
Before running the services, ensure you have configured the `.env` file in the root directory:
1. Open `.env` and fill in your Supabase credentials.
2. Set a secure `JWT_SECRET`.
3. Configure service ports if necessary.

## Tech Stack
- **Frontend**: HTML5, Vanilla JS, Tailwind CSS (CDN).
- **Backend**: Python Flask Microservices.
- **Visuals**: AI-Generated High-Resolution Imagery.

## Deployment (Render)

This project is configured for separate User and Admin deployments on Render using the `render.yaml` Blueprint.

### Services Defined:
1.  **veloura-user-frontend**: Static site for the customer showroom.
2.  **veloura-user-backend**: Microservices gateway and API for the user domain.
3.  **veloura-admin-frontend**: Static site for the administrative dashboard.
4.  **veloura-admin-backend**: Management services and authentication API.

### Steps to Deploy:
1.  Connect your GitHub repository to Render.
2.  Render will automatically detect the `render.yaml` file.
3.  Apply the Blueprint to create all 4 services.
4.  Ensure you set the necessary environment variables (like Supabase keys) in the Render dashboard for both backend services.
