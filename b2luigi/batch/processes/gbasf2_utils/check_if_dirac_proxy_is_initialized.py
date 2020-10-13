#!/usr/bin/env python2
"""
Script to run as subprocess in a gbasf2 environment (with ``run_with_gbasf``) to
interact with BelleDIRAC and if there is an alive DiracProxy in the system with
a positive amount of seconds left.

This script expects exactly one argument: an integer indicating the minimum of hours
left on the proxy. For example, to check if proxy is active for at least 48 hours::

    $ ./check_if_dirac_proxy_is_initialized.py 48
"""
import sys

from BelleDIRAC.gbasf2.lib.auth import getProxyInfo

if __name__ == "__main__":
    try:
        MinimumSeconds = int(sys.argv[1]) * 3600
    except (ValueError, IndexError):
        print(
            "This script expects an integer argument, indicating the minimum number of "
            "hours left on the proxy."
        )
        sys.exit(1)

    ProxyInfo = getProxyInfo()
    seconds = ProxyInfo["Value"]["secondsLeft"]
    if seconds > MinimumSeconds:
        sys.exit(0)
    sys.exit(1)
