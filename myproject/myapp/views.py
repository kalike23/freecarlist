from django.shortcuts import render, redirect, get_object_or_404
from .models import FreeTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# 列表页
def free_table_list(request):
    free_tables = FreeTable.objects.all()  # 获取所有记录
    return render(request, 'myapp/free_table_list.html', {'free_tables': free_tables})


# 添加
def add_free_table(request):
    if request.method == 'POST':
        car_no = request.POST.get('car_no')  # 获取车牌号
        reason = request.POST.get('reason')
        other = request.POST.get('other')

        if not car_no:  # 如果车牌号为空，提示错误
            return render(request, 'myapp/add_free_table.html', {'error': '车牌号不能为空'})

        FreeTable.objects.create(car_no=car_no, reason=reason, other=other)
        return redirect('/')
    return render(request, 'myapp/add_free_table.html')


# 修改
def edit_free_table(request, pk):
    free_table = get_object_or_404(FreeTable, pk=pk)
    if request.method == 'POST':
        free_table.car_no = request.POST.get('car_no')
        free_table.reason = request.POST.get('reason')
        free_table.other = request.POST.get('other')
        free_table.save()
        return redirect('free_table_list')
    return render(request, 'myapp/edit_free_table.html', {'free_table': free_table})

# 删除
def delete_free_table(request, pk):
    free_table = get_object_or_404(FreeTable, pk=pk)
    free_table.delete()
    return redirect('free_table_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('free_table_list')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})
