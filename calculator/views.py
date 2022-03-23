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
