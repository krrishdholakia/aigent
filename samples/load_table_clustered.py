# Copyright 2023 NNEXT Co.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

if typing.TYPE_CHECKING:
    import nnext


def load_table_clustered(table_id: str) -> "nnext.Table":
    # [START nnext_load_table_clustered]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    job_config = nnext.LoadJobConfig(
        skip_leading_rows=1,
        source_format=nnext.SourceFormat.CSV,
        schema=[
            nnext.SchemaField("timestamp", nnext.SqlTypeNames.TIMESTAMP),
            nnext.SchemaField("origin", nnext.SqlTypeNames.STRING),
            nnext.SchemaField("destination", nnext.SqlTypeNames.STRING),
            nnext.SchemaField("amount", nnext.SqlTypeNames.NUMERIC),
        ],
        time_partitioning=nnext.TimePartitioning(field="timestamp"),
        clustering_fields=["origin", "destination"],
    )

    job = nnclient.load_table_from_uri(
        ["gs://nnext-sample-data/nnext/sample-transactions/transactions.csv"],
        table_id,
        job_config=job_config,
    )

    job.result()  # Waits for the job to complete.

    table = nnclient.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
    # [END nnext_load_table_clustered]
    return table
