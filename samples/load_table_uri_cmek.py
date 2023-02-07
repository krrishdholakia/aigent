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


def load_table_uri_cmek(table_id: str, kms_key_name: str) -> None:
    # [START nnext_load_table_gcs_json_cmek]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name

    # Set the encryption key to use for the destination.
    # TODO: Replace this key with a key you have created in KMS.
    # kms_key_name = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
    #     "cloud-samples-tests", "us", "test", "test"
    # )

    job_config = nnext.LoadJobConfig(
        autodetect=True,
        source_format=nnext.SourceFormat.NEWLINE_DELIMITED_JSON,
        destination_encryption_configuration=nnext.EncryptionConfiguration(
            kms_key_name=kms_key_name
        ),
    )

    uri = "gs://nnext-sample-data/nnext/us-states/us-states.json"

    load_job = nnclient.load_table_from_uri(
        uri,
        table_id,
        location="US",  # Must match the destination dataset location.
        job_config=job_config,
    )  # Make an API request.

    assert load_job.job_type == "load"

    load_job.result()  # Waits for the job to complete.

    assert load_job.state == "DONE"
    table = nnclient.get_table(table_id)

    if table.encryption_configuration.kms_key_name == kms_key_name:
        print("A table loaded with encryption configuration key")

    # [END nnext_load_table_gcs_json_cmek]
