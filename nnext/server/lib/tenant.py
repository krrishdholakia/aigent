#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 NNext, Co."

# Standard Libraries

# External Libraries
from loguru import logger

# Internal Libraries
from nnext.server.lib.prisma import prisma

# Global Variables

# Functions
def init_default():
    agent = prisma.tenant.find_unique(where={"slug": 'default'}, include={"prompt": True})

    logger.info("🏠 Initialized default tenant")