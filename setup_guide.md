# 🚀 Quick Setup Guide

## Prerequisites
- Python 3.8+
- MySQL Server 8.0+
- Power BI Desktop (optional)

## Installation
```bash
# 1. Clone repository
git clone https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure database (update credentials in src/config.py)
# 4. Run ETL pipeline
python src/etl_pipeline.py

# 5. Connect Power BI to MySQL database
# 6. Explore results in /dashboards/

🔄 Data Flow
📊 Complete ETL Process:
📥 Extraction - Place new CSV files in data/01_raw/

🔄 Transformation - Run python src/etl_pipeline.py

⚡ Processing - Python enriches data with Pandas and NumPy

💾 Loading - Enriched data saved to MySQL database

📊 Connection - Power BI connects to MySQL for live data

📈 Visualization - Interactive dashboards with real-time insights

🔁 Adding New Data:
bash
# Simply execute the pipeline:
python src/etl_pipeline.py
# The system automatically detects and processes new files
# Refresh Power BI to see updated dashboards
🗄️ Database Configuration
Edit src/config.py with your MySQL credentials:

python
"""
Database Configuration for ALSA Transport Analytics
Update these values with your MySQL setup
"""

DATABASE_CONFIG = {
    'host': 'localhost',           # Your MySQL server address
    'user': 'your_username',       # Your database username
    'password': 'your_password',   # Your database password
    'database': 'transport_analysis',  # Database name
    'port': 3306                   # MySQL port (default: 3306)
}

# Connection string for SQLAlchemy
CONNECTION_STRING = f"mysql+mysqlconnector://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

📊 Power BI Database Connection
Step-by-Step Connection Guide:
Open Power BI Desktop

Get Data → MySQL Database

Enter Connection Details:

Server: localhost (or your MySQL server address)

Database: transport_analysis

Authentication:

Select "Database"

Username: your_username

Password: your_password

Import Data Tables:

Select all tables: buses, drivers, routes, trips, passengers

Create Data Model:

Establish relationships between tables

Use trip_id, bus_id, driver_id, route_id as keys

🔗 Recommended Table Relationships:
text
trips ────── buses
  │           │
  ├───── drivers
  │
  └───── routes
          │
passengers ─┘

🎛️ Power BI Dashboard Setup
Essential Steps for Dashboards:
Import all 5 tables from MySQL

Create relationships using primary/foreign keys

Build measures using DAX for:

On-time performance percentage

Revenue per passenger

Average delay by route

Satisfaction scores

Design visualizations based on provided dashboard examples

🔄 Data Refresh Process:
Add new CSV files to data/01_raw/

Run python src/etl_pipeline.py

Refresh Power BI data source

Dashboards automatically update with new insights

💡 Pro Tip:
For production environments, schedule the ETL pipeline to run automatically and set up Power BI scheduled refreshes for fully automated reporting.

⭐ Enjoy exploring the ALSA Transport Analytics pipeline!
