{
    "name" : "PT. BSP - Training",
    "description" : "Pelatihan Technical Odoo V17 untuk PT. Sanbe Farma",
    "author" : "PT. BSP, PT. Arkana Solusi Digital",
    "version" : "17.0.1.0.0",
    "category" : "Others",
    "license" : "OPL-1",
    "depends" : [
        "base", 
        "mail",
        "hr",
    ],
    "data" : [
        "security/planning_slot_role.xml",
        "security/ir.model.access.csv",
        "views/planning_role_views.xml",
        "views/planning_slot_views.xml",
        "views/planning_menu.xml",
        "data/hr_employee_data.xml",
    ],
    "auto_install" : False, 
    "installable" : True,
    "application" : True,
    "external_dependencies" : {"python" : []}
}