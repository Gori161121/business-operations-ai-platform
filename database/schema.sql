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
