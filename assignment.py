
def answer_five():
    l = census_df['STNAME'].value_counts(sort = True)
    m = l.max()
    return l.index[0]
    #return census_df[l == m].index.values[0]
answer_five()

def answer_four():
    df['Points'] = 3*df['Gold.2'] + 2*df['Silver.2'] + df['Bronze.2']
    return df['Points']
answer_four()

def answer_three():
    df['v'] = abs(df['Gold'] - df['Gold.1']) / df['Combined total']
    m = df['v'].max()
    return df[df['v'] == m].index.values[0]
answer_three()

def answer_two():
    df['diff'] = abs(df['Gold'] - df['Gold.1'])
    m = df['diff'].max()
    return df[df['diff'] == m].index.values[0]
answer_two()

def answer_one():
    m = df['Gold'].max()
    
    return df[df['Gold'] == m].index.values[0]
answer_one()

#
#census_df = census_df[census_df['SUMLEV'] == 50]
#def answer_six():
#    census_df.set_index('STNAME', ascending = False)
#    return census_df #census_df['STNAME'][:3]
#answer_six()

census_df = census_df[census_df['SUMLEV'] == 50]
col_keep = ['STNAME', 'CENSUS2010POP', 'CTYNAME']
n = census_df[col_keep]
n = n.set_index('CENSUS2010POP')
n = n.sort_index(ascending=False)
def answer_six():
    un = census_df['STNAME'].unique()
    l = []
    for i in range(3142):
        count = 0
        for u in un:
            if u == n['STNAME'].iloc[i] and count < 3:
                l.append(n['CTYNAME'].iloc[i])
                count += 1
    return l

    #return census_df['STNAME'][:3]
answer_six()

census_df = census_df[census_df['SUMLEV'] == 50]
census_df = census_df.set_index('CTYNAME')
def answer_seven():
    #ser= ['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    census_df['diff'] = census_df['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015'].max(axis=1) - census_df['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015'].min(axis =1)
    return census_df['diff'] #census_df.iloc[l.index(max(l))][6]
answer_seven()


census_df = census_df[census_df['SUMLEV'] == 50]
ser = ['POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
n = census_df[ser]
census_df = census_df.set_index('CTYNAME')
def answer_seven():
    census_df['diff'] = n.max(axis=1) - n.min(axis=1)
    m = census['diff'].max()
    return census_df[census_df['diff'] == m].index.values[0]

answer_seven()
