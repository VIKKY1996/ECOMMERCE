# List of countries with their codes and flag emojis
COUNTRIES = [
    {"code": "IN", "name": "India", "flag": "🇮🇳"},
    {"code": "US", "name": "United States", "flag": "🇺🇸"},
    {"code": "GB", "name": "United Kingdom", "flag": "🇬🇧"},
    {"code": "CA", "name": "Canada", "flag": "🇨🇦"},
    {"code": "AU", "name": "Australia", "flag": "🇦🇺"},
    {"code": "DE", "name": "Germany", "flag": "🇩🇪"},
    {"code": "FR", "name": "France", "flag": "🇫🇷"},
    {"code": "IT", "name": "Italy", "flag": "🇮🇹"},
    {"code": "ES", "name": "Spain", "flag": "🇪🇸"},
    {"code": "MX", "name": "Mexico", "flag": "🇲🇽"},
    {"code": "BR", "name": "Brazil", "flag": "🇧🇷"},
    {"code": "JP", "name": "Japan", "flag": "🇯🇵"},
    {"code": "CN", "name": "China", "flag": "🇨🇳"},
    {"code": "SG", "name": "Singapore", "flag": "🇸🇬"},
    {"code": "NL", "name": "Netherlands", "flag": "🇳🇱"},
    {"code": "SE", "name": "Sweden", "flag": "🇸🇪"},
    {"code": "CH", "name": "Switzerland", "flag": "🇨🇭"},
    {"code": "NZ", "name": "New Zealand", "flag": "🇳🇿"},
    {"code": "ZA", "name": "South Africa", "flag": "🇿🇦"},
    {"code": "AE", "name": "United Arab Emirates", "flag": "🇦🇪"},
    {"code": "KR", "name": "South Korea", "flag": "🇰🇷"},
    {"code": "TH", "name": "Thailand", "flag": "🇹🇭"},
    {"code": "MY", "name": "Malaysia", "flag": "🇲🇾"},
    {"code": "ID", "name": "Indonesia", "flag": "🇮🇩"},
    {"code": "PH", "name": "Philippines", "flag": "🇵🇭"},
    {"code": "VN", "name": "Vietnam", "flag": "🇻🇳"},
    {"code": "PK", "name": "Pakistan", "flag": "🇵🇰"},
    {"code": "BD", "name": "Bangladesh", "flag": "🇧🇩"},
    {"code": "LK", "name": "Sri Lanka", "flag": "🇱🇰"},
    {"code": "NG", "name": "Nigeria", "flag": "🇳🇬"},
    {"code": "KE", "name": "Kenya", "flag": "🇰🇪"},
    {"code": "EG", "name": "Egypt", "flag": "🇪🇬"},
    {"code": "AR", "name": "Argentina", "flag": "🇦🇷"},
    {"code": "CL", "name": "Chile", "flag": "🇨🇱"},
    {"code": "CO", "name": "Colombia", "flag": "🇨🇴"},
    {"code": "PE", "name": "Peru", "flag": "🇵🇪"},
    {"code": "GR", "name": "Greece", "flag": "🇬🇷"},
    {"code": "PT", "name": "Portugal", "flag": "🇵🇹"},
    {"code": "RU", "name": "Russia", "flag": "🇷🇺"},
    {"code": "TR", "name": "Turkey", "flag": "🇹🇷"},
    {"code": "SA", "name": "Saudi Arabia", "flag": "🇸🇦"},
    {"code": "IL", "name": "Israel", "flag": "🇮🇱"},
    {"code": "HK", "name": "Hong Kong", "flag": "🇭🇰"},
    {"code": "TW", "name": "Taiwan", "flag": "🇹🇼"},
    {"code": "BO", "name": "Bolivia", "flag": "🇧🇴"},
    {"code": "CZ", "name": "Czech Republic", "flag": "🇨🇿"},
    {"code": "PL", "name": "Poland", "flag": "🇵🇱"},
    {"code": "FI", "name": "Finland", "flag": "🇫🇮"},
    {"code": "DK", "name": "Denmark", "flag": "🇩🇰"},
    {"code": "NO", "name": "Norway", "flag": "🇳🇴"},
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
