from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
from IPython.display import Javascript, display

@magics_class
class JSXGraph(Magics):

    @magic_arguments()
    @argument(
        '-w', '--width', type=int, default=600,
        help="The width of the output frame (default: 600)."
    )
    @argument(
        'arg', type=str,
        help="id of a <div> element for embeding the board."
    )
    @argument(
        '-h', '--height', type=int, default=600,
        help="The height of the output frame (default: 600)."
    )
    @cell_magic
    def jsxgraph(self, line, cell):
        opts = parse_argstring(self.jsxgraph, line)
        display(Javascript(f"""
        var JXG_div = document.createElement("div");
        JXG_div.id = "{opts.arg}";
        JXG_div.style = "height:{opts.height}px;width:{opts.width}px";
        element.append(JXG_div);
        """))
        display(Javascript(cell,
        lib='https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js', 
        css='https://jsxgraph.org/distrib/jsxgraph.css'))

def load_ipython_extension(ipython):
    """
    Register the magics with a running IPython so the magics can be loaded via
     `%load_ext jsxgraph` or be configured to be autoloaded by IPython at startup time.
    """
    ipython.register_magics(JSXGraph)