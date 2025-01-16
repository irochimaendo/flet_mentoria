import flet as ft
import os

def main(page: ft.Page):
    page.title = "Exibindo Imagem no Flet"
    page.window_width = 393
    page.window_height = 852
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#ffffff"


    
    image_path = os.path.abspath(r"c:\Users\tiago\Downloads\logo.png")

    container_imagem = ft.Container(
        content= ft.Image(
            src = image_path,
            width= 230,
            height= 220,
            fit=ft.ImageFit.CONTAIN
        ),
        width = 230,
        height= 220,
        alignment=ft.alignment.top_center
    )

    login = ft.Container(
        content = ft.Text("Login", size= 30, color= "BLACK", weight=ft.FontWeight.BOLD),
        alignment=ft.alignment.top_center,
        bgcolor="#ffffff",
        height=44
    )

    email = ft.Container(
        content = ft.TextField(
            label = "Email ou número de celular",
            label_style=ft.TextStyle(color=ft.colors.GREY),
            color = ft.colors.BLACK,
            border_color= "BLUE",
            border = "underline",
            bgcolor = "WHITE",
            prefix_icon=ft.Icons.PERSON,
            width = 393
        ),
        alignment=ft.alignment.top_center
    )

    senha = ft.Container(
        content = ft.TextField(
            label="Senha", password=True, can_reveal_password=True,
            label_style=ft.TextStyle(color=ft.colors.GREY),
            color = ft.colors.BLACK,
            border_color= "BLUE",
            border = "underline",
            bgcolor= "WHITE",
            prefix_icon=ft.Icons.KEY_SHARP,
            width = 393
        ),
        alignment=ft.alignment.top_center
    )

    botao_senha = ft.Container(
        ft.TextButton(
            "Esqueci minha senha",
            style=ft.ButtonStyle(
                color="#2F4EFF",
                text_style=ft.TextStyle(
                weight=ft.FontWeight.W_800
                ),
            ),
        ),
        alignment=ft.alignment.top_center
    )

    container2 = ft.Container(
        alignment=ft.alignment.top_center,
        bgcolor="#ffffff",
        width=393,
        height=25
    )


    botao_login = ft.Container(
        content = ft.FilledButton(
            text="Login",
            bgcolor = "#2F4EFF",
            color = ft.colors.WHITE,
            width = 327
        ),
        alignment=ft.alignment.top_center
    )

    container3 = ft.Container(
        alignment=ft.alignment.top_center,
        bgcolor="#ffffff",
        width=393,
        height=25,
    )

    continuar = ft.Container(
        content= ft.Text(
            "ou continue com",
            size= 20, 
            color= "#747474"
        ),
        alignment=ft.alignment.top_center      
    )

    container4 = ft.Container(
        alignment=ft.alignment.top_center,
        bgcolor="#ffffff",
        width=393,
        height=32,
    )

    botao_login2 = ft.Container(
        content = ft.Row(
            controls = [
                ft.Container(
                    content = ft.ElevatedButton(
                        content = ft.Image(src=r"c:\Users\tiago\Downloads\logo google.png", width=40, height=40),
                        width = 70,
                        height = 70,
                        bgcolor= "#C9C9C9"
                    ),
                ),
                ft.Container(
                    content = ft.ElevatedButton(
                        content = ft.Image(src=r"c:\Users\tiago\Downloads\logo apple.png", width=40, height=40),
                        width = 70,
                        height = 70,
                        bgcolor= "#C9C9C9"
                    ),
                ),
                ft.Container(
                    content = ft.ElevatedButton(
                        content = ft.Image(src=r"c:\Users\tiago\Downloads\facebook icon.png", width=40, height=40),
                        width = 70,
                        height = 70,
                        bgcolor= "#C9C9C9"
                    ),
                ),
            ],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        width = 304
    )

    container5 = ft.Container(
        alignment=ft.alignment.top_center,
        bgcolor="#ffffff",
        width=393,
        height=10,
    )

    botao_criar_conta = ft.Container(
        ft.TextButton(
            "criar uma conta",
            style=ft.ButtonStyle(
                color="#2F4EFF",
                text_style=ft.TextStyle(
                weight=ft.FontWeight.W_800
                ),
            ),
        ),
        alignment=ft.alignment.top_center
    )

    page.add(container_imagem, login, email, senha, botao_senha, container2, botao_login, container3, continuar, container4, botao_login2, container5, botao_criar_conta)

ft.app(target=main)