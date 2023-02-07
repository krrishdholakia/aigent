# -*- coding: utf-8 -*-
#
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

__version__ = '0.1.0'

from .nnext_client import NNextClient


def _in_ipython() -> bool:
    """
    Check whether we're in an ipython environment, including jupyter notebooks.
    """
    try:
        eval('__IPYTHON__')
    except NameError:
        return False
    else:  # pragma: no cover
        return True


if _in_ipython():  # pragma: no cover
    # Python asyncio design is mediocre, it is not possible to await for a future, if there is another loop running.
    # Ipython uses asyncio, which makes it impossible to run other async functions, so we need to monkey-patch it.
    # It might be dangerous to do this in production, so we are doing it for Jupyter notebooks only.
    import nest_asyncio

    nest_asyncio.apply()
