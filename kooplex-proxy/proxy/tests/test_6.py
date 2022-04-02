from sqlalchemy.sql import text
from database import engine


req = text("""CREATE OR REPLACE VIEW test_view AS
    WITH tmp_meta1 as (
        SELECT "ena_run", CASE WHEN ("clean_country" = 'USA') THEN ('United States') WHEN NOT("clean_country" = 'USA') 
        THEN ("clean_country") END AS "country_name", "clean_collection_date", "date_isoyear" AS "date_year", 
        "date_isoweek" AS "date_week"
        FROM meta
        WHERE NOT ("clean_collection_date" IS NULL)
        AND "clean_host" = 'Homo sapiens'
        AND "clean_collection_date" > CAST('2020-03-15' AS DATE) 
    )
    , tmp_grouped as (
        SELECT "country_name", "date_year", "date_week", COUNT(*) AS "weekly_sample"
        FROM tmp_meta1
        GROUP BY "country_name", "date_year", "date_week"
    )
    SELECT "LHS"."country_name" AS "country_name", "LHS"."date_year" AS "date_year", "LHS"."date_week" AS "date_week", 
    "LHS"."weekly_sample" AS "weekly_sample", "RHS"."iso_a3" AS "iso_a3", "RHS"."iso_a2" AS "iso_a2", 
    "RHS"."country_name_local" AS "country_name_local", "RHS"."population" AS "population", 
    "RHS"."ecdc_covid_country_weekly_cases" AS "ecdc_covid_country_weekly_cases", 
    "RHS"."ecdc_covid_country_weekly_deaths" AS "ecdc_covid_country_weekly_deaths"
    FROM tmp_grouped as "LHS"
    LEFT JOIN "ecdc_covid_country_weekly" AS "RHS"
    ON ("LHS"."country_name" = "RHS"."country_name" AND "LHS"."date_year" = "RHS"."date_year" AND 
    "LHS"."date_week" = "RHS"."date_week");""")

with engine.connect() as conn:
    conn.execute(req)
    skip = 5
    limit = 10
    outp = conn.execute(f"""SELECT * FROM test_view OFFSET {skip} LIMIT {limit};""").all()
    conn.execute("""DROP VIEW test_view;""")

print(outp)
