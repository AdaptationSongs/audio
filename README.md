# audio
Analysis pipeline to automatically process audio recordings collected from the biomeridian monitoring stations.

This software is designed to run on a Hadoop cluster containing the raw audio data. Signal peaks will be identified based on acoustic properties such as spectrographic signature. Signals are then grouped by species and type of vocalization, and stored in a database for further analysis. 

## Useful R packages
* [bioacoustics](https://cran.r-project.org/web/packages/bioacoustics/index.html) - supports various audio formats, automatically extracts acoustic features
* [warbleR](https://cran.r-project.org/web/packages/warbleR/index.html) - higher level analysis of vocal signals, functions to download samples from [Xeno-Canto](http://xeno-canto.org/)
* [monitoR](https://cran.r-project.org/web/packages/monitoR/index.html) - acoustic template detection and monitoring database interface
* [tuneR](https://cran.r-project.org/web/packages/tuneR/index.html) - analyze music and speech, feature extraction, sound file support
* [seewave](http://rug.mnhn.fr/seewave/) - lower level time wave analysis, creates spectrograms
* [Rraven](https://cran.r-project.org/web/packages/Rraven/index.html) - tool to exchange data with Cornell's [Raven](http://www.birds.cornell.edu/brp/raven/RavenOverview.html) software
* [sparklyr](http://spark.rstudio.com/) - Spark interface to run R code in parallel on a Hadoop cluster, interface to [MLlib](https://spark.apache.org/mllib/) scalable machine learning library
* [guano-r](https://github.com/riggsd/guano-r) - reads metadata in the Grand Unified Acoustic Notation Ontology format
