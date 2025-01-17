import inspect

from pydantic import BaseModel
from nnext.client.http.api_client import ApiClient, AsyncApis, SyncApis  # noqa F401
from nnext.client.http.models import models

for model in inspect.getmembers(models, inspect.isclass):
    if model[1].__module__ == "nnext.http.models.models":
        model_class = model[1]
        if issubclass(model_class, BaseModel):
            model_class.update_forward_refs()
