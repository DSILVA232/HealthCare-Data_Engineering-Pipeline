# Healthcare Dataset Profiling Report

## Dataset Description

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
- `Rndrng_Prvdr_RUCA_Desc`: Description of rural/urban classification (excluded from statistical summaries due to high cardinality and non numeric nature)



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


## Dataset Shape
(145879, 15)

# Column Data types + Statistics + nan counts 

## Column Data Types

### Provider Columns

- `Rndrng_Prvdr_CCN` : `Int64`
- `Rndrng_Prvdr_Org_Name` : `String`
- `Rndrng_Prvdr_City` : `String`
- `Rndrng_Prvdr_St` : `String`
- `Rndrng_Prvdr_State_FIPS` : `Int64`
- `Rndrng_Prvdr_Zip5` : `Int64`
- `Rndrng_Prvdr_State_Abrvtn` : `String`
- `Rndrng_Prvdr_RUCA` : `Float64`
- `Rndrng_Prvdr_RUCA_Desc` : `String`

---

### DRG Columns

- `DRG_Cd` : `Int64`
- `DRG_Desc` : `String`

---

### Financial Columns

- `Tot_Dschrgs` : `Int64`
- `Avg_Submtd_Cvrd_Chrg` : `Float64`
- `Avg_Tot_Pymt_Amt` : `Float64`
- `Avg_Mdcr_Pymt_Amt` : `Float64`

---

# Statistics + null counts

## Provider Data

### Provider Identity Info (Part 1)

| statistic   |   Rndrng_Prvdr_CCN | Rndrng_Prvdr_Org_Name                              | Rndrng_Prvdr_City   | Rndrng_Prvdr_St       |
|:------------|-------------------:|:---------------------------------------------------|:--------------------|:----------------------|
| count       |             145879 | 145879                                             | 145879              | 145879                |
| null_count  |                  0 | 0                                                  | 0                   | 0                     |
| mean        |             253820 | nan                                                | nan                 | nan                   |
| std         |             153573 | nan                                                | nan                 | nan                   |
| min         |              10001 | Abbeville General Hospital                         | Abbeville           | #1 Medical Park Drive |
| 25%         |             100316 | nan                                                | nan                 | nan                   |
| 50%         |             240080 | nan                                                | nan                 | nan                   |
| 75%         |             380027 | nan                                                | nan                 | nan                   |
| max         |             670333 | Zuckerberg San Francisco General Hosp & Trauma Ctr | Zion                | W3985 County Road Nn  |

---

### Provider Location & Classification (Part 2)

| statistic   |   Rndrng_Prvdr_State_FIPS |   Rndrng_Prvdr_Zip5 | Rndrng_Prvdr_State_Abrvtn   |   Rndrng_Prvdr_RUCA |
|:------------|--------------------------:|--------------------:|:----------------------------|--------------------:|
| count       |               145879      |            145879   | 145879                      |        145879       |
| null_count  |                    0      |                 0   | 0                           |             0       |
| mean        |                   27.7355 |             47863.4 | nan                         |             1.74611 |
| std         |                   15.5566 |             28782.5 | nan                         |             6.24226 |
| min         |                    1      |              1040   | AK                          |             1       |
| 25%         |                   12      |             24014   | nan                         |             1       |
| 50%         |                   27      |             44106   | nan                         |             1       |
| 75%         |                   41      |             74401   | nan                         |             1       |
| max         |                   56      |             99801   | WY                          |            99       |

---

## Clinical Classification (DRG)

| statistic   |     DRG_Cd | DRG_Desc                                               |
|:------------|-----------:|:-------------------------------------------------------|
| count       | 145879     | 145879                                                 |
| null_count  |      0     | 0                                                      |
| mean        |    424.809 | nan                                                    |
| std         |    251.893 | nan                                                    |
| min         |      1     | ACUTE ADJUSTMENT REACTION AND PSYCHOSOCIAL DYSFUNCTION |
| 25%         |    233     | nan                                                    |
| 50%         |    378     | nan                                                    |
| 75%         |    640     | nan                                                    |
| max         |    988     | WOUND DEBRIDEMENTS FOR INJURIES WITH CC                |

---

## Financial Metrics

| statistic   |   Tot_Dschrgs |   Avg_Submtd_Cvrd_Chrg |   Avg_Tot_Pymt_Amt |   Avg_Mdcr_Pymt_Amt |
|:------------|--------------:|-----------------------:|-------------------:|--------------------:|
| count       |   145879      |       145879           |   145879           |    145879           |
| null_count  |        0      |            0           |        0           |         0           |
| mean        |       33.9492 |        96366.1         |    19151.3         |     15782.7         |
| std         |       50.5717 |       129335           |    22673.4         |     19662.9         |
| min         |       11      |         2058.38        |     1849.08        |       386.8         |
| 25%         |       14      |        36845.4         |     9057.27        |      7078.18        |
| 50%         |       20      |        61619.6         |    13217.4         |     10850.7         |
| 75%         |       35      |       110042           |    20960.4         |     17253           |
| max         |     3400      |            7.19664e+06 |        1.44331e+06 |         1.43667e+06 |

---

# NaN Counts (Float Columns Only)

|   Rndrng_Prvdr_RUCA |   Avg_Submtd_Cvrd_Chrg |   Avg_Tot_Pymt_Amt |   Avg_Mdcr_Pymt_Amt |
|--------------------:|-----------------------:|-------------------:|--------------------:|
|                   0 |                      0 |                  0 |                   0 |
