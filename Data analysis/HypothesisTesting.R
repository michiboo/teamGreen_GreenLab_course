library(tidyverse)
library(effsize)

#Data Loading

#csv file with ads data
ads <- read.csv("/Users/ehmad/Downloads/data_ads_analytics.csv")

#csv file with ads data
noads <- read.csv("/Users/ehmad/Downloads/data_without_ads_analytics.csv")


#Alpha = 0.05

#Wilcoxon Signed Rank Test

#energy
wilcox.test(noads$Energy.consumption, ads$Energy.consumption, alternative="less", paired = TRUE)
cliff.delta(noads$Energy.consumption, ads$Energy.consumption)

#cpu
wilcox.test(noads$CPU, ads$CPU, alternative="less", paired = TRUE)
cliff.delta(noads$CPU, ads$CPU)

#memory
wilcox.test(noads$Memory, ads$Memory, alternative="less", paired = TRUE)
cliff.delta(noads$Memory, ads$Memory)


