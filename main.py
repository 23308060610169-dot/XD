import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.padding = 40
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#0d0d0d" 

    titulo = ft.Text(
        value="REGISTRO DE EVENTOS",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="#e6e6e6"
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej: Conferencia de Tecnología 2026",
        bgcolor="#1a1a1a",
        color="white",
        border_color="#444444"
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia",
        bgcolor="#1a1a1a",
        color="white"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Presencial", label="Presencial"),
                ft.Radio(value="Virtual", label="Virtual")
            ],
            spacing=30
        ),
        value="Presencial"
    )

    requiere_inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    resumen_texto = ft.Text(
        value="",
        size=16,
        color="#cfcfcf"
    )

    mensaje_error = ft.Text(
        value="",
        color="#8b0000",
        size=14,
        weight=ft.FontWeight.BOLD
    )

    def mostrar_resumen(e):
        if nombre_evento.value.strip() == "":
            mensaje_error.value = "El nombre del evento no puede estar vacío."
            resumen_texto.value = ""
        else:
            mensaje_error.value = ""
            resumen_texto.value = f"""
Nombre: {nombre_evento.value}
Tipo: {tipo_evento.value}
Modalidad: {modalidad.value}
Requiere inscripción: {"Sí" if requiere_inscripcion.value else "No"}
Duración: {int(duracion.value)} horas
"""
        page.update()

    boton = ft.ElevatedButton(
        content=ft.Text("MOSTRAR RESUMEN"),
        on_click=mostrar_resumen,
        bgcolor="#3b0000",
        color="white"
    )

    formulario = ft.Column(
        [
            nombre_evento,
            tipo_evento,
            ft.Text("Modalidad:", weight=ft.FontWeight.BOLD, color="#bbbbbb"),
            modalidad,
            requiere_inscripcion,
            ft.Text("Duración (horas):", color="#bbbbbb"),
            duracion,
            boton,
        ],
        spacing=15,
        expand=True
    )

    panel_resumen = ft.Container(
        content=ft.Column(
            [
                ft.Text("RESUMEN", size=20, weight=ft.FontWeight.BOLD, color="#e6e6e6"),
                ft.Divider(color="#444444"),
                mensaje_error,
                resumen_texto
            ],
            spacing=10
        ),
        bgcolor="#141414",
        padding=20,
        border_radius=5,
        expand=True
    )

    contenido = ft.Column(
        [
            titulo,
            ft.Divider(color="#444444"),
            ft.Row(
                [
                    formulario,
                    panel_resumen
                ],
                spacing=40,
                alignment=ft.MainAxisAlignment.START
            )
        ],
        spacing=30
    )

    page.add(contenido)


ft.app(main)
