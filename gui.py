import customtkinter as ctk
import threading

from speech import listen
from ai import ask_gemini
from tts import speak, stop_speaking
from agent import run_agent
from tkinter import filedialog

# ==========================================
# THEME
# ==========================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ==========================================
# GUI
# ==========================================

class OrvynGUI:

    def pick_image(self):

        path = filedialog.askopenfilename(

            filetypes=[

                ("Images", "*.png *.jpg *.jpeg *.webp")

            ]

        )

        if not path:

            return

        threading.Thread(

            target=self.process_image,

            args=(path,),

            daemon=True

        ).start()

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("Orvyn AI")

        self.root.geometry("1400x850")

        self.root.minsize(1200, 750)

        self.root.configure(
            fg_color="#F8F5F1"
        )

        # ==================================
        # HEADER
        # ==================================

        self.header = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        self.header.pack(
            fill="x",
            pady=(25, 10)
        )

        self.logo = ctk.CTkLabel(
            self.header,
            text="⬢",
            text_color="#F97316",
            font=("Segoe UI", 46, "bold")
        )

        self.logo.pack()

        self.title = ctk.CTkLabel(
            self.header,
            text="ORVYN",
            text_color="#2D2D2D",
            font=("Segoe UI", 42, "bold")
        )

        self.title.pack()

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Your Intelligent Desktop Companion",
            text_color="#7C6F64",
            font=("Segoe UI", 18)
        )

        self.subtitle.pack()

        # ==================================
        # CHAT
        # ==================================

        self.chat = ctk.CTkScrollableFrame(
            self.root,
            fg_color="#FFF8F2",
            corner_radius=25
        )

        self.chat.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ==================================
        # STATUS
        # ==================================

        self.status = ctk.CTkLabel(
            self.root,
            text="🟢 Ready",
            text_color="#16A34A",
            font=("Segoe UI", 16, "bold")
        )

        self.status.pack(
            pady=5
        )

        # ==================================
        # BOTTOM BAR
        # ==================================

        self.bottom = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        self.bottom.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.entry = ctk.CTkEntry(
            self.bottom,
            height=52,
            font=("Segoe UI", 15),
            placeholder_text="Ask Orvyn anything..."
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 12)
        )

        self.entry.bind(
            "<Return>",
            lambda event: self.send_text()
        )

        self.send_btn = ctk.CTkButton(
            self.bottom,
            text="➜",
            width=60,
            height=52,
            corner_radius=26,
            fg_color="#F97316",
            hover_color="#EA580C",
            command=self.send_text
        )

        self.send_btn.pack(
            side="left",
            padx=5
        )

        self.voice_btn = ctk.CTkButton(
            self.bottom,
            text="🎤",
            width=60,
            height=52,
            corner_radius=26,
            fg_color="#F97316",
            hover_color="#EA580C",
            command=self.start_voice
        )

        self.voice_btn.pack(
            side="left",
            padx=5
        )

        self.stop_btn = ctk.CTkButton(

            self.bottom,

            text="⏹",

            width=60,

            height=52,

            corner_radius=26,

            fg_color="#DC2626",

            hover_color="#B91C1C",

            command=stop_speaking

        )

        self.stop_btn.pack(
            side="left",
            padx=5
        )

        self.image_btn = ctk.CTkButton(

            self.bottom,

            text="🖼",

            width=55,

            height=50,

            corner_radius=25,

            fg_color="#F97316",

            hover_color="#EA580C",

            command=self.pick_image

        )

        self.image_btn.pack(

            side="left",

            padx=5

        )

        self.add_bot_message(
            "👋 Hello, Jahnavi.\n\nI'm Orvyn.\n\nHow can I help you today?"
        )
    def stream_response(self, text):

        try:

            if not text:

                return
        
            reply = ask_gemini(text)

            self.root.after(
                    0,
                    lambda: self.add_bot_message(reply)
                )

            self.root.after(
                    0,
                    lambda: self.status.configure(
                        text="🗣️ Speaking...",
                        text_color="#EA580C"
                    )
                )

            try:

                speak(reply)

            except Exception as e:

                print("Speech Error:", e)
                
        except Exception as e:

            error_message = f"❌ Error:\n{str(e)}"

            self.root.after(

        0,

        lambda msg=error_message:

            self.add_bot_message(msg)

    )

        finally:

            self.root.after(
                0,
                lambda: self.status.configure(
                    text="🟢 Ready",
                    text_color="#16A34A"
                )
            )

            self.root.after(
                0,
                lambda: self.send_btn.configure(
                    state="normal"
                )
            )

            self.root.after(
                0,
                lambda: self.voice_btn.configure(
                    state="normal"
                )
            )

    # ==========================================
    # CREATE CHAT BUBBLE
    # ==========================================

    def create_card(
        self,
        sender,
        message,
        color,
        is_user=False
    ):

        container = ctk.CTkFrame(
            self.chat,
            fg_color="transparent"
        )

        container.pack(
            fill="x",
            padx=15,
            pady=8
        )

        bubble = ctk.CTkFrame(
            container,
            fg_color=color,
            corner_radius=18
        )

        if is_user:

            bubble.pack(
                anchor="e",
                padx=10
            )

        else:

            bubble.pack(
                anchor="w",
                padx=10
            )

        sender_label = ctk.CTkLabel(
            bubble,
            text=sender,
            font=("Segoe UI", 12, "bold"),
            text_color="#444444"
        )

        sender_label.pack(
            anchor="w",
            padx=12,
            pady=(8, 0)
        )

        message_label = ctk.CTkLabel(
            bubble,
            text=message,
            wraplength=700,
            justify="left",
            font=("Segoe UI", 15),
            text_color="#222222"
        )

        message_label.pack(
            anchor="w",
            padx=12,
            pady=(3, 10)
        )

        self.root.update_idletasks()

        try:

            self.chat._parent_canvas.yview_moveto(1.0)

        except:

            pass


    # ==========================================
    # USER MESSAGE
    # ==========================================

    def add_user_message(self, text):

        self.create_card(

            sender="👤 You",

            message=text,

            color="#FFD6B0",

            is_user=True

        )


    # ==========================================
    # BOT MESSAGE
    # ==========================================

    def add_bot_message(self, text):

        self.create_card(

            sender="🤖 Orvyn",

            message=text,

            color="#FFFFFF",

            is_user=False

        )

    def update_last_bot_message(self, text):

        try:

            last = self.chat.winfo_children()[-1]

            bubble = last.winfo_children()[0]

            body = bubble.winfo_children()[1]

            current = ""

            for word in text.split():

                current += word + " "

                body.configure(text=current)

                self.root.update()

                self.root.after(20)

        except:

            self.add_bot_message(text)

    # ==========================================
    # SEND TEXT
    # ==========================================

    def send_text(self):

        text = self.entry.get().strip()

        if not text:

            return

        self.entry.delete(
            0,
            "end"
        )

        threading.Thread(

            target=self.process_text,

            args=(text,),

            daemon=True

        ).start()


    # ==========================================
    # PROCESS TEXT
    # ==========================================
    def process_image(self, path):

        from vision import analyze_image

        self.root.after(
            0,
            lambda: self.status.configure(
                text="🖼 Analyzing...",
                text_color="#F97316"
            )
        )

        self.root.after(
            0,
            lambda: self.add_user_message(
                f"Selected image:\n{path}"
            )
        )

        try:

            reply = analyze_image(path)

            self.root.after(
                0,
                lambda msg=reply: self.add_bot_message(msg)
            )

            threading.Thread(
                target=speak,
                args=(reply,),
                daemon=True
            ).start()

        except Exception as e:

            error_message = f"Error: {str(e)}"

            self.root.after(
                0,
                lambda msg=error_message:
            self.add_bot_message(msg)
    )

        self.root.after(
            0,
            lambda: self.status.configure(
                text="🟢 Ready",
                text_color="#16A34A"
            )
        )

    def process_text(self, text):

        self.root.after(
            0,
            lambda: self.send_btn.configure(
            state="disabled"
        )
    )

        self.root.after(
            0,
            lambda: self.voice_btn.configure(
            state="disabled"
        )
    )

        self.root.after(
            0,
            lambda: self.add_user_message(text)
    )

        self.root.after(
            0,
            lambda: self.status.configure(
                text="🤔 Thinking...",
                text_color="#F97316"
        )
    )

        try:

            from command_router import execute

            text = text.strip()

            result = execute(text)

        # ----------------------------------
        # Desktop command handled
        # ----------------------------------

            if result is not None:

                self.root.after(
                    0,
                    lambda: self.add_bot_message(result)
            )

                threading.Thread(
                    target=speak,
                    args=(result,),
                    daemon=True
                ).start()

        # ----------------------------------
        # Otherwise ask Gemini
        # ----------------------------------

            else:

                self.stream_response(text)

                return

        except Exception as e:

            error_message = f"❌ Error:\n{str(e)}"

            self.root.after(
                0,
                lambda msg=error_message:
            self.add_bot_message(msg)
    )

        finally:

            self.root.after(
                0,
                lambda: self.status.configure(
                text="🟢 Ready",
                text_color="#16A34A"
            )
        )

            self.root.after(
            0,
            lambda: self.send_btn.configure(
                state="normal"
            )
        )

            self.root.after(
                0,
                lambda: self.voice_btn.configure(
                state="normal"
            )
        )



    # ==========================================
    # START VOICE
    # ==========================================

    def start_voice(self):

        threading.Thread(

            target=self.process_voice,

            daemon=True

        ).start()


    # ==========================================
    # PROCESS VOICE
    # ==========================================

    def process_voice(self):

        self.root.after(
            0,
            lambda: self.status.configure(
                text="🎤 Listening...",
                text_color="#2563EB"
            )
        )

        query = listen()

        if not query:

            self.root.after(
                0,
                lambda: self.status.configure(
                    text="🟢 Ready",
                    text_color="#16A34A"
                )
            )

            return

        self.root.after(
            0,
            lambda: self.entry.delete(
                0,
                "end"
            )
        )

        self.root.after(
            0,
            lambda: self.entry.insert(
                0,
                query
            )
        )

        threading.Thread(

            target=self.process_text,

            args=(query,),

            daemon=True

        ).start()


    # ==========================================
    # RUN
    # ==========================================

    def run(self):

        self.root.mainloop()


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    app = OrvynGUI()

    app.run()

