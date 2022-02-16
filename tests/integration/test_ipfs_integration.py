from scripts.advanced_collectible.create_metadata import upload_to_ipfs
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from brownie import network
import pytest


def test_can_upload_to_ipfs():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")

    image_uri = upload_to_ipfs("./img/pug.png")
    assert (
        image_uri
        == "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"
    )
