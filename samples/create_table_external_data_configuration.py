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


def create_table_external_data_configuration(
        table_id: str,
) -> None:
    """Create a table using an external data source"""
    orig_table_id = table_id
    # [START nnext_create_table_external_data_configuration]
    # [START nnext_create_external_table_definition]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "your-project.your_dataset.your_table_name"
    # [END nnext_create_table_external_data_configuration]
    table_id = orig_table_id
    # [START nnext_create_table_external_data_configuration]

    # TODO(developer): Set the external source format of your table.
    # Note that the set of allowed values for external data sources is
    # different than the set used for loading data (see :class:`~nnext.job.SourceFormat`).
    external_source_format = "AVRO"

    # TODO(developer): Set the source_uris to point to your data in NNext
    source_uris = [
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/a-twitter.avro",
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/b-twitter.avro",
        "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/c-twitter.avro",
    ]

    # Create ExternalConfig object with external source format
    external_config = nnext.ExternalConfig(external_source_format)
    # Set source_uris that point to your data in NNext
    external_config.source_uris = source_uris

    # TODO(developer) You have the option to set a reference_file_schema_uri, which points to
    # a reference file for the table schema
    reference_file_schema_uri = "gs://nnext-sample-data/nnext/federated-formats-reference-file-schema/b-twitter.avro"

    external_config.reference_file_schema_uri = reference_file_schema_uri
    # [END nnext_create_external_table_definition]

    table = nnext.Table(table_id)
    # Set the external data configuration of the table
    table.external_data_configuration = external_config
    table = nnclient.create_table(table)  # Make an API request.

    print(
        f"Created table with external source format {table.external_data_configuration.source_format}"
    )
    # [END nnext_create_table_external_data_configuration]
