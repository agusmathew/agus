class BACC:
	def __init__(self,ac_name):
		self.bal = 0
		self.name = ac_name
	def wd(self,am):
		self.bal -=am
		return self.bal
	def dp(self,am):
		self.bal +=am
		return self.bal
	def dis_bal(self):
		print self.bal
		return self.bal
class MIN_BACC(BACC):
	def __init__(self,cu,min_bal):

		BACC.__init__(self,cu)
		self.min_bal = min_bal
		self.bal = min_bal
	def wd(self,am):
		if self.bal -am < self.min_bal:
			print "maintain mi bal"
		else:
			BACC.wd(self,am)

cu_di = []
cu_li = []
def create_salary_acc():
	cu = raw_input("name:")
	a = MIN_BACC(cu,1000)
	cu_di.append((cu,a))
	cu_li.append(cu)
def create_savings_acc():
	cu = raw_input("name:")
	a = BACC(cu)
	cu_di.append((cu,a))
	cu_li.append(cu)
def transact():
	while True:
		select2 = raw_input("ur ch:\n1:wd 2:dp 3:dis 4:logout")
		if select2 == '1':
			am = int(raw_input("am:"))
			for i in cu_di:
				if i[0] == check_cu:
					i[1].wd(am)
		elif select2 == '2':
			am = int(raw_input("am:"))
			for i in cu_di:
				if i[0] == check_cu:

					i[1].dp(am)

		elif select2 == '3':
			for i in cu_di:
				if i[0] == check_cu:

					i[1].dis_bal()
		elif select2 == '4':
			break

while True:
	select1 = raw_input("ur ch:\n1:create 2:login 3:exit")
	if select1 == '1':
		ac = raw_input("1.Savings acc: 2.Salary acc:")
		if ac == '1':
			create_savings_acc()
		elif ac == '2':
			create_salary_acc()
		
	elif select1 == '2':
		check_cu = raw_input("acc name:")
		if check_cu in cu_li:
			transact()
		else:
			print "no such user"
	elif select1 == '3':
		break
