from django.shortcuts import render, redirect, get_object_or_404
from .models import FreeTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden

# 列表页（所有人可查看）
def free_table_list(request):
    query = request.GET.get('q')  # 支持车牌号查询
    if query:
        free_tables = FreeTable.objects.filter(car_no__icontains=query)
    else:
        free_tables = FreeTable.objects.all()
    return render(request, 'myapp/free_table_list.html', {'free_tables': free_tables})

# 添加（仅管理员可操作）
@login_required
@permission_required('myapp.add_freetable', raise_exception=True)
def add_free_table(request):
    if not request.user.is_staff:  # 限制仅管理员访问
        return HttpResponseForbidden("您没有权限进行此操作。")
    if request.method == 'POST':
        car_no = request.POST.get('car_no')
        reason = request.POST.get('reason')
        other = request.POST.get('other')
        if not car_no:
            return render(request, 'myapp/add_free_table.html', {'error': '车牌号不能为空'})
        FreeTable.objects.create(car_no=car_no, reason=reason, other=other)
        return redirect('free_table_list')
    return render(request, 'myapp/add_free_table.html')

# 修改（仅管理员可操作）
@login_required
@permission_required('myapp.change_freetable', raise_exception=True)
def edit_free_table(request, pk):
    free_table = get_object_or_404(FreeTable, pk=pk)
    if not request.user.is_staff:
        return HttpResponseForbidden("您没有权限进行此操作。")
    if request.method == 'POST':
        free_table.car_no = request.POST.get('car_no')
        if not free_table.car_no:
            return render(request, 'myapp/edit_free_table.html', {'free_table': free_table, 'error': '车牌号不能为空'})
        free_table.reason = request.POST.get('reason')
        free_table.other = request.POST.get('other')
        free_table.save()
        return redirect('free_table_list')
    return render(request, 'myapp/edit_free_table.html', {'free_table': free_table})

# 删除（仅管理员可操作）
@login_required
@permission_required('myapp.delete_freetable', raise_exception=True)
def delete_free_table(request, pk):
    free_table = get_object_or_404(FreeTable, pk=pk)
    if not request.user.is_staff:
        return HttpResponseForbidden("您没有权限进行此操作。")
    free_table.delete()
    return redirect('free_table_list')


