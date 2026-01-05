import tkinter as tk
from tkinter import ttk
from shadow import add_entry, analyze, weekly_summary

def submit_text():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        return
    add_entry(text)
    output_box.insert(tk.END, "✔ Noted.\n\n")
    input_box.delete("1.0", tk.END)
    input_box.focus()

def show_insight():
    result = analyze()
    output_box.insert(tk.END, "🔍 Insight:\n")
    output_box.insert(tk.END, result + "\n\n")
    output_box.see(tk.END)

def show_week():
    result = weekly_summary()
    output_box.insert(tk.END, "📅 Weekly Summary:\n")
    output_box.insert(tk.END, result + "\n\n")
    output_box.see(tk.END)

def on_enter(event):
    if event.state & 0x0001:
        return
    submit_text()
    return "break"

# --- GUI WINDOW ---
root = tk.Tk()
root.title("Digital Shadow")
root.geometry("600x700")
root.configure(bg="#1e1e1e")

# Configure styles
style = ttk.Style()
style.theme_use('clam')
style.configure('Title.TLabel', font=("Segoe UI", 14, "bold"), background="#1e1e1e", foreground="#ffffff")
style.configure('TLabel', font=("Segoe UI", 10), background="#1e1e1e", foreground="#cccccc")
style.configure('TButton', font=("Segoe UI", 10))

# --- INPUT SECTION ---
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(fill=tk.X, padx=15, pady=(15, 10))

input_label = ttk.Label(input_frame, text="Write freely:", style='Title.TLabel')
input_label.pack(anchor="w", pady=(0, 8))

input_box = tk.Text(
    root,
    height=6,
    font=("Consolas", 11),
    bg="#2d2d2d",
    fg="#ffffff",
    insertbackground="#00ff00",
    relief=tk.FLAT,
    borderwidth=2
)
input_box.pack(fill=tk.X, padx=15, pady=(0, 10))
input_box.bind("<Return>", on_enter)

# --- BUTTON SECTION ---
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(fill=tk.X, padx=15, pady=10)

save_btn = tk.Button(
    btn_frame,
    text="Save Entry",
    command=submit_text,
    font=("Segoe UI", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=8,
    relief=tk.FLAT,
    cursor="hand2"
)
save_btn.pack(side=tk.LEFT, padx=5)

insight_btn = tk.Button(
    btn_frame,
    text="Insight",
    command=show_insight,
    font=("Segoe UI", 10, "bold"),
    bg="#2196F3",
    fg="white",
    padx=15,
    pady=8,
    relief=tk.FLAT,
    cursor="hand2"
)
insight_btn.pack(side=tk.LEFT, padx=5)

week_btn = tk.Button(
    btn_frame,
    text=" Weekly",
    command=show_week,
    font=("Segoe UI", 10, "bold"),
    bg="#FF9800",
    fg="white",
    padx=15,
    pady=8,
    relief=tk.FLAT,
    cursor="hand2"
)
week_btn.pack(side=tk.LEFT, padx=5)

# --- OUTPUT SECTION ---
output_frame = tk.Frame(root, bg="#1e1e1e")
output_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(10, 15))

output_label = ttk.Label(output_frame, text="Reflection:", style='Title.TLabel')
output_label.pack(anchor="w", pady=(0, 8))

output_box = tk.Text(
    output_frame,
    bg="#0d0d0d",
    fg="#00ff00",
    font=("Consolas", 10),
    relief=tk.FLAT,
    borderwidth=2
)
output_box.pack(fill=tk.BOTH, expand=True)
output_box.insert(tk.END, "Digital Shadow is running.\nYour data stays local.\n\n")

root.mainloop()
