#import modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#configuring sns
sns.set(rc = {'figure.figsize':(24,6)})
sns.set(font_scale=.75)

#retrieve raw csv data
arrseats_df = pd.read_csv("/home/owner/programmingprojects/datasources/june2022arr.csv")

#turn date into pd datetime format, then manipulate it to month-day format
arrseats_df['date'] = pd.to_datetime(arrseats_df['date'])
arrseats_df['date'] = arrseats_df['date'].dt.strftime('%m-%d')

#create scatter plot of arriving airline seats
ag = sns.scatterplot(x="date", y="Total", data=arrseats_df)
ag.set(title="Arriving Airline Seats by Date", xlabel="Date", ylabel="Total Scheduled Airline Seats")
plt.savefig("x.png", bbox_inches='tight');