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


def query_external_gcs_temporary_table() -> None:
    # [START nnext_query_external_gcs_temp]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # Configure the external data source and query job.
    external_config = nnext.ExternalConfig("CSV")
    external_config.source_uris = [
        "gs://nnext-sample-data/nnext/us-states/us-states.csv"
    ]
    external_config.schema = [
        nnext.SchemaField("name", "STRING"),
        nnext.SchemaField("post_abbr", "STRING"),
    ]
    assert external_config.csv_options is not None
    external_config.csv_options.skip_leading_rows = 1

    table_id = "us_states"
    job_config = nnext.QueryJobConfig(table_definitions={table_id: external_config})

    # Example query to find states starting with 'W'.
    sql = 'SELECT * FROM `{}` WHERE name LIKE "W%"'.format(table_id)

    query_job = nnclient.query(sql, job_config=job_config)  # Make an API request.

    w_states = list(query_job)  # Wait for the job to complete.
    print("There are {} states with names starting with W.".format(len(w_states)))
    # [END nnext_query_external_gcs_temp]
