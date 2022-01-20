## install ##

# install.packages("tidyverse")
# install.packages("janitor")


## library ##

library(tidyverse)
library(janitor)


## wrangling ##

data_frame = read.csv2("Financial_Statement.csv")							#	use "read.csv2" if sep = ";". If sep = "," use "read.csv" instead 
col_names = janitor::make_clean_names(colnames(data_frame))

  
