# Database Design

## Purpose

The database serves as the central source of truth for all business operations, automation workflows, reporting systems, and AI-powered decision support.

The design focuses on scalability, automation readiness, and analytical reporting.

---

## Main Entities

### Employees

Stores information about employees and contractors.

Fields:

* employee_id
* full_name
* role
* contact_information
* status
* hire_date

---

### Locations

Stores business locations.

Fields:

* location_id
* location_name
* address
* status

---

### Shifts

Stores employee shift records.

Fields:

* shift_id
* employee_id
* location_id
* start_time
* end_time
* worked_hours

---

### Products

Stores products and services.

Fields:

* product_id
* product_name
* category
* price
* status

---

### Sales

Stores sales transactions.

Fields:

* sale_id
* product_id
* employee_id
* quantity
* revenue
* transaction_date

---

### Expenses

Stores operational expenses.

Fields:

* expense_id
* category
* amount
* date
* notes

---

### Payroll

Stores salary and commission calculations.

Fields:

* payroll_id
* employee_id
* worked_hours
* salary_amount
* commission_amount
* payment_period

---

### Reports

Stores generated reports.

Fields:

* report_id
* report_type
* generated_date
* summary

---

## Database Relationships

Employees → Shifts

Employees → Payroll

Locations → Shifts

Products → Sales

Sales → Reports

Expenses → Reports

Payroll → Reports

---

## Planned Technologies

* PostgreSQL
* SQL
* Supabase
* Airtable

---

## Future Development

* Data Warehouse
* Predictive Analytics
* AI Reporting Layer
* Real-Time Dashboards
* Advanced KPI Monitoring
