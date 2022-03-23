from django.shortcuts import render


def add(request):
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
    if value1 and value2:
        result = int(value1) + int(value2)
        return render(
            request,
            'calculator/add.html',
            context={
                'value1': value1,
                'value2': value2,
                'result': result,
            }
        )
    else:
        return render(
            request,
            'calculator/calculator_form.html'
        )


def add_post(request):
    value_1 = request.POST.get("value_1")
    value_2 = request.POST.get("value_2")

    if value_1 and value_2:
        res = int(value_1) + int(value_2)
        return redirect('calculator:result', res=res)

    return render(
        request,
        'calculator/add.html',
    )


def result(request, res):
    return render(
        request,
        'calculator/result.html',
        context={
            'res': res
        }
    )