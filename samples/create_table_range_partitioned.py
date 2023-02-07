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


def create_table_range_partitioned(table_id: str) -> "nnext.Table":
    # [START nnext_create_table_range_partitioned]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    schema = [
        nnext.SchemaField("full_name", "STRING"),
        nnext.SchemaField("city", "STRING"),
        nnext.SchemaField("zipcode", "INTEGER"),
    ]

    table = nnext.Table(table_id, schema=schema)
    table.range_partitioning = nnext.RangePartitioning(
        # To use integer range partitioning, select a top-level REQUIRED /
        # NULLABLE column with INTEGER / INT64 data type.
        field="zipcode",
        range_=nnext.PartitionRange(start=0, end=100000, interval=10),
    )
    table = nnclient.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )
    # [END nnext_create_table_range_partitioned]
    return table
