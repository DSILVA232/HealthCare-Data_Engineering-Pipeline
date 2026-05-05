import great_expectations as gx
from dotenv import load_dotenv


context = gx.get_context(mode="file",project_root_dir="/opt/airflow/health_care_project/gx_context")


#define data source
data_source = context.data_sources.add_pandas_gcs(
    name="healthcare_data_source",
    bucket_or_name="landing-zone-1",
    gcs_options={}
)


#define data asset
asset = data_source.add_csv_asset(
    name="hospital_csv",
    gcs_prefix="raw/data/"
)

#define batch
batch_definition = asset.add_batch_definition_path(
    name="hospital_2024",
    path="Medicare_IP_Hospitals_by_Provider_and_Service_2024.csv"
)

batch = batch_definition.get_batch()



# defining suite and expecation that go inside suite
suite = gx.ExpectationSuite(name="healthcare_data_basic_validation")
context.suites.add(suite)

suite.add_expectation(
    gx.expectations.ExpectTableColumnCountToEqual(value=15)
)

suite.add_expectation(
    gx.expectations.ExpectTableColumnsToMatchSet(
        column_set=[
            "Rndrng_Prvdr_CCN","Rndrng_Prvdr_Org_Name",
            "Rndrng_Prvdr_City","Rndrng_Prvdr_St",
            "Rndrng_Prvdr_State_FIPS","Rndrng_Prvdr_Zip5",
            "Rndrng_Prvdr_State_Abrvtn","Rndrng_Prvdr_RUCA",
            "Rndrng_Prvdr_RUCA_Desc","DRG_Cd","DRG_Desc",
            "Tot_Dschrgs","Avg_Submtd_Cvrd_Chrg",
            "Avg_Tot_Pymt_Amt","Avg_Mdcr_Pymt_Amt"
        ],
        exact_match=True
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="Rndrng_Prvdr_CCN"
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(
        column="DRG_Cd"
    )
)

suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="Avg_Tot_Pymt_Amt",
        min_value=0
    )
)

#def validation 

validation_definition = gx.ValidationDefinition(
    name="hospital_validation_2024",
    data=batch_definition,
    suite=suite
)
context.validation_definitions.add(validation_definition)

# defining checkpoint which will be the automatic run that will execute everything and return validation results

checkpoint = gx.Checkpoint(
    name="healthcare_checkpoint",
    validation_definitions=[validation_definition]
)

context.checkpoints.add(checkpoint)
