import pytest

from gendiff.formatters.format import formatting, res_formatting
from gendiff.parsers.generate_diff import gen_diff


@pytest.mark.parametrize(
	"data_a, data_b, expected",
	[
        ({}, {}, '{\n\n}'),
        ({'hey': 'karen'}, {}, '{\n  - hey: karen\n}'),
        ({}, {'hey': 'karen'}, '{\n  + hey: karen\n}'),
        ({'hello': 'world'}, {'hello': 'world'}, '{\n    hello: world\n}'),
        (
            {'hello': 'world'}, {'hello': 'sam'},
            '{\n  - hello: world\n  + hello: sam\n}'
            ),
    ]
)
def test_gen_diff(data_a, data_b, expected):
	diff = gen_diff(data_a, data_b)
	lines = formatting(diff)
	assert res_formatting(lines) == expected