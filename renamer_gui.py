#Simple file renamer GUI with customtkinter

import customtkinter as ctk
from simple_file_renamer import rename_files

def create_interface():
    # Create the main window
    app = ctk.CTk()
    app.title("Simple-file-renamer")
    app.geometry("600x770+700+130") # Set the size and position of the window

    # Variables
    normal_width = 250
    normal_height = 400
    normal_pady = 10
    normal_padx = 10
    spacing = 10  # Spacing between the text boxes
    saved_content = {}  # Dictionary to save the content of the text boxes
    
    # Create a frame to contain the elements
    frame = ctk.CTkFrame(app)
    frame.pack(pady=normal_pady, padx=normal_padx)

    # Label and textbox for "Old names"
    old_names_label = ctk.CTkLabel(frame, text="Old names")
    old_names_label.grid(row=0, column=0)

    old_names_text = ctk.CTkTextbox(frame, width=normal_width, height=normal_height)
    old_names_text.grid(row=1, column=0, padx=(spacing, spacing))

    # Set default text for testing purposes
    # old_names_text.insert("1.0", "mumu.txt\nmimi.txt")

    # Label and textbox for "New names"
    new_names_label = ctk.CTkLabel(frame, text="New names")
    new_names_label.grid(row=0, column=1)

    new_names_text = ctk.CTkTextbox(frame, width=normal_width, height=normal_height)
    new_names_text.grid(row=1, column=1, padx=(spacing, spacing))

    # Set default text for testing purposes
    # new_names_text.insert("1.0", "mimi.txt\nmomo.txt")

    # Textbox for output messages
    output_label = ctk.CTkLabel(frame, text="Output Log")
    output_label.grid(row=2, columnspan=2)

    output_text = ctk.CTkTextbox(frame, width=normal_width * 2, height=normal_height // 2)
    output_text.grid(row=3, columnspan=2, padx=(spacing, spacing))

    # Function to log messages
    def log_message(message):
        output_text.insert("end", message + "\n")
        output_text.see("end")  # Auto-scroll to the latest message

    # Function to show ask_if_overwrite dialog box
    def ask_if_overwrite(filename):
        # Create the main window
        window = ctk.CTk()
        window.title("Overwrite File")
        window.geometry("400x210+800+240")
        

        # Variable for the result
        result = ctk.StringVar(value="2")  # Standard value is "No"

        def set_result_and_close(choice):
            """Set the result and close the window."""
            if window.winfo_exists():  # Check if the window still exists
                result.set(choice)
                window.quit()  # Ends the mainloop but does not destroy the window immediately
                window.destroy()  # Safely close the window


        # Label
        label = ctk.CTkLabel(
            window,
            text=(f"File '{filename}' already exists. Do you want to overwrite it?\n")
        )
        label.pack(pady=10)

        # Buttons
        button_yes = ctk.CTkButton(
            window,
            text="Yes",
            command=lambda: set_result_and_close("1")
        )
        button_yes_all = ctk.CTkButton(
            window,
            text="Yes, and overwrite all conflicts",
            command=lambda: set_result_and_close("3")
        )
        button_no = ctk.CTkButton(
            window,
            text="No",
            command=lambda: set_result_and_close("2")
        )

        button_no_all = ctk.CTkButton(
            window,
            text="No, and skip all conflicts",
            command=lambda: set_result_and_close("4")
        )

        # Position of buttons
        button_yes.pack(pady=5)
        button_no.pack(pady=5)
        button_yes_all.pack(pady=5)
        button_no_all.pack(pady=5)

        # Start the GUI
        window.mainloop()

        # Return the result
        return result.get()

        

    # Swap function for old and new names
    def swap_names():
        # Get the content of the text boxes
        old_content = old_names_text.get("1.0", "end").strip()
        new_content = new_names_text.get("1.0", "end").strip()
        
        # Clean and set new content
        old_names_text.delete("1.0", "end")
        new_names_text.delete("1.0", "end")
        old_names_text.insert("1.0", new_content)
        new_names_text.insert("1.0", old_content)

    # Function to apply changes
    def apply_changes():
        # Save the content of the text boxes in a dictionary and log it
        saved_content['old_names'] = old_names_text.get("1.0", "end").strip().splitlines()
        saved_content['new_names'] = new_names_text.get("1.0", "end").strip().splitlines()
        log_message("Contenido guardado: {}".format(saved_content))  # Log saved content

        # Call the rename_files function with the saved content
        old_names = saved_content["old_names"]
        new_names = saved_content["new_names"]
        rename_files(old_names, new_names, log_message, ask_if_overwrite)

    # Create the swap button
    swap_button = ctk.CTkButton(app, text="Swap", command=swap_names)
    swap_button.pack(pady=normal_pady / 4)

    # Create the apply changes button
    apply_button = ctk.CTkButton(app, text="Apply Changes", command=apply_changes)
    apply_button.pack(pady=normal_pady)

    # Start the GUI event loop
    app.mainloop()

# Call the function to create the interface
create_interface()