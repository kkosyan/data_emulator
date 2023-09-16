# data_emulator

Project provides an opportunity to automate test stand creation and modification for database connected procecess.
Single table use case extracts necessary DDL from sample database (e.g. production DB), generates via DL tool and
uploads synthetic data to another database (e.g. testing DB).

The project includes docker compose dev file for service testing.
To get started locally, you'll need:
1. Update databases credentials with settings/settings.toml and settings/.secrets.toml files
2. Install pg_dump utility
3. Install dependencies with pyproject.toml file
4. Run service with command`python cli.py single-table-emulator --table-name {sample_table_name}`
