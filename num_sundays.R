library(lubridate)
days <- seq(ymd("1901-01-01"), ymd("2000-12-31"), by="days")
sum(day(days)==1 & wday(days)==1)