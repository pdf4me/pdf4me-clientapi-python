The Pdf4me Client API is a python package which connects to its highly scalable SaaS cloud service with many functionalities to solve your document and PDF requirements. The SaaS API provides expert functionality to convert, optimize, compress, produce, merge, split, ocr, enrich, archive, print documents and PDF's.

Feature | Description 
------------ | ------------- 
**Optimize** | PDF's can often be optimized by removing structural redundancy. This leads to much smaller PDF's.
**Merge** | Multiple PDF's can be merged into single optimized PDFs.
**Split** | A PDF can be splitted into multiple PDF's.
**Extract** | From a PDF extract multiple pages into a new document.
**Images** | Extract images from your document, can be any type of document.
**Create Pdf/A** | Create a archive conform PDF/A including xmp Metadata.
**Convert to PDF** | Convert your documents from any format to a proper PDF document.
**Stamp** | Stamp your document with text or images.
**Rotate** | Rotates pages in your document.
**Protect** | Protects or Unlocks your document with given password.
**Validation** | Validate your document for PDF/A compliance.
**Repair** | Repairs your document.

## Getting Started

To get started get a Token by dropping us an [email](mailto:support-dev@pdf4me.com) or registering in our [portal](https://portal.pdf4me.com/).

The Token is required for Authentication. The Pdf4me Client Api provides you already with the necessary implementation. You need only to get an instance for the Pdf4meClient as shown in the sample below.

```python
"""
Either you store them in the config.properties file with token 
Do not use any quotes:
Correct: token=sample-not-working-key-aaaaaaa
Incorrect: token="sample-not-working-key-aaaaaaa"

In case the location of your config.properties differs from the default location ('../config.properties'), provide the optional argument path_to_config_file.

"""
pdf4me_client = Pdf4meClient(path_to_config_file='path_to_my_config.properties')

""" or you pass them as arguments when constructing the Pdf4meClient object """
pdf4me_client = Pdf4meClient(token=token)

# The pdf4meClient object delivers the necessary authentication when instantiating the different pdf4meClients such as for instance Merge
merge_client = MergeClient(pdf4me_client)
merged_pdf = merge_client.merge_2_pdfs(
    file1=FileReader().get_file_handler(path='my_first_pdf.pdf'),
    file2=FileReader().get_file_handler(path='my_second_pdf.pdf')
)
```

## Documentation

Please visit our [documentation](https://developer.pdf4me.com/docs/api/) for more information about all the functionalities provided and on how to use pdf4me.

## Recommendation

It's recommended to create an instance of `Pdf4meClient` per thread in a multithreaded environment to avoid any potential issues.