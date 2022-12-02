# Styled Text Output

Output text with style in a variety of formats.  This is useful for highlighting target text to improve reviewing experience in NLP scenarios.

Styled output formats include:

* html for jupyter notebooks
* excel workbooks


## Usage

### Notebook

Within a notebook cell:

```
>>> from styled_text import StyledText
>>> txt = "This is a long sentence."
>>> StyledText.text_to_notebook_output(txt,[(5,7),(8,9),(15,23)], True)

<z style="color: gray;" >This <b style="color: black;">is</b> <b style="color: black;">a</b> long <b style="color: black;">sentence</b>.</z>
This is a long sentence.
```

### Doccano

Using Doccano text labeling application:

* group individual messages into single dialogues
* upload dialogues into Doccano
* download jsonl, then process with `StyledText.df_to_excel()`

For detailed instructions, see `./tests/doccano_workflow.md`.


## Install

TODO


## Test

`pytest --collect-only`


## TODO

* overlapping highlights
* condense code to improve maintainability
* make more robust
* functionality for additional output mediums