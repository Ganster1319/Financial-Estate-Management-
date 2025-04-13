import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import func, cast, Integer

from config import config
from database import db
import models

def create_app(config_name='default'):
    """Factory function to create the Flask application"""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)  # Allow requests from frontend origin

    # Register blueprints/routes

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Financial Estate API!"})

    # Client routes
    @app.route('/api/clients', methods=['GET'])
    def get_clients():
        # Filter out deleted clients
        clients = models.Client.query.filter_by(is_deleted=False).all()
        return jsonify([client.to_dict() for client in clients])

    @app.route('/api/clients/<int:client_id>', methods=['GET'])
    def get_client(client_id):
        client = models.Client.query.get_or_404(client_id)
        if client.is_deleted:
            return jsonify({"error": "Client not found"}), 404
        return jsonify(client.to_dict())

    @app.route('/api/clients', methods=['POST'])
    def create_client():
        import logging
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Received request data: {data}")
        data = request.json

        # Basic validation
        if not data.get('full_name') or not data.get('personal_id'):
            return jsonify({"error": "Missing required fields"}), 400

        # Check for duplicate personal_id
        if models.Client.query.filter_by(personal_id=data['personal_id']).first():
            return jsonify({"error": "A client with this personal ID already exists"}), 400

        # Create new client
        new_client = models.Client(
            full_name=data['full_name'],
            personal_id=data['personal_id'],
            date_of_birth=data.get('date_of_birth'),
            gender_id=data.get('gender_id'),
            occupation=data.get('occupation'),
            smoker_status=data.get('smoker_status'),
            # Add other fields as needed
        )

        db.session.add(new_client)
        logging.info(f"Client created successfully: {new_client.to_dict()}")
        db.session.commit()

        return jsonify(new_client.to_dict()), 201

    @app.route('/api/clients/<int:client_id>', methods=['PUT'])
    def update_client(client_id):
        client = models.Client.query.get_or_404(client_id)
        if client.is_deleted:
            return jsonify({"error": "Client not found"}), 404

        data = request.json

        # Update fields
        if 'full_name' in data:
            client.full_name = data['full_name']
        if 'date_of_birth' in data:
            client.date_of_birth = data['date_of_birth']
        if 'gender_id' in data:
            client.gender_id = data['gender_id']
        if 'occupation' in data:
            client.occupation = data['occupation']
        if 'smoker_status' in data:
            client.smoker_status = data['smoker_status']
        # Update other fields as needed

        db.session.commit()

        return jsonify(client.to_dict())

    @app.route('/api/clients/<int:client_id>', methods=['DELETE'])
    def delete_client(client_id):
        client = models.Client.query.get_or_404(client_id)

        # Soft delete
        client.is_deleted = True
        db.session.commit()

        return jsonify({"message": "Client deleted successfully"})

    # Visualization API Endpoints

    # Business Portfolio Endpoints
    @app.route('/api/analytics/gender-distribution', methods=['GET'])
    def get_gender_distribution():
        # Query to count clients by gender
        gender_counts = db.session.query(
            models.Gender.name,
            func.count(models.Client.client_id)
        ).join(
            models.Client, models.Client.gender_id == models.Gender.gender_id
        ).filter(
            models.Client.is_deleted == False
        ).group_by(
            models.Gender.name
        ).all()

        return jsonify({
            'labels': [g[0] for g in gender_counts],
            'data': [g[1] for g in gender_counts]
        })

    @app.route('/api/analytics/policy-type-distribution', methods=['GET'])
    def get_policy_type_distribution():
        # Query to count policies by type
        policy_type_counts = db.session.query(
            models.PolicyType.type_name,
            func.count(models.Policy.policy_id)
        ).join(
            models.Policy, models.Policy.policy_type_id == models.PolicyType.policy_type_id
        ).filter(
            models.Policy.is_deleted == False
        ).group_by(
            models.PolicyType.type_name
        ).all()

        return jsonify({
            'labels': [pt[0] for pt in policy_type_counts],
            'data': [pt[1] for pt in policy_type_counts]
        })

    @app.route('/api/analytics/geographical-distribution', methods=['GET'])
    def get_geographical_distribution():
        # Query to count clients by postal code sector (first 2 digits)
        postal_code_counts = db.session.query(
            func.substr(models.Client.res_postal_code, 1, 2).label('postal_sector'),
            func.count(models.Client.client_id)
        ).filter(
            models.Client.is_deleted == False,
            models.Client.res_postal_code.isnot(None)
        ).group_by(
            'postal_sector'
        ).all()

        return jsonify({
            'postalSectors': [pc[0] for pc in postal_code_counts],
            'counts': [pc[1] for pc in postal_code_counts]
        })

    # Individual Client Portfolio Endpoints
    @app.route('/api/clients/<int:client_id>/policy-types', methods=['GET'])
    def get_client_policy_types(client_id):
        # Query to get policy types for a specific client
        client_policy_types = db.session.query(
            models.PolicyType.type_name,
            func.count(models.Policy.policy_id)
        ).join(
            models.Policy, models.Policy.policy_type_id == models.PolicyType.policy_type_id
        ).filter(
            models.Policy.client_id == client_id,
            models.Policy.is_deleted == False
        ).group_by(
            models.PolicyType.type_name
        ).all()

        return jsonify({
            'labels': [pt[0] for pt in client_policy_types],
            'data': [pt[1] for pt in client_policy_types]
        })

    @app.route('/api/clients/<int:client_id>/insurers', methods=['GET'])
    def get_client_insurers(client_id):
        # Query to get insurers for a specific client
        client_insurers = db.session.query(
            models.Insurer.insurer_name,
            func.count(models.Policy.policy_id)
        ).join(
            models.Policy, models.Policy.insurer_id == models.Insurer.insurer_id
        ).filter(
            models.Policy.client_id == client_id,
            models.Policy.is_deleted == False
        ).group_by(
            models.Insurer.insurer_name
        ).all()

        return jsonify({
            'labels': [i[0] for i in client_insurers],
            'data': [i[1] for i in client_insurers]
        })

    @app.route('/api/clients/<int:client_id>/coverage-by-type', methods=['GET'])
    def get_client_coverage_by_type(client_id):
        # Query to get coverage amounts by event type for a specific client
        coverage_by_type = db.session.query(
            models.EventType.name,
            func.sum(models.Coverage.coverage_amount)
        ).join(
            models.Coverage, models.Coverage.event_type_id == models.EventType.event_type_id
        ).join(
            models.Policy, models.Policy.policy_id == models.Coverage.policy_id
        ).filter(
            models.Policy.client_id == client_id,
            models.Policy.is_deleted == False
        ).group_by(
            models.EventType.name
        ).all()

        return jsonify({
            'labels': [c[0] for c in coverage_by_type],
            'data': [float(c[1]) for c in coverage_by_type]
        })

    @app.route('/api/clients/<int:client_id>/coverage-cessation', methods=['GET'])
    def get_client_coverage_cessation(client_id):
        # Query to get coverage cessation ages for a specific client
        coverage_cessation = db.session.query(
            models.Coverage.pay_till_age,
            func.sum(models.Coverage.coverage_amount)
        ).join(
            models.Policy, models.Policy.policy_id == models.Coverage.policy_id
        ).filter(
            models.Policy.client_id == client_id,
            models.Policy.is_deleted == False,
            models.Coverage.pay_till_age.isnot(None)
        ).group_by(
            models.Coverage.pay_till_age
        ).all()

        return jsonify({
            'ages': [c[0] for c in coverage_cessation],
            'amounts': [float(c[1]) for c in coverage_cessation]
        })

    # TODO: Add routes for policies, claims, documents, etc.

    return app

# Create the application instance
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Set debug=False in production