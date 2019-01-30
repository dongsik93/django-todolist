from django.shortcuts import render, redirect
from .models import Todo, Comment

def index(request):
    todos = Todo.objects.order_by("due_date").all()
    return render(request, "todo/index.html", {"todos":todos})
    
def new(request):
    return render(request, "todo/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    # todo = Todo(title=title, content=content, due_date=due_date)
    # todo.save()
    
    ## 줄인 형태
    Todo.objects.create(title=title, content=content, due_date=due_date)
    
    return redirect("/todos")
    
def read(request, id):
    todo = Todo.objects.get(pk=id)
    
    return render(request, "todo/read.html",{"todo":todo})

def delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    
    return redirect("/todos")
    
def edit(request, id):
    todo = Todo.objects.get(pk=id)
    return render(request, "todo/edit.html", {"todo":todo})

def update(request, id):
    todo = Todo.objects.get(pk=id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    # 수정된 내용을 원본에 저장
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()
    
    return redirect(f"/todos/{id}/")
    
def comment(request, id):
    todo = Todo.objects.get(pk=id)
    content = request.POST.get("content")
    
    Comment.objects.create(todo=todo, content=content)
    
    return redirect(f"/todos/{id}/")
    
def delete(request, t_id, c_id):
    comment = Comment.objects.get(pk=c_id)
    comment.delete()
    
    return redirect(f"/todos/{t_id}/")