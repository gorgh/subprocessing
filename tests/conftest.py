# -*- coding: utf-8 -*-

"""Pytest configuration file."""

import logging

import subprocessing

HANDLER = logging.StreamHandler()


def configure_logger(name: str, config, add_handler: bool = False):
    """Configure a logger object depending on the verbosity level of pytest.

    Parameters
    ----------
    name
        Name of the logger to configure.
    config
        Pytest configuration object containing command line arguments.
    add_handler
        Add ``HANDLER`` to the logger. Deactivate by default.
    """
    logger = logging.getLogger(name)

    # Add the centralized handler
    if add_handler and HANDLER not in logger.handlers:
        logger.addHandler(HANDLER)

    # Set the verbosity level of the logger
    if config.getoption("verbose") > 1:
        logger.setLevel(logging.DEBUG)
    elif config.getoption("verbose"):
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARN)


def pytest_configure(config):
    """Perform initial configuration of pytest environment.

    This hook is called for every plugin and initial conftest file after command
    line options have been parsed.
    """
    configure_logger(subprocessing.__name__, config, add_handler=False)
