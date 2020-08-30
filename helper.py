from urllib.parse import urlsplit


def get_domain(url):
	"""Get domain from url

	Args:
		url (string): target URL

	Returns:
		string: URL domain
	"""
	return urlsplit(url).netloc
