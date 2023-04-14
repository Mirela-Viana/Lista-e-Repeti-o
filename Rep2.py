print("Inserir usuário:")
Usuario = (input())
print("Inserir senha:")
senha = (input())
while Usuario == senha:
    print("Senha inválida, insira a senha:")
    senha = (input())
print("senha válida:",senha)