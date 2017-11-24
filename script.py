import django, csv
from django.utils import html
from skoolpal.org.models.subject import MGradeSubject

obj = MGradeSubject.objects.all()

def export_csv(out_file, name, headers, lines, context=None):
	writer = csv.writer(out_file)

	# Write headers to CSV file
	writer.writerow(headers)

	# Write data to CSV file
	for line in lines:
		writer.writerow(list(map(html.strip_tags, line)))

head = ['class', 'subject']
name = 'file_test.csv'
out_file = open('myfile.csv', 'w')
lines = obj
lines = [str(x) for x in lines]
lines = [list(map(str, i.split(': '))) for i in lines]

export_csv(out_file, name, headers, lines)
