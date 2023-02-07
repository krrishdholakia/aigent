# Copyright 2023 NNEXT Co.
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


def client_query_destination_table_clustered(table_id: str) -> None:
    # [START nnext_query_clustered_table]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"

    sql = "SELECT * FROM `nnext-public-data.samples.shakespeare`"
    cluster_fields = ["corpus"]

    job_config = nnext.QueryJobConfig(
        clustering_fields=cluster_fields, destination=table_id
    )

    # Start the query, passing in the extra configuration.
    query_job = nnclient.query(sql, job_config=job_config)  # Make an API request.
    query_job.result()  # Wait for the job to complete.

    table = nnclient.get_table(table_id)  # Make an API request.
    if table.clustering_fields == cluster_fields:
        print(
            "The destination table is written using the cluster_fields configuration."
        )
    # [END nnext_query_clustered_table]
