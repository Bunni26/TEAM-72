"""SQLAlchemy Models."""

from datetime import datetime
from typing import Optional
from uuid import UUID
import uuid

from sqlalchemy import Column, String, Text, Integer, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.database import Base


class AuditLog(Base):
    """Audit log for all interactions."""
    
    __tablename__ = "audit_logs"
    
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(String(255), nullable=False, index=True)
    user_id = Column(String(255))
    message_type = Column(String(50), nullable=False)
    intent = Column(String(50))
    user_message = Column(Text)
    retrieved_sources = Column(JSON)
    llm_prompt = Column(Text)
    llm_response = Column(Text)
    action_type = Column(String(100))
    action_payload = Column(JSON)
    action_result = Column(JSON)
    error_message = Column(Text)
    latency_ms = Column(Integer)
    token_count = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    metadata = Column(JSON)


class ConversationMemory(Base):
    """Short-term and long-term conversation memory."""
    
    __tablename__ = "conversation_memory"
    
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(String(255), nullable=False, index=True)
    user_id = Column(String(255))
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    embedding_id = Column(String(255))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    expires_at = Column(DateTime(timezone=True))


class Ticket(Base):
    """Support tickets."""
    
    __tablename__ = "tickets"
    
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ticket_number = Column(String(50), unique=True, nullable=False)
    title = Column(String(500), nullable=False)
    description = Column(Text)
    priority = Column(String(20), default="medium")
    status = Column(String(50), default="open")
    category = Column(String(100))
    customer_email = Column(String(255))
    customer_name = Column(String(255))
    assigned_to = Column(String(255))
    session_id = Column(String(255))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime(timezone=True))
    metadata = Column(JSON)


class Document(Base):
    """Document metadata for ingested files."""
    
    __tablename__ = "documents"
    
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String(500), nullable=False)
    file_path = Column(String(1000))
    file_type = Column(String(50))
    file_size = Column(Integer)
    chunk_count = Column(Integer, default=0)
    embedding_ids = Column(JSON)
    status = Column(String(50), default="pending")
    error_message = Column(Text)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    processed_at = Column(DateTime(timezone=True))
    metadata = Column(JSON)
