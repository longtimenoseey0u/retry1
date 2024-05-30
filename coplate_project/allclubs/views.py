from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def allclubs(request):
    return render(request, 'allclubs.html')

def clubs(request, todo_id=None):
    if todo_id is not None:  # todo_id가 전달된 경우
        todo_item = get_object_or_404(TodoItem, id=todo_id)
        return render(request, 'clubs.html', {'todo_item': todo_item})
    elif request.method == 'POST':  # POST 요청일 때
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        TodoItem.objects.create(title=title, description=description)
        return redirect('clubs_detail', todo_id=TodoItem.objects.latest('id').id)  # 생성된 항목의 ID로 리다이렉트
    else:  # GET 요청일 때
        return render(request, 'clubs.html')