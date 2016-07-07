# Arduino-PyPlot
A collection of Python and Arduino source files to plot data in real time.


### Requirements
Install requirements by running `pip install -r requirements.txt`. Additionally, if you're using MacOSX you must add the following function to your `~/.bash_rc` then `source ~/.bash_rc` to make that command available.

```bash
function frameworkpython {
  if [[ ! -z "$VIRTUAL_ENV" ]]; then
    PYTHONHOME=$VIRTUAL_ENV /usr/local/bin/python "$@"
  else
    /usr/local/bin/python "$@"
  fi
}
```

### To use
Setup Arduino to be something like this:

![Image of circuit]
(http://i64.tinypic.com/3h4k8.png)


And run on mac `frameworkpython src/python/stream_data.py` else `python src/python/stream_data.py`
