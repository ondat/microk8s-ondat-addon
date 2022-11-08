import pytest
import os
import platform

from validators import (
    # ensure that the "validate_ondat" function is
    # called here, alongside other functions in this file.
    # https://github.com/canonical/microk8s-community-addons/tree/main/tests
    validate_ondat,
)

from utils import (
    microk8s_enable,
    microk8s_disable,
)

from subprocess import PIPE, STDOUT, CalledProcessError, check_call, run, check_output


class TestAddons(object):
    # append the following Ondat add-on tests
    # here, alongside other add-ons in this file.
    # https://github.com/canonical/microk8s-community-addons/tree/main/tests
    @pytest.mark.skipif(
        platform.machine() != "x86_64",
        reason="Ondat tests are only relevant in x86 architectures",
    )
    #@pytest.mark.skipif(
    #    os.environ.get("UNDER_TIME_PRESSURE") == "True",
    #    reason="Skipping Ondat tests as we are under time pressure",
    #)
    def test_ondat(self):
        """
        Setup and validates Ondat.
        """
        print("Enabling Ondat.")
        microk8s_enable("ondat")
        print("Validating Ondat.")
        validate_ondat()
        print("Disabling Ondat.")
        microk8s_disable("ondat")
