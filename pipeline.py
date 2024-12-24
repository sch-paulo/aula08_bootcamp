from etl import pipeline_calculate_kpi_of_total_sales_consolidated

file = 'data'
output_format = 'parquet and csv'
pipeline_calculate_kpi_of_total_sales_consolidated(file, output_format)