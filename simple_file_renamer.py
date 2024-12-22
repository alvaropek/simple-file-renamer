#Simple file renamer logic

import os
# Set default value for overwrite
overwrite = None

# Create empty list to store results
results_sum = []

# Definition of renamer function
def rename_files(old_names_list, new_names_list, log_callback, ask_if_overwrite_callback):
    global overwrite
    global results_sum

    # Check that the two lists are the same length and are therefore paired.
    if len(old_names_list) != len(new_names_list):
        log_callback("Error: The number of old names and new names must be the same.")
        return


# Keep lists of renamed, failed and skipped files
    renamed_files = []
    skipped_files = []
    not_found_files = []
    overwritten_files = []


    # Rename each file to the its new name if file exists and manage overwriting
    for old_name, new_name in zip(old_names_list, new_names_list):   
            if os.path.isfile(new_name) and os.path.isfile(old_name):

                # if overwrite is True or False, user will not be prompted
                if overwrite is None:
                    # Check if the user wants to overwrite the file
                    cleaned_answer = ask_if_overwrite_callback(new_name)

                    # Option 2: Skip this file
                    if cleaned_answer == "2":
                        log_callback(f"Not overwriting {new_name}. Will skip file")
                        skipped_files.append((old_name))
                        continue
                    # Option 4: Skip this file and all other conflicting files
                    elif cleaned_answer == "4":
                        overwrite = False
                        log_callback(f"Skipping {old_name} and all other conflicting files")
                        skipped_files.append((old_name))
                        continue
                    # Option 3: Overwrite this file
                    elif cleaned_answer == "3":
                        overwrite = True
                        log_callback(f"Overwriting all conflicting files")

            try:
                # Rename the file if it exists and the new name is not already taken
                if not os.path.isfile(new_name):
                    os.rename(old_name, new_name)
                    log_callback(f"Renamed {old_name} to {new_name}.")
                    renamed_files.append((old_name))
                else:
                # Overwrite the file if the user has chosen to do so
                    if overwrite != False:
                        os.replace(old_name, new_name)
                        log_callback(f"Overwriting {new_name} with {old_name}.")
                        overwritten_files.append((new_name))
                        renamed_files.append((old_name))
                # Skip file if overwrite is False
                    else:
                        log_callback(f"Skipping {old_name}.")
                        skipped_files.append((old_name))
                
            # Report files not found
            except FileNotFoundError:
                log_callback(f"Error: File {old_name} not found.")
                not_found_files.append(old_name)
    
    def clean_output(string):
        return string.replace("[", "").replace("]", "").replace("'", "")

    # Store and display results on GUI terminal           
    results_sum = [renamed_files, skipped_files, not_found_files, overwritten_files]
    log_callback(clean_output(f"\nRenamed:  {results_sum[0]}"))
    log_callback(clean_output(f"Skipped:  {results_sum[1]}"))
    log_callback(clean_output(f"Not found:  {results_sum[2]}"))
    log_callback(clean_output(f"Overwritten:  {results_sum[3]}\n"))
    
    # Reset overwrite to None for future actions
    overwrite = None
 


