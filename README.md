This repository contains the replication package of the experiment with title: "The Cost of Ads and Analytics in Mobile Web Apps". 


The dataset connsists information about: (i)Python scripts to remove ads and analytics from the web apps (ii)raw data of the experiment (iii) R scripts used for data analysis (iv)relevant diagrams which aren't included in the paper (iv)\textit{README} file containing guidelines for replicating the experiment.

The following is the information of each folder in this repository:
- *AndroidRunner*: A fork version of Android Runner framework on which we did some customization for running our experiment.
- *Data Analysis*: This folder consists the final CSVs file for both the treatments with 200 repetitions. It also has all the R scripts used for all the phases(data extration, data exploration, normality tests, and hypothesis testing) of  data analysis.
- *Scripts*: It contains all the Python scripts needed to handle the events(before run, before experiment, before close, after launch, after experiment, etc) of the experiment.
- *Experiments*: It contains config files and Python scripts needed to run the experiment.
- *Figures*: It contains all the diagram from data exploration, normality checks, and hypothesis testings.
- *pythonscripts*: It has individual Python scripts to remove ads and analytics from each 10 web apps.
- *interaction*: It is a configuration file for usage scenario for Monkey player
- *run.sh*: It is a shell file to trigger Monkey player
