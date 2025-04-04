from nicegui import ui

def show_answer(answer):
    ui.notify(answer)  # Shows a pop-up notification

ui.label('What Can I Do For You?').classes('text-lg font-bold mt-4')

with ui.card().classes('bg-gray-200 p-4 w-full mt-2'):
    ui.input(placeholder='command here')

ui.label('FAQ').classes('text-lg font-bold mt-6')

with ui.column().classes('space-y-2 mt-4'):
    ui.button('What is the number of Programs in UIU?', on_click=lambda: show_answer('17 Programs'))
    ui.button('What is the location of UIU?', on_click=lambda: show_answer('United City, Madani Avenue, Badda, Dhaka, Dhaka 1212, Bangladesh'))
    ui.button('Who is Vice Chancellor of UIU?', on_click=lambda: show_answer('Prof. Dr. Md. Abul Kashem Mia'))
    ui.button('What is the location of UIU library?', on_click=lambda: show_answer('Ground Floor, UIU Campus'))
    ui.button('What is the location of UIU cafeteria?', on_click=lambda: show_answer('Ground Floor, UIU Campus'))
    ui.button('What is required Credit for Bachelor of CSE Program?', on_click=lambda: show_answer('Total 132 Credits'))
ui.run()  
