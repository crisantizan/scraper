from urllib.parse import urlsplit


def split_url(url):
	"""Get domain from url

	Args:
		url (string): target URL

	Returns:
		SplitResult: URL parts
	"""
	return urlsplit(url)
