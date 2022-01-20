#library####
library(tidyverse)
library(ggpubr)

#wrangling####


read.csv2("Dati_Francesco_G.csv" ) %>% 
  `colnames<-`(janitor::make_clean_names(colnames(.))) %>%
  separate(i_ca3digo_da_conta, c("X1", "X2", "X3", "X4", "X5"),
           sep = "\\.") %>% group_by(`X1`) %>%
  do(mutate(., `X1` = descri_a_a_o_da_conta[1])) %>%
  ungroup() %>% filter(!is.na(`X2`)) %>% droplevels() %>%
  group_by(`X2`) %>% 
  do(mutate(., `X2` = descri_a_a_o_da_conta[1])) %>%
  ungroup() %>% filter(!is.na(`X3`)) %>% droplevels() %>%
  group_by(`X3`) %>% 
  do(mutate(., `X3` = descri_a_a_o_da_conta[1])) %>%
  ungroup() %>% group_by(`X4`) %>%
  do(mutate(., `X4` = ifelse(is.na(`X4`), NA ,descri_a_a_o_da_conta[1]))) %>%
  ungroup() %>% 
  filter(is.na(`X4`) | `X4` != descri_a_a_o_da_conta) %>%
  ungroup() %>% 
  mutate(`X5` = ifelse(is.na(`X5`), NA, descri_a_a_o_da_conta),
         descri_a_a_o_da_conta = NULL,
         trimestre_atual = as.numeric(trimestre_atual),
         exerc_a_cio_anterior = as.numeric(exerc_a_cio_anterior),
         `X4` = ifelse(is.na(`X4`), `X3`, `X4`),
         `X5` = ifelse(is.na(`X5`), `X4`, `X5`)) %>%
  #arrange(`X2`) %>% edit()
  #write.csv("results.csv)
  ggbarplot(x = "X3", y = "trimestre_atual", facet.by = "X2",
            orientation = "horizontal",
            fill = "X4", position = position_stack()) +
  theme_minimal() + grids() +
  theme(axis.text.x = element_text(color = "black", angle = 90,
                                   vjust = 0.5))

  
