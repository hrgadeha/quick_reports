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
        return [_("Invoice Number") + ":Link/Sales Invoice:100",
                _("Posting Date") + ":Date:150",
		_("Invoice Value") + ":Currency:100",
		_("Place Of Supply") + ":Data:150",
                _("E-Commerce GSTIN") + ":Data:180",
		_("Rate") + ":Float:80",
		_("Taxable Amount") + ":Currency:150"]

def get_data(conditions,filters):
        invoice = frappe.db.sql("""SELECT
    			si.name, si.posting_date, Round(si.rounded_total,2),
    			si.place_of_supply,
	    		si.ecommerce_gstin,
    			sii.gst_percent,
    			Round(sum(sii.net_amount),2)
		FROM
    			`tabSales Invoice` si, `tabSales Invoice Item` sii
		WHERE
			sii.parent = si.name and si.grand_total > 250000 and si.gst_category = "Unregistered" and si.is_opening = "No" 
			and si.docstatus = 1 and si.is_return = 0 %s group by si.name,sii.gst_percent;"""%conditions, filters, as_list=1)
        return invoice

def get_conditions(filters):
	conditions = ""
	if filters.get("company"): conditions += " and si.company = %(company)s"
	if filters.get("from_date"): conditions += " and si.posting_date >= %(from_date)s"
	if filters.get("to_date"): conditions += "and si.posting_date <= %(to_date)s"

	return conditions, filters
