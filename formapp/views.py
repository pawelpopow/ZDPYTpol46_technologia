from django.shortcuts import render


def name_get(request):
    name = request.GET.get('name')


    if name:
        return render(
            request,
            'formapp/hello.html',
            context={
                "name":name,
            }
        )

    return render(
        request,
        'formapp/name.html',
    )
