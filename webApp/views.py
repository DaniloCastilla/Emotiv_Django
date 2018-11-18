from django.shortcuts import render

from bokeh.plotting import figure, output_file, show 
from bokeh.resources import CDN
from bokeh.embed import components

# Create your views here.
def index(request):
	x= [i for i in range(10)] #[0,1,2,3,4,5,6,7,8,9]
	x2= [i**2 for i in range(10)]
	x3= [i**3 for i in range(10)]
	title_ = "y = f(x) = x^2"

	plot = figure(title= title_,  x_axis_label= 'Indep.', y_axis_label= 'Dep.', plot_width =600,  plot_height =400)

	plot.line(x, x2, legend= 'x^2', line_width = 2)
	plot.line(x, x3, legend= 'x^3', line_width = 2)
    	#Store components 
	script, div = components(plot,CDN)

	return render(request, 'webApp/index.html', {'script_plot' : script , 'div_plot' : div} )


def registerTherapist(request):
	return render(request, 'webApp/registroterapeuta.html')

def searchPatient(request):
	return render(request, 'webApp/consultarpaciente.html')
