# import os
#
# # gives the path of demo.py
# path = os.path.realpath(__file__)
#
# # gives the directory where demo.py
# # exists
# dir = os.path.dirname(path)
# print(dir)

# import app.Main as Main
#
# url = "www.dantri.com"
# print(url[4:])

import app.Main as Main
url = "https://github.com"
Main.check_url(url)
