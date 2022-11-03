library(tidyverse)
library(car)
library(dplyr)
library(ggplot2)
library(gridExtra)

#reading data
ads_data = read.csv('../data_ads_analytics.csv')
noads_data = read.csv('../data_without_ads_analytics.csv')

both_ads_noads_data = read.csv('../both_data_ads_analytics.csv')


ads_data  = ads_data %>% 
  mutate_at(c("Experiment", "Type", "Webapps.name", "Browser"), as.factor)
noads_data  = noads_data %>% 
  mutate_at(c("Experiment", "Type", "Webapps.name", "Browser"), as.factor)

#getting numeric column names
num_cols <- colnames(ads_data)[unlist(lapply(ads_data, is.numeric))]
num_cols
ads_data
ads_data[num_cols]
noads_data[num_cols]


#Descriptive statistics
summary(ads_data)
sd(ads_data$CPU)
sd(ads_data$Memory)
sd(ads_data$Energy.consumption)

summary(noads_data)
sd(noads_data$CPU)
sd(noads_data$Memory)
sd(noads_data$Energy.consumption)

#plotting boxplots
#ggplot(noads_data, aes(x=Type,y=Energy.consumption)) +
#geom_boxplot(outlier.size = 0.5) + stat_summary(fun=mean, color='black', shape=5, size=1.5)
cpu_box <- ggplot(both_ads_noads_data, aes(x = Type, y=CPU, group=Type)) + 
  geom_boxplot(outlier.size = 1, width=0.5) + ylab("CPU (%)") + ggtitle("CPU (%), With or without ads and analytics") + theme(plot.title = element_text(size=13, hjust = 0.3, face = "bold"))
cpu_box <- cpu_box + stat_summary(fun=mean, geom="point", shape=10, size=4) + theme(text = element_text(size = 13)) + scale_x_discrete(labels=c("With", "Without")) + labs(x = "")

memory_box <- ggplot(both_ads_noads_data, aes(x = Type, y=Memory, group=Type)) + 
  geom_boxplot(outlier.size = 1, width=0.5) + ylab("Memory(KB)") + ggtitle("Memory(KB), With or without ads and analytics") + theme(plot.title = element_text(size=13, hjust = 0.3, face = "bold"))
memory_box <- memory_box + stat_summary(fun=mean, geom="point", shape=10, size=4) + theme(text = element_text(size = 13)) + scale_x_discrete(labels=c("With", "Without")) + labs(x = "")

energy_box <- ggplot(both_ads_noads_data, aes(x = Type, y=Energy, group=Type)) + 
  geom_boxplot(outlier.size = 1, width=0.5) + ylab("Energy(J)") + ggtitle("Energy(J), With or without ads and analytics") + theme(plot.title = element_text(size=13, hjust = 0.3, face = "bold"))
energy_box <- energy_box + stat_summary(fun=mean, geom="point", shape=10, size=4) + theme(text = element_text(size = 13)) + scale_x_discrete(labels=c("With", "Without")) + labs(x = "")

grid.arrange(cpu_box, memory_box, energy_box, ncol=2)


#Transformation using log, square, and reciprocal
data_transformation <- function(data){
  transformed_data <- data %>%
    mutate(CPU_log = log(CPU),
           CPU_sqrt = sqrt(CPU),
           CPU_reciprocal = 1/CPU,
           Memory_log = log(Memory),
           Memory_sqrt = sqrt(Memory),
           Memory_reciprocal = 1/Memory,
           Energy_log = log(Energy.consumption),
           Energy_sqrt = sqrt(Energy.consumption),
           Energy_reciprocal = 1/Energy.consumption)
  return(transformed_data)
}

#columns for transformed data
columns_transformeddata <- c('CPU_log', 'CPU_sqrt', 'CPU_reciprocal','Memory_log', 'Memory_sqrt',
                             'Memory_reciprocal',  'Energy_log', 'Energy_sqrt', 'Energy_reciprocal')

#transformed data for both with and without ads and analytics
transformed_adsata <- data_transformation(ads_data) %>% 
  mutate_at(columns_transformeddata, as.numeric)
transformed_adsata

transformed_noadsdata <- data_transformation(noads_data) %>% 
  mutate_at(columns_transformeddata, as.numeric)
transformed_noadsdata


#density plots for both with/without ads and analytics
par(mfrow=c(3,2))
plot(density(transformed_adsata$CPU), 
     xlab="CPU(%)", ylim=c(0, 0.07), col="red", main="Density plot for CPU(%) usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$CPU), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Memory), 
     xlab="Memory(KB)", ylim=c(0, 0.000007),col="red", main="Density plot for Memory usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Memory), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Energy.consumption), 
     xlab="Energy(J)", ylim=c(0, 0.04),col="red", main="Density plot for Energy consumption", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Energy.consumption), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)

plot(density(transformed_adsata$CPU_log), 
     xlab="log(CPU)", ylim=c(0, 2.2), col="red", main="Density plot for log(CPU) usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$CPU_log), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$CPU_sqrt), 
     xlab="sqrt(CPU)", ylim=c(0, 0.8), col="red", main="Density plot for sqrt(CPU) usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$CPU_sqrt), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$CPU_reciprocal), 
     xlab="1/CPU", ylim=c(0, 38), col="red", main="Density plot for 1/CPU usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$CPU_reciprocal), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Energy_log), 
     xlab="log(Energy)", ylim=c(0, 2.9), col="red", main="Density plot for log(Energy) consumption", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Energy_log), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Energy_sqrt), 
     xlab="sqrt(Energy)", ylim=c(0, 0.7), col="red", main="Density plot for sqrt(Energy) consumption", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Energy_sqrt), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Energy_reciprocal), 
     xlab="1/Energy", ylim=c(0, 250), col="red", main="Density plot for 1/Energy consumption", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Energy_reciprocal), col="green")
legend("topleft", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Memory_log), 
     xlab="log(Memory)", ylim=c(0, 9), col="red", main="Density plot for log(Memory) usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Memory_log), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Memory_sqrt), 
     xlab="sqrt(Memory)", ylim=c(0, 0.017), col="red", main="Density plot for sqrt(Memory) usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Memory_sqrt), col="green")
legend("topright", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)
plot(density(transformed_adsata$Memory_reciprocal), 
     xlab="1/Memory", ylim=c(0e+00, 11e+06), col="red", main="Density plot for 1/Memory usage", 
     cex.main=1.5, cex.lab=1.2, cex.axis=1.0)
lines(density(transformed_noadsdata$Memory_reciprocal), col="green")
legend("topleft", c("With ads and analytics", "Without ads and analytics"),
       fill=c("red","green"), cex=1.0)




#normality check function
check_normality <- function(data, axis_text, variable){
  #par(mfrow=c(2,1))
  # plot(density(data), 
  #      xlab=axis_text, col="blue", 
  #      main=paste("Density plot of", variable),
  #      cex.main=1.3, cex.lab=1.5, cex.axis=1.2)
  car::qqPlot(data, main=paste('Q-Q plot of',variable), ylab=axis_text)
  print(shapiro.test(data))
}


#Normality check for ads and analytics along with its transformation
par(mfrow=c(4,2))
check_normality(transformed_adsata$CPU , "CPU(%)", "CPU(%) with ads and analytics")
check_normality(transformed_adsata$Memory , "Memory(KB)", "Memory(KB) with ads and analytics")
check_normality(transformed_adsata$Energy.consumption , "Energy(J)", "Energy(J) with ads and analytics")
check_normality(transformed_adsata$CPU_log , "log(CPU) transformation", "log(CPU) transformation with ads and analytics")
check_normality(transformed_adsata$CPU_sqrt , "Sqrt(CPU) transformation", "Sqrt(CPU) transformation with ads and analytics")
check_normality(transformed_adsata$CPU_reciprocal , "1/CPU transformation", "1/CPU transformation with ads and analytics")
check_normality(transformed_adsata$Memory_log , "log(Memory) transformation", "log(Memory) transformation with ads and analytics")
check_normality(transformed_adsata$Memory_sqrt , "Sqrt(Memory) transformation", "Sqrt(Memory) transformation with ads and analytics")
check_normality(transformed_adsata$Memory_reciprocal , "1/Memory transformation", "1/Memory transformation with ads and analytics")
check_normality(transformed_adsata$Energy_log , "log(Energy) transformation", "log(Energy) transformation with ads and analytics")
check_normality(transformed_adsata$Energy_sqrt , "Sqrt(Energy) transformation", "Sqrt(Energy) transformation with ads and analytics")
check_normality(transformed_adsata$Energy_reciprocal , "1/Energy transformation", "1/Energy transformation with ads and analytics")


#Normality check for without ads and analytics along with its transformation
par(mfrow=c(6,2))
check_normality(transformed_noadsdata$CPU , "CPU(%)", "CPU(%) without ads and analytics")
check_normality(transformed_noadsdata$Memory , "Memory(KB)", "Memory(KB) without ads and analytics")
check_normality(transformed_noadsdata$Energy.consumption , "Energy(J)", "Energy(J) without ads and analytics")
check_normality(transformed_noadsdata$CPU_log , "log(CPU) transformation", "log(CPU) transformation without ads and analytics")
check_normality(transformed_noadsdata$CPU_sqrt , "Sqrt(CPU) transformation", "Sqrt(CPU) transformation without ads and analytics")
check_normality(transformed_noadsdata$CPU_reciprocal , "1/CPU transformation", "1/CPU transformation without ads and analytics")
check_normality(transformed_noadsdata$Memory_log , "log(Memory) transformation", "log(Memory) transformation without ads and analytics")
check_normality(transformed_noadsdata$Memory_sqrt , "Sqrt(Memory) transformation", "Sqrt(Memory) transformation without ads and analytics")
check_normality(transformed_noadsdata$Memory_reciprocal , "1/Memory transformation", "1/Memory transformation without ads and analytics")
check_normality(transformed_noadsdata$Energy_log , "log(Energy) transformation", "log(Energy) transformation without ads and analytics")
check_normality(transformed_noadsdata$Energy_sqrt , "Sqrt(Energy) transformation", "Sqrt(Energy) transformation without ads and analytics")
check_normality(transformed_noadsdata$Energy_reciprocal , "1/Energy transformation", "1/Energy transformation without ads and analytics")


