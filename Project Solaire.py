import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class SolarPanelDefectDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar Panel Defect Detector")
        self.root.geometry("800x600")

        # Title Label
        title_label = ttk.Label(root, text="Solar Panel Defect Detector", font=("Helvetica", 24))
        title_label.pack(pady=20)

        # Frame for Image Selection and Display
        image_frame = ttk.LabelFrame(root, text="Step 1: Upload Solar Panel Image", padding=(20, 10))
        image_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.image_label = ttk.Label(image_frame, text="No image selected", font=("Helvetica", 12))
        self.image_label.pack()

        upload_button = ttk.Button(image_frame, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

        # Frame for Defect Detection
        detection_frame = ttk.LabelFrame(root, text="Step 2: Detect Defects", padding=(20, 10))
        detection_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.defect_result_label = ttk.Label(detection_frame, text="Defect Detection Result: None", font=("Helvetica", 12))
        self.defect_result_label.pack(pady=10)

        detect_button = ttk.Button(detection_frame, text="Detect Defects", command=self.detect_defects)
        detect_button.pack()

        # Exit Button
        exit_button = ttk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(pady=10)

        self.image_path = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            image = image.resize((400, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
        else:
            messagebox.showerror("Error", "No image selected!")

    def detect_defects(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        # Simulate defect detection logic (replace with actual detection model logic)
        defects_detected = ["Cracks", "Discoloration", "Hotspots"]

        self.defect_result_label.config(
            text=f"Defect Detection Result: {', '.join(defects_detected)}"
        )
        messagebox.showinfo("Detection Complete", "Defect detection has been completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SolarPanelDefectDetectorApp(root)
    root.mainloop()
