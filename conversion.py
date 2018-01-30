import csv
import json

csvfile = open('courses.csv', 'r')
jsonfile = open('000001.json', 'w')

fieldnames = ("_typeName","code","title","subject","university","description","id")
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',')
    jsonfile.write('\n')


# import csvmapper

# jsonfile = open('3.json', 'w')

# fields = ("_typeName","code","title","subject","university","description")
# parser = CSVParser('courses.csv', csvmapper.FieldMapper(fields))

# converter = csvmapper.JSONConverter(parser)

# jsondata = converter.doConvert(pretty=True)

# json.dump(jsondata, jsonfile)
