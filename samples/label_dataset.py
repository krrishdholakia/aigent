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


def label_dataset(dataset_id: str) -> None:
    # [START nnext_label_dataset]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set dataset_id to the ID of the dataset to fetch.
    # dataset_id = "your-project.your_dataset"

    dataset = nnclient.get_dataset(dataset_id)  # Make an API request.
    dataset.labels = {"color": "green"}
    dataset = nnclient.update_dataset(dataset, ["labels"])  # Make an API request.

    print("Labels added to {}".format(dataset_id))
    # [END nnext_label_dataset]
