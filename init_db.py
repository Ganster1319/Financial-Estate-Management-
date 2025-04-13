"""
Database initialization script for Financial Estate application.
This script creates the database tables and runs the initial migrations.
"""

import os
from flask_migrate import Migrate, init, migrate, upgrade
from app import create_app, db

def init_database():
    """Initialize the database with tables from models"""
    app = create_app()
    
    with app.app_context():
        # Create migrations directory if it doesn't exist
        if not os.path.exists('migrations'):
            print("Initializing migrations directory...")
            init()
        
        # Generate initial migration
        print("Creating migration...")
        migrate(message='Initial migration')
        
        # Apply migration to database
        print("Applying migration...")
        upgrade()
        
        print("Database initialization complete!")

if __name__ == '__main__':
    init_database()