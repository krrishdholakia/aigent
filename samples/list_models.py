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


def list_models(dataset_id: str) -> None:
    """Sample ID: go/samples-tracker/1512"""

    # [START nnext_list_models]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set dataset_id to the ID of the dataset that contains
    #                  the models you are listing.
    # dataset_id = 'your-project.your_dataset'

    models = nnclient.list_models(dataset_id)  # Make an API request.

    print("Models contained in '{}':".format(dataset_id))
    for model in models:
        full_model_id = "{}.{}.{}".format(
            model.project, model.dataset_id, model.model_id
        )
        friendly_name = model.friendly_name
        print("{}: friendly_name='{}'".format(full_model_id, friendly_name))
    # [END nnext_list_models]
