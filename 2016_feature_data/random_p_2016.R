library(lubridate)
library(dplyr)
library(plyr)
library(xts)
setwd("/Users/rita/Google Drive/Archipelagos/Dolphins_prediction/Data_2016")
points_2016= read.csv("/Users/rita/Google Drive/Archipelagos/Dolphins_prediction/Data_2016/alldata2016.csv")
date16<-points_2016$Date
date16<-ymd(as.matrix(date16))
track16<- read.csv("/Users/rita/Google Drive/Archipelagos/Dolphins_prediction/Data_2016/track16_from_Archipelagos.csv")

track16= track16 %>%
  select(NS1.Time,Latitude,Longitude)%>%
  mutate(Date=NS1.Time, Point_Y=Latitude, Point_X=Longitude)%>%
  select(Date, Point_X, Point_Y)

# get track16 supplied data from "GPS WAYPOINTS UTD06.12.2016.csv" from Archipelagos

track16_s<- read.csv("/Users/rita/Google Drive/Archipelagos/Dolphins_prediction/Data_2016/absence_supply.csv")
track16<- rbind(track16_s,track16)

track16$Point_X= gsub(",",".",track16$Point_X)
track16$Point_Y= gsub(",",".",track16$Point_Y)
date_t_16<- track16$Date
date_t_16<- as.character(date_t_16)
date_t_16<- gsub("(.*?)T.*","\\1",date_t_16)
date_t_16<- as.Date(date_t_16)
track16$Date <- date_t_16
set.seed(456)
number=nrow(count(date16))
sample_list<- vector("list",length=number)
names(sample_list)<- paste0("sample",seq_len(number))
for (i in 1:number){
  time_list<- as.matrix(count(date16)[1])
  dates= as.Date(time_list[i])
  sample_base<- track16[date_t_16 == dates,]
  if (nrow(sample_base)>0){
    times<- as.matrix(count(date16)[2])[i]
    sample_list[[i]]<-sample_base[sample(nrow(sample_base),times),]
  }
}
sample_list
sampledf<- do.call("rbind", lapply(sample_list, as.data.frame)) 
sampledf$P_A <- 0
absencedata<- xts(x=sampledf[,-1],order.by=as.POSIXct(sampledf$Date))

absencedata<- as.data.frame(absencedata)
write.csv(absencedata, file = "/Users/rita/Google Drive/Archipelagos/Dolphins_prediction/Data_2016/absence_2016_test.csv",row.names = TRUE)
