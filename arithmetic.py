import random
from reportlab.pdfgen import canvas
from reportlab import platypus
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))
Style=getSampleStyleSheet()

def getAdd(startNum,endNum):
	allFormula = []
	for i in range(startNum,endNum+1):
		for j in range(1,i):
			allFormula.append((j,i-j))
	print(len(allFormula))
	#random.shuffle(allFormula)
	print(allFormula)
	return(allFormula)
	
def genTable():
	formulas1 = getAdd(1,10)
	formulas2 = getAdd(11,20)
	formulas3 = getAdd(21,25)
	formulas4 = getAdd(26,30)
	print(len(formulas1))
	print(len(formulas2))
	print(len(formulas3))
	print(len(formulas4))
	allFormulas = formulas1*6
	allFormulas.extend(formulas2*4)
	allFormulas.extend(formulas3*3)
	allFormulas.extend(formulas4)
	random.shuffle(allFormulas)
	print(allFormulas)
	print(len(allFormulas))
	data=[]
	for item in allFormulas:
		formula = []
		formula.append("%s "%item[0])
		formula.append("+")
		formula.append("%s"%item[1])
		formula.append("=   ")
		data.append(formula)
	#data= [['3 ', '+', '4','=   '],
	#	   ['3 ', '+', '4','=   '],
	#	   ['3 ', '+', '4','=   '],
	#	   ['3 ', '+', '4','=   '],
	#	   ['3 ', '+', '4','=   '],
	#	   ['3 ', '+', '4','=   ']]
	print(data[:5])
	print(len(data))
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