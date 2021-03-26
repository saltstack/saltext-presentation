import pytest
import salt.modules.test as testmod
import saltext.presentation.modules.presentation_mod as presentation_module
import saltext.presentation.states.presentation_mod as presentation_state


@pytest.fixture
def configure_loader_modules():
    return {
        presentation_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        presentation_state: {
            "__salt__": {
                "presentation.example_function": presentation_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": "The 'presentation.example_function' returned: '{}'".format(echo_str),
    }
    assert presentation_state.exampled(echo_str) == expected
