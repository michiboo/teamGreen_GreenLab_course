library(tidyverse)

both_ads_analytics_data <- read.csv("/Users/ehmad/Downloads/both_data_ads_analytics.csv")

par(mfrow=c(1,1))

boundaries <- boxplot((CPU~Type+Webapp),
                      data = both_ads_analytics_data,
                      ylim=c(0,100),
                      #varwidth=TRUE,
                      #horizontal=TRUE,
                      #notch=TRUE,
                      #las=2,
                      xlab="CPU usage by each web app due to ads and analytics",
                      ylab="CPU usage (%)",
                      col=(c("indianred1","turquoise")),
                      at = c(0:1, 3:4, 6:7, 9:10, 12:13, 15:16, 18:19, 21:22, 24:25, 27:28),
                      names= c("With", "Without","With", "Without","With", "Without","With", "Without","With", "Without","With", "Without","With", "Without","With", "Without","With", "Without","With", "Without"))

grid(nx = 10, ny = 0, col = "lightgray", lty = "dotted")

names <- c("accuweather", "bbc", "cnblogs", "imdb", "investing", "livejournal", "mirror-co-uk", "psychologytoday", "science-org", "speedtest-net")

text(
  x= c(0, 3, 6, 9.2, 12.5, 15.5, 18.6, 21.8, 24.8, 27.8),
  y= 95,
  paste(names, sep="  ")  
)

# Add a legend
legend("topleft", legend = c("With","Without") , 
       col = c("indianred1" , "turquoise") , bty = "n", pch=20 , pt.cex = 3, cex = 1, horiz = FALSE, inset = c(0, 0.1))

