from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

from include.constants import jaffle_shop_path, venv_execution_config, dbt_executable

dbt_profile_overrides = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(str(jaffle_shop_path)),
    profile_config=ProfileConfig(
        # these map to dbt/jaffle_shop/profiles.yml
        profile_name="airflow_db",
        target_name="dev",
        profile_mapping=PostgresUserPasswordProfileMapping(
            conn_id="airflow_metadata_db",
            profile_args={"schema": "my_dbt_schema"},
        ),
    ),
    execution_config=venv_execution_config,
    operator_args={
        "dbt_executable_path": str(dbt_executable),
    },
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_profile_overrides",
    tags=["profiles"],
)