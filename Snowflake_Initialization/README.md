# Initialization Folder – Snowflake Environment Setup

## Purpose

The SQL files contained in this directory perform the **manual setup and initialization** of the Snowflake environment, including the secure communication layer between Snowflake and Google Cloud Platform (GCP).

This setup establishes the core infrastructure required for the data pipeline, such as:

* Roles and access permissions
* Virtual warehouse configuration
* Database and schema creation
* Storage integration between Snowflake and GCP
* External staging foundation for data ingestion

These components form the **infrastructure layer** of the pipeline and are designed to be executed once during initial environment provisioning.

---

## Execution Instructions

Each SQL script in this directory is intended to be:

* Run **manually**
* Executed **once**
* Run in the correct order, following the comments within each script

All scripts should be executed using a role with sufficient privileges, typically:

```
ACCOUNTADMIN
```

This is required because some objects created in this setup (such as storage integrations and warehouses) are **account-level resources**.

Example:

```
USE ROLE ACCOUNTADMIN;
```

---

## Important Notes

### 1. One-Time Infrastructure Setup

Most objects created here are persistent infrastructure components and should not be recreated during normal pipeline execution.

Examples:

* Roles
* Warehouse
* Database
* Schemas
* Storage Integration

These objects are expected to exist long term and are only modified intentionally.

---

### 2. Storage Integration Behavior

The storage integration connecting Snowflake to GCP is a **security sensitive object** and does not support `IF NOT EXISTS`.

It should be:

* Created once
* Verified after creation
* Not replaced unless configuration changes are required

Recreating the integration may generate a new service account and require reconfiguration of cloud permissions.

---

### 3. Manual vs Automated Execution

This project uses a **manual initialization process** for my own learning sake.

In production environments, these steps are typically automated using:

* Infrastructure-as-Code tools
* CI/CD pipelines
* Deployment orchestration

Automated ingestion mechanisms such as **Snowpipe** can also be configured for continuous loading, but this project focuses on controlled, manual execution.

---

## Security Design Principle

This setup follows the **principle of least privilege**.

The Snowflake integration is configured with:

* Read-only access to the GCP storage bucket
* No permission to modify or delete source files

This ensures:

* Source data integrity
* Auditability
* Safe ingestion behavior

---

## Folder Responsibility

This directory is responsible only for:

```
Environment initialization
Infrastructure setup
Security configuration
External system integration
```

It is **not responsible for**:

```
Data ingestion
Data transformation
Data modeling
Pipeline scheduling
```

Those responsibilities belong to the ingestion and transformation layers.

---

## Typical Execution Order

1. Create roles
2. Create warehouse
3. Create database
4. Create schemas
5. Grant permissions
6. Create storage integration
7. Configure external stage access

---

## Troubleshooting Tips

 If usage tips are followed everything should work just fine but in specific cases check for the following:

* Always fix the **first error** encountered before rerunning scripts
* Run scripts sequentially during initial setup
* Verify the active role before execution:

If its not any of the above just ask chat gpt , i was able to troubleshoot most of my problems through it, hey it even helped me formar this nice and helpfull README 

```
SELECT CURRENT_ROLE();
```

* Snowflake identifiers are case-sensitive when quoted
* Most infrastructure objects are persistent and should not be recreated routinely

---

## References and Supporting Documentation

Snowflake – Loading Data from Google Cloud Storage:

https://docs.snowflake.com/en/user-guide/data-load-gcs

Community Tutorial – Snowflake and GCP Integration
Credits to Daniel Wilczak:

https://sfc-gh-dwilczak.github.io/tutorials/clouds/google/storage/

---

## Summary

This initialization layer establishes the foundational infrastructure required for the data pipeline.
Once completed successfully, the environment is ready for:

* Raw data ingestion
* Transformation workflows
* Data modeling
* Analytics and reporting
