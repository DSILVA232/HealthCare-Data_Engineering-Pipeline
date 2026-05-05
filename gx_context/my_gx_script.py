import great_expectations as gx

def run_gx_validation():
    context = gx.get_context(
        mode="file",
        project_root_dir="/opt/airflow/health_care_project/gx_context"
    )

    checkpoint = context.checkpoints.get("healthcare_checkpoint")

    result = checkpoint.run()

    if not result.success:
        raise ValueError("GX validation failed")

    return result.success