import csv

class CsvHelper :
    def __init__(self, functionName) :
        self.functionName = functionName

    def PrintCsvFile(self, fileName, delimiter = ',') :
        with open(fileName, "r") as inputFile :
            csvReader = csv.reader(inputFile, delimiter = delimiter)

            for line in csvReader :
                print(line)

    def CopyCsvFileAfterChangingDelimiter(self, inputFileName, outputFileName, inputDelimiter = ',', outputDelimiter = '-') :
        with open(inputFileName, "r") as inputFile :
            csvReader = csv.reader(inputFile)

            with open(outputFileName, 'w') as outputFile :
                csvWriter = csv.writer(outputFile, delimiter = outputDelimiter)

                for line in csvReader :
                    csvWriter.writerow(line)

def main() :
    csvHelper =  CsvHelper("CsvHelper")
    csvHelper.PrintCsvFile("D:\Programs\git\MachileLearning\Datasets\CSV\IRIS.csv")
    csvHelper.CopyCsvFileAfterChangingDelimiter("D:\Programs\git\MachileLearning\Datasets\CSV\IRIS.csv", "D:\Programs\git\MachileLearning\Datasets\CSV\IRIS_new.csv")
    csvHelper.PrintCsvFile("D:\Programs\git\MachileLearning\Datasets\CSV\IRIS_new.csv", '\t')

main()
