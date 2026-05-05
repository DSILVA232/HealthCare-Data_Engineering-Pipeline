def get_dataset_description_md():
    return """
This dataset is sourced from the **CMS Medicare Inpatient Hospitals – Provider and Service (2024)** dataset. It contains aggregated information on inpatient hospital services across providers in the United States, including diagnostic groupings, service volumes, and financial metrics such as submitted charges and Medicare payments.

The primary purpose of this dataset is to enable analysis of:
- Hospital service utilization (discharges)
- Cost and payment structures across diagnosis-related groups (DRGs)
- Geographic and provider-level variations in Medicare inpatient services


## Column Structure Overview

The dataset is organized into three main logical groups:

### 1. Provider Information 
These columns describe the healthcare provider and its geographic classification.

- `Rndrng_Prvdr_CCN`: CMS Certification Number identifying the hospital/provider
- `Rndrng_Prvdr_Org_Name`: Name of the hospital or organization
- `Rndrng_Prvdr_City`: City location of the provider
- `Rndrng_Prvdr_St`: State abbreviation
- `Rndrng_Prvdr_State_FIPS`: Federal Information Processing Standard state code
- `Rndrng_Prvdr_Zip5`: 5-digit ZIP code
- `Rndrng_Prvdr_State_Abrvtn`: State abbreviation (redundant geographic label)
- `Rndrng_Prvdr_RUCA`: Rural-Urban Commuting Area code
- `Rndrng_Prvdr_RUCA_Desc`: Description of rural/urban classification (excluded from statistical summaries due to high cardinality and non-numeric nature)



### 2. Clinical Classification (DRG)
These columns define the diagnosis-related grouping used for billing and categorization of inpatient services.

- `DRG_Cd`: Diagnosis-Related Group code
- `DRG_Desc`: Human-readable description of the DRG category



### 3. Financial & Utilization Metrics 
These columns capture service volume and cost-related measures.

- `Tot_Dschrgs`: Total number of discharges
- `Avg_Submtd_Cvrd_Chrg`: Average submitted covered charge
- `Avg_Tot_Pymt_Amt`: Average total payment amount
- `Avg_Mdcr_Pymt_Amt`: Average Medicare payment amount


## Notes on Data Processing

- Missing values are handled via separate null and NaN profiling.
- NaN detection is applied only to floating-point columns to avoid type errors.
- The column `Rndrng_Prvdr_RUCA_Desc` is excluded from statistical summaries due to its purely descriptive nature and high cardinality, making it unsuitable for numerical aggregation or summary statistics.


"""