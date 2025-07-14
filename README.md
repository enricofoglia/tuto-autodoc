# Autodoc: please make your code readable

Code is nice. Readable code is *nicer*. Readable code that comes with a nicely structured documentation is fucking **awesome**. And all you have to do is follow some simple steps and install a couple packages. Really, you have no escuses.

1. **Install UV**: [UV](https://docs.astral.sh/uv/) is a virtual environment and package manager for python written in rust. 
2. **Initialize your project**: run
    ```
    uv init
    ```
    to make you current directory a python project. You can now use `uv add <package>` to add any library you need. For this tutorial you will need [sphinx](https://www.sphinx-doc.org/en/master/index.html):
   ```
   uv add sphinx
   ```
3. **Install your package locally**: run
    ```
    uv pip install . -e
    ```
    to intall your package locally. You can now import it where you need it, and sphinx will recognize it as something worth documenting.
4. **Initialize the docs**: using your newly acquired sphinx powers, run:
    ```
    sphinx-quickstart docs
    ```
    to initialize the documentation into a new folder named `docs/`. You will be prompted with some questions, reply as you feel more confortable. I would definetely advice to separate the `source/` and `build/` directories though, otherwise thing will get messy.
5. **Include autodoc**: open your `source/conf.py` file. Add:
     ```python
     import sys
     from pathlib import Path
      
     sys.path.insert(0, str(Path('path/to/your/package').resolve()))
     ```
     to let sphinx know where your package is. Don't forget to add the autodoc extension:
     ```python
     extensions = [
      ...
      'sphinx.ext.autodoc',
      'sphinx.ext.autosummary',
      'sphinx.ext.napoleon',
      ]

     ```
6. **Add your modules to the party**: somewhere (either in the `index.rst` file directly or in another `.rst` file *indexed in some table of content*) add your modules:
     ```rst
    .. automodule:: <your_module>
       :members:
       :undoc-members:
       :show-inheritance:
     ```
7. **Make your Doc!**: you are now ready to make your Doc! Go inside the `docs` directory and let the Makefile do its thing:
    ```
    cd docs
    make <format>
    ```
    nice formats are `html` and `latexpdf`, but honestly the sky (installed sphinx libraries) is the limit! The compiled files are going to be in the `docs/build/<format>` directory.
   
