from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader 
from .models import Question


# Homepage: Start the quiz
def home(request):
    questions = Question.objects.all()
    template = loader.get_template('home.html')
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))

# Submit answers and calculate the score
def submit_quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score = 0
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_option:
                score += 1
        template = loader.get_template('result.html')
        context = {
            'score': score,
            'total': len(questions),
        }
        return HttpResponse(template.render(context, request))
    return redirect('home')

# Add a new question
def add_question(request):
    if request.method == 'POST':
        text = request.POST['text']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        correct_option = request.POST['correct_option']
        Question.objects.create(
            text=text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=correct_option
        )
        return redirect('home')
    template = loader.get_template('add_question.html')
    return HttpResponse(template.render({}, request))

# View all questions
def all_questions(request):
    questions = Question.objects.all()
    template = loader.get_template('all_questions.html')
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))
