import survey

def main():
	table = survey.Pregnancies()
	table.ReadRecords()
	unfilteredLiveBirthWeights = [(p.birthwgt_lb, p.birthwgt_oz) for p in table.records if p.outcome == 1]
	liveBirthWeights = [lbs * 16 + oz for lbs, oz in unfilteredLiveBirthWeights if type(lbs) == int and type(oz) == int and lbs * 16 + oz <= 200]
	print(liveBirthWeights[0])


def Skewness(data):
	m2 = (1/len(data)) * 


if  __name__ == '__main__':
	main()
