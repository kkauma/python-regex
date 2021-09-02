# Phone and Email regex generator using Python

import pyperclip, re

# Create regex for phone numbers
phone_regex = re.compile(r"""
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)?						# separator
	(\d{3})							# first 3 digits
	(\s|-|\.)						# separator
	(\d{4})							# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)""", re.VERBOSE)

# Create email regex
email_regex = re.compile(r"""
	[a-zA-Z0-9._%+-]+				# username
	@								# @ symbol
	[a-zA-Z0-9.-]+					# domain name
	(\.[a-zA-z]{2,4})				# dot-something
	)""", re.VERBOSE)





