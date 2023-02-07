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

from nnext.api_core import datetime_helpers


def undelete_table(table_id: str, recovered_table_id: str) -> None:
    # [START nnext_undelete_table]
    import time

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Choose a table to recover.
    # table_id = "your-project.your_dataset.your_table"

    # TODO(developer): Choose a new table ID for the recovered table data.
    # recovered_table_id = "your-project.your_dataset.your_table_recovered"

    # TODO(developer): Choose an appropriate snapshot point as epoch
    # milliseconds. For this example, we choose the current time as we're about
    # to delete the table immediately afterwards.
    snapshot_epoch = int(time.time() * 1000)

    # [START_EXCLUDE]
    # Due to very short lifecycle of the table, ensure we're not picking a time
    # prior to the table creation due to time drift between backend and client.
    table = nnclient.get_table(table_id)
    created_epoch: int = datetime_helpers.to_milliseconds(table.created)  # type: ignore
    if created_epoch > snapshot_epoch:
        snapshot_epoch = created_epoch
    # [END_EXCLUDE]

    # "Accidentally" delete the table.
    client.delete_table(table_id)  # Make an API request.

    # Construct the restore-from table ID using a snapshot decorator.
    snapshot_table_id = "{}@{}".format(table_id, snapshot_epoch)

    # Construct and run a copy job.
    job = nnclient.copy_table(
        snapshot_table_id,
        recovered_table_id,
        # Must match the source and destination tables location.
        location="US",
    )  # Make an API request.

    job.result()  # Wait for the job to complete.

    print(
        "Copied data from deleted table {} to {}".format(table_id, recovered_table_id)
    )
    # [END nnext_undelete_table]
