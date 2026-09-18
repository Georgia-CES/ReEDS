southern_co_bas = ['p88','p89','p90','p94']
georgia_bas = ['p94']
static_presets = [
    #Full
    {'name': 'SERTP Generation (TWh)', 'sheet_name':'gen', 'result': 'Generation National (TWh)', 'preset': 'Stacked Bars'},
    {'name': 'SERTP Capacity (GW)', 'sheet_name':'cap', 'result': 'Capacity National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'SERTP New Annual Capacity (GW)', 'sheet_name':'cap_new_ann', 'result': 'New Annual Capacity National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'SERTP Annual Retirements (GW)', 'sheet_name':'retire_ann', 'result': 'Annual Retirements National (GW)', 'preset': 'Stacked Bars'},
    {'name': 'SERTP Final Gen by timeslice (GW)', 'sheet_name':'gen_final_timeslice', 'result': 'Gen by timeslice national (GW)', 'preset': 'Stacked Bars Final'},
    {'name': 'SERTP Bulk System Electricity Price ($/MWh)', 'sheet_name':'elec_price', 'result': 'Requirement Prices and Quantities National', 'preset': 'Bulk System Electricity Price ($/MWh)'},
    {'name': 'SERTP System Cost of Electricity ($/MWh)', 'sheet_name':'scoe', 'result': 'National Average Electricity Cost ($/MWh)', 'preset': 'Average Electricity Cost by Year ($/MWh)'},
    {'name': 'SERTP Undiscounted Annual System Cost (Bil $)', 'sheet_name':'sys_cost', 'result': 'Sys Cost Annualized (Bil $)', 'preset': 'Undiscounted by Year'},
    {'name': 'SERTP Emissions (metric tons)', 'sheet_name':'emissions', 'result': 'Emissions National (metric tons)', 'preset': 'Scenario Lines Over Time'},
    {'name': 'Runtime (hours)', 'sheet_name':'runtime', 'result': 'Runtime', 'preset': 'Stacked Bars'},

    #Southern Company
    {'name': 'SoCo Generation (TWh)', 'sheet_name':'gen_soco', 'result': 'Generation BA (TWh)', 'preset': 'Stacked Bars', 'config':{'filter':{'rb':southern_co_bas}}},
    {'name': 'SoCo Capacity (GW)', 'sheet_name':'cap_soco', 'result': 'Capacity BA (GW)', 'preset': 'Stacked Bars', 'config':{'filter':{'rb':southern_co_bas}}},
    {'name': 'SoCo Bulk System Electricity Price ($/MWh)', 'sheet_name':'elec_price_soco', 'result': 'Requirement Prices and Quantities BA', 'preset': 'Bulk System Electricity Price ($/MWh)', 'config':{'filter':{'rb':southern_co_bas}}},
    {'name': 'SoCo Undiscounted Annual System Cost (Bil $)', 'sheet_name':'sys_cost_soco', 'result': 'Sys Cost Annualized BA/State (Bil $)', 'preset': 'Undiscounted by Year - BA', 'config':{'filter':{'r':southern_co_bas}}},
    {'name': 'SoCo CO2 Emissions (metric tons)', 'sheet_name':'emissions_soco', 'result': 'CO2 Emissions BA (metric tons)', 'preset': 'Scenario Lines Over Time', 'config':{'filter':{'rb':southern_co_bas}}},

    #Georgia
    {'name': 'GA Generation (TWh)', 'sheet_name':'gen_ga', 'result': 'Generation BA (TWh)', 'preset': 'Stacked Bars', 'config':{'filter':{'rb':georgia_bas}}},
    {'name': 'GA Capacity (GW)', 'sheet_name':'cap_ga', 'result': 'Capacity BA (GW)', 'preset': 'Stacked Bars', 'config':{'filter':{'rb':georgia_bas}}},
    {'name': 'GA Bulk System Electricity Price ($/MWh)', 'sheet_name':'elec_price_ga', 'result': 'Requirement Prices and Quantities BA', 'preset': 'Bulk System Electricity Price ($/MWh)', 'config':{'filter':{'rb':georgia_bas}}},
    {'name': 'GA Undiscounted Annual System Cost (Bil $)', 'sheet_name':'sys_cost_ga', 'result': 'Sys Cost Annualized BA/State (Bil $)', 'preset': 'Undiscounted by Year - BA', 'config':{'filter':{'r':georgia_bas}}},
    {'name': 'GA CO2 Emissions (metric tons)', 'sheet_name':'emissions_ga', 'result': 'CO2 Emissions BA (metric tons)', 'preset': 'Scenario Lines Over Time', 'config':{'filter':{'rb':georgia_bas}}},
]
