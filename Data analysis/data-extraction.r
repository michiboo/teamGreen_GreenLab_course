library(tidyverse)
library(bayestestR)
#csv paths initiation for both ads and noads in case of performance
ads_csvpaths_performance <- list.files(path = "./data-ads", recursive = TRUE, pattern="^KYVKK.*\\.csv",
                                       full.names = TRUE)
noads_csvpaths_performance <- list.files(path = "./data-noads", recursive = TRUE, pattern="^KYVKK.*\\.csv",
                                         full.names = TRUE)

#csv paths initiation for both ads and noads in case of energy consumption
ads_csvpaths_energyconsumption <- list.files(path = "./data-ads", recursive = TRUE, pattern="^kyvkk.*\\.csv",
                                       full.names = TRUE)
noads_csvpaths_energyconsumption <- list.files(path = "./data-noads", recursive = TRUE, pattern="^kyvkk.*\\.csv",
                                         full.names = TRUE)

length(ads_csvpaths_energyconsumption)
#dataframe creation for both ads and noads data
column_names <- c("Experiment", "Type", "Webapps name", "Browser", "CPU", "Memory", "Energy consumption")
ads_data = data.frame(matrix(nrow = 200, ncol = length(column_names)))
colnames(ads_data) <- column_names
ads_data

noads_data = data.frame(matrix(nrow = 200, ncol = length(column_names)))
colnames(noads_data) <- column_names
noads_data

#types definition for both types
experiment_type_ads <- c(rep("AdsAnalytics", length(ads_csvpaths_performance)))
experiment_type_ads

experiment_type_noads <- c(rep("WithoutAdsAnalytics", length(noads_csvpaths_performance)))
experiment_type_noads


#webapps name and browser name extraction from ads-analytics type
eachfilepath_array <- ads_csvpaths_performance %>%
  strsplit("/", fixed=TRUE)
webapps <- eachfilepath_array %>%
  rapply(nth, n=8)
webapps
browser <- eachfilepath_array %>%
  rapply(nth, n=9)
browser


#experiment count variable definition
no_experiment <- 1:10
no_experiment <- c(rep(no_experiment, 20))
no_experiment

#function to calculate average value of each csv file
calculate_average <- function(csv_data, type){
  cpuavg<-''
  memavg<-''
  data <- 0
  performance_list <- ''
  energy_consumption <- ''
  for(i in 1:length(csv_data)){
    data <- read.csv(csv_data[i], stringsAsFactors=F) 
    if (type == 'performance'){
      cpuavg[i] <- mean(as.numeric(data$cpu), rm.NA=T)
      memavg[i] <- mean(as.numeric(data$mem), rm.NA=T)
      # cpu_value <- as.numeric(data$cpu)
      # ifelse(cpu_value < 0, print(csv_data[i]), 0)
    }else{
      colnames(data)[1] <- "Time"
      colnames(data)[2] <- "Power"
      colnames(data)[3] <- "Power_Delta"
      data <- data %>% filter(!is.na(Time))
      time <- as.numeric(data$Time)
      power <- as.numeric(data$Power)
      ifelse(is.na(power), print(csv_data[i]), tail(data, n=5))
      energy_consumption[i] <- as.numeric(auc(time, power))/1000000000
    }
  }
  if (type == 'performance'){
    performance_list <- list("cpu"=cpuavg, "mem"=memavg)
    return(performance_list)
  }else{
    return(energy_consumption)
  }
}

#function call to get mean value of performance for both types
performance_data_ads <- calculate_average(ads_csvpaths_performance, "performance")
performance_data_ads
performance_data_noads <- calculate_average(noads_csvpaths_performance, "performance")
performance_data_noads

#function call to get  energy consumption of both types
energy_data_ads <- calculate_average(ads_csvpaths_energyconsumption, "energy")
energy_data_ads
energy_data_noads <- calculate_average(noads_csvpaths_energyconsumption, "energy")
energy_data_noads


#pouplating ads type table
ads_data['Experiment'] <- no_experiment
ads_data['Type'] <- experiment_type_ads
ads_data['Webapps name'] <- webapps
ads_data['Browser'] <- browser
ads_data['CPU'] <- performance_data_ads$cpu
ads_data['Memory'] <- performance_data_ads$mem
ads_data['Energy consumption'] <- energy_data_ads




#populting noads type table
noads_data['Experiment'] <- no_experiment
noads_data['Type'] <- experiment_type_noads
noads_data['Webapps name'] <- webapps
noads_data['Browser'] <- browser
noads_data['CPU'] <- performance_data_noads$cpu
noads_data['Memory'] <- performance_data_noads$mem
noads_data['Energy consumption'] <- energy_data_noads


#ads data to csv file
write.csv(ads_data, "data_ads_analytics.csv", row.names = FALSE)

#nonads data to csv file
write.csv(noads_data, "data_without_ads_analytics.csv", row.names = FALSE)


# data <- 0
# energy_consumption <- ''
# for(i in 1:length(noads_csvpaths_energyconsumption)){
#   data <- read.csv(noads_csvpaths_energyconsumption[i], stringsAsFactors=F)
#   colnames(data)[1] <- "Time"
#   colnames(data)[2] <- "Power"
#   colnames(data)[3] <- "Power_Delta"
#   data <- data %>% filter(!is.na(Time))
#   time <- as.numeric(data$Time)
#   power <- as.numeric(data$Power)
#   ifelse(is.na(power), print(noads_csvpaths_energyconsumption[i]), tail(data, n=5))
#   energy_consumption[i] <- as.numeric(auc(time, power))/1000000000
# }
# energy_consumption
