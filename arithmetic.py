import random
from reportlab.pdfgen import canvas
from reportlab import platypus
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime

pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))
Style=getSampleStyleSheet()

data_regroup = [['10 ', ' +', ' 4 ',' =   '],
	   ['10 ', ' +', ' 1 ',' =   '],
	   [' ', '', '','   '],
	   ['10 ', ' +', ' 10',' =   '],
	   [' 4', ' +', ' 1 ',' =   '],
	   [' ', '', '','   '],
	   ['14 ', ' +', ' 11',' =   ']]

def getRegroup(a,b):
	tenth1 = a-a%10
	single1 = a%10
	tenth2 = b-b%10
	single2 = b%10
	item1 = ['%s '%tenth1, ' +', ' %s '%single1,' =   ']
	item2 = ['%s '%tenth2, ' +', ' %s '%single2,' =   ']
	item3 = [' ', ' ', ' ','   ']
	item4 = ['%s '%tenth1, ' +', ' %s'%tenth2,' =   ']
	item5 = [' %s'%single1, ' +', ' %s '%single2,' =   ']
	item6 = [' ', '', '','   ']
	item7 = [' ', '', '','   ']
	item8 = ['%s '%a, ' +', ' %s'%b,' =   ']
	data=[]
	data.append(item1)
	data.append(item2)
	data.append(item3)
	data.append(item4)
	data.append(item5)
	data.append(item6)
	data.append(item7)
	data.append(item8)
	print(data)
	return data
	pass

def getAdd(startNum,endNum):
	allFormula = []
	for i in range(startNum,endNum+1):
		for j in range(1,i):
			allFormula.append((j,i-j))
	print(len(allFormula))
	#random.shuffle(allFormula)
	print(allFormula)
	return(allFormula)
def getSubstract(startNum,endNum):
	allFormula = []
	for i in range(startNum,endNum+1):
		for j in range(1,i):
			allFormula.append((j,i))
	print(len(allFormula))
	#random.shuffle(allFormula)
	print(allFormula)
	return(allFormula)
	
def genTable_sub():
	data=[]
	allFormulas = getSubstract(1,99)
	allFormulas = allFormulas*2
	random.shuffle(allFormulas)
	for item in allFormulas:
		formula = []
		formula.append("%s "%item[1])
		formula.append("-")
		formula.append("%s"%item[0])
		formula.append("=   ")
		data.append(formula)
		
def getAdd_twodigits():
	data=[]
	for a in range(1,90):
		for b in range(1,90):
			if a+b > 100:
				continue
			if a%10 + b%10 <= 10:
				continue
			data.append((a,b))
	data1 = []
	for item in data:
		if item[1]<item[0]:
			data1.append((item[1],item[0]))
		else:
			data1.append(item)
	data1 = list(set(data1))
	random.shuffle(data1)
	print(data1)
	return(data1)
	
def genTable():
	formulas1 = getAdd(11,18)
	formulas2 = getAdd(11,20)
	formulas3 = getAdd(21,25)
	formulas4 = getAdd(30,50)
	print(len(formulas1))
	print(len(formulas2))
	print(len(formulas3))
	print(len(formulas4))
	allFormulas=[]
	for item in formulas4:
		if (item[0]>=30 and item[1]>=10) or (item[1]>=30 and item[0]>=10) or (item[1]<30 and item[0]<30):
			continue
		allFormulas.append(item)
	allFormulas = getAdd_twodigits()
	#allFormulas.extend(formulas2*4)
	#allFormulas.extend(formulas3*3)
	#allFormulas.extend(formulas4)
	random.shuffle(allFormulas)
	print(allFormulas)
	print(len(allFormulas))
	
	data=[]
	'''for item in allFormulas:
		formula = []
		formula.append("%s "%item[0])
		formula.append("+")
		formula.append("%s"%item[1])
		formula.append("=   ")
		data.append(formula)'''

	for item in allFormulas:
		formula = []
		formula.append("%s "%(item[0]+item[1]))
		formula.append("-")
		formula.append("%s"%item[1])
		formula.append("=   ")
		data.append(formula)

	table = platypus.Table(data, 1*inch, 1.2*inch, [('FONT', (0,0), (-1,-1), 'Courier',70)])
	return table
def toPdf():
	doc = platypus.SimpleDocTemplate('test.pdf', topMargin=0.9*inch, bottomMargin=0.9*inch, title='DaDa Math', author='qyb') 
	elements = []
	for i in range(1):
		elements.append(genTable())
		elements.append(platypus.flowables.PageBreak())
 
	doc.build(elements)

if __name__ == '__main__':
	#getAdd(6,8)
	toPdf()