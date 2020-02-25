# Pdf4me.Client - the python package for the Pdf4me Saas API


![PyPI](https://img.shields.io/pypi/v/pdf4me.svg) ![license](https://img.shields.io/github/license/mashape/apistatus.svg) ![Maintenance](https://img.shields.io/maintenance/yes/2018.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdf4me.svg) ![PyPI - Status](https://img.shields.io/pypi/status/pdf4me.svg)

We have integrated our unittests into the build process.
 > python 2.7: ![Build](https://ynoox.visualstudio.com/_apis/public/build/definitions/2e29c2f0-3f4a-40e1-a4b1-1cc465571206/312/badge)
 > python 3.6: ![Build](https://ynoox.visualstudio.com/_apis/public/build/definitions/2e29c2f0-3f4a-40e1-a4b1-1cc465571206/290/badge)


The [Pdf4me Client API](https://developer.pdf4me.com/) is a python package which connects to its highly scalable SaaS cloud service with many functionalities to solve your document and PDF requirements. The SaaS API provides expert functionality to convert, optimize, compress, produce, merge, split, ocr, enrich,  archive, rotate, protect, validate, repair, print documents and PDF's.

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

The Token is required for Basic Authentication. The Pdf4me Client Api provides you already with the necessary implementation. You need only to get an instance for the Pdf4meClient as shown in the sample below.

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

## Contribution

Contributions are very welcome. Please have a look at the instructions below for a smooth project setup.

1. Fork pdf4me
2. Clone your copy of pdf4me
3. Setup the project interpreter of your choice. In PyCharm it is done the following way:
 > - Click on File -> Settings... -> 
 > - Navigate to: Project: pdf4me-clientApi-python -> Project Interpreter
 > - Click on the settings symbol in the upper right corner, choose: *'Show All...'*
 > - Hit the '+' symbol to add a new interpreter: add a new Virtualenv Environment. It allows you to install all dependencies locally in the project, instead of installing them globally.
 > - Create a new environment: 
        - `Location`: the path to the pdf4me-clientApi-python/env folder, env is a new folder where the environment will be stored in.
        - `Base Interperter`: the path to your python.exe file, e.g., in case you have Anaconda installed, it is found in the top level folder of the Anaconda installation.
 > - Once you have added the new interpreter, click on the '+' sign to install all necessary dependencies. You find them in the [setup.py](https://github.com/pdf4me/pdf4me-clientapi-python/blob/master/pdf4me/Pdf4mePythonClientApi/setup.py) below the keyword: `install_requires`. On top of that, the following two dependencies are needed for testing: `nose` & `pytest`. 
4. Add the two project folders: *Pdf4mePythonClientApi* and *Pdf4mePythonClientApiTest* to the python path. 
In PyCharm they must be added to the project interpreter:
> - Click on the settings symbol in the upper right corner, choose: *'Show All...'* and select the newly defined project interpreter. Then click on *'Show paths for the selected interpreter'*, the symbol displayed on the bottom of right taskbar. Hit the '+' symbol to add the paths to the *Pdf4mePythonClientApi* and *Pdf4mePythonClientApiTest* folders.
5. You are ready to go

#### Running the Test Cases
In order for the test cases to run, a config.properties file containing the token must be stored in the [pdf4me\Pdf4mePythonClientApiTest](https://github.com/pdf4me/pdf4me-clientapi-python/tree/master/pdf4me/Pdf4mePythonClientApiTest) folder. Please drop us an [email](mailto:support-dev@pdf4me.com), so we can provide you the developer a token for testing the code of your pull request.
The test cases are available in [pdf4me\Pdf4mePythonClientApiTest\unittests](https://github.com/pdf4me/pdf4me-clientapi-python/tree/master/pdf4me/Pdf4mePythonClientApiTest/unittests).

#### PDF4me Consumer
Those who are looking for PDF4me online tool can find it at [PDF4me.com](https://pdf4me.com/)
