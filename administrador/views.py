from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from candidato.models import Candidato
from empresa.models import Empresa,Vaga

@login_required(login_url='login')
def dashboard(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('login')

    qtd_candidatos = Candidato.objects.count()
    qtd_empresas = Empresa.objects.count()
    qtd_vagas = Vaga.objects.count()
    qtd_vagas_ativas = Vaga.objects.filter(ativa=True).count()

    context = {
        'qtd_candidatos': qtd_candidatos,
        'qtd_empresas': qtd_empresas,
        'qtd_vagas': qtd_vagas,
        'qtd_vagas_ativas': qtd_vagas_ativas,
    }

    return render(request, 'administrador/dashboard.html', context)
@login_required
def gerenciamento_view(request):
    nome_query = request.GET.get('nome', '').strip()
    email_query = request.GET.get('email', '')
    status_query = request.GET.get('status', '')

    usuarios = Usuario.objects.exclude(tipo_usuario='admin')


    if nome_query:
     usuarios = usuarios.filter(
        id__in=[
            u.id for u in usuarios
            if (
                (u.tipo_usuario == 'candidato' and
                 Candidato.objects.filter(usuario=u, nome__icontains=nome_query).exists())
                or
                (u.tipo_usuario == 'empresa' and
                 Empresa.objects.filter(usuario=u, razao_social__icontains=nome_query).exists())
            )
        ]
    )


    if email_query:
        usuarios = usuarios.filter(email__icontains=email_query)

    if status_query:
        if status_query.lower() == 'ativo':
            usuarios = usuarios.filter(is_active=True)
        elif status_query.lower() == 'inativo':
            usuarios = usuarios.filter(is_active=False)

    dados = []

    for user in usuarios:
        nome = user.get_full_name() or user.username
        foto = None

        if user.tipo_usuario == 'candidato':
            candidato = Candidato.objects.filter(usuario=user).first()
            if candidato:
                nome = candidato.nome

        elif user.tipo_usuario == 'empresa':
            empresa = Empresa.objects.filter(usuario=user).first()
            if empresa:
                nome = empresa.razao_social
                foto = empresa.foto_perfil

        dados.append({
            'id': user.id,
            'nome': nome,
            'email': user.email,
            'tipo': user.tipo_usuario,
            'foto': foto,
            'ativo': user.is_active,
        })

    return render(request, 'administrador/gerenciamento.html', {
        'usuarios': dados,
        'request': request, 
    })

def tela_moderar_vagas_view(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('login')
    
    vagas = Vaga.objects.select_related('empresa').all()

    return render(request,'administrador/tela_moderar_vagas.html',{
        'vagas':vagas
    })

@login_required
def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.user.tipo_usuario != 'admin':
        return redirect('login')

    usuario.delete()
    return redirect('administrador:gerenciamento')

@login_required
def excluir_vaga(request, id):
    vaga = get_object_or_404(Vaga, id=id)

    if request.user.tipo_usuario != 'admin':
        return redirect('login')

    vaga.delete()
    return redirect('administrador:gerenciamento')
    
@login_required
def detalhes_usuario(request, id):
    if request.user.tipo_usuario != 'admin':
        return redirect('login')

    usuario = get_object_or_404(Usuario, id=id)

    candidato = Candidato.objects.filter(usuario=usuario).first()
    empresa = Empresa.objects.filter(usuario=usuario).first()

    context = {
        'usuario': usuario,
        'candidato': candidato,
        'empresa': empresa,
    }

    return render(request, 'administrador/detalhes_usuario.html', context)
