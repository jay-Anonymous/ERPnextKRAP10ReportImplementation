from . import __version__ as app_version

app_name = "Techsavanna.ke"
app_title = "Techsavanna.ke"
app_publisher = "Techsavanna Limited"
app_description = "ERPNextKraP10ReportImplementation"
app_icon = "drag"
app_color = "grey"
app_email = "gnjakai@yahoo.com"



fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                   	"Employee-national_id",
					"Employee-nhif_no",
					"Employee-nssf_no",
					"Employee-tax_id",
                    "Salary Component-p10a_tax_deduction_card_type",								
                ),
            ]
        ],
    },
]



user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"Techsavanna.ke.auth.validate"
# ]

