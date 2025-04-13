from database import db
from datetime import datetime

# --- Lookup Tables ---

class Gender(db.Model):
    __tablename__ = 'genders'
    
    gender_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Gender {self.name}>'

class PolicyStatus(db.Model):
    __tablename__ = 'policy_statuses'
    
    policy_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<PolicyStatus {self.name}>'

class PremiumFrequency(db.Model):
    __tablename__ = 'premium_frequencies'
    
    premium_frequency_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<PremiumFrequency {self.name}>'

class PaymentMode(db.Model):
    __tablename__ = 'payment_modes'
    
    payment_mode_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<PaymentMode {self.name}>'

class EventType(db.Model):
    __tablename__ = 'event_types'
    
    event_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<EventType {self.name}>'

class ClaimStatus(db.Model):
    __tablename__ = 'claim_statuses'
    
    claim_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<ClaimStatus {self.name}>'

# --- Core Data Tables ---

class Client(db.Model):
    __tablename__ = 'clients'

    client_id = db.Column(db.BigInteger, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    personal_id = db.Column(db.String(50), unique=True, nullable=False) # Remember to encrypt this!
    date_of_birth = db.Column(db.Date, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.gender_id'), nullable=True)
    
    # Residential Address
    res_block_house_no = db.Column(db.String(30), nullable=True)
    res_street_name = db.Column(db.String(255), nullable=True)
    res_unit_no = db.Column(db.String(20), nullable=True)
    res_postal_code = db.Column(db.String(10), nullable=True)
    res_country = db.Column(db.String(100), nullable=True, default='Singapore')
    
    mailing_address_same_as_residential = db.Column(db.Boolean, nullable=False, default=True)
    
    # Mailing Address
    mail_block_house_no = db.Column(db.String(30), nullable=True)
    mail_street_name = db.Column(db.String(255), nullable=True)
    mail_unit_no = db.Column(db.String(20), nullable=True)
    mail_postal_code = db.Column(db.String(10), nullable=True)
    mail_country = db.Column(db.String(100), nullable=True, default='Singapore')
    
    occupation = db.Column(db.String(100), nullable=True)
    smoker_status = db.Column(db.Boolean, nullable=True)
    
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    gender = db.relationship('Gender', backref='clients')
    contacts = db.relationship('ClientContact', backref='client', lazy=True)
    policies = db.relationship('Policy', backref='client', lazy=True)
    claims = db.relationship('Claim', backref='client', lazy=True)

    def to_dict(self):
        return {
            'client_id': self.client_id,
            'full_name': self.full_name,
            # 'personal_id': self.personal_id, # Avoid sending raw PII
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'gender': self.gender.name if self.gender else None,
            'occupation': self.occupation,
            'smoker_status': self.smoker_status,
            'is_deleted': self.is_deleted,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ClientContact(db.Model):
    __tablename__ = 'client_contacts'
    
    contact_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.BigInteger, db.ForeignKey('clients.client_id'), nullable=False)
    contact_type = db.Column(db.String(20), nullable=False)
    contact_value = db.Column(db.String(255), nullable=False)
    is_primary = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ClientContact {self.contact_type}: {self.contact_value}>'

class Relationship(db.Model):
    __tablename__ = 'relationships'
    
    relationship_id = db.Column(db.Integer, primary_key=True)
    client_id_1 = db.Column(db.BigInteger, db.ForeignKey('clients.client_id'), nullable=False)
    client_id_2 = db.Column(db.BigInteger, db.ForeignKey('clients.client_id'), nullable=False)
    relationship_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    
    # Define unique constraint
    __table_args__ = (db.UniqueConstraint('client_id_1', 'client_id_2', 'relationship_type'),)
    
    # Relationships
    client_1 = db.relationship('Client', foreign_keys=[client_id_1], backref='relationships_as_first')
    client_2 = db.relationship('Client', foreign_keys=[client_id_2], backref='relationships_as_second')
    
    def __repr__(self):
        return f'<Relationship {self.relationship_type}>'

class Insurer(db.Model):
    __tablename__ = 'insurers'
    
    insurer_id = db.Column(db.Integer, primary_key=True)
    insurer_name = db.Column(db.String(150), nullable=False, unique=True)
    contact_person = db.Column(db.String(150), nullable=True)
    contact_phone = db.Column(db.String(30), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    policies = db.relationship('Policy', backref='insurer', lazy=True)
    
    def __repr__(self):
        return f'<Insurer {self.insurer_name}>'

class PolicyType(db.Model):
    __tablename__ = 'policy_types'
    
    policy_type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    policies = db.relationship('Policy', backref='policy_type', lazy=True)
    
    def __repr__(self):
        return f'<PolicyType {self.type_name}>'

class Policy(db.Model):
    __tablename__ = 'policies'
    
    policy_id = db.Column(db.BigInteger, primary_key=True)
    client_id = db.Column(db.BigInteger, db.ForeignKey('clients.client_id'), nullable=False)
    insurer_id = db.Column(db.Integer, db.ForeignKey('insurers.insurer_id'), nullable=False)
    policy_type_id = db.Column(db.Integer, db.ForeignKey('policy_types.policy_type_id'), nullable=False)
    policy_number = db.Column(db.String(100), nullable=False)
    policy_name = db.Column(db.String(200), nullable=True)
    premium_amount = db.Column(db.Numeric(12, 2), nullable=False)
    premium_frequency_id = db.Column(db.Integer, db.ForeignKey('premium_frequencies.premium_frequency_id'), nullable=False)
    payment_mode_id = db.Column(db.Integer, db.ForeignKey('payment_modes.payment_mode_id'), nullable=False)
    inception_date = db.Column(db.Date, nullable=False)
    maturity_date = db.Column(db.Date, nullable=True)
    policy_status_id = db.Column(db.Integer, db.ForeignKey('policy_statuses.policy_status_id'), nullable=False)
    policy_owner = db.Column(db.String(200), nullable=True)
    life_insured = db.Column(db.String(200), nullable=True)
    premium_term = db.Column(db.String(50), nullable=True)
    pay_till_age = db.Column(db.String(20), nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Define unique constraint
    __table_args__ = (db.UniqueConstraint('insurer_id', 'policy_number'),)
    
    # Relationships
    premium_frequency = db.relationship('PremiumFrequency', backref='policies')
    payment_mode = db.relationship('PaymentMode', backref='policies')
    policy_status = db.relationship('PolicyStatus', backref='policies')
    coverages = db.relationship('Coverage', backref='policy', lazy=True)
    claims = db.relationship('Claim', backref='policy', lazy=True)
    
    def __repr__(self):
        return f'<Policy {self.policy_number}>'

class Coverage(db.Model):
    __tablename__ = 'coverages'
    
    coverage_id = db.Column(db.BigInteger, primary_key=True)
    policy_id = db.Column(db.BigInteger, db.ForeignKey('policies.policy_id', ondelete='CASCADE'), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_types.event_type_id'), nullable=False)
    benefit_category = db.Column(db.String(20), nullable=False)
    coverage_amount = db.Column(db.Numeric(14, 2), nullable=False)
    coverage_details = db.Column(db.Text, nullable=True)
    benefit_name = db.Column(db.String(168), nullable=True)
    pay_till_age = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    event_type = db.relationship('EventType', backref='coverages')
    
    def __repr__(self):
        return f'<Coverage {self.benefit_category} for {self.event_type.name if self.event_type else "Unknown"} event>'

class Document(db.Model):
    __tablename__ = 'documents'
    
    document_id = db.Column(db.BigInteger, primary_key=True)
    related_entity_type = db.Column(db.String(20), nullable=False)
    related_entity_id = db.Column(db.BigInteger, nullable=False)
    document_type = db.Column(db.String(100), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(512), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    upload_timestamp = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Document {self.document_type}: {self.file_name}>'

class Claim(db.Model):
    __tablename__ = 'claims'
    
    claim_id = db.Column(db.BigInteger, primary_key=True)
    policy_id = db.Column(db.BigInteger, db.ForeignKey('policies.policy_id'), nullable=False)
    client_id = db.Column(db.BigInteger, db.ForeignKey('clients.client_id'), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_types.event_type_id'), nullable=False)
    date_of_event = db.Column(db.Date, nullable=False)
    date_submitted = db.Column(db.Date, nullable=False)
    claim_status_id = db.Column(db.Integer, db.ForeignKey('claim_statuses.claim_status_id'), nullable=False)
    amount_claimed = db.Column(db.Numeric(14, 2), nullable=True)
    amount_paid = db.Column(db.Numeric(14, 2), nullable=True)
    payout_date = db.Column(db.Date, nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    event_type = db.relationship('EventType', backref='claims')
    claim_status = db.relationship('ClaimStatus', backref='claims')
    
    def __repr__(self):
        return f'<Claim {self.claim_id} for policy {self.policy_id}>'