from flytekit import workflow
from flytekit.types.file import FlyteFile
from typing import TypeVar, NamedTuple
from flytekitplugins.domino.helpers import Input, Output, run_domino_job_task
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask, GitRef, EnvironmentRevisionSpecification, EnvironmentRevisionType, DatasetSnapshot

# Set the name of this variable to the name of your Domino's standard environment
environment_name="Domino Standard Environment Py3.10 R4.4"

# Set if you want caching on or off. 
cache=False

@workflow
def retrieve_data(data_path_a: str): 
    '''

    pyflyte run --remote data_csv.py retrieve_data --data_path_a /mnt/datasetA.csv
    '''

    task1 = run_domino_job_task(
        flyte_task_name='Retrieve Audit ',
        command='python load-data-A.py',
        inputs=[Input(name='data_path', type=str, value=data_path_a)],
        output_specs=[Output(name='datasetA', type=FlyteFile[TypeVar('csv')])],
        use_project_defaults_for_omitted=True,
        environment_name=environment_name,
        hardware_tier_name="Small",
        cache=cache,
        cache_version="1.0"
    )

    return 
