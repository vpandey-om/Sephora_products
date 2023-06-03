import os
root=os.getcwd()
import pandas as pd 
from plotnine import *

class Utility():
    def __init__(self):
        ''' initilize some varibales'''
        self.__project__='Sephora data analysis'
        
    def read_all_data(self):
        ''' read all products, brand, and review of customers'''
         ## import hourly,daily,weekly,monthly data sets
  
        product_info_df=pd.read_csv(os.path.join(root,'sephora', 'product_info.csv'),sep=',')
       
        reviews_0_250=pd.read_csv(os.path.join(root,'sephora', 'reviews_0_250.csv'),sep=',')
        reviews_250_500=pd.read_csv(os.path.join(root,'sephora', 'reviews_250_500.csv'),sep=',')
        reviews_500_750=pd.read_csv(os.path.join(root,'sephora', 'reviews_500_750.csv'),sep=',')
        reviews_750_1000=pd.read_csv(os.path.join(root,'sephora', 'reviews_750_1000.csv'),sep=',')
        reviews_1000_1500=pd.read_csv(os.path.join(root,'sephora',\
                                                        'reviews_1000_1500.csv'),sep=',')
        reviews_1500_end=pd.read_csv(os.path.join(root,'sephora', 'reviews_1500_end.csv'),sep=',')
        ###
        review_df=pd.concat([reviews_0_250,reviews_250_500,
                   reviews_500_750,reviews_750_1000,
                   reviews_1000_1500,reviews_1500_end])
        
        ## join review and product data 
        # Lets check df_product_info which columns that similar with df_reviews
        self.combine_reviews_product(product_info_df,review_df)
        
    def combine_reviews_product(self,product_info_df,review_df):
        ''' join review and product info dataframes '''
        
        cols_to_use = set(product_info_df.columns)-set(review_df.columns)
        cols_to_use = list(cols_to_use)
        cols_to_use.append('product_id')
        print(cols_to_use)
        df = pd.merge(review_df, product_info_df[cols_to_use], how='outer',\
                      on=['product_id', 'product_id'])
        
        ### drop 'Unnamed: 0'
        df.drop('Unnamed: 0',inplace=True,axis=1)
        print(df.shape)
        self.data_df=df
        
    def plot_bar(self,df,x,y,c):
        ''' plot bar chart '''
        return (ggplot(df) + geom_bar(aes(x=x,y=y, fill=c)))
        
    def plot_top_product_candidates(self,n=10,tcol='is_recommended'):
        ''' lets plot top rated candidates'''
        df=self.data_df.copy()
        ## group brand_id and tcol  
        most_reccomended = df.groupby(['product_id','product_name','brand_name']).\
        sum(numeric_only=True)[tcol].reset_index()\
        .sort_values(tcol,ascending=False).head(n)
        return most_reccomended
        
        ##
        # fig = px.bar(most_reccomended, x=tcol, y='product_name',color='product_name')
        # fig.show()
        
    def plot_price_based(self,n=10):
        '''find most expansive products '''
        df=self.data_df.copy()
        most_expensive = df.groupby(['product_id','product_name','price_usd']).\
        sum(numeric_only=True).reset_index().sort_values('price_usd',ascending=False).\
        head(n).sort_values('price_usd',ascending=False)
        most_expensive=most_expensive.drop_duplicates(subset=['product_name'])
#         fig1 = px.bar(most_expensive , x='price_usd', y='product_name',color='product_name')
       
#         fig1.show()
        
        most_cheap = df.groupby(['product_id','product_name','price_usd']).\
        sum(numeric_only=True).reset_index().sort_values('price_usd',ascending=True)\
        .head(n).sort_values('price_usd',ascending=False)
        most_cheap=most_cheap.drop_duplicates(subset=['product_name'])
        return most_expensive,most_cheap
#         fig2 = px.bar(most_cheap , x='price_usd', y='product_name',color='product_name')

#         fig2.show()
        
    def missing_values_analysis(self):
        ''' Summarize the data, examine pattern in data and visualize'''
        ### analyze missing values 
        df=self.data_df.copy()
        missing = []
        unique = []
        types = []
        variables = []
        count = []
        missing_percent=[]

        for column in df.columns:
            variables.append(column)
            missing.append(df[column].isnull().sum())
            unique.append(df[column].nunique())
            types.append(df[column].dtypes)
            count.append(len(df[column]))
            missing_percent.append((df[column].isnull().sum()/len(df[column]))*100)
        output = pd.DataFrame({
        'variable': variables, 
        'dtype': types,
        'count': count,
        'unique': unique,
        'missing': missing, 
        'missing(%)':missing_percent
        })
        print("missing info : ")
        output=output.sort_values("missing",ascending=False).reset_index(drop=True)
        print(output.head())

        ### get columns where more than 50 % columns are deleted 
        drop_columns=output.loc[output['missing(%)']>25,'variable'].to_list()
        print('More than 25 % missing values are found in the features:\n',drop_columns)
        
        