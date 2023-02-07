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

from .. import dataset_exists

if typing.TYPE_CHECKING:
    import pytest


def test_dataset_exists(
        capsys: "pytest.CaptureFixture[str]",
        random_dataset_id: str,
        client: nnext.Client,
) -> None:
    dataset_exists.dataset_exists(random_dataset_id)
    out, err = capsys.readouterr()
    assert "Dataset {} is not found".format(random_dataset_id) in out
    dataset = nnext.Dataset(random_dataset_id)
    dataset = nnclient.create_dataset(dataset)
    dataset_exists.dataset_exists(random_dataset_id)
    out, err = capsys.readouterr()
    assert "Dataset {} already exists".format(random_dataset_id) in out
