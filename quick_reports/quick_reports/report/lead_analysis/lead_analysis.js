// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Lead Analysis"] = {
	"filters": [
		{
        	    "fieldname": "from_date",
       		    "label": __("From Date"),
        	    "fieldtype": "Date",
		    "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1)
        	},
		{
        	    "fieldname": "to_date",
        	    "label": __("To Date"),
        	    "fieldtype": "Date",
		    "default": frappe.datetime.get_today()
        	},
		{
                    "fieldname": "status",
                    "label": __("Status"),
                    "fieldtype": "Select",
                    "options": "\nLead\nOpen\nReplied\nOpportunity\nQuotation\nLost Quotation\nInterested\nConverted\nDo Not Contact",
                },
		{
                    "fieldname": "source",
                    "label": __("Source"),
                    "fieldtype": "Link",
                    "options": "Lead Source",
                },
		{
        	    "fieldname": "lead_owner",
       		    "label": __("Lead Owner"),
        	    "fieldtype": "Link",
		    "options": "User",
        	}
	]
};
