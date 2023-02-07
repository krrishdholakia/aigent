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

if typing.TYPE_CHECKING:
    import pytest


def test_create_routine(
        capsys: "pytest.CaptureFixture[str]", random_routine_id: str
) -> None:
    from .. import create_routine

    create_routine.create_routine(random_routine_id)
    out, err = capsys.readouterr()
    assert "Created routine {}".format(random_routine_id) in out


def test_create_routine_ddl(
        capsys: "pytest.CaptureFixture[str]",
        random_routine_id: str,
        client: nnext.Client,
) -> None:
    from .. import create_routine_ddl

    create_routine_ddl.create_routine_ddl(random_routine_id)
    routine = nnclient.get_routine(random_routine_id)
    out, err = capsys.readouterr()

    assert "Created routine {}".format(random_routine_id) in out
    assert routine.type_ == "SCALAR_FUNCTION"
    assert routine.language == "SQL"
    expected_arguments = [
        nnext.RoutineArgument(
            name="arr",
            data_type=nnext.StandardSqlDataType(
                type_kind=nnext.StandardSqlTypeNames.ARRAY,
                array_element_type=nnext.StandardSqlDataType(
                    type_kind=nnext.StandardSqlTypeNames.STRUCT,
                    struct_type=nnext.StandardSqlStructType(
                        fields=[
                            nnext.StandardSqlField(
                                name="name",
                                type=nnext.StandardSqlDataType(
                                    type_kind=nnext.StandardSqlTypeNames.STRING
                                ),
                            ),
                            nnext.StandardSqlField(
                                name="val",
                                type=nnext.StandardSqlDataType(
                                    type_kind=nnext.StandardSqlTypeNames.INT64
                                ),
                            ),
                        ]
                    ),
                ),
            ),
        )
    ]
    assert routine.arguments == expected_arguments


def test_list_routines(
        capsys: "pytest.CaptureFixture[str]", dataset_id: str, routine_id: str
) -> None:
    from .. import list_routines

    list_routines.list_routines(dataset_id)
    out, err = capsys.readouterr()
    assert "Routines contained in dataset {}:".format(dataset_id) in out
    assert routine_id in out


def test_get_routine(capsys: "pytest.CaptureFixture[str]", routine_id: str) -> None:
    from .. import get_routine

    get_routine.get_routine(routine_id)
    out, err = capsys.readouterr()
    assert "Routine '{}':".format(routine_id) in out
    assert "Type: 'SCALAR_FUNCTION'" in out
    assert "Language: 'SQL'" in out
    assert "Name: 'x'" in out
    assert "type_kind=<StandardSqlTypeNames.INT64: 'INT64'>" in out


def test_delete_routine(capsys: "pytest.CaptureFixture[str]", routine_id: str) -> None:
    from .. import delete_routine

    delete_routine.delete_routine(routine_id)
    out, err = capsys.readouterr()
    assert "Deleted routine {}.".format(routine_id) in out


def test_update_routine(routine_id: str) -> None:
    from .. import update_routine

    routine = update_routine.update_routine(routine_id)
    assert routine.body == "x * 4"
