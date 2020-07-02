try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def list_of_sites(query):
    site_list = search(query, tld="co.in", num=10, stop=10, pause=2)
    return site_list
