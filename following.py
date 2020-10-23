from igramscraper.instagram import Instagram

from settings import user_id, inst_username, inst_password


from igramscraper.instagram import Instagram

instagram = Instagram()

# authentication supported
instagram.with_credentials(inst_username, inst_password)
instagram.login()

