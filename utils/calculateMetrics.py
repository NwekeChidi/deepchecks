from models.log_alerts import LogAlertsModel
from datetime import datetime

def calculate_metrics(llm_log, threshold, input_condition, output_condition):
  condition_map = {
    "gt": lambda x: x > threshold,
    "ge": lambda x: x >= threshold,
    "eq": lambda x: x == threshold,
    "lt": lambda x: x < threshold,
    "le": lambda x: x <= threshold
  }

  condition_alert = {
    "gt": " too short",
    "ge": " too short",
    "eq": " does not meet threshold",
    "lt": " too long",
    "le": " too long"
  }

  schema_keys = ["id", "input", "output", "alert", "timestamp"]

  alert = ""
  if condition_map[input_condition](len(llm_log[1])): alert += "input is OK"
  else: alert += "input is" + condition_alert[input_condition]

  if condition_map[output_condition](len(llm_log[2])): alert += ", output is OK"
  else: alert += ", output is" + condition_alert[output_condition]

  llm_log.append(alert); llm_log.append(datetime.now())
  return LogAlertsModel(**dict(zip(schema_keys, llm_log)))


