-- ==========================================
-- Business Operations AI Platform
-- Database Schema v1
-- ==========================================

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    phone VARCHAR(30),
    email VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    address TEXT,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE shifts (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    location_id INTEGER REFERENCES locations(id),

    shift_date DATE NOT NULL,

    start_time TIME,
    end_time TIME,

    worked_hours DECIMAL(5,2),

    status VARCHAR(30) DEFAULT 'scheduled',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sales_reports (
    id SERIAL PRIMARY KEY,

    shift_id INTEGER REFERENCES shifts(id),

    free_count INTEGER DEFAULT 0,
    classic_count INTEGER DEFAULT 0,
    premium_count INTEGER DEFAULT 0,
    diamond_count INTEGER DEFAULT 0,

    revenue DECIMAL(12,2) DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics_snapshots (
    id SERIAL PRIMARY KEY,

    snapshot_date DATE NOT NULL,

    total_revenue DECIMAL(12,2),
    total_hours DECIMAL(10,2),
    total_shifts INTEGER,
    total_employees INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- Indexes
-- ==========================================

CREATE INDEX idx_shifts_employee
ON shifts(employee_id);

CREATE INDEX idx_shifts_location
ON shifts(location_id);

CREATE INDEX idx_reports_shift
ON sales_reports(shift_id);

CREATE INDEX idx_analytics_date
ON analytics_snapshots(snapshot_date);
-- ==========================================
-- Extended Operations Tables
-- ==========================================

CREATE TABLE raw_reports (
    id SERIAL PRIMARY KEY,
    source VARCHAR(50),
    raw_message TEXT NOT NULL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processing_status VARCHAR(30) DEFAULT 'pending'
);

CREATE TABLE review_queue (
    id SERIAL PRIMARY KEY,
    raw_report_id INTEGER REFERENCES raw_reports(id),
    reason VARCHAR(100) NOT NULL,
    status VARCHAR(30) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE payroll_records (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    shift_id INTEGER REFERENCES shifts(id),
    worked_hours DECIMAL(5,2),
    salary_amount DECIMAL(10,2),
    bonus_amount DECIMAL(10,2),
    total_payout DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bonus_records (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    shift_id INTEGER REFERENCES shifts(id),
    company_revenue DECIMAL(12,2),
    bonus_percentage DECIMAL(5,2),
    bonus_amount DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_raw_reports_status ON raw_reports(processing_status);
CREATE INDEX idx_review_queue_status ON review_queue(status);
CREATE INDEX idx_payroll_employee ON payroll_records(employee_id);
CREATE INDEX idx_bonus_employee ON bonus_records(employee_id);
