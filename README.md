# Bibliometrics API Script

The [Scopus](https://dev.elsevier.com/) database was accesses using the [pybliometrics](https://pypi.org/project/pybliometrics/) package.\
The [Web of Science](https://apps.webofknowledge.com/) database was accessed using the [wos](https://pypi.org/project/wos/) package.\
The [Dimensions](https://www.dimensions.ai/) database was accessed using the [dimcli](https://pypi.org/project/dimcli/) package.

_This script was used for bibliometric analysis of publications dating to the early days of light-emitting diodes. This data was used to better understand the advancements of light-emitting diode technology. The research project was jointly undertaken by teams of the University of Minnesota, the University of Harvard and the University of Cambridge. It was [funded by the Alfred P. Sloan foundation](https://sloan.org/grant-detail/8567)._

Request throttling per service:

- Web of Science: [**Standard (ETHZ)**](https://developer.clarivate.com/apis/wos#)
- Scopus: [**Subscriber (ETHZ)**](https://dev.elsevier.com/api_key_settings.html)

    "20.000 weekly quota at 9 requests per second"

#### Caveats

- The `scibliometrics` package:
   - The readthedocs.io manual must be manually set to latest` for compatibility with the version privided by pip
   - The `config.ini` file storing the API access key is located at `~/.scopus/config.ini`
- The `DatFrame` split-up script:
   - The index has to be reset with `DataFrame.reset_index()` prior to writing to a feather file.
   - All `DataFrame` commands must include the parameter `inplace=True` to overwrite the object operated on. 
#### Search peculiarities

- The search query "GaN" will yield potentially irrelevant results due to the similarity with the Chinese symbol "干" for "dry". Include only papers from the subject area Physical Sciences.
#### Databases

Downloaded data is stored in the [feather file format](https://blog.rstudio.com/2016/03/29/feather/) for best save and load performance.

DataFrame databases in feather file format are managed with [Git Large File Storage](https://git-lfs.github.com/) (`git-lfs`). [Files are stored on GitHub servers, in a peer of the original repository.](https://stackoverflow.com/questions/32927704/how-to-specify-where-git-lfs-files-will-be-stored)

Manual:
- [Managing large files on GitHub](https://help.github.com/en/github/managing-large-files)
- [`git-lfs` tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial)


Michael Weinold\
University of Cambridge\
2019-2020
