# coding=utf-8
"""Utilities for interacting with OS tree."""
from pulp_smash.tests.pulp2 import utils
from pulp_smash.utils import uuid4


def set_up_module():
    """Skip tests if Pulp 2 isn't under test or if OSTree isn't installed."""
    utils.require_pulp_2()
    utils.require_issue_3159()
    utils.require_unit_types({'ostree'})


def gen_repo():
    """Return a semi-random dict for use in creating an OSTree repository."""
    return {
        'id': uuid4(),
        'importer_type_id': 'ostree_web_importer',
        'importer_config': {},
        'distributors': [],
        'notes': {'_repo-type': 'OSTREE'},
    }


def gen_distributor():
    """Return a semi-random dict for use in creating an OSTree distributor.

    For more information, see the generic `repository CRUD`_ documentation and
    the OSTree `distributor configuration`_ documentation.

    .. NOTE: The OSTree `distributor configuration`_ documentation doesn't list
        the available parameters. To discover which parameters are available,
        execute ``pulp-admin -vv ostree repo create …``. See `Pulp #2254`_.

    .. _repository CRUD:
        http://docs.pulpproject.org/dev-guide/integration/rest-api/repo/cud.html
    .. _distributor configuration:
        http://docs.pulpproject.org/plugins/pulp_ostree/tech-reference/distributor.html
    .. _Pulp #2254: https://pulp.plan.io/issues/2254
    """
    return {
        'distributor_id': uuid4(),
        'distributor_type_id': 'ostree_web_distributor',
    }
