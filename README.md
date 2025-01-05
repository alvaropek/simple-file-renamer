# simple-file-renamer
A simple python program to easily rename files within a folder of your OS based on two paired columns of text.


## GUI apperance
As soon as the renamer_gui.py is executed, a large GUI interface will be desplayed.

The upper two scrollable boxes contain the input for the current name (old names) and the future name (new names) of the files.
Below is a read-only Output Log box, to keep track of changes.

![vb9aS6pK6G](https://github.com/user-attachments/assets/d3409cf6-5272-4b5f-94d8-330f20771859)

Also when additional user input is needed (overwriting, conflicts, etc), a pop window appears with the available options as buttons:

![pGIaMU9T6Y](https://github.com/user-attachments/assets/7206fe3d-fdfe-464c-ac44-df904be53d91)



## Functionality

The program allows users to quickly and easily rename files in bulk based on a column for both the current names of files and the desired names to change them to (this wouls often come from a spreadsheet).

The names correspond one-to-one, and empty lines do not count as lines.
Both boxes need to have the same number of names (non-empty lines) for the renaming to take place and the program checks for that.

![6AuRUB0tIw](https://github.com/user-attachments/assets/0c81129a-f47b-4660-b3a2-16022d982be2)

Once the two columns are places in their respective boxes, they can be easily swapped by clicking the _**swap**_ button.
The start the renaming process, simply click the _**Apply changes**_ button.

The program will not override any files without prompting the user before continuing.

## Installation
As of rigth now, both files need to be installed in the folder where the files are located.
(This will soon be modified so that the program can work on any path of the system)


### Dependencies
Make sure the #customtkinter# library is installed:

```bash
pip install customtkinter
```
### Script installation
Install in the directory containing the files you plan on renaming.
```bash
#Cloning the repository
git clone https://github.com/alvaropek/simple-file-renamer.git

#Extracting the files
mv simple-file-renamer/*.py .
rm -rf simple-file-renamer

```
## Usage
In order to use the program, simply execute the ranamer_gui.py file on the folder were the files to rename and the _simple_file_renamer.py_ file are located.

```bash
python3 renamer_gui.py
```
This will display the GUI, which is the only way to operate the program.

Soon, a path selector will be added, allowing the program to act on any chosen path without the need to move the python files there.




