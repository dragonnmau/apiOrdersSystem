import imp
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import user
import json
# Create your views here.
# clase para las vistas que retornan datos

class userView (View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get (self, request, id=0):
        
        if (id>0):

            userData=list(user.objects.filter(id=id).values())
            if len(userData)>0:
                datos = {'menssage':"success", 'code':'200', 'datos':userData}
            else:
                datos = {'menssage':"user not found", 'code':'404'}
            
        else:
            users = list(user.objects.values())
            if len(users)>0:
                datos = {'menssage':"success", 'code':'200', 'datos':users}
            else:
                datos = {'menssage':"data not found", 'code':'404'}
        return JsonResponse(datos)



    def post (self, request):
        jsonTrans = json.loads(request.body) 
        #print(jsonTrans)
        user.objects.create(
            username=jsonTrans["username"],
            password=jsonTrans["password"],
            email=jsonTrans["email"],
            telephone=jsonTrans["telephone"]
            )
        datos = {'menssage':"success", 'code':'200'}
        return JsonResponse(datos)

    def put (self, request, id):
        pjsonTrans = json.loads(request.body) 
        userData=list(user.objects.filter(id=id).values())
        if len(userData)>0:
            dataSearch = user.objects.get(id=id)
            dataSearch.username=pjsonTrans['username']
            dataSearch.password=pjsonTrans['password']
            dataSearch.email=pjsonTrans['email']
            dataSearch.telephone=pjsonTrans['telephone']
            dataSearch.save()
            datos = {'menssage':"success, user updated", 'code':'200'}
            
        else: 
            datos = {'menssage':"user not found", 'code':'404'}
        return JsonResponse(datos)

    def delete (self, request, id):
        userData=list(user.objects.filter(id=id).values())
        if len(userData)>0:
            user.objects.filter(id=id).delete()
            datos = {'menssage':"success, user deleted", 'code':'200'}
        else:
            datos = {'menssage':"user not found", 'code':'404'}
        return JsonResponse(datos)


class clientView (View):
    def get (self, request):
        pass
    def post (self, request):
        pass
    def put (self, request):
        pass
    def delete (self, request):
        pass

class orderView (View):
    def get (self, request):
        pass
    def post (self, request):
        pass
    def put (self, request):
        pass
    def delete (self, request):
        pass

class methods:
    functio