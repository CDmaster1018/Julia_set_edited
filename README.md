# Julia_set_edited
A package for drawing Mandelbrot and Julia sets.
## Installation
1. Clone the repository to your local machine using the command
`git clone https://github.com/CDmaster1018/Julia_set_edited.git`
in a directory of your choice.
2. Navigate to the M2R-Julia-Sets folder (first `cd Julia_set_edited`, then `cd M2R-Julia-Set`)
3. Use pip to install the package
    
    a. In editable mode: `pip install -e .`
    
    b. Without editable mode: `pip install .`
## Using the GUI
In order to use the GUI, install the package and then follow the instructions in the [GUI_README](./GUI_README.md) file.
### Important For Mac Users:
If an error message about Preview app come up when you try to produce pictures of Julia set through terminal command, then try the following command:
`ln -s /System/Applications/Preview.app/ /Applications/Preview.app`
This could create a soft link so that Preview app can now be called from its current directory by python.
