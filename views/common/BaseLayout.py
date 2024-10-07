import customtkinter as ctk

def initialize_window():
    root = ctk.CTk()
    root.title("RENTAL SYSTEM")
    root.geometry("1000x700")
    return root


def create_background(root):
    background_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='white')
    background_frame.place(relwidth=1, relheight=1)
    return background_frame


def create_title(parent, text):
    title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
    title_frame.pack(pady=20)

    title_label = ctk.CTkLabel(
        title_frame,
        text=text,
        font=('Poppins Medium', 50, 'bold'),
        text_color='#8f8e8e'
    )
    title_label.grid(row=0, column=0, pady=10)
