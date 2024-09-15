from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from .forms import ReportForm
from .utils import generate_response, generate_priority, generate_supplies, generate_user_actions
from django.http import HttpRequest
from django.urls import reverse

def report_list(request):
    report = Report.objects.filter(resolved=False).order_by('priority').first()
    next_report = Report.objects.filter(resolved=False).filter(priority__gt=report.priority).order_by('priority').first()
    return render(request, 'report/report_list3.html', {'report': report, 'next_report': next_report})

def submit_report(request):
    response = None
    user_input = ""
    
    # Initialize conversation history
    conversation_history = []

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save() 

            user_input = form.cleaned_data['description']
            conversation_history.append({"role": "user", "content": user_input})
            
            response_text = generate_response(conversation_history)
            priority = generate_priority(conversation_history)
            supplies = generate_supplies(conversation_history)
            user_action = generate_user_actions(conversation_history)
            
            #Save AI responses to the report
            report.priority = priority
            report.actionResponse = response_text
            report.suppliesResponse = supplies
            report.save()
            
            conversation_history.append({"role": "assistant", "content": response_text})

            # Save response to session
            request.session['ai_response'] = user_action
            return redirect(reverse('report_summary', kwargs={'report_id': report.id}))
    else:
        form = ReportForm()

    return render(request, 'report/submit_report2.html', {'form': form})

def report_summary(request, report_id):
    # Retrieve the report using the report_id
    report = get_object_or_404(Report, id=report_id)
    
    # Retrieve the AI response from the session
    response_text = request.session.get('ai_response', '')

    if 'ai_response' in request.session:
        del request.session['ai_response']
    
    return render(request, 'report/report_summary.html', {
        'report': report,
        'response': response_text,
    })

def mark_resolved(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    report.resolved = True
    report.save()
    return redirect('report_list')