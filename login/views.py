from django.shortcuts import render, redirect
from login.models import Login


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username)
        print(password)

        obj = Login.objects.filter(username=username, password=password).first()

        if obj is not None:

            request.session["u_id"] = obj.u_id

            if obj.type == "admin":
                return redirect('/admin-page/')

            elif obj.type == "teacher":
                return redirect('/teacher/')

            elif obj.type == "parent":
                return redirect('/parent/')

        else:

            context = {
                'msg': "username or password incorrect.... please try again....!"
            }

            return render(request,'login/login.html',context)

    return render(request,'login/login.html')