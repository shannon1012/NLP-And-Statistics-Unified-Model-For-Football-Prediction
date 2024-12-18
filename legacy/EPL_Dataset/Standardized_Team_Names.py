standardized_team_names = {
    "AFC Bournemouth": ["Bournemouth"],
    "Birmingham City": ["Birmingham"],
    "Blackburn Rovers": ["Blackburn"],
    "Bolton Wanderers": ["Bolton"],
    "Bradford City": ["Bradford"],
    "Brighton & Hove Albion": ["Brighton"],
    "Cardiff City": ["Cardiff"],
    "Charlton Athletic": ["Charlton"],
    "Coventry City": ["Coventry"],
    "Crystal Palace": ["Palace"],
    "Derby County": ["Derby"],
    "Huddersfield Town": ["Huddersfield"],
    "Hull City": ["Hull"],
    "Ipswich Town": ["Ipswich"],
    "Leeds United": ["Leeds Utd", "Leeds"],
    "Leicester City": ["Leicester"],
    "Manchester City": ["Man City", "Manchester city"],
    "Manchester United": ["Man Utd", "Man United"],
    "Newcastle United": ["Newcastle Utd"],
    "Norwich City": ["Norwich"],
    "Nottingham Forest": ["Nott'm Forest", "Nottingham"],
    "Oldham Athletic": ["Oldham"],
    "Portsmouth": ["Pompey"],
    "Queens Park Rangers": ["QPR"],
    "Sheffield United": ["Sheff Utd"],
    "Sheffield Wednesday": ["Sheff Wed", "Sheffield Weds"],
    "Stoke City": ["Stoke"],
    "Swansea City": ["Swansea"],
    "Tottenham Hotspur": ["Tottenham", "Tottenham Hostpur", "Spurs"],
    "West Bromwich Albion": ["West Brom", "West Bromwich"],
    "West Ham United": ["West Ham"],
    "Wigan Athletic": ["Wigan"],
    "Wolverhampton Wanderers": ["Wolves"],
}

def get_standardize_team_name(name, standardized_names):
    for standard_name, variations in standardized_names.items():
        if name in variations:
            return standard_name
    return name