# Data Engineering Glossary

## Data ingestion

Data ingestion is the process of collecting and moving raw data from sources such as APIs, files, applications, or databases into a centralized destination such as a database, data lake, or data warehouse for storage and analysis.

## ETL

**Extract, Transform, Load**:
- **Extract:** obtain data from a source.
- **Transform:** validate, clean, normalize, or enrich it.
- **Load:** write it to the target system.

## Payload

The payload is the data being sent or processed. For a rejected record, storing a sanitized copy of its payload allows a handler to inspect or retry the record later. Payloads should not contain passwords, tokens, or other secrets.

## Transaction

A transaction groups database operations into a unit. In the usual all-or-nothing pattern, successful completion commits the changes; an error that escapes the transaction context causes rollback of uncommitted changes.

## SAVEPOINT

A SAVEPOINT is a named checkpoint inside a transaction. `ROLLBACK TO SAVEPOINT` can undo changes since that checkpoint while allowing the outer transaction to continue, provided the error is appropriately handled.

## Idempotency

An operation is idempotent when repeating it does not change the final state after the first successful application. Stable IDs and carefully designed UPSERTs can make data loading retry-friendly.

## Rejected / quarantine record

A record that failed validation or processing and is retained with its payload, failure reason, stage, timestamp, and status for later review or replay.
