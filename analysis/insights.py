import pandas as pd

# Load data
df = pd.read_csv('data/data.csv')

# 1. Dominance of BJP
def bjp_dominance(df):
    bjp_seats = df[df['Party Abbreviation'] == 'BJP']['Total'].sum()
    inc_seats = df[df['Party Abbreviation'] == 'INC']['Total'].sum()
    return f"BJP has {bjp_seats} seats, more than double of INC's {inc_seats} seats."

# 2. Regional Party Performance
def regional_performance(df):
    sp_seats = df[df['Party Abbreviation'] == 'SP']['Total'].sum()
    aitc_seats = df[df['Party Abbreviation'] == 'AITC']['Total'].sum()
    return f"SP and AITC have strong regional influence with {sp_seats} and {aitc_seats} seats respectively."

# 3. Southern Influence
def southern_influence(df):
    dmk_seats = df[df['Party Abbreviation'] == 'DMK']['Total'].sum()
    tdp_seats = df[df['Party Abbreviation'] == 'TDP']['Total'].sum()
    return f"DMK and TDP show political significance with {dmk_seats} and {tdp_seats} seats each."

# 4. Emergence of New Alliances
def new_alliances(df):
    shsubt_seats = df[df['Party Abbreviation'] == 'SHSUBT']['Total'].sum()
    shs_seats = df[df['Party Abbreviation'] == 'SHS']['Total'].sum()
    return f"Shiv Sena split: SHSUBT has {shsubt_seats} seats, SHS has {shs_seats} seats."

# 5. Smaller Parties Making Impact
def smaller_parties(df):
    ljprv_seats = df[df['Party Abbreviation'] == 'LJPRV']['Total'].sum()
    ncpsp_seats = df[df['Party Abbreviation'] == 'NCPSP']['Total'].sum()
    return f"LJPRV and NCPSP have {ljprv_seats} and {ncpsp_seats} seats, influencing outcomes despite limited reach."

# 6. Communist Parties Holding Ground
def communist_parties(df):
    cpim_seats = df[df['Party Abbreviation'] == 'CPI(M)']['Total'].sum()
    cpi_seats = df[df['Party Abbreviation'] == 'CPI']['Total'].sum()
    return f"CPI(M) and CPI have {cpim_seats} and {cpi_seats} seats, maintaining left-wing presence."

# 7. Independent Candidates
def independent_candidates(df):
    ind_seats = df[df['Party Abbreviation'] == 'IND']['Total'].sum()
    return f"Independent candidates secured {ind_seats} seats, indicating voter discontent with traditional parties."

# 8. Variety of Political Ideologies
def political_ideologies(df):
    unique_parties = df['Party Abbreviation'].nunique()
    return f"Diverse landscape with {unique_parties} different political ideologies represented."

# 9. Single Seat Parties
def single_seat_parties(df):
    single_seat = df[df['Total'] == 1]['Party Abbreviation'].tolist()
    return f"Single seat parties include: {', '.join(single_seat)}."

# 10. Significance of Caste and Regional Parties
def caste_regional_parties(df):
    rjd_seats = df[df['Party Abbreviation'] == 'RJD']['Total'].sum()
    rld_seats = df[df['Party Abbreviation'] == 'RLD']['Total'].sum()
    return f"RJD and RLD won {rjd_seats} and {rld_seats} seats, highlighting the importance of caste dynamics."

# Generate insights
insights = [
    bjp_dominance(df),
    regional_performance(df),
    southern_influence(df),
    new_alliances(df),
    smaller_parties(df),
    communist_parties(df),
    independent_candidates(df),
    political_ideologies(df),
    single_seat_parties(df),
    caste_regional_parties(df)
]

# Print insights
for insight in insights:
    print(insight)
