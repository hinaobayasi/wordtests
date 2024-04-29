from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WordlistE
import random

def index(request):
    return render(request, "word/index.html")

def lists(request):
    wordliste = WordlistE.objects.all()
    context = {
        "wordliste": wordliste,
    }
    return render(request, "word/lists.html", context)

def choice(request):
    choice_list =[]
    cata_list =[]
    sentaku_list =[]
    count = WordlistE.objects.count()
    qnum = random.randint(1,count+1)
    question = get_object_or_404(WordlistE, pk=qnum)
    choice_list.append(question)
    for i in range(count):
        word = WordlistE.objects.get(pk=i+1)
        if question.vocab == word.vocab:
            continue
        elif question.cata == word.cata:
            cata_list.append(word)
    qnum = cata_list
    for i in range(3):
        sen = random.choice(cata_list)
        cata_list.remove(sen)
        choice_list.append(sen)
    for i in range(4):
        sentaku = random.choice(choice_list)
        sentaku_list.append(sentaku)
        choice_list.remove(sentaku)
    context = {
        "question":question,
        "sentaku_list":sentaku_list
    }
    return render(request, "word/choice.html", context)

def choiceans(request, question_id):
    question = get_object_or_404(WordlistE, pk=question_id)
    count = WordlistE.objects.count()
    try:
        if request.method == 'POST':
            ans = request.POST.get('cho', '')
            for i in range(count):
                word = WordlistE.objects.get(pk=i+1)
                if ans == question.mean:
                    choice_id = question_id
                    break
                elif ans == word.mean:
                    choice_id = i + 1
                    text = WordlistE.objects.get(pk=choice_id)
                    break
                elif i == 4:
                    choice_id = 0
            if choice_id == 0:
                typ = "3"
                context ={
                    "question": question,
                    "typ":typ,
                }
            elif question_id == choice_id: 
                typ = "1"
                context ={
                    "question": question,
                    "typ":typ,
                }
            elif choice_id != 0:
                typ = "2"
                context ={
                    "question": question,
                    "text": text,
                    "typ":typ,
                }
            return render(request, "word/choiceans.html", context)
        else:
            return HttpResponse("エラーが発生しました")
    except (WordlistE.DoesNotExist):
        return render(request, "word/choiceans.html")

def write(request):
    wordliste = WordlistE.objects.all()
    question = random.choice(wordliste)
    context = {
        "question": question,
        "wordliste": wordliste,
    }
    return render(request, "word/write.html", context)

def writeans(request, question_id):
    count = WordlistE.objects.count()
    question = get_object_or_404(WordlistE, pk=question_id)
    try:
        if request.method == 'POST':
            ans = request.POST.get('text', '')
            text_id = 0
            for i in range(count):
                word = WordlistE.objects.get(pk=i+1)
                if word.vocab == ans:
                    text_id = i + 1
                    text = WordlistE.objects.get(pk=text_id)
                    break
            if text_id == 0:
                typ = "3"
                context ={
                    "question": question,
                    "typ":typ,
                }
            if question_id == text_id: 
                typ = "1"
                context ={
                    "question": question,
                    "typ":typ,
                }
            elif text_id != 0:
                typ = "2"
                context ={
                    "question": question,
                    "text": text,
                    "typ":typ,
                }
            return render(request, "word/writeans.html", context)
        else:
            return HttpResponse("エラーが発生しました")
    except (WordlistE.DoesNotExist):
        return render(request, "word/writeans.html")


def detail(request, wordlist_id):
    wordliste = get_object_or_404(WordlistE, pk=wordlist_id)
    context = {
        "wordliste": wordliste,
    }
    return render(request, "word/detail.html", context)