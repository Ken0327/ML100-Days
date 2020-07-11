import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data_path
dir_data = './data/TW'
f_app_train = os.path.join(dir_data, 'BANK_MCT_ALL_AG.CSV')
app_train = pd.read_csv(f_app_train)

def drawplotbyage(age):
    N = 1
    fig, ax = plt.subplots()
    x = np.arange(N)    # the x locations for the groups
    width = 0.05        # the width of the bars
    ax.bar(x, app_train['food_' + age +'_price'].mean(), width, yerr=app_train['food_' + age + '_price'].std(), label='food')
    ax.bar(x + width, app_train['clothes_' + age +'_price'].mean(), width, yerr=app_train['clothes_' + age +'_price'].std(), label='clothes')
    ax.bar(x + width*2, app_train['hotel_' + age +'_price'].mean(), width, yerr=app_train['hotel_' + age +'_price'].std(), label='hotel')
    ax.bar(x + width*3, app_train['transpotation_' + age +'_price'].mean(), width, yerr=app_train['transpotation_' + age +'_price'].std(), label='transpotation')
    ax.bar(x + width*4, app_train['entertainment_' + age +'_price'].mean(), width, yerr=app_train['entertainment_' + age +'_price'].std(), label='entertainment')
    ax.bar(x + width*5, app_train['mall_' + age +'_price'].mean(), width, yerr=app_train['mall_' + age +'_price'].std(), label='mall')
    ax.bar(x + width*6, app_train['other_' + age +'_price'].mean(), width, yerr=app_train['other_' + age +'_price'].std(), label='other')

    ax.set_ylabel('Price')
    ax.set_title(age + ' comsumer price by group')
    ax.set_xticks(x)
    ax.set_xlabel(('age ' + age ))
    ax.legend()
#     fig.set_size_inches(5, 5, forward=True)
#     plt.savefig('PricebyAge_meanstd_food.pdf', dpi=300)
    ax.autoscale_view()
    plt.show()

# plot by age
drawplotbyage('<20')
drawplotbyage('20-25')
drawplotbyage('25-30')
drawplotbyage('30-35')
drawplotbyage('35-40')
drawplotbyage('40-45')
drawplotbyage('45-50')
drawplotbyage('50-55')
drawplotbyage('55-60')
drawplotbyage('60-65')
drawplotbyage('65-70')
drawplotbyage('70-75')
drawplotbyage('75-80')
drawplotbyage('>80')


def drawplotbygroup(group):
    N = 1
    under20_means = app_train[ group + '_<20_price'].mean()
    under20_std = app_train[ group + '_<20_price'].std()

    t20to25_means = app_train[ group + '_20-25_price'].mean()
    t20to25_std = app_train[ group + '_20-25_price'].std()

    t25to30_means = app_train[ group + '_25-30_price'].mean()
    t25to30_std = app_train[ group + '_25-30_price'].std()

    t30to35_means = app_train[ group + '_30-35_price'].mean()
    t30to35_std = app_train[ group + '_30-35_price'].std()

    t35to40_means = app_train[ group + '_35-40_price'].mean()
    t35to40_std = app_train[ group + '_35-40_price'].std()

    t40to45_means = app_train[ group + '_40-45_price'].mean()
    t40to45_std = app_train[ group + '_40-45_price'].std()

    t45to50_means = app_train[ group + '_45-50_price'].mean()
    t45to50_std = app_train[ group + '_45-50_price'].std()

    t50to55_means = app_train[ group + '_50-55_price'].mean()
    t50to55_std = app_train[ group + '_50-55_price'].std()

    t55to60_means = app_train[ group + '_55-60_price'].mean()
    t55to60_std = app_train[ group + '_55-60_price'].std()

    t60to65_means = app_train[ group + '_60-65_price'].mean()
    t60to65_std = app_train[ group + '_60-65_price'].std()

    t65to70_means = app_train[ group + '_65-70_price'].mean()
    t65to70_std = app_train[ group + '_65-70_price'].std()

    t70to75_means = app_train[ group + '_70-75_price'].mean()
    t70to75_std = app_train[ group + '_70-75_price'].std()

    t75to80_means = app_train[ group + '_75-80_price'].mean()
    t75to80_std = app_train[ group + '_75-80_price'].std()

    over80_means = app_train[ group + '_>80_price'].mean()
    over80_std = app_train[ group + '_>80_price'].std()

    fig, ax = plt.subplots()

    ind = np.arange(N)    # the x locations for the groups
    width = 0.05        # the width of the bars
    ax.bar(ind, under20_means, width, yerr=under20_std, label='<20')
    ax.bar(ind + width, t20to25_means, width, yerr=t20to25_std, label='20-25')
    ax.bar(ind + width*2, t25to30_means, width, yerr=t25to30_std, label='25-30')
    ax.bar(ind + width*3, t30to35_means, width, yerr=t30to35_std, label='30-35')
    ax.bar(ind + width*4, t35to40_means, width, yerr=t35to40_std, label='35-40')
    ax.bar(ind + width*5, t40to45_means, width, yerr=t40to45_std, label='40-45')
    ax.bar(ind + width*6, t45to50_means, width, yerr=t45to50_std, label='45-50')
    ax.bar(ind + width*7, t50to55_means, width, yerr=t50to55_std, label='50-55')
    ax.bar(ind + width*8, t55to60_means, width, yerr=t55to60_std, label='55-60')
    ax.bar(ind + width*9, t60to65_means, width, yerr=t60to65_std, label='60-65')
    ax.bar(ind + width*10, t65to70_means, width, yerr=t65to70_std, label='65-70')
    ax.bar(ind + width*11, t70to75_means, width, yerr=t70to75_std, label='70-75')
    ax.bar(ind + width*12, t75to80_means, width, yerr=t75to80_std, label='75-80')
    ax.bar(ind + width*13, over80_means, width, yerr=over80_std, label='>80')

    ax.set_ylabel('Price')
    ax.set_title('Price by group and age')
    ax.set_xticks(ind + width*13 / 7)
    ax.set_xticklabels(( group + '', 'clothes', 'hotel', 'transpotation', 'entertainment', 'mall', 'other'))
    ax.legend()
#     fig.set_size_inches(10, 10, forward=True)
#     plt.savefig('PricebyAge_meanstd.pdf', dpi=300)
    ax.autoscale_view()
    plt.show()

# plot by group
drawplotbygroup('food')
drawplotbygroup('clothes')
drawplotbygroup('hotel')
drawplotbygroup('transpotation')
drawplotbygroup('entertainment')
drawplotbygroup('mall')
drawplotbygroup('other')