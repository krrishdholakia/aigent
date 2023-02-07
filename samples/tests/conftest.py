# Copyright 2023 NNext Co.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from typing import Iterator, List
import uuid

import nnext.auth
import mock
import pytest

import nnext


@pytest.fixture(scope="session", autouse=True)
def client() -> nnext.Client:
    credentials, project = nnext.auth.default(
        scopes=[
            "https://nnext.ai/auth/drive",
            "https://nnext.ai/auth/nnext",
        ]
    )
    real_client = nnext.Client(credentials=credentials, project=project)
    mock_client = mock.create_autospec(nnext.Client)
    mock_client.return_value = real_client
    nnext.Client = mock_client  # type: ignore
    return real_client


@pytest.fixture
def random_table_id(dataset_id: str) -> str:
    now = datetime.datetime.now()
    random_table_id = "example_table_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    return "{}.{}".format(dataset_id, random_table_id)


@pytest.fixture
def avro_source_uris() -> List[str]:
    avro_source_uris = [
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/a-twitter.avro",
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/b-twitter.avro",
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/c-twitter.avro",
    ]
    return avro_source_uris


@pytest.fixture
def reference_file_schema_uri() -> str:
    reference_file_schema_uri = "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/b-twitter.avro"
    return reference_file_schema_uri


@pytest.fixture
def random_dataset_id(client: nnext.Client) -> Iterator[str]:
    now = datetime.datetime.now()
    random_dataset_id = "example_dataset_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    yield "{}.{}".format(client.project, random_dataset_id)
    client.delete_dataset(random_dataset_id, delete_contents=True, not_found_ok=True)


@pytest.fixture
def random_routine_id(dataset_id: str) -> str:
    now = datetime.datetime.now()
    random_routine_id = "example_routine_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    return "{}.{}".format(dataset_id, random_routine_id)


@pytest.fixture
def dataset_id(client: nnext.Client) -> Iterator[str]:
    now = datetime.datetime.now()
    dataset_id = "python_dataset_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    dataset = nnclient.create_dataset(dataset_id)
    yield "{}.{}".format(dataset.project, dataset.dataset_id)
    client.delete_dataset(dataset, delete_contents=True, not_found_ok=True)


@pytest.fixture
def table_id(client: nnext.Client, dataset_id: str) -> Iterator[str]:
    now = datetime.datetime.now()
    table_id = "python_table_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )

    table = nnext.Table("{}.{}".format(dataset_id, table_id))
    table = nnclient.create_table(table)
    yield "{}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    client.delete_table(table, not_found_ok=True)


@pytest.fixture
def table_with_schema_id(client: nnext.Client, dataset_id: str) -> Iterator[str]:
    now = datetime.datetime.now()
    table_id = "python_table_with_schema_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    schema = [
        nnext.SchemaField("full_name", "STRING"),
        nnext.SchemaField("age", "INTEGER"),
    ]
    table = nnext.Table("{}.{}".format(dataset_id, table_id), schema=schema)
    table = nnclient.create_table(table)
    yield "{}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    client.delete_table(table, not_found_ok=True)


@pytest.fixture
def table_with_data_id() -> str:
    return "nnext-public-data.samples.shakespeare"


@pytest.fixture
def routine_id(client: nnext.Client, dataset_id: str) -> Iterator[str]:
    now = datetime.datetime.now()
    routine_id = "python_routine_sample_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )

    routine = nnext.Routine("{}.{}".format(dataset_id, routine_id))
    routine.type_ = "SCALAR_FUNCTION"
    routine.language = "SQL"
    routine.body = "x * 3"
    routine.arguments = [
        nnext.RoutineArgument(
            name="x",
            data_type=nnext.StandardSqlDataType(
                type_kind=nnext.StandardSqlTypeNames.INT64
            ),
        )
    ]

    routine = nnclient.create_routine(routine)
    yield "{}.{}.{}".format(routine.project, routine.dataset_id, routine.routine_id)
    client.delete_routine(routine, not_found_ok=True)


@pytest.fixture
def model_id(client: nnext.Client, dataset_id: str) -> str:
    model_id = "{}.{}".format(dataset_id, uuid.uuid4().hex)

    # The only way to create a model resource is via SQL.
    # Use a very small dataset (2 points), to train a model quickly.
    sql = """
    CREATE MODEL `{}`
    OPTIONS (
        model_type='linear_reg',
        max_iteration=1,
        learn_rate=0.4,
        learn_rate_strategy='constant'
    ) AS (
        SELECT 'a' AS f1, 2.0 AS label
        UNION ALL
        SELECT 'b' AS f1, 3.8 AS label
    )
    """.format(
        model_id
    )

    client.query(sql).result()
    return model_id


@pytest.fixture
def kms_key_name() -> str:
    return "projects/cloud-samples-tests/locations/us/keyRings/test/cryptoKeys/test"
