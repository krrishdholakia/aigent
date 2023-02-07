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


def delete_routine(routine_id: str) -> None:
    # [START nnext_delete_routine]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set the fully-qualified ID for the routine.
    # routine_id = "my-project.my_dataset.my_routine"

    client.delete_routine(routine_id)  # Make an API request.

    print("Deleted routine {}.".format(routine_id))
    # [END nnext_delete_routine]
