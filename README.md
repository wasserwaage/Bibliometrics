# Bibliometrics API Script

The [Scopus](https://dev.elsevier.com/) database was accesses using the [pybliometrics](https://pypi.org/project/pybliometrics/) package.\
The [Web of Science](https://apps.webofknowledge.com/) database was accessed using the [wos](https://pypi.org/project/wos/) package.\
The [Dimensions](https://www.dimensions.ai/) database was accessed using the [dimcli](https://pypi.org/project/dimcli/) package.

_This script was used for bibliometric analysis of publications dating to the early days of light-emitting diodes. This data was used to better understand the advancements of light-emitting diode technology. The research project was jointly undertaken by teams of the University of Minnesota, the University of Harvard and the University of Cambridge. It was [funded by the Alfred P. Sloan foundation](https://sloan.org/grant-detail/8567)._

#### Caveats

- The scibliometrics package:
   - The readthedocs.io manual must be manually set to latest` for compatibility with the version privided by pip
   - The `config.ini` file storing the API access key is located at `~/.scopus/config.ini`
   
Michael Weinold\
University of Cambridge\
2019-2020
