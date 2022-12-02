#!/usr/bin/env python3
"""
Test the XXX.
"""

__author__ = "Jason Beach"
__version__ = "0.1.0"
__license__ = "MIT"

import pandas as pd

from pathlib import Path
import json

from styled_text import StyledText as st


def test_text_to_notebook_output():
    txt = "This is a long sentence."
    output = st.text_to_notebook_output(txt,[(5,7),(8,9),(15,23)], False, False)
    assert output == '<z style="color: gray;" >This <b style="color: black;">is</b> <b style="color: black;">a</b> long <b style="color: black;">sentence</b>.</z>'


def test_df_to_xlsx():
    dir_path = Path('./tests/data/')
    test_cases_files_and_results = {'export.jsonl':
                                        ["<class 'xlsxwriter.format.Format'>|This is |<class 'xlsxwriter.format.Format'>|some basic|<class 'xlsxwriter.format.Format'>| text. This is some basic |<class 'xlsxwriter.format.Format'>|text|<class 'xlsxwriter.format.Format'>|.",
                                         "<class 'xlsxwriter.format.Format'>|This is some |<class 'xlsxwriter.format.Format'>|basic|<class 'xlsxwriter.format.Format'>| text. This is some |<class 'xlsxwriter.format.Format'>|basic text|<class 'xlsxwriter.format.Format'>|."
                                         ],
                                    'export_timestamp.jsonl':
                                        ["<class 'xlsxwriter.format.Format'>|2017-12-16 03:02:35.500000    (Bob Iger): This is some |<class 'xlsxwriter.format.Format'>|basic text|<class 'xlsxwriter.format.Format'>|.\n2017-12-17 03:02:35.500000    (Mikey Mouse): This is |<class 'xlsxwriter.format.Format'>|also|<class 'xlsxwriter.format.Format'>| some basic text.",
                                         "<class 'xlsxwriter.format.Format'>|2017-12-18 03:02:35.500000    (Mikey Mouse): This is |<class 'xlsxwriter.format.Format'>|much more|<class 'xlsxwriter.format.Format'>| basic text.\n2017-12-19 03:02:35.500000    (Bob Iger): This is |<class 'xlsxwriter.format.Format'>|little|<class 'xlsxwriter.format.Format'>| text."
                                         ],
                                    'export_three_labels.jsonl': 
                                        ["<class 'xlsxwriter.format.Format'>|This is some |<class 'xlsxwriter.format.Format'>|basic|<class 'xlsxwriter.format.Format'>| text. Thi|<class 'xlsxwriter.format.Format'>|s is some |<class 'xlsxwriter.format.Format'>|basic |<class 'xlsxwriter.format.Format'>|text|<class 'xlsxwriter.format.Format'>|. This is some basic text."
                                         ],
                                    'export_end_points.jsonl':
                                        ["<class 'xlsxwriter.format.Format'>|This is |<class 'xlsxwriter.format.Format'>|some basic text. This is some basic |<class 'xlsxwriter.format.Format'>|text|<class 'xlsxwriter.format.Format'>|."
                                         ],
                                    #TODO: overlap fails
                                    'export_overlap.jsonl':
                                        ["<class 'xlsxwriter.format.Format'>|This |<class 'xlsxwriter.format.Format'>|is some basic text. |<class 'xlsxwriter.format.Format'>|This is some basic text."
                                         ]
                                    }
    # USER INPUT >>>                                
    TGT_TEST_CASE = [0,1,2,3]
    test_cases = [item for idx,item in enumerate(list(test_cases_files_and_results.items())) if idx in TGT_TEST_CASE] 
    for (file, test_case_results) in test_cases:
        input_path = dir_path / file
        output_path = dir_path / 'TEST.xlsx'
        data = []
        with open(input_path, 'r') as f:
            for line in f:
                data.append(json.loads(line))
        df = pd.DataFrame(data)
        case_results = st.df_to_xlsx(df=df, output_path=output_path, verbose=True)
        file_created_result = output_path.is_file()
        assert file_created_result == True
        for case, test_case in zip(case_results, test_case_results):
            assert case == test_case