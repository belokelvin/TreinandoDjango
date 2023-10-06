from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'pages/home.html')




'''
def criar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nome = request.POST['nome']
        email = request.POST['email']

        # Converter a imagem em base64 e armazená-la
        foto = request.FILES['foto']
        foto_base64 = None
        if foto:
            with foto.open('rb') as img_file:
                foto_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        #Cria uma senha segura
        password = make_password(password)

        # Crie uma instância do MongoConnection e do Usuario
        mongo_uri = 'mongodb+srv://kelvincrdzbl:535846*Mud@orion.6qr8efr.mongodb.net/?retryWrites=true&w=majority'
        mongo_connection = Usuario.create_mongo_connection(mongo_uri)
        usuario = Usuario(mongo_connection)

        # Chame o método create_user do seu modelo com a imagem em base64
        resultado = usuario.create_user(username, password, nome, email, foto_base64)

        if resultado == "Usuário criado com sucesso!":
            return redirect('home')  # Redirecione para a página de sucesso
        else:
            return render(request, 'create_user.html', {'erro': resultado})

    return render(request, 'create_user.html')
'''
