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


def get_table(table_id: str) -> None:
    # [START nnext_get_table]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the model to fetch.
    # table_id = 'your-project.your_dataset.your_table'

    table = nnclient.get_table(table_id)  # Make an API request.

    # View table properties
    print(
        "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
    )
    print("Table schema: {}".format(table.schema))
    print("Table description: {}".format(table.description))
    print("Table has {} rows".format(table.num_rows))
    # [END nnext_get_table]
