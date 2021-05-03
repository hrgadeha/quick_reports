from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
                        "label": _("Account"),
                        "items": [
                                {
                                        "type": "report",
					"is_query_report": True,
                                        "name": "General Ledger",
                                        "doctype": "GL Entry"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Accounts Receivable",
                                        "doctype": "Sales Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Accounts Receivable Summary",
                                        "doctype": "Sales Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Accounts Payable",
                                        "doctype": "Purchase Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Accounts Payable Summary",
                                        "doctype": "Purchase Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Balance Sheet",
                                        "doctype": "GL Entry"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Profit and Loss Statement",
                                        "doctype": "GL Entry"
                                }
                        ]
                },
		{
                        "label": _("Sales"),
                        "items": [
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Gross Profit",
                                        "doctype": "Sales Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Sales Analytics",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Sales Order Trends",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Sales Order Summary",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Sales Order Overview",
                                        "doctype": "Sales Order"
                                }
                        ]
                },
		{
                        "label": _("Purchase"),
                        "items": [
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Analytics",
                                        "doctype": "Purchase Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Order Trends",
                                        "doctype": "Purchase Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Invoice Trends",
                                        "doctype": "Purchase Invoice"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Receipt Trends",
                                        "doctype": "Purchase Receipt"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Order Summary",
                                        "doctype": "Purchase Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Purchase Order Overview",
                                        "doctype": "Purchase Order"
                                }
                        ]
                },
		{
                        "label": _("Custom Report (Develped By ERP Team)"),
                        "items": [
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Item Wise Purchase Summery",
                                        "doctype": "Purchase Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "All Items Projection Report",
                                        "doctype": "Bin"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Item Wise Order Summery",
					"label": "Item Wise Order Summery (Sales)",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Customer Wise Transaction Summery",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Order Summery",
					"label": "Order Summery (Sales)",
                                        "doctype": "Sales Order"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Customer Abstract",
                                        "doctype": "Payment Entry"
                                },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Customer Average Abstract",
                                        "doctype": "Payment Entry"
                                },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Supplier Abstract",
                                        "doctype": "Payment Entry"
                                },
                                {
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Supplier Average Abstract",
                                        "doctype": "Payment Entry"
                                }
                        ]
                },
		{
                        "label": _("Stock Reports"),
                        "items": [
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Stock Balance",
                                        "doctype": "Stock Ledger Entry"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Stock Ledger",
                                        "doctype": "Stock Ledger Entry"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Stock Projected Qty",
                                        "doctype": "Item"
                                },
				{
                                        "type": "report",
                                        "is_query_report": True,
                                        "name": "Stock Ageing",
                                        "doctype": "Item"
                                }
                        ]
                }
]
