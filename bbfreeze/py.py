#! /usr/bin/env python
"""interactive python prompt with tab completion"""

# code inspired by matplotlib
# (http://matplotlib.sourceforge.net/examples/interactive.py)

import code
import rlcompleter
try:
    import readline
except ImportError:
    readline = None
    

class MyConsole(code.InteractiveConsole):
    def __init__(self, *args, **kwargs):
        code.InteractiveConsole.__init__(self, *args, **kwargs)
        
        try:  # this form only works with python 2.3
            self.completer = rlcompleter.Completer(self.locals)
        except: # simpler for py2.2
            self.completer = rlcompleter.Completer()

        if not readline:
            return
        
        readline.set_completer(self.completer.complete)
        # Use tab for completions
        readline.parse_and_bind('tab: complete')
        # This forces readline to automatically print the above list when tab
        # completion is set to 'complete'.
        readline.parse_and_bind('set show-all-if-ambiguous on')
        # Bindings for incremental searches in the history. These searches
        # use the string typed so far on the command line and search
        # anything in the previous input history containing them.
        readline.parse_and_bind('"\C-r": reverse-search-history')
        readline.parse_and_bind('"\C-s": forward-search-history')

if __name__=='__main__':
    if readline:
        import os
        histfile = os.path.expanduser("~/.pyhistory")
        if os.path.exists(histfile):
            readline.read_history_file(histfile)
        
    try:
        MyConsole(locals=dict()).interact()
    finally:
        if readline:
            readline.write_history_file(histfile)
