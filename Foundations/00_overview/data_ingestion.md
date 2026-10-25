# Data Ingestion

Data ingestion is the process of collecting and moving raw data from sources such as APIs, files, applications, or databases into a destination such as a database, data lake, or data warehouse for storage and analysis.

## Typical flow

```text
Source (API / CSV / database)
          |
          v
      Ingestion
          |
          v
     Raw / staging
          |
          v
Validation and transformation
          |
          v
 Destination storage
```

Ingestion focuses on getting data from the source to the target reliably. Validation and transformation are often downstream stages in a larger data pipeline.
