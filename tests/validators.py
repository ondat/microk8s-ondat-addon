import platform

from utils import (
    wait_for_pod_state,
    wait_for_installation,
)

# append the following "validate_ondat" function
# alongside other functions in this file.
# https://github.com/canonical/microk8s-community-addons/tree/main/tests
def validate_ondat():
    """
    Validate the Ondat addon.
    """
    if platform.machine() != "x86_64":
        print("Ondat tests are only relevant in x86 architectures")
        return
    wait_for_installation()
    wait_for_pod_state(
        "storageos-cli", "storageos", "running", label="app=storageos-cli"
    )
    wait_for_pod_state(
        "ondat-ondat-operator", "storageos", "running", label="app=ondat-operator"
    )
    wait_for_pod_state("storageos-node", "storageos", "running", label="app=storageos")
