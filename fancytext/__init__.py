import json
import os
import random
import re
import string
import unicodedata


MAPPING_FILE = os.path.join(os.path.dirname(__file__), 'fancy_mapping.json')


class FancyMapping(object):
	"""
	This class is for generating a fancy unicode mapping.
	"""

	regex_template = '^LETTER {0}\s.*$|^.*\sLETTER {0}$|^.*\sLETTER {0}\s.*$'

	def __init__(self):
		self.mapping = self._generate()

	def _generate(self):
		self.unicode_char_names = self._get_unicode_names()
		return self._get_mapping()

	def _get_mapping(self):
		char_mapping = {}
		for character in string.lowercase:
			char_mapping[character] = self._get_mapping_for_char(character)
		return char_mapping

	def _get_mapping_for_char(self, character):
		char_regex_string = self.regex_template.format(character)
		char_regex = re.compile(char_regex_string, flags=re.IGNORECASE)
		matches = set()
		for unicode_name in self.unicode_char_names:
			if char_regex.match(unicode_name):
				unicode_char = unicodedata.lookup(unicode_name)
				if character.lower() != unicode_char.lower():
					matches.add(unicode_name)
		return list(matches)

	def _get_unicode_names(self):
		unicode_char_names = set()
		for code_point_offset in range(10**6):
			try:
				unicode_char = unichr(0x0 + code_point_offset)
			except ValueError:
				pass
			else:
				try:
					name = unicodedata.name(unicode_char)
				except ValueError:
					pass
				else:
					unicode_char_names.add(name)
		return unicode_char_names


with open(MAPPING_FILE, 'r') as f:
	fancy_mapping = json.load(f)


def fancy(string, mapping=None):
	if mapping is None:
		mapping = fancy_mapping

	result = ''
	for char in string:
		lowercase_char = char.lower()
		try:
			fancy_char_names = mapping[lowercase_char]
		except KeyError:
			result += char
		else:
			fancy_char_name = random.sample(fancy_char_names, 1)[0]
			result += unicodedata.lookup(fancy_char_name)

	return result
