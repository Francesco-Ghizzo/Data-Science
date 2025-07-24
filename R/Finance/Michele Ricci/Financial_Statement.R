##library##
library(tidyverse)
library(janitor)

##wrangling##

financial_statement <- read.csv2("Financial_Statement.csv")	%>%     #	use "read.csv2" if sep = ";". If sep = "," use "read.csv" instead 
  janitor::clean_names()  

tiers_df <- separate(data=financial_statement, col='codigo_da_conta', into=c("Tier1", "Tier2", "Tier3", "Tier4", "Tier5"), sep="\\.")

grouped_1 <- dplyr::group_by(tiers_df, `Tier1`)
tier1 <- dplyr::ungroup(dplyr::mutate(grouped_1, `Tier1`=descricao_da_conta[1]))
column <- select(tier1, `Tier1`)
condition1 <- column == select(tier1, `descricao_da_conta`)
vect <- pull(column)
condition2 <- c()
for(i in 1:(length(vect)-1)) {
     condition2[i] <- (vect[i] == vect[i+1])
}
condition2 <- append(condition2, FALSE)
mask <- !(condition1 & condition2)
tier1 <- dplyr::filter(tier1, mask)

grouped_2 <- dplyr::group_by(tier1, `Tier2`)
tier2 <- dplyr::ungroup(dplyr::mutate(grouped_2, `Tier2`=descricao_da_conta[1]))
column <- select(tier2, `Tier2`)
condition1 <- column == select(tier2, `descricao_da_conta`)
vect <- pull(column)
condition2 <- c()
for(i in 1:(length(vect)-1)) {
  condition2[i] <- (vect[i] == vect[i+1])
}
condition2 <- append(condition2, FALSE)
mask <- !(condition1 & condition2)
tier2 <- dplyr::filter(tier2, mask)

grouped_3 <- dplyr::group_by(tier2, `Tier3`)
tier3 <- dplyr::ungroup(dplyr::mutate(grouped_3, `Tier3`=descricao_da_conta[1]))
column <- select(tier3, `Tier3`)
condition1 <- column == select(tier3, `descricao_da_conta`)
vect <- pull(column)
condition2 <- c()
for(i in 1:(length(vect)-1)) {
  condition2[i] <- (vect[i] == vect[i+1])
}
condition2 <- append(condition2, FALSE)
mask <- !(condition1 & condition2)
tier3 <- dplyr::filter(tier3, mask)

grouped_4 <- dplyr::group_by(tier3, `Tier4`)
tier4 <- dplyr::ungroup(dplyr::mutate(grouped_4, `Tier4`=descricao_da_conta[1]))
column <- select(tier4, `Tier4`)
condition1 <- column == select(tier4, `descricao_da_conta`)
vect <- pull(column)
condition2 <- c()
for(i in 1:(length(vect)-1)) {
  condition2[i] <- (vect[i] == vect[i+1])
}
condition2 <- append(condition2, FALSE)
mask <- !(condition1 & condition2)
tier4 <- dplyr::filter(tier4, mask)

tier5 <- tier4
tier5[['Tier5']] <- tier5[['descricao_da_conta']]
tier5
