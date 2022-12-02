
# Doccano Workflow

These instructions demonstrate a typical workflow for annotating message dialogue data with Doccano.  The data is then exported to jsonl (see example file `./tests/data/export_timestamp.jsonl`) for use with StyledText.


Start Doccano web server.

```bash
doccano init
doccano createuser
doccano webserver
```

Manual method of preparing data in Doccano.  Once download is complete, it can be loaded into a df for use with StyleText.

* don't use doccano exported fields.  The default fields are: `id`, `data`, `label`, `<any_meta_data>`
* import data
* annotate the text
* download as zip file


Programmatic method of preparing data and loading with Doccano client.  This also demonstrates grouping individual messages into dialogues.

```python
from doccano_client import DoccanoClient

#create messages data
bodys = ["This is some basic text.",
         "This is some basic text.",
         "This is some basic text.",
         "This is some basic text.",
         ]
dialogues = ["a","a","b","b"]
df = pd.DataFrame({'body':bodys, 'dialogue':dialogues})

#group messages into dialogue records
df_dialogues = df.groupby(by=['dialogue'])['body'].apply(lambda x: ' '.join(x)).reset_index()
jsonl = df_dialogues.to_json(orient='records', lines=True)

#prepare db with client
client = DoccanoClient("http://localhost:8000")
client.login(username='admin', password='password')
client.get_profile()

client.project.create(name="test", project_type="DocumentClassification", description="test")
prj = list(client.list_projects())[0]

#load dialogue records
file_path = './tests/tmp/test.jsonl'
client.upload(
            prj.id,
            file_paths=[file_path],
            task="DocumentClassification",
            format="JSONL",
            column_data="text",
            column_label="labels",
        )

#download ofen has problems, so don't do this
client.download(prj.id, format='JSONL')
```

A good example of the downloaded dialogue data is `./tests/data/export_timestamp.jsonl`.