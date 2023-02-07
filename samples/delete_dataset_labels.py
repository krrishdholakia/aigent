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

if typing.TYPE_CHECKING:
    import nnext


def delete_dataset_labels(dataset_id: str) -> "nnext.Dataset":
    # [START nnext_delete_label_dataset]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set dataset_id to the ID of the dataset to fetch.
    # dataset_id = "your-project.your_dataset"

    dataset = nnclient.get_dataset(dataset_id)  # Make an API request.

    # To delete a label from a dataset, set its value to None.
    dataset.labels["color"] = None

    dataset = nnclient.update_dataset(dataset, ["labels"])  # Make an API request.
    print("Labels deleted from {}".format(dataset_id))
    # [END nnext_delete_label_dataset]
    return dataset
