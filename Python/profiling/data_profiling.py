import polars as pl
import pandas as pd
from pathlib import Path
from data_set_description import get_dataset_description_md
#future improvments : add a section at the end of the markdown with some quick isngiths ie: top drg, highest payment , missing percentage per column 


#file directory 

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "raw" / "Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv"
df = pl.read_csv(file_path, infer_schema_length=10000)


# BASIC PROFILING

def df_attributes(df):
    null_count = df.null_count()
    df_description = df.describe()
    column_dtypes = df.schema
    shape = df.shape

    return null_count, df_description, column_dtypes, shape


null_count, df_description, column_dtypes, shape = df_attributes(df)


# COLUMN GROUPS (DOMAIN SPLIT)

provider_cols_list1 = [
    'Rndrng_Prvdr_CCN',
    'Rndrng_Prvdr_Org_Name',
    'Rndrng_Prvdr_City',
    'Rndrng_Prvdr_St'
]

provider_cols_list2 = [
    'Rndrng_Prvdr_State_FIPS',
    'Rndrng_Prvdr_Zip5',
    'Rndrng_Prvdr_State_Abrvtn',
    'Rndrng_Prvdr_RUCA'
]

complete_provider_list = provider_cols_list1 + provider_cols_list2

drg_cols_list = ['DRG_Cd','DRG_Desc']

charge_cols_list = [
    'Tot_Dschrgs',
    'Avg_Submtd_Cvrd_Chrg',
    'Avg_Tot_Pymt_Amt',
    'Avg_Mdcr_Pymt_Amt'
]


# COLUMN SPLITTING

def column_sep(df, provider_list1,provider_list2, drg_list, charge_list):
    provider_cols1 = df.select(provider_list1)
    provider_cols2 = df.select(provider_list2)
    drg_cols = df.select(drg_list)
    charge_cols = df.select(charge_list)

    return provider_cols1,provider_cols2, drg_cols, charge_cols


provider_df1,provider_df2, drg_df, charge_df = column_sep(
    df,
    provider_cols_list1,provider_cols_list2,
    drg_cols_list,
    charge_cols_list
)


# NAN COUNT (SAFE FOR FLOATS ONLY)

nan_count = df.select([
    pl.col(col).is_nan().sum().alias(col)
    for col, dtype in df.schema.items()
    if dtype in [pl.Float32, pl.Float64]
])


#Write data type columns 

def write_schema_group(df, column_list, section_name):
    schema = df.schema

    lines = []
    lines.append(f"### {section_name}\n\n")

    for col in column_list:
        dtype = schema.get(col, "Unknown")
        lines.append(f"- `{col}` : `{dtype}`\n")

    lines.append("\n---\n\n")

    return "".join(lines)

def write_all_schema_sections(f, df):
    f.write("## Column Data Types\n\n")

    f.write(write_schema_group(df, complete_provider_list, "Provider Columns"))
    f.write(write_schema_group(df, drg_cols_list, "DRG Columns"))
    f.write(write_schema_group(df, charge_cols_list, "Financial Columns"))
    

# MARKDOWN REPORT

with open("profiling_report.md", "w", encoding="utf-8") as f:
    f.write("# Healthcare Dataset Profiling Report\n\n")

    f.write("## Dataset Description\n")
    f.write(get_dataset_description_md())


    f.write(f"## Dataset Shape\n{shape}\n\n")


    f.write("# Column Data types + Statistics + nan counts \n\n")
    write_all_schema_sections(f, df)


    f.write("# Statistics + null counts\n\n")
    f.write("## Provider Data\n\n")
    f.write("### Provider Identity Info (Part 1)\n\n")
    f.write(provider_df1.describe().to_pandas().to_markdown(index=False))
    f.write("\n\n---\n\n")
    f.write("### Provider Location & Classification (Part 2)\n\n")
    f.write(provider_df2.describe().to_pandas().to_markdown(index=False))
    f.write("\n\n---\n\n")


    f.write("## Clinical Classification (DRG)\n\n")
    f.write(drg_df.describe().to_pandas().to_markdown(index=False))
    f.write("\n\n---\n\n")

    f.write("## Financial Metrics\n\n")
    f.write(charge_df.describe().to_pandas().to_markdown(index=False))
    f.write("\n\n---\n\n")

    f.write("# NaN Counts (Float Columns Only)\n\n")
    f.write(nan_count.to_pandas().to_markdown(index=False))
    f.write("\n")