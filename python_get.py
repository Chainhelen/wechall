import httplib
conn = httplib.HTTPConnection("www.wechall.net")
conn.request('GET',
	'/challenge/training/programming1/index.php?action=request',
	headers = {
		"Cookie":"WC=7812854-12854-Cq73NBAI7vFuiyrX",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
		})
r1 = conn.getresponse()
data = r1.read()

conn.request('GET',
	'/challenge/training/programming1/index.php?answer=' + data,
	headers = {
		"Cookie":"WC=7812854-12854-Cq73NBAI7vFuiyrX",
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
})
conn.getresponse()
