import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
from datetime import datetime
from google.cloud import vision
import io

class FoodTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Item Tracker")
        
        # Initialize CSV file with current week
        current_date = datetime.now()
        year, week, _ = current_date.isocalendar()
        self.csv_file = f"food_database_{year}_week_{week}.csv"
        self.init_csv()
        
        self.create_widgets()
        self.calculate_budget()

    def create_widgets(self):
        # Labels
        labels = [
            "Food Item:", "Price (MXN):", "Amount (kg):",
            "Serving Size (g):", "Calories per Serving:", "Store Purchased:"
        ]
        for idx, text in enumerate(labels):
            tk.Label(self.root, text=text).grid(row=idx, column=0, padx=10, pady=5, sticky="w")

        # Entry fields
        self.entries = {
            "food_item": tk.Entry(self.root, width=30),
            "price": tk.Entry(self.root, width=30),
            "amount": tk.Entry(self.root, width=30),
            "serving_size": tk.Entry(self.root, width=30),
            "calories": tk.Entry(self.root, width=30)
        }

        # Store Combobox
        self.store_var = tk.StringVar()
        self.entries["store"] = ttk.Combobox(
            self.root, 
            textvariable=self.store_var,
            values=["Alsuper", "Aurrera", "Walmart", "Farmers market", "Other"],
            width=27
        )

        # Grid layout for widgets
        for idx, key in enumerate(self.entries.keys()):
            self.entries[key].grid(row=idx, column=1, padx=10, pady=5)

        # Budget display
        tk.Label(self.root, text="Total Budget:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.budget_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.budget_var).grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Buttons
        tk.Button(self.root, text="Submit", command=self.save_entry).grid(row=7, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Clear", command=self.clear_fields).grid(row=7, column=1, padx=10, pady=10)
        tk.Button(self.root, text="New Week", command=self.new_week).grid(row=7, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Upload Receipt", command=self.upload_receipt).grid(row=8, column=0, padx=10, pady=10)

    def init_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Food Item", "Price (MXN)", "Amount (kg)",
                    "Serving Size (g)", "Calories per Serving", "Store Purchased"
                ])

    def save_entry(self):
        try:
            data = {
                "food_item": self.entries["food_item"].get(),
                "price": float(self.entries["price"].get()),
                "amount": float(self.entries["amount"].get()),
                "serving_size": float(self.entries["serving_size"].get()),
                "calories": float(self.entries["calories"].get()),
                "store": self.entries["store"].get()
            }

            with open(self.csv_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    data["food_item"], data["price"], data["amount"],
                    data["serving_size"], data["calories"], data["store"]
                ])

            self.clear_fields()
            self.calculate_budget()
            messagebox.showinfo("Success", f"Entry saved to {self.csv_file}!")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for numeric fields")

    def clear_fields(self):
        for entry in self.entries.values():
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            else:
                entry.delete(0, tk.END)

    def calculate_budget(self):
        total = 0.0
        try:
            with open(self.csv_file, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    try:
                        total += float(row[1])
                    except (ValueError, IndexError):
                        continue
            self.budget_var.set(f"{total:.2f} MXN")
        except FileNotFoundError:
            self.budget_var.set("0.00 MXN")

    def new_week(self):
        current_date = datetime.now()
        year, week, _ = current_date.isocalendar()
        self.csv_file = f"food_database_{year}_week_{week}.csv"
        self.init_csv()
        self.calculate_budget()
        messagebox.showinfo("New Week", f"New weekly sheet created: {self.csv_file}")

    def upload_receipt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            try:
                # Initialize the Google Cloud Vision client
                client = vision.ImageAnnotatorClient()

                # Load the image file
                with io.open(file_path, 'rb') as image_file:
                    content = image_file.read()

                image = vision.Image(content=content)

                # Perform text detection
                response = client.text_detection(image=image)
                texts = response.text_annotations

                if texts:
                    # Extract the first block of text (usually the entire receipt text)
                    receipt_text = texts[0].description

                    # Parse the receipt text (this is a simple example, you may need a more sophisticated parser)
                    lines = receipt_text.split('\n')
                    for line in lines:
                        if "Total" in line:
                            total_price = line.split()[-1]
                            self.entries["price"].insert(0, total_price)
                        # Add more parsing logic here based on your receipt format

                    messagebox.showinfo("Receipt Uploaded", "Receipt text extracted and parsed.")
                else:
                    messagebox.showinfo("Receipt Uploaded", "No text found in the receipt.")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodTrackerApp(root)
    root.mainloop()