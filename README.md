# Pension Management System Analysis  
**End-to-End Data Analytics Project (ETL → SQL → Power BI)**

## 📌 Project Overview
The **Pension Management System Analysis** is an end-to-end data analytics project that demonstrates the complete analytics lifecycle — from raw data ingestion and cleaning to SQL-based analysis and interactive dashboarding.

The project simulates a real-world pension administration scenario and focuses on producing **accurate, reliable, and decision-ready insights** to support financial planning, workforce management, and pension policy oversight.

---

## 🎯 Project Objectives
- Clean and standardise raw pension data  
- Resolve data quality issues, particularly around years of service  
- Perform SQL-based analytical queries  
- Build a professional Power BI dashboard  
- Translate analysis into actionable business insights  

---

## 🗂️ Data Overview
- **Dataset size:** 20,000 records  
- **Source format:** CSV  
- **Processed storage:** MySQL  

**Key attributes include:**
- Pensioner identifiers  
- Dates (DOB, join date, retirement date)  
- Pension amounts  
- Region  
- Pension type and status  

Data quality checks were applied to ensure consistency, accuracy, and analytical reliability.

---

## 🔄 Project Workflow

### Phase 1 – Python ETL
Python (Pandas) was used for data extraction, cleaning, feature engineering, and loading.

**Key steps:**
- Extraction: Loading pension records from a raw CSV file (20,000 rows).

  <img width="576" height="48" alt="image" src="https://github.com/user-attachments/assets/4c8c464d-7e6e-48cc-8dc7-d7f99c1c4c27" />

- Cleaning & Standardization: Formatting dates, correcting numerical errors, and standardizing text fields
  
  <img width="455" height="100" alt="image" src="https://github.com/user-attachments/assets/3ac7275f-ec06-4f89-a0a3-4ae4f1c66d72" />
  
  <img width="536" height="103" alt="image" src="https://github.com/user-attachments/assets/1a75798b-5c7f-482c-af8c-393023f412f2" />

  
  <img width="512" height="99" alt="image" src="https://github.com/user-attachments/assets/eea82564-5d26-453c-8787-9a233c43cc91" />

- Data Consistency & Derivation:	Deriving new metrics such as age at retirement, pension status and re-calculating the years_of_service field based on the logic (retirement_date - join_date) to resolve discrepancies between recorded service years and actual timeline data.

  <img width="435" height="87" alt="image" src="https://github.com/user-attachments/assets/b80c8124-e134-4b60-a447-029e80ac1c85" />

  <img width="293" height="112" alt="image" src="https://github.com/user-attachments/assets/30863659-b454-4628-b942-68571271cf4b" />


  <img width="497" height="69" alt="image" src="https://github.com/user-attachments/assets/b584fc06-5ddb-47ea-8e84-0ab1842ce079" />
  
- Removing or masking sensitive personal information

  <img width="408" height="92" alt="image" src="https://github.com/user-attachments/assets/7320a336-4190-43af-ace0-38f561b1ae50" />

- Loading the cleaned dataset into MySQL  

  <img width="576" height="263" alt="image" src="https://github.com/user-attachments/assets/ba2185c8-9a5a-4ad8-8282-a478766bc18e" />

---

### Phase 2 – SQL Analysis
SQL queries were executed on the cleaned MySQL database to answer key business questions.

**Key analyses performed:**
1. Average pension payout by region

   <img width="248" height="181" alt="image" src="https://github.com/user-attachments/assets/b89ef829-827a-465d-97f0-f6f572a8ce27" />

3. Identification of top pensioners by payout

   <img width="310" height="181" alt="image" src="https://github.com/user-attachments/assets/eb07b5b8-fe2a-46dd-85b2-b0b479f70e11" />
  
4. Employees nearing retirement
   
5. Pension type and status distribution

   <img width="315" height="92" alt="image" src="https://github.com/user-attachments/assets/fb307f7f-6f55-4d09-84d6-e68d964092f8" />
 
   <img width="278" height="106" alt="image" src="https://github.com/user-attachments/assets/05ed8eed-cced-4761-9f22-67e6fbc40feb" />

6. Bucketing pension values and tenure to analyse service length vs payout
 
   <img width="298" height="134" alt="image" src="https://github.com/user-attachments/assets/ade51182-4b32-42df-828f-16a7ee451f8f" />


---

### Phase 3 – Power BI Visualisation
An interactive Power BI dashboard was developed to present insights clearly and intuitively.

<img width="576" height="327" alt="image" src="https://github.com/user-attachments/assets/21aae47f-7766-4058-a6cf-1c82725a0d7b" />


---

## 📊 Business Insights
- **Regional Consistency:** Pension payouts are highly consistent across regions, indicating uniform policy implementation.  
- **Pension Scheme Structure:** Defined Benefit pensions account for a larger share of pensioners, highlighting long-term financial obligations.  
- **Retirement Trends:** Stable retirement patterns suggest predictable workforce exits and manageable forecasting.  
- **Pension Value Distribution:** Most pensioners fall within a central payout range, while a smaller group of high-value pensions contributes disproportionately to total costs.  
- **Workforce Planning:** Employees nearing retirement can be clearly identified, enabling proactive succession planning.

---

## 🛠️ Tools & Technologies
- **Python (Pandas):** Data cleaning, transformation, and feature engineering  
- **MySQL:** Data storage and analytical querying  
- **Power BI:** Interactive dashboards and visual reporting  

---

## ✅ Key Outcomes
- End-to-end analytics pipeline implemented using industry-standard tools  
- Clean, structured SQL analysis aligned with real business questions  
- Interactive dashboard designed for non-technical stakeholders  
- Strong focus on data quality, governance, and insight generation  

---

## 📌 Conclusion
This project demonstrates practical experience in:
- Building structured ETL pipelines  
- Applying SQL to real-world analytical problems  
- Designing professional Power BI dashboards  
- Translating data into meaningful business insights  

The **Pension Management System Analysis** reflects an industry-aligned analytics workflow suitable for healthcare, public sector, and financial reporting environments.

