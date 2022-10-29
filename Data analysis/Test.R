library(tidyverse)

webapps_data <- read.csv("/Users/ehmad/Downloads/data_ads_analytics.csv")

tail(webapps_data)

webapps_data [c('CPU','Memory')]
webapps_data$Webapps_name

webapps_data[3:7, c('CPU')]

summary(webapps_data)


lapply(webapps_data, is.numeric)

num_cols <- colnames(webapps_data)[unlist(lapply(webapps_data, is.numeric))]

num_cols

hist(webapps_data$CPU, main='Distribution of CPU')

data <- webapps_data [c('CPU','Memory', 'Energy')]

col_names <- colnames(data)

check_normality <- function(data){
  par(mfrow=c(1,2))
  mapply(hist, data, main=paste('Distribution of',col_names), xlab=col_names)
}

library(dplyr)

transformed_data <- data %>%
  mutate(CPU_log = log(CPU),
         CPU_sqrt = sqrt(CPU),
         CPU_reciprocal = 1/CPU,
         Memory_log = log(Memory),
         Memory_sqrt = sqrt(Memory),
         Memory_reciprocal = 1/Memory,
         Energy_log = log(Energy),
         Enery_sqrt = sqrt(Energy),
         Energy_reciprocal = 1/Energy)

transformed_data

col_names <- colnames(transformed_data)

check_normality_of_tranformed_data <- function(transformed_data){
  #Histogram
  par(mfrow=c(3,4))
  mapply(hist, transformed_data, main=paste('Distribution of',col_names), xlab=col_names)
}

library(car)

check_normality_of_tranformed_data <- function(transformed_data){
  #QQPlot
  par(mfrow=c(3,4))
  mapply(car::qqPlot, transformed_data, main=paste('QQ Plot of',col_names), xlab=col_names)
}

library(ggplot2)

check_normality_by_densityplot <- function(test){
  #DensityPlot
  #par(mfrow=c(2,4))
  mapply(ggplot, test)
}

transformed_data %>%
  check_normality_by_densityplot



