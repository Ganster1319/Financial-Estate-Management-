# Financial-Estate-Management-

# Financial Estate App

A comprehensive application for managing clients personal information, insurance policy information and storing past claims information. This application helps financial advisors track their clients' insurance portfolios, policy details, and claims.

## Features

- Client management (personal details, contact information)
- Policy tracking (policy details, coverage, premiums)
- Past Claims record
- Financial Service Manager portfolio dashboard with visualizations
- Individual Client portfolio dashboard with visualizations
- Document management

## Tech Stack

### Frontend
- React (with React Router for navigation)
- Tailwind CSS for styling
- Recharts for data visualization
- Lucide icons

### Backend
- Flask (Python web framework)
- SQLite for app development
- SQLAlchemy ORM
- PostgreSQL database
- Flask-Migrate for database migrations

## Setup Instructions

### Prerequisites
- Node.js and npm
- Python 3.8+
- PostgreSQL
- SQLite

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Configure the database:
   - Update the `.env` file with your PostgreSQL credentials
   - Make sure PostgreSQL is running

6. Initialize the database:
   ```
   python init_db.py
   ```

7. Seed the database with initial data:
   ```
   python seed_data.py
   ```

8. Run the Flask application:
   ```
   python app.py
   ```

The backend API will be available at http://localhost:5000

### Frontend Setup

1. From the project root, install dependencies:
   ```
   npm install
   ```

2. Start the development server:
   ```
   npm run dev
   ```

The frontend application will be available at http://localhost:5173

## Project Structure

```
financial-estate-app/
├── backend/                 # Flask backend
│   ├── __init__.py
│   ├── app.py               # Main application file
│   ├── config.py            # Configuration
│   ├── database.py          # Database setup
│   ├── models.py            # Database models
│   ├── seed_data.py         # Sample data script
│   ├── init_db.py           # Database initialization
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
│
├── src/                     # React frontend
│   ├── components/          # Reusable UI components
│   ├── pages/               # Page components
│   ├── services/            # API services
│   ├── App.jsx              # Main React component
│   ├── main.jsx             # Entry point
│   └── index.css            # Global styles
│
├── public/                  # Static assets
├── Documentations/          # Project documentation
├── package.json             # Node.js dependencies
└── README.md                # Project documentation
```

## Database Schema

The database schema is defined in `Documentations/FE Database Schema V2.md` and implemented in `backend/models.py`.

## UI/UX Design

The UI/UX design plan is available in `Documentations/FE UI.md`.

## License

[Your License Here]
