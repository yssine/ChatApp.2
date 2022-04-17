




class User:
	def __init__(self, usn='', pdp=None, conn=None, addr=None):
		self.usn = usn
		self.pdp = pdp
		self.conn = conn
		self.addr = addr

	def pr(self):
		print(self.usn,", ",self.pdp)



class Message:
	def __init__(self, usr=None, msg=None, typ=''):
		self.usr = usr
		self.msg = msg
		self.typ = typ


# ysn=User(conn='lol')
# ysn.pr()
