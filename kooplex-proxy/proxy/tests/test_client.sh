#!/bin/bash

echo "\n1---------------------------------------------------\n"
curl http://localhost:8080/

echo "\n\n2---------------------------------------------------\n"
echo 'country_samples ->'
curl http://localhost:8080/country_samples/

echo "\n\n3---------------------------------------------------\n"
echo 'human_meta_mv ->'
curl http://localhost:8080/human_meta_mv/

echo "\n\n4---------------------------------------------------\n"
echo 'human_meta_mv_jhd ->'
curl http://localhost:8080/human_meta_mv_jhd/

echo "\n\n5---------------------------------------------------\n"
echo 'lineage_def ->'
curl http://localhost:8080/lineage_def/

echo "\n\n6---------------------------------------------------\n"
echo 'lineage ->'
curl http://localhost:8080/lineage/

echo "\n\n7---------------------------------------------------\n"
echo 'new_cases_jhd ->'
curl http://localhost:8080/new_cases_jhd/

echo "\n\n8---------------------------------------------------\n"
echo 'variants_weekly ->'
curl http://localhost:8080/variants_weekly/

echo "\n\n9---------------------------------------------------\n"
echo 'unique_ena_run_sum ->'
curl http://localhost:8080/unique_ena_run_sum/

echo "\n\n10---------------------------------------------------\n"
echo 'filter_custom_browser_cov ->'
curl "http://localhost:8080/filter_custom_browser_cov/?included=p.Asp80Ala%2Cp.Asp215Gly&excluded=p.Asp77Al%2Cp.Asp102Ala"

echo "\n\n11---------------------------------------------------\n"
echo 'filter_custom_browser_cov_time ->'
curl "http://localhost:8080/filter_custom_browser_cov_time/?included=p.Asp80Ala%2Cp.Asp215Gly&excluded=p.Asp77Al%2Cp.Asp102Ala"
echo "\n\n-----------------------------------------------------\n"
