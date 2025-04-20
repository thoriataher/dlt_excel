import dlt 
from dlt_resources.excel_reader import excel_rows

pipeline = dlt.pipeline(
    pipeline_name="excel_pipeline",
    destination="filesystem",
    dataset_name="excel_data"
)

load_info = pipeline.run(excel_rows("./data/extractPivotReportSnowflake_20250411030708.xlsx"))
print(load_info)

print("Loaded Data Preview:")
for row in load_info:
    print(row)
    break 

