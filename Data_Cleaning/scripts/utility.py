import pycountry


def check_and_clean_dataset(df):
    """
    Performs a final data quality check and basic cleaning on a DataFrame.

    Steps performed:
    1. Checks for missing values in each column and prints a summary.
    2. Displays unique values for categorical columns:
       - experience_level
       - employment_type
       - company_size
       - remote_ratio
    3. Prints salary statistics and the min/max range for 'salary_in_usd'.
    4. Validates ISO country codes for 'employee_residence' and 'company_location',
       allowing 'Kosovo' as a special case.
    5. Identifies and prints any duplicate rows.
    6. Removes duplicate rows and prints the new dataset shape.
    7. Displays the final shape of the dataset and data types of each column.

    Parameters:
    df (pandas.DataFrame): Input dataset to be checked and cleaned.

    Returns:
    pandas.DataFrame: Cleaned dataset with duplicates removed.
    """

    print("\n" + "-" * 40)
    print("        FINAL DATA QUALITY CHECK")
    print("-" * 40 + "\n")

    # Missing values
    missing_summary = df.isnull().sum()
    if missing_summary.sum() > 0:
        print("✅ Missing values per column:")
        print(missing_summary[missing_summary > 0])
    else:
        print("✅ No missing values found in any column.")

    # Unique values for categorical columns
    print("\n✅ Unique values for categorical columns:")
    for col in ['experience_level', 'employment_type', 'company_size', 'remote_ratio']:
        print(f"🔹 {col}: {df[col].unique()}")

    # Salary ranges and stats
    print("\n✅ Salary (USD) statistics:")
    print(f"🔹 Range: {df['salary_in_usd'].min()} to {df['salary_in_usd'].max()}")
    print(f"🔹 Summary:\n{df['salary_in_usd'].describe()}")

    # Country code validation
    valid_codes = [c.alpha_2 for c in pycountry.countries]

    invalid_residences = [code for code in df['employee_residence'].unique()
                          if code not in valid_codes and code != 'Kosovo']
    invalid_locations = [code for code in df['company_location'].unique()
                         if code not in valid_codes and code != 'Kosovo']

    if invalid_residences:
        print("\n⚠️ Invalid employee residence codes:", invalid_residences)
    else:
        print("\n✅ All employee residence codes are valid.")

    if invalid_locations:
        print("⚠️ Invalid company location codes:", invalid_locations)
    else:
        print("✅ All company location codes are valid.")

    # Remove duplicates
    duplicates_count = df.duplicated().sum()
    print(f"\n✅ Total duplicates found: {duplicates_count}")

    df_cleaned = df.drop_duplicates()
    print(f"✅ Duplicates removed. New dataset shape: {df_cleaned.shape}")

    # Final shape & dtypes
    print("\n✅ Final dataset shape:", df_cleaned.shape)
    print("\n✅ Column data types:")
    print(df_cleaned.dtypes)

    return df_cleaned
