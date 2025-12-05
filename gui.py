# gui.py

import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from algorithms import fcfs, sstf, scan, cscan, look
from simulator import simulate


# =======================
# Animate Graph
# =======================
def animate_graph(steps, algo):
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#1e272e")
    ax.set_facecolor("#2f3640")

    ax.set_title(f"Disk Head Animation - {algo}", color="white", fontsize=14)
    ax.set_xlabel("Step", color="white")
    ax.set_ylabel("Cylinder", color="white")
    ax.tick_params(colors="white")

    ax.grid(True, color="#718093")

    ax.set_xlim(0, len(steps))
    ax.set_ylim(min(steps) - 10, max(steps) + 10)

    line, = ax.plot([], [], marker="o", color="#00a8ff", linewidth=2)

    def update(i):
        line.set_data(range(i + 1), steps[:i + 1])
        return line,

    ani = FuncAnimation(fig, update, frames=len(steps),
                        interval=400, repeat=False)

    plt.show()


# =======================
# Simulation Logic
# =======================
def run_simulation():
    try:
        req = request_entry.get().strip()
        requests = list(map(int, req.split(",")))
        head = int(head_entry.get())
    except:
        messagebox.showerror("Input Error", "Example:\n12,44,56,77,88,54")
        return

    algo_name = algo_dropdown.get()

    mapping = {
        "FCFS": fcfs,
        "SSTF": sstf,
        "SCAN": scan,
        "C-SCAN": cscan,
        "LOOK": look
    }

    order = mapping[algo_name](requests, head)
    total, avg, steps = simulate(order, head)

    result_label.config(
        text=f"{algo_name} Results:\n"
             f"Total Seek Time = {total}\n"
             f"Average Seek Time = {avg:.2f}"
    )

    animate_graph(steps, algo_name)


# =======================
# GUI Setup
# =======================

root = tk.Tk()
root.title("Disk Scheduling Simulator - DASH UI")
root.geometry("600x520")
root.configure(bg="#1e272e")

# Header
header = tk.Label(root, text="Disk Scheduling Simulator",
                  font=("Segoe UI", 20, "bold"),
                  fg="#00a8ff", bg="#1e272e")
header.pack(pady=20)

# Card Frame (Dashboard Style)
card = tk.Frame(root, bg="#2f3640", bd=0, relief="ridge")
card.pack(pady=10, padx=20, fill="both")

# Requests
tk.Label(card, text="Requests (comma-separated):",
         font=("Segoe UI", 11), fg="#dcdde1", bg="#2f3640").pack(pady=5)
request_entry = tk.Entry(card, width=45, font=("Segoe UI", 11), bg="#353b48", fg="white")
request_entry.pack(pady=5)

# Head
tk.Label(card, text="Initial Head Position:",
         font=("Segoe UI", 11), fg="#dcdde1", bg="#2f3640").pack(pady=5)
head_entry = tk.Entry(card, width=15, font=("Segoe UI", 11), bg="#353b48", fg="white")
head_entry.pack(pady=5)

# Algorithm Dropdown
tk.Label(card, text="Select Algorithm:",
         font=("Segoe UI", 11), fg="#dcdde1", bg="#2f3640").pack(pady=5)
algo_dropdown = ttk.Combobox(card,
                             values=["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK"])
algo_dropdown.current(0)
algo_dropdown.pack(pady=5)

# Run Button – Neon Style
run_btn = tk.Button(card,
                    text="Run Simulation",
                    font=("Segoe UI", 12, "bold"),
                    bg="#00a8ff",
                    fg="black",
                    padx=15, pady=8,
                    relief="flat",
                    command=run_simulation)
run_btn.pack(pady=15)

# Hover effect for button
def on_enter(e):
    run_btn['bg'] = "#0097e6"

def on_leave(e):
    run_btn['bg'] = "#00a8ff"

run_btn.bind("<Enter>", on_enter)
run_btn.bind("<Leave>", on_leave)

# Result Label
result_label = tk.Label(root, text="",
                        font=("Segoe UI", 14),
                        fg="#fbc531",
                        bg="#1e272e")
result_label.pack(pady=10)

root.mainloop()
