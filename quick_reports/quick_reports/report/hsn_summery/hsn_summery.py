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
        return [_("GST/HSN") + ":Data:100",
                _("Description") + ":Data:150",
		_("Stock Qty") + ":Float:100",
		_("Stock UOM") + ":Data:100",
                _("Total Taxable Amount") + ":Currency:180",
		_("Tax Rate") + ":Float:80",
		_("IGST") + ":Currency:150",
		_("CGST") + ":Currency:150",
		_("SGST") + ":Currency:150"]

def get_data(conditions,filters):
        invoice = frappe.db.sql("""SELECT
				sii.gst_hsn_code,(select description from `tabGST HSN Code` where hsn_code = sii.gst_hsn_code),
				sum(sii.stock_qty),sii.stock_uom,
				ROUND(sum(sii.net_amount),2),sii.gst_percent,
    			IF(si.tax_category like "Out State", ROUND((ROUND(sum(sii.net_amount),2) * sii.gst_percent / 100),2), 0),
    			IF(si.tax_category like "In State", ROUND(ROUND(sum(sii.net_amount),2) * (sii.gst_percent / 2) / 100,2), 0),
    			IF(si.tax_category like "In State", ROUND(ROUND(sum(sii.net_amount),2) * (sii.gst_percent / 2) / 100,2), 0)
		FROM
    			`tabSales Invoice` si, `tabSales Invoice Item` sii
		WHERE
			sii.parent = si.name and si.is_opening = "No" and si.docstatus = 1 %s 
			group by sii.gst_hsn_code, sii.item_tax_template order by sii.gst_percent;"""%conditions, filters, as_list=1)
        return invoice

def get_conditions(filters):
	conditions = ""
	if filters.get("company"): conditions += " and si.company = %(company)s"
	if filters.get("from_date"): conditions += " and si.posting_date >= %(from_date)s"
	if filters.get("to_date"): conditions += "and posting_date <= %(to_date)s"

	return conditions, filters
