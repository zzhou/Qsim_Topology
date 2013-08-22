#!/usr/bin/python
# $Id$

import sys

from Cobalt.Components.cluster_system import ClusterSystem
from Cobalt.Components.base import run_component

if __name__ == "__main__":
    try:
        run_component(ClusterSystem, register=True, state_name="cluster_system")
    except KeyboardInterrupt:
        sys.exit(1)
