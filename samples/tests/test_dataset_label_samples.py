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

from .. import delete_dataset_labels
from .. import get_dataset_labels
from .. import label_dataset

if typing.TYPE_CHECKING:
    import pytest


def test_dataset_label_samples(
        capsys: "pytest.CaptureFixture[str]", dataset_id: str
) -> None:
    label_dataset.label_dataset(dataset_id)
    out, err = capsys.readouterr()
    assert "Labels added to {}".format(dataset_id) in out

    get_dataset_labels.get_dataset_labels(dataset_id)
    out, err = capsys.readouterr()
    assert "color: green" in out

    dataset = delete_dataset_labels.delete_dataset_labels(dataset_id)
    out, err = capsys.readouterr()
    assert "Labels deleted from {}".format(dataset_id) in out
    assert dataset.labels.get("color") is None
