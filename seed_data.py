"""
Seed script to populate the database with initial lookup values and sample data.
Run this after setting up the database with Flask-Migrate.
"""

import os
import sys
from datetime import datetime, date
from app import create_app, db
import models

def seed_lookup_tables():
    """Populate lookup tables with standard values"""
    
    # Genders
    genders = [
        models.Gender(name='Male'),
        models.Gender(name='Female')
    ]
    
    # Policy Statuses
    policy_statuses = [
        models.PolicyStatus(name='Active', description='Policy is in force'),
        models.PolicyStatus(name='Lapsed', description='Policy has lapsed due to non-payment'),
        models.PolicyStatus(name='Matured', description='Policy has reached its maturity date'),
        models.PolicyStatus(name='Surrendered', description='Policy has been surrendered by the policyholder')
    ]
    
    # Premium Frequencies
    premium_frequencies = [
        models.PremiumFrequency(name='Monthly'),
        models.PremiumFrequency(name='Quarterly'),
        models.PremiumFrequency(name='Semi-Annually'),
        models.PremiumFrequency(name='Annually')
    ]
    
    # Payment Modes
    payment_modes = [
        models.PaymentMode(name='GIRO'),
        models.PaymentMode(name='Credit Card'),
        models.PaymentMode(name='Bank Transfer'),
        models.PaymentMode(name='Cheque')
    ]
    
    # Event Types
    event_types = [
        models.EventType(name='Death', description='Death benefit'),
        models.EventType(name='Total & Permanent Disability', description='TPD benefit'),
        models.EventType(name='Critical Illness', description='CI benefit'),
        models.EventType(name='Early Stage CI', description='Early stage critical illness'),
        models.EventType(name='Long-Term Care', description='LTC benefit'),
        models.EventType(name='Personal Accident', description='PA coverage'),
        models.EventType(name='Hospital & Surgical', description='H&S coverage')
    ]
    
    # Claim Statuses
    claim_statuses = [
        models.ClaimStatus(name='Submitted'),
        models.ClaimStatus(name='Processing'),
        models.ClaimStatus(name='Info Requested'),
        models.ClaimStatus(name='Approved'),
        models.ClaimStatus(name='Rejected'),
        models.ClaimStatus(name='Paid')
    ]
    
    # Add all to session
    for items in [genders, policy_statuses, premium_frequencies, payment_modes, event_types, claim_statuses]:
        db.session.add_all(items)
    
    # Commit the lookup tables
    db.session.commit()
    print("Lookup tables populated successfully")

def seed_sample_data():
    """Add sample clients, insurers, policies, etc."""
    
    # Sample Insurers
    insurers = [
        models.Insurer(
            insurer_name='Prudential Assurance',
            contact_person='John Smith',
            contact_phone='+65 6123 4567',
            website='https://www.prudential.com.sg'
        ),
        models.Insurer(
            insurer_name='AIA Singapore',
            contact_person='Jane Doe',
            contact_phone='+65 6876 5432',
            website='https://www.aia.com.sg'
        ),
        models.Insurer(
            insurer_name='Great Eastern Life',
            contact_person='Robert Johnson',
            contact_phone='+65 6321 7654',
            website='https://www.greateasternlife.com'
        )
    ]
    db.session.add_all(insurers)
    db.session.commit()
    
    # Sample Policy Types
    policy_types = [
        models.PolicyType(
            type_name='Whole Life',
            description='Provides coverage for the entire lifetime of the insured'
        ),
        models.PolicyType(
            type_name='Term Life',
            description='Provides coverage for a specified term/period'
        ),
        models.PolicyType(
            type_name='Endowment',
            description='Provides both insurance coverage and savings component'
        ),
        models.PolicyType(
            type_name='Investment-Linked',
            description='Combines insurance coverage with investment'
        ),
        models.PolicyType(
            type_name='Health Insurance',
            description='Covers medical expenses'
        )
    ]
    db.session.add_all(policy_types)
    db.session.commit()
    
    # Sample Clients
    clients = [
        models.Client(
            full_name='John Doe',
            personal_id='S1234567A',  # In production, encrypt this!
            date_of_birth=date(1985, 5, 15),
            gender_id=1,  # Male
            occupation='Software Engineer',
            smoker_status=False,
            res_block_house_no='123',
            res_street_name='Main Street',
            res_unit_no='#12-34',
            res_postal_code='123456',
            res_country='Singapore'
        ),
        models.Client(
            full_name='Jane Smith',
            personal_id='S7654321B',  # In production, encrypt this!
            date_of_birth=date(1990, 11, 20),
            gender_id=2,  # Female
            occupation='Marketing Manager',
            smoker_status=False,
            res_block_house_no='456',
            res_street_name='High Street',
            res_unit_no='#05-67',
            res_postal_code='654321',
            res_country='Singapore'
        )
    ]
    db.session.add_all(clients)
    db.session.commit()
    
    # Sample Client Contacts
    contacts = [
        models.ClientContact(
            client_id=1,
            contact_type='Mobile',
            contact_value='+65 9123 4567',
            is_primary=True
        ),
        models.ClientContact(
            client_id=1,
            contact_type='Email',
            contact_value='john.doe@example.com',
            is_primary=True
        ),
        models.ClientContact(
            client_id=2,
            contact_type='Mobile',
            contact_value='+65 8765 4321',
            is_primary=True
        ),
        models.ClientContact(
            client_id=2,
            contact_type='Email',
            contact_value='jane.smith@example.com',
            is_primary=True
        )
    ]
    db.session.add_all(contacts)
    db.session.commit()
    
    # Sample Policies
    policies = [
        models.Policy(
            client_id=1,
            insurer_id=1,
            policy_type_id=1,  # Whole Life
            policy_number='POL-1001',
            policy_name='PruLife',
            premium_amount=1200.00,
            premium_frequency_id=4,  # Annually
            payment_mode_id=1,  # GIRO
            inception_date=date(2020, 1, 15),
            maturity_date=None,  # Whole life policies don't have maturity dates
            policy_status_id=1,  # Active
            remarks='Main life insurance policy'
        ),
        models.Policy(
            client_id=1,
            insurer_id=2,
            policy_type_id=5,  # Health Insurance
            policy_number='AIA-H2001',
            policy_name='AIA HealthShield Gold Max',
            premium_amount=600.00,
            premium_frequency_id=4,  # Annually
            payment_mode_id=2,  # Credit Card
            inception_date=date(2020, 3, 10),
            maturity_date=None,
            policy_status_id=1,  # Active
            remarks='Integrated Shield Plan'
        ),
        models.Policy(
            client_id=2,
            insurer_id=3,
            policy_type_id=3,  # Endowment
            policy_number='GE-E3001',
            policy_name='Great Eastern Smart Saver',
            premium_amount=3000.00,
            premium_frequency_id=4,  # Annually
            payment_mode_id=1,  # GIRO
            inception_date=date(2019, 7, 20),
            maturity_date=date(2039, 7, 20),  # 20-year endowment
            policy_status_id=1,  # Active
            remarks='Education savings plan'
        )
    ]
    db.session.add_all(policies)
    db.session.commit()
    
    # Sample Coverages
    coverages = [
        models.Coverage(
            policy_id=1,
            event_type_id=1,  # Death
            benefit_category='Basic',
            coverage_amount=500000.00,
            coverage_details='Death benefit'
        ),
        models.Coverage(
            policy_id=1,
            event_type_id=2,  # TPD
            benefit_category='Basic',
            coverage_amount=500000.00,
            coverage_details='Total & Permanent Disability benefit'
        ),
        models.Coverage(
            policy_id=1,
            event_type_id=3,  # CI
            benefit_category='Supplementary',
            coverage_amount=250000.00,
            coverage_details='Critical Illness Accelerator rider'
        ),
        models.Coverage(
            policy_id=2,
            event_type_id=7,  # H&S
            benefit_category='Basic',
            coverage_amount=1000000.00,
            coverage_details='Hospitalization coverage'
        ),
        models.Coverage(
            policy_id=3,
            event_type_id=1,  # Death
            benefit_category='Basic',
            coverage_amount=100000.00,
            coverage_details='Death benefit'
        )
    ]
    db.session.add_all(coverages)
    db.session.commit()
    
    print("Sample data populated successfully")

def main():
    """Main function to seed the database"""
    app = create_app()
    with app.app_context():
        print("Starting database seeding...")
        
        # Check if tables already have data
        if models.Gender.query.first() is not None:
            print("Database already contains data. Skipping lookup tables.")
        else:
            seed_lookup_tables()
        
        # Check if sample data already exists
        if models.Client.query.first() is not None:
            print("Sample data already exists. Skipping sample data.")
        else:
            seed_sample_data()
        
        print("Database seeding completed successfully!")

if __name__ == '__main__':
    main()