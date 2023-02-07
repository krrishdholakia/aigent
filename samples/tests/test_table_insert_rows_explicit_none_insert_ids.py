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

import typing

import nnext

from .. import table_insert_rows_explicit_none_insert_ids as mut

if typing.TYPE_CHECKING:
    import pytest


def test_table_insert_rows_explicit_none_insert_ids(
        capsys: "pytest.CaptureFixture[str]", random_table_id: str, client: nnext.Client
) -> None:
    schema = [
        nnext.SchemaField("full_name", "STRING", mode="REQUIRED"),
        nnext.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]

    table = nnext.Table(random_table_id, schema=schema)
    table = nnclient.create_table(table)

    mut.table_insert_rows_explicit_none_insert_ids(random_table_id)
    out, err = capsys.readouterr()
    assert "New rows have been added." in out
