'''
desciption: get ISP Information
dependencies: pip install speedtest-cli
'''
import speedtest

def getISPInfo():
	try:
		s = speedtest.Speedtest()
		s.get_servers([])
		s.get_best_server()
		res = s.results.dict()
		client = res['client']

		ip = client['ip']
		isp = client['isp']
		isp_rating = client['isprating']

		return [ip, isp, isp_rating,1]
	except:
		return [0, 0, 0,0]



def getInternetSpeed():
	try:
		pass
		s = speedtest.Speedtest()
		s.get_servers([])
		s.get_best_server()
		s.download(threads=None)
		s.upload(threads=None)
		s.results.share()
		res = s.results.dict()

		download = res['download'] * 0.000001
		upload = res['upload'] * 0.000001
		ave_speed = (res['download']+res['upload']) / 2 * 0.000001

		ping = res['ping']
		bytes_sent = res['bytes_sent']
		bytes_received = res['bytes_received']
		png_result = res['share']
		return [ave_speed, download, upload, ping, bytes_sent, bytes_received, png_result,1]		
	except:
		return [0, 0, 0, 0, 0, 0, 0,0]		







