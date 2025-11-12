# List of countries with their codes
COUNTRIES = [
    {"code": "IN", "name": "India"},
    {"code": "US", "name": "United States"},
    {"code": "GB", "name": "United Kingdom"},
    {"code": "CA", "name": "Canada"},
    {"code": "AU", "name": "Australia"},
    {"code": "DE", "name": "Germany"},
    {"code": "FR", "name": "France"},
    {"code": "IT", "name": "Italy"},
    {"code": "ES", "name": "Spain"},
    {"code": "MX", "name": "Mexico"},
    {"code": "BR", "name": "Brazil"},
    {"code": "JP", "name": "Japan"},
    {"code": "CN", "name": "China"},
    {"code": "SG", "name": "Singapore"},
    {"code": "NL", "name": "Netherlands"},
    {"code": "SE", "name": "Sweden"},
    {"code": "CH", "name": "Switzerland"},
    {"code": "NZ", "name": "New Zealand"},
    {"code": "ZA", "name": "South Africa"},
    {"code": "AE", "name": "United Arab Emirates"},
    {"code": "KR", "name": "South Korea"},
    {"code": "TH", "name": "Thailand"},
    {"code": "MY", "name": "Malaysia"},
    {"code": "ID", "name": "Indonesia"},
    {"code": "PH", "name": "Philippines"},
    {"code": "VN", "name": "Vietnam"},
    {"code": "PK", "name": "Pakistan"},
    {"code": "BD", "name": "Bangladesh"},
    {"code": "LK", "name": "Sri Lanka"},
    {"code": "NG", "name": "Nigeria"},
    {"code": "KE", "name": "Kenya"},
    {"code": "EG", "name": "Egypt"},
    {"code": "AR", "name": "Argentina"},
    {"code": "CL", "name": "Chile"},
    {"code": "CO", "name": "Colombia"},
    {"code": "PE", "name": "Peru"},
    {"code": "GR", "name": "Greece"},
    {"code": "PT", "name": "Portugal"},
    {"code": "RU", "name": "Russia"},
    {"code": "TR", "name": "Turkey"},
    {"code": "SA", "name": "Saudi Arabia"},
    {"code": "IL", "name": "Israel"},
    {"code": "HK", "name": "Hong Kong"},
    {"code": "TW", "name": "Taiwan"},
    {"code": "BO", "name": "Bolivia"},
    {"code": "CZ", "name": "Czech Republic"},
    {"code": "PL", "name": "Poland"},
    {"code": "FI", "name": "Finland"},
    {"code": "DK", "name": "Denmark"},
    {"code": "NO", "name": "Norway"},
]

def get_countries_list():
    """Return a sorted list of countries"""
    return sorted(COUNTRIES, key=lambda x: x['name'])

def get_country_name(code):
    """Get country name by code"""
    for country in COUNTRIES:
        if country['code'] == code:
            return country['name']
    return "India"  # Default
