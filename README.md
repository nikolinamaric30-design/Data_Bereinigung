# 💙 Job Salaries in 2025

Analyze **global salary trends in Data Science, Machine Learning, and AI jobs** from 2020 to 2025.  

This project demonstrates **data cleaning, preprocessing, and exploratory data analysis (EDA)** using Python and Jupyter Notebook.

---

## 💡 About the Dataset

This dataset contains real-world salary data for Data Science, AI, and ML roles, collected from kaggle.com

**Key columns:**

| Column               | Description |
|---------------------|-------------|
| `work_year`          | Year salary was reported (2020–2025) |
| `experience_level`   | Seniority level: EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type`    | Contract type: FT (Full-time), PT (Part-time), CT (Contract), FL (Freelance) |
| `job_title`          | Specific role title (e.g., Data Scientist, ML Engineer, AI Specialist |
| `salary`             | Gross annual salary in the original currency (before taxes) |
| `salary_currency`    | Original currency (e.g., USD, EUR, INR) |
| `salary_in_usd`      | Salary converted to USD using 2025 exchange rates |
| `employee_residence` | Employee’s country (ISO 3166-1 alpha-2 code) |
| `remote_ratio`       | Remote work percentage: 0 = On-site, 50 = Hybrid, 100 = Fully remote |
| `company_location`   | Company headquarters country (ISO 3166-1 alpha-2 code)|
| `company_size`       | Company size: S (1–50), M (51–500), L (501+ employees) |

---

## 🧹 Data Cleaning & Preprocessing

- **Handle missing values**:
  - `job_title` → fill with `'Unknown'`
  - `salary` → fill with median
  - `employee_residence` → infer from company location or mode
- **Standardize categories**:
  - `experience_level`, `employment_type`, `company_size`, `salary_currency`, `remote_ratio`
- **Fix invalid country codes** (`employee_residence` & `company_location`)
- **Convert object columns to `category`** type for memory efficiency

---


## Project Structure

- `notebooks/` - Jupyter Notebook(s) for analysis
- `data/` - raw or sample datasets
- `scripts/` - helper Python scripts
