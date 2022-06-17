# jsxgraph-magic

**jsxgraph-magic** is an **IPython** magic wrapper for the famous JavaScript math-sketching package [JSXGraph](https://github.com/jsxgraph/jsxgraph). **jsxgraph-magic** enables you to use **JSXGraph** in Notebook and see the sketching in the output cell.

## Requirements
- A network connection is required to fetch the **JavaScript** and **CSS** file for **JSXGraph**.
- **IPython** is required since the magics are concept from the **IPython**.
- **IPython** alone cannot be much useful. It is usually accompanied with Jupyter Notebook or Jupyter Lab. Please try either.

## Installation

- From source code
  
  ```shell
  git clone https://github.com/chunxy/jsxgraph-magic.git
  cd jsxgraph-magic
  pip install ./
  ```

## Usage

- As with usual **IPython** magic, remember to `%load_ext jsxgraph-magic` before using this magic.

- This repo contains two magics: one line magic and one cell magic, both named as **jsxgraph**. 

  - The line magic requires no arguments and simply prompt the help message. 

    ```
    %jsxgraph
    ```
  
  - The cell magic may be used as follows:

    It will create one div element in the output cell, with id being `id`, and height being  `height` in the unit of `px`.  `JSXGraph descriptions`  is the JavaScript code to bind the drawboard with corresponding `HTMLElement` as well as to describe the graphs.
  
    ```
    %%jsxgraph -w 500 -h 500 box
    // Initialize board
    var b = JXG.JSXGraph.initBoard('box');
    // More code
    ```
    
    As an example, the above code will create a `div` with height and width `500px`. `box` is the id of the `<div>` block in the cell output that binds to the drawboard.



