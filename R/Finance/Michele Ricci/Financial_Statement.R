#library####
library(tidyverse)
library(janitor)

#wrangling####

financial_statement <- read.csv2("Financial_Statement.csv")	%>%     #	use "read.csv2" if sep = ";". If sep = "," use "read.csv" instead 
  janitor::clean_names()  

tiers_df <- separate(data=financial_statement, col='codigo_da_conta', into=c("Tier1", "Tier2", "Tier3", "Tier4", "Tier5"), sep="\\.")

grouped_1 <- dplyr::group_by(tiers_df, `Tier1`)
tier1 <- dplyr::ungroup(dplyr::mutate(grouped_1, `Tier1`=descricao_da_conta[1]))
tier1 <- dplyr::filter(tier1, !is.na(Tier2))

grouped_2 <- dplyr::group_by(tier1, `Tier2`)
tier2 <- dplyr::ungroup(dplyr::mutate(grouped_2, `Tier2`=descricao_da_conta[1]))
tier2 <- dplyr::filter(tier2, !is.na(Tier3))

grouped_3 <- dplyr::group_by(tier2, `Tier3`)
tier3 <- dplyr::ungroup(dplyr::mutate(grouped_3, `Tier3`=descricao_da_conta[1]))
tier3 <- dplyr::filter(tier3, !is.na(Tier4))

grouped_4 <- dplyr::group_by(tier3, `Tier4`)
tier4 <- dplyr::ungroup(dplyr::mutate(grouped_4, `Tier4`=descricao_da_conta[1]))
tier4 <- dplyr::filter(tier4, !is.na(Tier5))

  
