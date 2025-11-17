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
| `experience_level`   | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type`    | FT, PT, CT, FL |
| `job_title`          | Role title (e.g., Data Scientist, ML Engineer) |
| `salary`             | Gross annual salary in original currency |
| `salary_currency`    | Currency (USD, EUR, INR, etc.) |
| `salary_in_usd`      | Salary converted to USD |
| `employee_residence` | ISO country code of employee |
| `remote_ratio`       | % of remote work (0, 50, 100) |
| `company_location`   | ISO country code of company HQ |
| `company_size`       | S, M, L |

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
