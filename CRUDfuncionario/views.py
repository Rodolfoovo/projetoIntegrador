from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from CRUDfuncionario.models import Funcionario
from django.http import HttpResponse

def home(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "index.html", {"funcionarios": funcionarios})

def salvarFuncionario(request):
    if request.method == 'GET':
        return render(request, "index.html")
    elif request.method == 'POST':
        vusername = request.POST.get("username")
        vEnderecoFuncionario = request.POST.get("enderecoFuncionario")
        vCPF = request.POST.get("CPF")
        vCEP = request.POST.get("CEP")
        vTelefone = request.POST.get("telefone")
        vpassword = request.POST.get("password")
        vFuncao = request.POST.get("funcao")

        # Verifica se já existe um usuário com o mesmo username
        try:
            usuarioAux = Funcionario.objects.get(username=vusername)
            return redirect(home)
        except Funcionario.DoesNotExist:
            # Cria um novo usuário
            novo_funcionario = Funcionario.objects.create_user(
                nivelDeAcesso=1,
                username=vusername,
                enderecoFuncionario=vEnderecoFuncionario,
                cpf=vCPF,
                CEP=vCEP,
                telefone=vTelefone,
                password=vpassword,
                funcao=vFuncao
            )

            # Autentica o novo usuário
            # user = authenticate(request, username=vusername, password=vpassword)
            
            if user:
                funcionarios = Funcionario.objects.all()
                return redirect(home)
            else:
                return HttpResponse(user)

def editar(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    return render(request, "update.html", {"funcionario": funcionario})

def update(request, id):
    if request.method == 'POST':
        funcionario = Funcionario.objects.get(idFuncionario=id)

        # Atualiza os campos do funcionário com base nos dados do formulário
        funcionario.username = request.POST.get("username")
        funcionario.enderecoFuncionario = request.POST.get("enderecoFuncionario")
        funcionario.CPF = request.POST.get("CPF")
        funcionario.CEP = request.POST.get("CEP")
        funcionario.telefone = request.POST.get("telefone")
        funcionario.password = request.POST.get("password")
        funcionario.funcao = request.POST.get("funcao")

        funcionario.save()
        return redirect(home)
    else:
        # Se o método não for POST, redirecione para a página de origem ou trate conforme necessário
        return HttpResponse('Método não permitido')
    
def delete(request, id):
    funcionario = Funcionario.objects.get(idFuncionario=id) 
    funcionario.delete()
    return redirect(home)