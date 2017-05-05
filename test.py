# -*- coding:utf-8 -*-
import urllib2
import json
import MySQLdb as D
from lxml import etree

host1 = 'http://cn.morningstar.com/handler/fundranking.ashx?date=??????&fund=&category\
=stock&rating=&company=&cust=&sort=StarRating3&direction=desc&tabindex=0&pageindex=1&pagesize=50'

host2 = 'http://cn.morningstar.com/handler/fundranking.ashx?date=??????&fund=&category\
=mix_radical&rating=&company=&cust=&sort=StarRating3&direction=desc&tabindex=0&pageindex=1&pagesize=50'
host3 = 'http://cn.morningstar.com/handler/fundranking.ashx?date=??????&fund=&category\
=mix_standard&rating=&company=&cust=&sort=StarRating3&direction=desc&tabindex=0&pageindex=1&pagesize=20'



Config_DBhost='127.0.0.1'
Config_DBuser='root'
Config_DBpasswd = 'root'
Config_DBtable = 'Jstock'

class Finance():
	"""docstring for finance"""
	api = '123'
	def SetApi(self,url):
		self.api = url

	def ReadWeb(self,Decode='gbk'):
		pass

	def LoadJson(self):
		pass

	def test(self):
		print("Hello world")
		print(self.api)
class JJ(Finance):
	"""docstring for JJ"""
	update = 'http://cn.morningstar.com/fundtools/fundranking/default.aspx'
	data =''
	def Get_time(self):
		self.data = ''
		html = self.ReadWeb('utf-8',self.update)
		html = etree.HTML(html)
		return  html.xpath('//*[@id="FRTool"]/div/select[3]/option//text()')
		
	def ReadWeb(self,Decode='gbk',api=''):
		if not api:
			api = self.api
		html= urllib2.urlopen(api).read().decode(Decode)
		return html

	def LoadEtree(self):
		update = self.Get_time()
		tapi = self.api 
		tapi = tapi.replace("??????",update[0])
		#//*[@id="fr_divPage1"]/div[2]/table/tbody/tr[1]
		text =  self.ReadWeb(api=tapi,Decode='utf-8')
		return etree.HTML(text)
	def get_data(self,host,mflag):
		self.api = host
		data = self.ReadWeb(Decode = 'utf-8',api = host)
		Etreedata = self.LoadEtree()
		iflag = 1
		jlist = []
		while 1:
			print "分析进度:",iflag
			if iflag > mflag:
				break
			perjj = Etreedata.xpath('//*[@id="fr_divPage1"]/div[2]/table//tr[%d]//text()'%iflag)
			if len(perjj)>1:
				del perjj[1]
				for index,i in enumerate(perjj):
					if "\r\n" in perjj[index]:
						del perjj[index]
				for index,i in enumerate(perjj):
					if "\r\n" in perjj[index]:
						del perjj[index]
				del perjj[10]
				jlist.append(perjj)
			iflag += 1	

		return jlist



class DB():

	DBhost = Config_DBhost
	DBroot = Config_DBuser
	DBpasswd = Config_DBpasswd
	DBtable = Config_DBtable
	def __init__(self):
		pass

	def connectDB(self):
		try:
			self.conn = D.connect(self.DBhost,self.DBroot,self.DBpasswd,self.DBtable)
			self.conn.set_character_set('utf8')
			self.cursor = self.conn.cursor()
		except Exception as e:
			print "错误代码:",e[0],"\n信息:",e[1]
			#raise "异常退出"
	def insertDB(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except Exception as e:
			print "Error: it is rollbacking"
			print e
			self.conn.rollback()
	def queryDB(self,sql):
		try:
			self.cursor.execute(sql)
			return self.cursor.fetchall()
		except Exception as e:
			print "Error: unable to fecth data"
			print e
			return None

	def updateDB(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
		except Exception as e:
			print e
			self.conn.rollback()
	def deleteDB(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			print "执行 |  ",sql,"  | 完毕"
		except Exception as e:
			print e
			self.conn.rollback()
	def closeDB(self):
		self.conn.close()


		


class Get_stock_code():
	"""docstring for Get_stock_code"""
	def __init__(self, arg):
		self.G = DB()
		self.api = arg
		
	def GetAllCode(self):
		self.G.connectDB()
		b = self.G.queryDB('select jjcode,name from jcode')
		stock = []
		#for i in b:
		#	api = self.api.replace("??????",i[0])
		#	self.ReadWeb(api,Decode='utf-8')'''
		for i in b:
			api = self.api.replace("??????",i[0])
			data = self.ReadWeb(api,Decode='utf-8')
			print "抓取代码",i[0],"任务URL：",api
			num = len(data.xpath('/html/body/div/div/table/tbody//tr'))
			mflag = 1
			while 1:
				if mflag > num:
					break
				text = data.xpath('/html/body/div/div/table/tbody//tr[%d]//text()'%mflag)
				stock.append([text[1],text[2],text[7],i[0],i[1]])
				mflag += 1
		self.G.closeDB()
		return  stock

	def ReadWeb(self,api,Decode='gbk'):
		html = urllib2.urlopen(api).read().decode(Decode)
		return  etree.HTML(html)

def updatestock():
	a = Get_stock_code('http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=jjcc&code=??????&topline=40')
	stock = a.GetAllCode() #有重复项，记得去重	

	G = DB()
	G.connectDB()
	G.deleteDB("delete from scode")
	for i in stock:
		
		sql = """INSERT INTO scode (gpcode,name,percent,jjcode,jjname) VALUES ('%s','%s',%s,'%s','%s')
		"""%(i[0],i[1],i[2][:-1],i[3].decode('utf-8'),i[4].decode('utf-8'))
		G.insertDB(sql)	

	G.deleteDB('delete from scode where percent <  0.3')
	G.closeDB()		


def updatejj():
	# 晨星基金评级 三个月更新一次
	a = DB()
	a.connectDB()	
	b = JJ()
	Recvdata = b.get_data(host1,50)
	Recvdata.extend(b.get_data(host2,50))
	Recvdata.extend(b.get_data(host3,20))
	a.deleteDB("delete from jcode")
	for c in Recvdata:
		sql =  """INSERT INTO jcode(jjcode, name, dwjz, 3ybdfd,3ybdpj,cxfxxx,cxpj,xpbl3y,xppj3y,fromyl)
		VALUES ('%s','%s',%s,%s,'%s',%s,'%s',%s,'%s',%s)"""%(c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9])
		a.insertDB(sql)
	a.closeDB()

updatejj()
updatestock()

"""
CREATE TABLE jcode (
		code CHAR(10) NOT NULL PRIMARY KEY,
		name CHAR(60) NOT NULL,
		dwjz DOUBLE NOT NULL,
		3ybdfd DOUBLE NOT NULL,
		3ybdpj CHAR(10) NOT NULL,
		cxfxxx DOUBLE NOT NULL,
		cxpj CHAR(10) NOT NULL,
		xpbl3y DOUBLE NOT NULL,
		xppj3y CHAR(10) NOT NULL,
		fromyl DOUBLE NOT NULL
)DEFAULT CHARSET=utf8;
"""

"""
CREATE TABLE scode (
		code CHAR(10) NOT NULL PRIMARY KEY,
		name CHAR(60) NOT NULL,
		percent DOUBLE NOT NULL
)DEFAULT CHARSET=utf8;

"""


	#print "基金代码 基金名称 单位净值 波动幅度 评价 晨星风险系数 评价 最近三年 评价 今年以来总回报率 排名"
#http://fund.eastmoney.com/f10/FundArchivesDatas.aspx?type=jjcc&code=000311&topline=40
	

