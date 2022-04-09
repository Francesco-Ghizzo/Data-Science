## install ##

# install.packages("tidyverse")


## library ##

library(tidyverse)


## wrangling ##

data_frame = read.csv2("Financial_Statement.csv")							#	use "read.csv2" if sep = ";". If sep = "," use "read.csv" instead 
# col_names = janitor::make_clean_names(colnames(data_frame))
separate(data_frame, Código.da.Conta, into=c("Tier1", "Tier2", "Tier3", "Tier4", "Tier5"))
