import customtkinter as ctk

from theme import *


class ChatBubble(ctk.CTkFrame):

    def __init__(self, master, sender, message, is_user=False):

        bubble_color = USER_BUBBLE if is_user else BOT_BUBBLE

        super().__init__(
            master=master,
            fg_color=bubble_color,
            corner_radius=15
        )

        self.pack(fill="x", padx=15, pady=8)

        sender_label = ctk.CTkLabel(
            self,
            text=sender,
            font=("Segoe UI", 13, "bold"),
            text_color=TEXT,
            anchor="w"
        )

        sender_label.pack(
            anchor="w",
            padx=12,
            pady=(8, 2)
        )

        message_label = ctk.CTkLabel(
            self,
            text=message,
            font=CHAT_FONT,
            text_color=TEXT,
            justify="left",
            wraplength=700,
            anchor="w"
        )

        message_label.pack(
            anchor="w",
            padx=12,
            pady=(0, 10)
        )