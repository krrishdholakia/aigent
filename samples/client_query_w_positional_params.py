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


def client_query_w_positional_params() -> None:
    # [START nnext_query_params_positional]
    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    query = """
        SELECT word, word_count
        FROM `nnext-public-data.samples.shakespeare`
        WHERE corpus = ?
        AND word_count >= ?
        ORDER BY word_count DESC;
    """
    # Set the name to None to use positional parameters.
    # Note that you cannot mix named and positional parameters.
    job_config = nnext.QueryJobConfig(
        query_parameters=[
            nnext.ScalarQueryParameter(None, "STRING", "romeoandjuliet"),
            nnext.ScalarQueryParameter(None, "INT64", 250),
        ]
    )
    query_job = nnclient.query(query, job_config=job_config)  # Make an API request.

    for row in query_job:
        print("{}: \t{}".format(row.word, row.word_count))
    # [END nnext_query_params_positional]
