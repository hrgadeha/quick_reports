# Copyright (c) 2013, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	conditions, filters = get_conditions(filters)
	columns = get_column()
	data = get_data(conditions,filters)
	return columns,data

def get_column():
	return [_("Lead Owner") + ":Link/User:120",
                _("Lead Owner Name") + ":Data:150",
                _("Status") + ":Data:150",
		_("Source") + ":Link/Lead Source:150",
		_("Total Lead") + ":Int:150",
                _("Lead") + ":Data:150"]

def get_data(conditions,filters):
	summery = frappe.db.sql("""SELECT
	ld.lead_owner as "Lead Owner::190",
	(select full_name from `tabUser` where name = ld.lead_owner) as "Lead Owner Name::150",
	ld.status as "Status::120",
	ld.source as "Source::120",
	count(ld.name) as "Total Lead:Int:120",
	GROUP_CONCAT(ld.name) as "Lead::300"
FROM
	`tabLead` ld
WHERE
	ld.docstatus <2 %s
GROUP BY
    ld.lead_owner, ld.status, ld.source
ORDER BY
	ld.lead_owner asc;"""%conditions, filters, as_list=1)
	return summery

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"): conditions += " and date(ld.creation) >= %(from_date)s"
	if filters.get("to_date"): conditions += " and date(ld.creation) <= %(to_date)s"
	if filters.get("status"): conditions += "and ld.status = %(status)s"
	if filters.get("source"): conditions += "and ld.source = %(source)s"
	if filters.get("lead_owner"): conditions += "and ld.lead_owner = %(lead_owner)s"

	return conditions, filters

