import pandas as pd
import numpy as np

data = pd.read_csv('/Users/jinshuo/Desktop/sample.txt',sep='\t')

df = data.copy()
df = df[df.critic_score.notnull()]
df = df[df.audience_score.notnull()]

# convert object data type to numeric data type
df.critic_score = df.critic_score.str[:-1].astype(int)
df.audience_score = df.audience_score.str[:-1].astype(int)
df['target_value'] = df.critic_score - df.audience_score
df = df.drop(['critic_score','audience_score'],axis=1)

# split In Theaters
df['month_day'],df['year_range']=df['In Theaters'].str.split(',',1).str
df['month'],df['day'] = df['month_day'].str.split(' ',1).str
df['year'],df['range']=df['year_range'].str.split().str
df = df.drop(['In Theaters','month_day','year_range','month','day'],axis=1)

# range
df['range'] = df['range'].fillna('N') # total 491, 3% are missing value 
df['range'] = df['range'].map( {'limited': 0, 'wide': 1,'N':2} ).astype(int)

# year 
df['year'] = df['year'].fillna(0)
df['year'] = df['year'].astype(int)
df.loc[ df['year'] <= 1978, 'year']= 0
df.loc[(df['year'] > 1978) & (df['year'] <= 1988), 'year'] = 1
df.loc[(df['year'] > 1988) & (df['year'] <= 1998), 'year'] = 2
df.loc[(df['year'] > 1998) & (df['year'] <= 2008), 'year'] = 4
df.loc[(df['year'] > 2008) & (df['year'] <= 2018), 'year'] = 5


# acotor_links_num(same as the actor_names)
df['actor_num'] = df.actor_links.apply(lambda x: len(x.split(',')))
# df.plot.scatter(x='actor_num',y='target_value')
df = df.drop(['actor_links'],axis=1)

# Runtime
df['runtime'],df['minutes'] = df.Runtime.str.split(' ',1).str
df.runtime = pd.to_numeric(df.runtime)
mean = df.runtime.mean()
df.runtime = df.runtime.fillna(mean)
df.loc[ df['runtime'] <= 50, 'runtime']= 0
df.loc[(df['runtime'] > 50) & (df['runtime'] <= 100), 'runtime'] = 1
df.loc[(df['runtime'] > 100) & (df['runtime'] <= 150), 'runtime'] = 2
df.loc[(df['runtime'] > 150) & (df['runtime'] <= 200), 'runtime'] = 3
df.loc[(df['runtime'] > 200) & (df['runtime'] <= 250), 'runtime'] = 4
df.loc[(df['runtime'] > 250) & (df['runtime'] <= 300), 'runtime'] = 5
df.loc[(df['runtime'] > 300), 'runtime'] = 6
df = df.drop(['minutes','Runtime'],axis=1)
# df.runtime.fillna(median, inplace=True)
# df.runtime = df.runtime.astype(int)
# df.runtime.where(df.runtime < 300, 300, inplace=True)
# bins = np.arange(0,300,50)
# df = pd.concat([df,pd.get_dummies(pd.cut(df.runtime,bins),prefix ='runtime')],axis=1)

# Rating 
df['rating'],df['something'] = df.Rating.str.split(' ',1).str
df = df.drop(['something','Rating'],axis=1)
df['rating'] = df['rating'].map({'R': 0, 'NR': 1,'PG-13':2,'PG':3,'G':4,'NC17':5}).astype(int)

#Genre
genre = df.set_index('movie_id').Genre.str.split(r',', expand=True).stack().reset_index(level=1, drop=True).to_frame('Genre')
genre['Genre'] = genre['Genre'].apply(lambda x: x.replace(' ',''))
genre_dummies = pd.get_dummies(genre, prefix='G', columns=['Genre']).groupby(level=0).sum()
genre_dummies.reset_index(inplace=True)
df = pd.merge(df, genre_dummies , on=['movie_id','movie_id'])
df = df.drop(['Genre'],axis=1)

df.to_csv('data_clean.csv')

