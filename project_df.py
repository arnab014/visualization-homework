import pandas as pd


import matplotlib.pyplot as plt
import os
import xlrd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}')


branch = pd.read_excel(r'C:/Users/Arnab/Desktop/branch_data.xlsx')
#pretty_print("Printing an entire dataframe", branch.to_string())

os.makedirs('prj_plots', exist_ok=True)

# Plotting line chart
plt.plot(branch['BRANCH_ID'],branch['TOT_CD_AC_MAY'], color='red')
plt.title('BRANCH_ID')
plt.ylabel('CD_AC')
plt.savefig(f'prj_plots/TOT_CD_AC.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(branch['TOT_SB_AC_MAY'], bins=3, color='g')
plt.title('TOT_SB_AC_MAY')
plt.xlabel('TOT_SB_AC_MAY')
plt.ylabel('TOT_SB_AC_MAY')
plt.savefig(f'prj_plots/TOT_SB_AC_MAY.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(branch['BRANCH_ID'], branch['TOT_FDR_AC_MAY'], color='b')
plt.title('Age Vs Charges')
plt.xlabel('BRANCH_ID')
plt.ylabel('TOT_FDR_AC_MAY')
plt.savefig(f'prj_plots/TOT_FDR_AC_MAY.png', format='png')

plt.close()

