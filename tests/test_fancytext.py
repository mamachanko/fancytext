import string
import unicodedata

import pytest

from fancytext import fancy, fancy_mapping, FancyMapping


@pytest.fixture
def mapping():
	return FancyMapping().mapping


def test_empty_string():
	assert fancy('') == ''


def test_all_fancy_ascii_characters():
	original_text = string.lowercase + string.uppercase
	_assert_fancy_text(original_text, fancy(original_text))


def test_fancy_string_mapping_injection():
	mapping = {'p': [unicodedata.name(u'b')],
               'h': [unicodedata.name(u'e')]}
	assert fancy('Python', mapping=mapping) == 'byteon'


def test_fancy_string_empty_mapping():
	assert fancy('Fancy text!', mapping={}) == 'Fancy text!'


def test_fancy_string_with_generated_mapping(mapping):
	original_text = 'This is fancy, or is it not?'
	fancy_text = fancy(original_text, mapping=mapping)
	_assert_fancy_text(original_text, fancy_text, mapping=mapping)


def _assert_fancy_text(original_text, fancy_text, mapping=fancy_mapping):
	for original_char, fancy_char in zip(original_text, fancy_text):
		if original_char.isalpha():
			assert fancy_char != original_char
			fancy_char_names = mapping[original_char.lower()]
			assert fancy_char in map(unicodedata.lookup, fancy_char_names)


if __name__ == "__main__":
	sample_phrases = [
		'Everybody loves him.',
		'My university has dormitories.',
		'He is unpopular for some reason.',
		'The driver told us which bus we should take.',
		'Keep out.',
		'Is he a teacher?']

	for phrase in sample_phrases:
		print(fancy(phrase))
