from frappe import _

def get_data():
    return [
        {
            "module_name": "Tfrenzy",
            "color": "blue",
            "icon": "octicon octicon-settings",
            "type": "link",
            "label": _("Refurbished Products"),
            "link": "/app/tfrenzy-doctype",
        }
    ]
