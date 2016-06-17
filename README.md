# Arduino-PyPlot
A collection of Python and Arduino source files to plot data in real time.


### Requirements
Install requirements by running `pip install -r requirements.txt`


Because matplotlib has issues with virtualenv on macosx one must add the following function
to ~/.bash_rc

  `function frameworkpython {
     if [[ ! -z "$VIRTUAL_ENV" ]]; then
          PYTHONHOME=$VIRTUAL_ENV /usr/local/bin/python "$@"
      else
          /usr/local/bin/python "$@"
      fi
  }`
