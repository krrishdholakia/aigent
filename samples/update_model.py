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


def update_model(model_id: str) -> None:
    """Sample ID: go/samples-tracker/1533"""

    # [START nnext_update_model_description]

    import nnext

    # Construct a NNext client object.
    nnclient = nnext.Client()

    # TODO(developer): Set model_id to the ID of the model to fetch.
    # model_id = 'your-project.your_dataset.your_model'

    model = nnclient.get_model(model_id)  # Make an API request.
    model.description = "This model was modified from a Python program."
    model = nnclient.update_model(model, ["description"])  # Make an API request.

    full_model_id = "{}.{}.{}".format(model.project, model.dataset_id, model.model_id)
    print(
        "Updated model '{}' with description '{}'.".format(
            full_model_id, model.description
        )
    )
    # [END nnext_update_model_description]
