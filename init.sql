-- Initialize Support Automation Database

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Audit logs table
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255) NOT NULL,
    user_id VARCHAR(255),
    message_type VARCHAR(50) NOT NULL, -- 'user', 'assistant', 'system', 'action'
    intent VARCHAR(50), -- 'answer', 'action', 'unknown'
    user_message TEXT,
    retrieved_sources JSONB,
    llm_prompt TEXT,
    llm_response TEXT,
    action_type VARCHAR(100),
    action_payload JSONB,
    action_result JSONB,
    error_message TEXT,
    latency_ms INTEGER,
    token_count INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    metadata JSONB
);

-- Conversation memory table
CREATE TABLE IF NOT EXISTS conversation_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255) NOT NULL,
    user_id VARCHAR(255),
    role VARCHAR(20) NOT NULL, -- 'user', 'assistant', 'system'
    content TEXT NOT NULL,
    embedding_id VARCHAR(255), -- Reference to vector DB
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE
);

-- Tickets table (mock ticketing system)
CREATE TABLE IF NOT EXISTS tickets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ticket_number VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    priority VARCHAR(20) DEFAULT 'medium', -- 'low', 'medium', 'high', 'urgent'
    status VARCHAR(50) DEFAULT 'open', -- 'open', 'in_progress', 'resolved', 'closed'
    category VARCHAR(100),
    customer_email VARCHAR(255),
    customer_name VARCHAR(255),
    assigned_to VARCHAR(255),
    session_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    resolved_at TIMESTAMP WITH TIME ZONE,
    metadata JSONB
);

-- Documents metadata table
CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    filename VARCHAR(500) NOT NULL,
    file_path VARCHAR(1000),
    file_type VARCHAR(50),
    file_size INTEGER,
    chunk_count INTEGER DEFAULT 0,
    embedding_ids JSONB, -- Array of vector DB IDs
    status VARCHAR(50) DEFAULT 'pending', -- 'pending', 'processing', 'completed', 'failed'
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    processed_at TIMESTAMP WITH TIME ZONE,
    metadata JSONB
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_audit_logs_session_id ON audit_logs(session_id);
CREATE INDEX IF NOT EXISTS idx_audit_logs_created_at ON audit_logs(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_audit_logs_intent ON audit_logs(intent);
CREATE INDEX IF NOT EXISTS idx_conversation_memory_session_id ON conversation_memory(session_id);
CREATE INDEX IF NOT EXISTS idx_conversation_memory_created_at ON conversation_memory(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_tickets_status ON tickets(status);
CREATE INDEX IF NOT EXISTS idx_tickets_created_at ON tickets(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_documents_status ON documents(status);

-- Insert some sample data for testing
INSERT INTO tickets (ticket_number, title, description, priority, status, category, customer_email, customer_name)
VALUES 
    ('TKT-001', 'Sample Ticket 1', 'This is a sample ticket for testing', 'medium', 'open', 'general', 'test@example.com', 'Test User'),
    ('TKT-002', 'Billing Issue', 'Customer reported billing discrepancy', 'high', 'in_progress', 'billing', 'billing@example.com', 'Billing User')
ON CONFLICT (ticket_number) DO NOTHING;


