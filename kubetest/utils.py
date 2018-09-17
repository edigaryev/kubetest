"""Utility functions for kubetest."""

import time


def new_namespace(test_name):
    """Create a new namespace for the given test name.

    Kubernetes namespace names follow a DNS-1123 label that consists
    of lower case alphanumeric characters or '-' and must start with
    an alphanumeric.

    The test name and current timestamp are formatted to comply to
    this spec and appended to the 'kubetest' prefix.

    Args:
        test_name (str): The name of the test case for the namespace.

    Returns:
        str: The namespace name.
    """
    return 'kubetest-{}-{}'.format(
        test_name.replace('_', '-').lower(),
        int(time.time())
    )


def label_string(labels):
    """Create a label string from the given label dictionary.

    Args:
        labels (dict): The labels to stringify.

    Returns:
        str: The label string for the given label dictionary.
    """
    return ','.join(['{}={}'.format(k, v) for k, v in labels.items()])