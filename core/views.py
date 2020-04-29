from django.shortcuts import render
from django.forms import formset_factory
from .forms import wordForm
import itertools

# Create your views here.
def home(request):
	final = []
	form = formset_factory(wordForm, extra=3)
	formset = form()

	#Get POST Request
	if request.method == "POST":

		#Parsing Values From The Request
		first = request.POST['form-0-word']
		second = request.POST['form-1-word']
		third = request.POST['form-2-word']
		wrapper = request.POST['wrapper']
		separator_from_request = request.POST['separator']

		#Cleaning The Data
		first, second, third = clean_data(first, second, third)
		data  = [list(x) for x in get_data(first, second, third)]

		#Getting The Final Data List
		separator = get_separator(separator_from_request)
		for elem in data:
			final.append(separator.join(elem))
		context = {
				'formset':formset,
				'data':final,
				'flag':'True',
				'wrapper':wrapper,
			}
		return render(request,'home.html', context=context)

	else:
		form = formset_factory(wordForm, extra=3)
		formset = form()
		context = {
			'formset':formset,
			'flag':'False',
		}
		return render(request,'home.html',context=context)

def get_separator(separator):
	if separator == "minus":
		return '-'
	elif separator == 'plus':
		return '+'
	elif separator == 'space' or separator == "nothing":
		return ' '

def get_data(first, second, third):
	if first == '' and second != '' and third != '':
		return list(itertools.product(second, third))
	if second == '' and first != '' and third != '':
		return list(itertools.product(first, third))
	if third == '' and first != '' and second != '':
		return list(itertools.product(first, second))
	if first== '' and second == '' and third != '':
		return third
	if first== '' and third == '' and second != '':
		return second
	if third== '' and second == '' and first != '':
		return first
	if third == '' and second == '' and first == '':
		return None
	else:
		return list(itertools.product(first,second,third))

def clean_data(a,b,c):
	data = []
	x,y,z = [],[],[]
	if '\r\n' in a:
		x = a.split('\r\n')
	else:
		x.append(a)
	if '\r\n' in b:
		y = b.split('\r\n')
	else:
		y.append(b)
	if '\r\n' in c:
		z = c.split('\r\n')
	else:
		z.append(c)
	return x,y,z