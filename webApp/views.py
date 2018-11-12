from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'webApp/index.html')

def registerTherapist(request):
	return render(request, 'webApp/registroterapeuta.html')

def searchPatient(request):
	return render(request, 'webApp/consultarpaciente.html')
