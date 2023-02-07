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
from typing import Union

if typing.TYPE_CHECKING:
    from nnext import LoadJob, CopyJob, ExtractJob, QueryJob


def create_job() -> "Union[LoadJob, CopyJob, ExtractJob, QueryJob]":
    # [START nnext_create_job]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    query_job = nnclient.create_job(
        # Specify a job configuration, providing a query
        # and/or optional job resource properties, as needed.
        # The job instance can be a LoadJob, CopyJob, ExtractJob, QueryJob
        # Here, we demonstrate a "query" job.
        #
        # Example use cases for .create_job() include:
        #    * to retry failed jobs
        #    * to generate jobs with an experimental API property that hasn't
        #      been added to one of the manually written job configuration
        #      classes yet
        #
        # NOTE: unless it is necessary to create a job in this way, the
        # preferred approach is to use one of the dedicated API calls:
        #   client.query()
        #   client.extract_table()
        #   client.copy_table()
        #   client.load_table_file(), client.load_table_from_dataframe(), etc
        job_config={
            "query": {
                "query": """
                         SELECT country_name
                         FROM `nnext-public-data.utility_us.country_code_iso`
                         LIMIT 5
                         """,
            },
            "labels": {"example-label": "example-value"},
            "maximum_bytes_billed": 10000000,
        }
    )  # Make an API request.

    print(f"Started job: {query_job.job_id}")
    # [END nnext_create_job]

    return query_job
