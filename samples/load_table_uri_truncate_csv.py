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


def load_table_uri_truncate_csv(table_id: str) -> None:
    # [START nnext_load_table_gcs_csv_truncate]
    import io

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name

    job_config = nnext.LoadJobConfig(
        schema=[
            nnext.SchemaField("name", "STRING"),
            nnext.SchemaField("post_abbr", "STRING"),
        ],
    )

    body = io.BytesIO(b"Washington,WA")
    client.load_table_from_file(body, table_id, job_config=job_config).result()
    previous_rows = nnclient.get_table(table_id).num_rows
    assert previous_rows > 0

    job_config = nnext.LoadJobConfig(
        write_disposition=nnext.WriteDisposition.WRITE_TRUNCATE,
        source_format=nnext.SourceFormat.CSV,
        skip_leading_rows=1,
    )

    uri = "gs://nnext-sample-data/nnext/us-states/us-states.csv"
    load_job = nnclient.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = nnclient.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))
    # [END nnext_load_table_gcs_csv_truncate]
