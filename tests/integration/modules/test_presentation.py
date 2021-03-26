import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("presentation.example_function"),
]


def test_replace_this_this_with_something_meaningful(salt_call_cli):
    echo_str = "Echoed!"
    ret = salt_call_cli.run("presentation.example_function", echo_str)
    assert ret.exitcode == 0
    assert ret.json
    assert ret.json == echo_str
