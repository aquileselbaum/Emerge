from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm
from .utils import generate_response

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report/report_list.html', {'reports': reports})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save() 
            return redirect('report_form')  
    else:
        form = ReportForm()
    return render(request, 'report/report_form.html', {'form': form})

def chat_view(request):
    response = None
    user_input = ""
    
    # Initialize conversation history
    conversation_history = []
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Append the user message to conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Get response from OpenAI
        response_text = generate_response(conversation_history)
        
        # Append the assistant response to conversation history
        conversation_history.append({"role": "assistant", "content": response_text})
        
        # Render the response and user input in the template
        response = response_text
    
    return render(request, 'report/chat.html', {'response': response, 'user_input': user_input})